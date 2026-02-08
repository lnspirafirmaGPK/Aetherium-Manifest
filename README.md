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
- Add a server-side URL ingestion proxy to avoid browser CORS limitations.
- Store telemetry in a time-series backend and add UX/latency dashboards.
- Add locale bundles (`en`, `th`, `ja`, `es`) through dynamic i18n resources.
- Route voice mode to specialized multilingual ASR models.
- Add deterministic multi-client state sync (CRDT/OT).

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
- ทำ URL proxy ฝั่งเซิร์ฟเวอร์เพื่อลดปัญหา CORS
- เก็บ telemetry ลง time-series DB เพื่อวิเคราะห์ประสิทธิภาพ UX
- ทำ i18n แบบแยกไฟล์ภาษา
- เลือกโมเดลเสียงตามภาษา/ภูมิภาค
- เพิ่ม state sync แบบ deterministic สำหรับหลายผู้ใช้
