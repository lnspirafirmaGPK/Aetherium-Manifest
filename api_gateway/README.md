# AGNS Cognitive DSL API Gateway

เอกสารและโค้ดตัวอย่างสำหรับระบบรับ Cognitive DSL จากโมเดลภายนอก (OpenAI / Anthropic / Google / Custom)

## Endpoints

- `POST /api/v1/cognitive/emit`
- `POST /api/v1/cognitive/validate`
- `GET /health`
- `WS /ws/cognitive-stream`

## Header Requirements

- `X-API-Key` (บังคับทั้ง REST และ WebSocket `/ws/cognitive-stream`)
- `X-Model-Provider` (เฉพาะ emit)
- `X-Model-Version` (เฉพาะ emit)

> สำหรับ WebSocket สามารถส่ง API key ผ่าน header `X-API-Key` หรือ query string `?api_key=...` ระหว่าง handshake ได้

## ตัวอย่างรัน

### 1) โหมดพัฒนาแบบเร็ว (local dev)

```bash
# ต้องมี API key สำหรับเรียกใช้งาน endpoint ที่ป้องกันสิทธิ์
export OPENAI_API_KEY=demo-key

uvicorn api_gateway.main:app --host 0.0.0.0 --port 8080 --reload
```

### 2) โหมดใกล้ production (สคริปต์มาตรฐาน)

```bash
# ต้องตั้งค่าอย่างน้อยหนึ่งคีย์: OPENAI_API_KEY / ANTHROPIC_API_KEY / GOOGLE_API_KEY
./api_gateway/start_cognitive_api.sh
```

> หมายเหตุ: สคริปต์ `start_cognitive_api.sh` ใช้ `uv run uvicorn` พร้อมค่า environment พื้นฐานและ worker หลายตัว จึงเหมาะกับการรันที่ใกล้ production มากกว่าโหมด dev.

## ตัวอย่างทดสอบ

```bash
curl -X POST http://localhost:8080/api/v1/cognitive/validate \
  -H "Content-Type: application/json" \
  -H "X-API-Key: demo-key" \
  -d @api_gateway/sample_emit_payload.json
```


## AetherBusExtreme Utilities

เพิ่มโมดูล `api_gateway/aetherbus_extreme.py` สำหรับงาน low-latency transport:

- Zero-copy socket send (`zero_copy_send` ผ่าน `memoryview`)
- Immutable envelope (`EnvelopeHeader`, `AkashicEnvelope.create`)
- Async queue bus พร้อม backpressure (`AetherBusExtreme`)
- MsgPack serialization (`serialize_to_msgpack`, `deserialize_from_msgpack`)
- NATS async publisher (`NATSJetStreamManager`)
- Deterministic state convergence (`StateConvergenceProcessor`)

รันทดสอบเฉพาะโมดูล:

```bash
python -m unittest api_gateway/test_aetherbus_extreme.py
```
