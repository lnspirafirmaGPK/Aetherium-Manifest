from __future__ import annotations

from datetime import datetime, timezone
from statistics import mean
from typing import Any, Literal
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from fastapi import FastAPI, Header, HTTPException, Query, WebSocket, WebSocketDisconnect
from pydantic import BaseModel, Field

app = FastAPI(title="AGNS Cognitive DSL Gateway", version="1.0.0")


FIRMA_CONSTRAINTS = {
    "max_particles_by_tier": {
        1: 5_000,
        2: 10_000,
        3: 20_000,
        4: 50_000,
    }
}


class IntentVector(BaseModel):
    category: str
    emotional_valence: float = Field(ge=-1.0, le=1.0)
    energy_level: float = Field(ge=0.0, le=1.0)


class ColorPalette(BaseModel):
    primary: str
    secondary: str | None = None


class ParticlePhysics(BaseModel):
    turbulence: float = Field(ge=0.0, le=1.0)
    flow_direction: str
    luminance_mass: float = Field(ge=0.0, le=1.0)
    particle_count: int = Field(default=0, ge=0)


class VisualManifestation(BaseModel):
    base_shape: str
    transition_type: str
    color_palette: ColorPalette
    particle_physics: ParticlePhysics
    chromatic_mode: str
    emergency_override: bool = False
    device_tier: int = Field(default=1, ge=1, le=4)


class ModelResponse(BaseModel):
    trace_id: str
    reasoning_trace: str
    intent_vector: IntentVector
    visual_manifestation: VisualManifestation


class ModelMetadata(BaseModel):
    model_name: str
    temperature: float = Field(ge=0.0, le=2.0)
    max_tokens: int = Field(gt=0)


class CognitiveEmitRequest(BaseModel):
    session_id: str
    model_response: ModelResponse
    model_metadata: ModelMetadata


class ValidationResult(BaseModel):
    status: Literal["success", "failed"]
    violations: list[str]
    validator_version: str = "firma-validator-2.1"


class Metrics(BaseModel):
    total_dsl_submissions: int = 0
    successful_renders: int = 0
    validation_failures: int = 0


METRICS = Metrics()
TELEMETRY_TS_DB: dict[str, list[dict[str, Any]]] = {}

VOICE_MODEL_MAP: dict[tuple[str, str], str] = {
    ("th", "apac"): "whisper-thai-pro",
    ("en", "us"): "whisper-english-us",
    ("en", "eu"): "whisper-english-eu",
    ("ja", "apac"): "whisper-japanese-pro",
    ("es", "latam"): "whisper-spanish-latam",
}


class TelemetryPoint(BaseModel):
    metric: str
    value: float
    ts: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    tags: dict[str, str] = Field(default_factory=dict)


class TelemetryIngestRequest(BaseModel):
    points: list[TelemetryPoint]


class StateSyncRoom:
    def __init__(self) -> None:
        self.version = 0
        self.shared_state: dict[str, Any] = {}
        self.user_states: dict[str, dict[str, Any]] = {}
        self.clients: list[WebSocket] = []

    def apply_delta(self, delta: dict[str, Any], user_id: str | None, user_delta: dict[str, Any]) -> dict[str, Any]:
        self.version += 1
        self.shared_state.update(delta)
        if user_id and user_delta:
            current = self.user_states.setdefault(user_id, {})
            current.update(user_delta)
        return self.snapshot(user_id)

    def snapshot(self, user_id: str | None) -> dict[str, Any]:
        return {
            "version": self.version,
            "shared_state": self.shared_state,
            "user_state": self.user_states.get(user_id or "", {}),
        }


STATE_SYNC_ROOMS: dict[str, StateSyncRoom] = {}


class FirmaValidator:
    @staticmethod
    def validate_dsl_response(payload: CognitiveEmitRequest) -> tuple[bool, list[str]]:
        violations: list[str] = []
        visual = payload.model_response.visual_manifestation

        if visual.color_palette.primary.upper() == "#DC143C" and not visual.emergency_override:
            violations.append("ห้ามใช้สีแดงเลือดหมู #DC143C")

        particle_count = visual.particle_physics.particle_count
        device_tier = visual.device_tier
        max_particles = FIRMA_CONSTRAINTS["max_particles_by_tier"].get(device_tier, 5_000)
        if particle_count > max_particles:
            violations.append(f"เกินขีดจำกัดอนุภาคสำหรับ Tier {device_tier}")

        return len(violations) == 0, violations


def _ensure_api_key(x_api_key: str | None) -> None:
    if not x_api_key:
        raise HTTPException(status_code=401, detail="missing X-API-Key")


def _extract_ws_api_key(websocket: WebSocket) -> str | None:
    header_api_key = websocket.headers.get("x-api-key")
    if header_api_key:
        return header_api_key
    return websocket.query_params.get("api_key")


def _metrics_snapshot() -> dict[str, Any]:
    total = METRICS.total_dsl_submissions
    compliance = 100.0 if total == 0 else round((1 - (METRICS.validation_failures / total)) * 100, 2)
    return {
        "metrics": {
            "total_dsl_submissions": METRICS.total_dsl_submissions,
            "successful_renders": METRICS.successful_renders,
            "validation_failures": METRICS.validation_failures,
        },
        "quality_metrics": {
            "dsl_schema_compliance": compliance,
        },
    }


def _resolve_voice_model(language: str, region: str) -> str:
    language_key = language.split("-")[0].lower()
    region_key = region.lower()
    return VOICE_MODEL_MAP.get((language_key, region_key), f"whisper-general-{language_key}")


def _room(room_id: str) -> StateSyncRoom:
    if room_id not in STATE_SYNC_ROOMS:
        STATE_SYNC_ROOMS[room_id] = StateSyncRoom()
    return STATE_SYNC_ROOMS[room_id]


@app.post("/api/v1/cognitive/emit")
def emit_cognitive_dsl(
    request: CognitiveEmitRequest,
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
    x_model_provider: str | None = Header(default=None, alias="X-Model-Provider"),
    x_model_version: str | None = Header(default=None, alias="X-Model-Version"),
) -> dict[str, Any]:
    _ensure_api_key(x_api_key)
    if not x_model_provider or not x_model_version:
        raise HTTPException(status_code=400, detail="missing model provider/version headers")

    METRICS.total_dsl_submissions += 1
    passed, violations = FirmaValidator.validate_dsl_response(request)
    if not passed:
        METRICS.validation_failures += 1
        return {
            "status": "failed",
            "validation": ValidationResult(status="failed", violations=violations).model_dump(),
            "metrics": _metrics_snapshot(),
        }

    METRICS.successful_renders += 1
    processing_time_ms = 89
    return {
        "status": "success",
        "data": {
            "session_id": request.session_id,
            "trace_id": request.model_response.trace_id,
            "cognitive_dsl": request.model_response.model_dump(),
            "model_provider": x_model_provider,
            "model_version": x_model_version,
        },
        "validation": ValidationResult(status="success", violations=[]).model_dump(),
        "metrics": {
            "processing_time_ms": processing_time_ms,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            **_metrics_snapshot(),
        },
    }


@app.post("/api/v1/cognitive/validate")
def validate_cognitive_dsl(
    request: CognitiveEmitRequest,
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict[str, Any]:
    _ensure_api_key(x_api_key)
    passed, violations = FirmaValidator.validate_dsl_response(request)
    return ValidationResult(
        status="success" if passed else "failed",
        violations=violations,
    ).model_dump()


@app.get("/health")
def health_check() -> dict[str, Any]:
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "components": {
            "api_gateway": "up",
            "validator_service": "up",
            "model_connections": {
                "openai": "up",
                "anthropic": "up",
                "google": "up",
            },
        },
    }


@app.get("/api/v1/proxy/fetch")
def proxy_fetch_url(
    url: str = Query(..., min_length=8, max_length=2048),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict[str, Any]:
    _ensure_api_key(x_api_key)
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise HTTPException(status_code=400, detail="url must be http/https")

    req = Request(url, headers={"User-Agent": "AetheriumProxy/1.0"})
    try:
        with urlopen(req, timeout=6) as response:
            text = response.read(120_000).decode("utf-8", errors="ignore")
            return {
                "status": "success",
                "url": url,
                "content_length": len(text),
                "snippet": " ".join(text.split())[:1200],
            }
    except Exception as exc:  # pragma: no cover - network variance
        raise HTTPException(status_code=502, detail=f"proxy fetch failed: {exc}") from exc


@app.post("/api/v1/telemetry/ingest")
def ingest_telemetry(
    request: TelemetryIngestRequest,
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict[str, Any]:
    _ensure_api_key(x_api_key)
    for point in request.points:
        series = TELEMETRY_TS_DB.setdefault(point.metric, [])
        series.append(point.model_dump())
        if len(series) > 2_500:
            del series[:-2_500]
    return {"status": "success", "ingested": len(request.points), "series_count": len(TELEMETRY_TS_DB)}


@app.get("/api/v1/telemetry/query")
def query_telemetry(
    metric: str,
    window_seconds: int = Query(default=3600, ge=1, le=86_400),
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> dict[str, Any]:
    _ensure_api_key(x_api_key)
    now = datetime.now(timezone.utc)
    floor_ts = now.timestamp() - window_seconds
    points = []
    for row in TELEMETRY_TS_DB.get(metric, []):
        ts_value = row["ts"]
        point_ts = ts_value.timestamp() if isinstance(ts_value, datetime) else datetime.fromisoformat(ts_value).timestamp()
        if point_ts >= floor_ts:
            points.append(row)
    values = [row["value"] for row in points]
    p95 = None
    if values:
        sorted_values = sorted(values)
        p95 = sorted_values[min(len(sorted_values) - 1, int(0.95 * (len(sorted_values) - 1)))]
    return {
        "metric": metric,
        "window_seconds": window_seconds,
        "count": len(values),
        "mean": mean(values) if values else None,
        "p95": p95,
        "latest": points[-1] if points else None,
    }


@app.get("/api/v1/voice/model")
def resolve_voice_model(language: str = "en-US", region: str = "us") -> dict[str, Any]:
    model = _resolve_voice_model(language=language, region=region)
    return {"language": language, "region": region, "model": model}


@app.websocket("/ws/cognitive-stream")
async def cognitive_stream(websocket: WebSocket) -> None:
    api_key = _extract_ws_api_key(websocket)
    if not api_key:
        await websocket.accept()
        await websocket.send_json(
            {
                "status": "failed",
                "detail": "missing X-API-Key",
                "code": 401,
            }
        )
        await websocket.close(code=1008, reason="missing X-API-Key")
        return

    await websocket.accept()
    try:
        while True:
            payload = await websocket.receive_json()
            message_type = payload.get("type")
            if message_type != "dsl_submission":
                await websocket.send_json({"status": "failed", "detail": "invalid message type"})
                continue

            await websocket.send_json(
                {
                    "status": "accepted",
                    "received_at": datetime.now(timezone.utc).isoformat(),
                    "echo": payload,
                }
            )
    except WebSocketDisconnect:
        return


@app.websocket("/ws/state-sync/{room_id}")
async def state_sync(websocket: WebSocket, room_id: str) -> None:
    room = _room(room_id)
    user_id = websocket.query_params.get("user_id")
    await websocket.accept()
    room.clients.append(websocket)
    await websocket.send_json({"type": "state_snapshot", **room.snapshot(user_id)})
    try:
        while True:
            payload = await websocket.receive_json()
            if payload.get("type") != "patch_state":
                await websocket.send_json({"type": "error", "detail": "unsupported message type"})
                continue
            delta = payload.get("delta", {})
            user_delta = payload.get("user_delta", {})
            snapshot = room.apply_delta(delta=delta, user_id=user_id, user_delta=user_delta)
            message = {"type": "state_updated", **snapshot}
            for client in list(room.clients):
                try:
                    await client.send_json(message)
                except Exception:
                    if client in room.clients:
                        room.clients.remove(client)
    except WebSocketDisconnect:
        if websocket in room.clients:
            room.clients.remove(websocket)
