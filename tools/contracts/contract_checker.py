#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path
from typing import Any, Literal

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = REPO_ROOT / "docs" / "schemas"
PAYLOAD_DIR = Path(__file__).resolve().parent / "payloads"

CHECKS = {
    "akashic_envelope_v2": {
        "schema": SCHEMA_DIR / "akashic_envelope_v2.json",
        "payload": PAYLOAD_DIR / "akashic_envelope_v2.payload.json",
    },
    "embodiment_v1": {
        "schema": SCHEMA_DIR / "embodiment_v1.json",
        "payload": PAYLOAD_DIR / "embodiment_v1.payload.json",
    },
    "ipw_v1": {
        "schema": SCHEMA_DIR / "ipw_v1.json",
        "payload": PAYLOAD_DIR / "ipw_v1.payload.json",
    },
}

DEFAULT_CADENCE_BY_PHASE = {
    "nirodha": {"bpm": 22.0, "phase": 0.0, "jitter": 0.02},
    "awakened": {"bpm": 72.0, "phase": 0.0, "jitter": 0.05},
    "processing": {"bpm": 110.0, "phase": 0.0, "jitter": 0.08},
}

Mode = Literal["strict", "legacy"]


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _type_ok(expected: str, value: Any) -> bool:
    return {
        "object": lambda v: isinstance(v, dict),
        "array": lambda v: isinstance(v, list),
        "string": lambda v: isinstance(v, str),
        "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
        "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
        "boolean": lambda v: isinstance(v, bool),
    }.get(expected, lambda _v: True)(value)


def _validate(schema: dict[str, Any], payload: Any, path: str = "<root>") -> list[str]:
    errors: list[str] = []

    expected_type = schema.get("type")
    if expected_type and not _type_ok(expected_type, payload):
        return [f"{path}: expected {expected_type}, got {type(payload).__name__}"]

    if "const" in schema and payload != schema["const"]:
        errors.append(f"{path}: expected const value {schema['const']!r}")

    if "enum" in schema and payload not in schema["enum"]:
        errors.append(f"{path}: value {payload!r} not in enum {schema['enum']!r}")

    if isinstance(payload, (int, float)) and not isinstance(payload, bool):
        if "minimum" in schema and payload < schema["minimum"]:
            errors.append(f"{path}: value {payload} below minimum {schema['minimum']}")
        if "maximum" in schema and payload > schema["maximum"]:
            errors.append(f"{path}: value {payload} above maximum {schema['maximum']}")

    if isinstance(payload, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in payload:
                errors.append(f"{path}: missing required property '{key}'")

        properties = schema.get("properties", {})
        additional_allowed = schema.get("additionalProperties", True)
        if additional_allowed is False:
            for key in payload.keys() - properties.keys():
                errors.append(f"{path}: unexpected property '{key}'")

        for key, subschema in properties.items():
            if key in payload:
                errors.extend(_validate(subschema, payload[key], f"{path}.{key}"))

    if isinstance(payload, list):
        if "minItems" in schema and len(payload) < schema["minItems"]:
            errors.append(f"{path}: expected at least {schema['minItems']} items")
        item_schema = schema.get("items")
        if item_schema:
            for idx, value in enumerate(payload):
                errors.extend(_validate(item_schema, value, f"{path}[{idx}]"))

    return errors


def _inject_embodiment_defaults(payload: dict[str, Any], audits: list[str]) -> None:
    visual = payload.setdefault("visual_manifestation", {})
    if "cadence" in visual:
        return

    phase = str(payload.get("temporal_state", {}).get("phase", "awakened")).strip().lower()
    cadence = copy.deepcopy(DEFAULT_CADENCE_BY_PHASE.get(phase, DEFAULT_CADENCE_BY_PHASE["awakened"]))
    visual["cadence"] = cadence
    audits.append(f"embodiment_v1: injected deterministic cadence default for phase={phase!r}: {cadence}")


def _check_ipw_probability_policy(payload: dict[str, Any], audits: list[str]) -> list[str]:
    errors: list[str] = []
    policy = payload.get("probability_policy", {})
    if not policy.get("requires_normalization", False):
        return errors

    epsilon = float(policy.get("epsilon", 0.0001))
    on_violation = policy.get("on_violation", "error")
    predictions = payload.get("predictions", [])

    probabilities: list[float] = []
    for idx, row in enumerate(predictions):
        value = row.get("p")
        if value is None or isinstance(value, bool):
            errors.append(f"<root>.predictions[{idx}].p: missing or invalid numeric probability")
            continue
        numeric = float(value)
        if math.isnan(numeric) or math.isinf(numeric):
            errors.append(f"<root>.predictions[{idx}].p: NaN/Inf is not allowed")
            continue
        if numeric < 0:
            errors.append(f"<root>.predictions[{idx}].p: negative probability is not allowed")
            continue
        probabilities.append(numeric)

    if errors:
        return errors

    total = sum(probabilities)
    if total == 0:
        return ["<root>.predictions: probability sum is 0, cannot normalize"]

    if abs(total - 1.0) <= epsilon:
        return errors

    if on_violation == "normalize":
        for row in predictions:
            row["p"] = row["p"] / total
        audits.append(
            (
                "ipw_validation.audit.normalized=true "
                f"ipw_validation.audit.original_sum={total:.8f} "
                f"ipw_validation.audit.epsilon={epsilon}"
            )
        )
        return errors

    errors.append(
        f"<root>.predictions: probability sum {total:.8f} violates normalization policy with epsilon={epsilon}"
    )
    return errors


def _apply_contract_policy(contract_name: str, payload: dict[str, Any], audits: list[str], mode: Mode) -> list[str]:
    if contract_name == "embodiment_v1" and mode == "legacy":
        _inject_embodiment_defaults(payload, audits)
    if contract_name == "ipw_v1":
        return _check_ipw_probability_policy(payload, audits)
    return []


def run_contract_checks(mode: Mode = "strict") -> int:
    failures = 0
    for contract_name, pair in CHECKS.items():
        schema = _load_json(pair["schema"])
        payload = _load_json(pair["payload"])
        audits: list[str] = []

        errors = _apply_contract_policy(contract_name, payload, audits, mode=mode)
        errors.extend(_validate(schema, payload))

        if errors:
            failures += 1
            print(f"[FAIL] {contract_name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"[PASS] {contract_name}")

        for audit in audits:
            print(f"  [AUDIT] {audit}")

    return failures


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate canonical contracts against real payload fixtures")
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--strict", action="store_true", help="Strict mode for CI/PR gate (default)")
    mode_group.add_argument("--legacy", action="store_true", help="Legacy compatibility mode with cadence injection")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    selected_mode: Mode = "legacy" if args.legacy else "strict"
    raise SystemExit(1 if run_contract_checks(mode=selected_mode) else 0)
