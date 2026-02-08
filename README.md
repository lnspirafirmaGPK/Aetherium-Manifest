# Aetherium Manifest

## English Documentation

### Overview
Aetherium Manifest is the frontend expression layer of the Aetherium ecosystem. It visualizes AI intent, confidence, and runtime state through light, motion, and abstract form.

### Architecture
- **AETHERIUM-GENESIS (Backend):** reasoning core, intent generation, telemetry interpretation.
- **Aetherium Manifest (Frontend):** visual embodiment and interaction runtime.
- **Transport:** API/WebSocket contract over AetherBus.

### Current Runtime Capabilities
- Real-time particle/shape rendering mapped from intent vectors.
- Voice interaction pipeline (VAD mock + STT mock + intent mapping).
- Adaptive quality tier and frame-rate management.
- Accessibility-focused controls with visual microphone feedback.
- Window manager for all HUD panels:
  - close (✕) per panel
  - reopen from Settings > Panels
  - drag-to-move and resize
- Settings with 5 tabs: `Display`, `Panels`, `Links`, `Language`, `Voice`.
- External URL analysis entry point in Settings (`Analyze URL`).
- Event-driven command bus + telemetry counters + delta-state patch helper.

### API Gateway (Prototype)
The `api_gateway/` folder includes a sample Cognitive DSL gateway:
- `POST /api/v1/cognitive/emit`
- `POST /api/v1/cognitive/validate`
- `GET /health`
- `WS /ws/cognitive-stream`

### AetherBusExtreme Utilities
`api_gateway/aetherbus_extreme.py` includes:
- Zero-copy socket send (`memoryview`)
- Immutable envelope models
- Async queue bus with backpressure
- MsgPack helpers
- NATS async manager
- State convergence processor

### Run Locally
```bash
python3 -m http.server 4173
# open http://localhost:4173
```

### Recommended Next Steps
- ✅ Added server-side URL ingestion proxy endpoint (`/api/v1/proxy/fetch`) to avoid browser CORS limitations.
- ✅ Added telemetry ingest/query endpoints (`/api/v1/telemetry/*`) as a lightweight time-series store for UX performance analysis.
- ✅ Added locale bundles (`en`, `th`, `ja`, `es`) as external JSON resources loaded dynamically at runtime.
- ✅ Added language/region based voice-model resolver (`/api/v1/voice/model`) and frontend region selector.
- ✅ Added deterministic multi-client state sync WebSocket (`/ws/state-sync/{room_id}`) with shared + user-specific deltas.

---

## เอกสารภาษาไทย

### ภาพรวม
Aetherium Manifest คือเลเยอร์แสดงผลฝั่ง Frontend ของระบบ Aetherium โดยแปลงเจตนาและสถานะของ AI ให้เป็นภาพเคลื่อนไหวเชิงนามธรรม

### โครงสร้างระบบ
- **AETHERIUM-GENESIS (Backend):** คิด วิเคราะห์ และสร้าง intent
- **Aetherium Manifest (Frontend):** แสดงผลและโต้ตอบผู้ใช้
- **การเชื่อมต่อ:** ผ่าน API/WebSocket บน AetherBus

### ความสามารถปัจจุบัน
- ระบบแสดงผลแบบเรียลไทม์ด้วยอนุภาคและรูปทรงตาม intent
- Voice pipeline (VAD/STT แบบ mock) + intent mapping
- ปรับคุณภาพกราฟิกตามเครื่องและจัดการเฟรมเรต
- ปุ่มควบคุมที่เป็นมิตรต่อการเข้าถึง (Accessibility)
- HUD ทุกหน้าต่างมีปุ่มปิด เปิดคืนได้จาก Settings และลาก/ย่อ-ขยายได้
- Settings แบ่ง 5 แท็บ: `Display`, `Panels`, `Links`, `Language`, `Voice`
- มีช่องวิเคราะห์ลิงก์ URL ภายนอก
- มีโครง telemetry + event bus + delta-state สำหรับต่อยอด

### API Gateway (ต้นแบบ)
โฟลเดอร์ `api_gateway/` มีตัวอย่าง Cognitive DSL gateway พร้อม endpoint สำหรับ emit/validate/health/websocket

### แนวทางต่อยอด
- ✅ ทำ URL proxy ฝั่งเซิร์ฟเวอร์ผ่าน `/api/v1/proxy/fetch` เพื่อลดปัญหา CORS
- ✅ เก็บ telemetry ลง time-series store ผ่าน `/api/v1/telemetry/ingest` และสรุปผลผ่าน `/api/v1/telemetry/query`
- ✅ ทำ i18n แบบแยกไฟล์ภาษาใน `locales/*.json` และโหลดแบบ dynamic
- ✅ เลือกโมเดลเสียงตามภาษา/ภูมิภาคผ่าน `/api/v1/voice/model` และตัวเลือกภูมิภาคในหน้า Settings
- ✅ เพิ่ม state sync แบบ deterministic สำหรับหลายผู้ใช้ด้วย `/ws/state-sync/{room_id}`


## Extension Ideas
- Add persisted TSDB backend (InfluxDB/TimescaleDB) with retention + downsampling policies.
- Add proxy allowlist/denylist + content-type and size guardrails for stronger SSRF safety.
- Add locale QA checks (missing key scanner + pseudolocale) in CI.
- Add voice A/B routing and collect WER / latency metrics by language-region cohort.
- Add CRDT merge (Yjs/Automerge) for conflict-free collaborative editing beyond simple delta updates.
