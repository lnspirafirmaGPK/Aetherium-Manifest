from __future__ import annotations

import argparse
import hashlib
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ReplayEvent:
    tick: int
    event_type: str
    intent: str
    amplitude: float


class DeterministicNode:
    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)
        self._state = {
            "energy": 0.0,
            "coherence": 1.0,
            "last_intent": "idle",
            "ticks": 0,
        }

    def apply(self, event: ReplayEvent) -> None:
        jitter = self._rng.uniform(-0.02, 0.02)
        signed = event.amplitude + jitter
        if event.event_type == "emotion":
            self._state["energy"] = max(0.0, min(1.0, self._state["energy"] + signed * 0.8))
            self._state["coherence"] = max(0.0, min(1.0, self._state["coherence"] - abs(signed) * 0.25))
        elif event.event_type == "intent_switch":
            self._state["coherence"] = max(0.0, min(1.0, self._state["coherence"] - abs(signed) * 0.35))
            self._state["energy"] = max(0.0, min(1.0, self._state["energy"] + abs(signed) * 0.2))

        self._state["ticks"] = event.tick
        self._state["last_intent"] = event.intent

    def digest(self) -> str:
        normalized = json.dumps(self._state, sort_keys=True)
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def replay_lockstep(seed: int, event_log: list[dict[str, Any]], node_count: int = 2) -> dict[str, Any]:
    nodes = [DeterministicNode(seed=seed) for _ in range(node_count)]
    events = [ReplayEvent(**row) for row in event_log]

    for event in events:
        for node in nodes:
            node.apply(event)

    digests = [node.digest() for node in nodes]
    return {
        "seed": seed,
        "digests": digests,
        "lockstep": len(set(digests)) == 1,
        "events": len(events),
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deterministic replay harness")
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--event-log", type=Path, required=True)
    parser.add_argument("--nodes", type=int, default=2)
    return parser.parse_args()


def _main() -> int:
    args = _parse_args()
    with args.event_log.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    result = replay_lockstep(seed=args.seed, event_log=payload, node_count=args.nodes)
    print(json.dumps(result, indent=2))
    return 0 if result["lockstep"] else 1


if __name__ == "__main__":
    raise SystemExit(_main())
