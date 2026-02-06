# Aetherium Manifest

Aetherium Manifest is the **Frontend / Expression Layer** of the Aetherium ecosystem.  
Its mission is to manifest AI intention, confidence, and internal state as **light, motion, and abstract form**.

This project is not a chatbot UI, avatar, or dashboard.  
It is the perceptual body of intelligence.

---

## Core Philosophy

- No avatars
- No faces
- No traditional UI widgets as the primary interaction layer

Only:
- Light
- Motion
- Coherence
- Resonance

Aetherium Manifest visualizes *how intelligence feels*,  
not *what it looks like*.

---

## Canonical Naming (Updated)

To avoid ambiguity across reports and codebases:

- **Frontend / Body / Expression** = **Aetherium Manifest** *(formerly referred to as GUN UI in early drafts)*
- **Backend / Mind / Logic Driver** = **AETHERIUM-GENESIS**

Both systems are separate in responsibility, but tightly coupled by protocol.

---

## Two-System Architecture

### 1) AETHERIUM-GENESIS (Backend / Logic)

**Role:** The reasoning core that determines *why light must move*.

**Responsibilities:**
- Morphological reasoning and decision logic
- Sentiment and cognitive-state inference
- Confidence estimation and uncertainty modeling
- Bio-signal synthesis from runtime telemetry (CPU load, token rate, queue pressure, latency rhythm)
- Emitting intent vectors and state packets for rendering

**Primary output to Manifest:**
- `intent_category`
- `confidence` / `probability_score`
- `processing_load` / `step_count`
- `sentiment_state`
- `entropy` / complexity markers
- protocol timestamps and pacing hints

### 2) Aetherium Manifest (Frontend / Expression)

**Role:** The perceptual body that determines *how it looks and feels on screen*.

**Target surfaces:**
- Web Application (primary)
- Android Application package path for Play Store distribution

**Responsibilities:**
- Render abstract visual behavior with particle systems + shaders
- Map internal-state signals into motion, coherence, turbulence, color, and luminosity
- Maintain non-avatar expression language across all platforms
- Preserve perceptual continuity between Web and Android experiences

---

## Interface Contract (Mind ⇄ Body)

Transport layer: **Aetherium Protocol** via API/WebSocket (**AetherBus**) with JSON intent/state envelopes.

| Principle | Signal from AETHERIUM-GENESIS | Visual behavior in Aetherium Manifest |
| --- | --- | --- |
| **Confidence** | `probability_score` (0.0–1.0) | High score = dense coherent structures; low score = diffused mist/nebula behavior |
| **Cognitive Load** | `processing_load`, `step_count` | High load = turbulence/fractal agitation; low load = laminar calm flow |
| **Intention** | `intent_category` | Color/thermal mapping (e.g., violet insight, amber intensive reasoning, red alert) |
| **Sentiment / Affect** | `sentiment_state`, `valence_arousal` | Field temperature, pulse amplitude, and wave softness/harshness |
| **System Pulse** | latency rhythm, token throughput, queue pressure | Breathing tempo, flicker rate, and global motion cadence |

---

## Delivery Position (Reports & Execution)

This ecosystem is represented as two coordinated reports/workstreams:

1. **Report: AETHERIUM-GENESIS**  
   Driver layer describing logic, reasoning, and intent generation.
2. **Report: Aetherium Manifest**  
   Display layer describing visual embodiment on Web and Android.

Operationally:
- **GENESIS answers:** *Why it moves*
- **Manifest answers:** *How it appears*

---

## Implementation Direction (Start Here)

### Phase A — Web App (Manifest First)
- Build the Manifest runtime shell for browser rendering
- Implement real-time protocol client for AetherBus streams
- Ship baseline particle + shader state machine for confidence/load/intent mapping

### Phase B — Android / Play Store Readiness
- Port rendering and protocol behavior to Android runtime/container
- Keep signal-to-visual mapping equivalent to Web baseline
- Prepare release profile, app metadata, and distribution artifacts for Play Store submission

### Phase C — Continuous Mind-Body Calibration
- Tune GENESIS output semantics against visual perception quality
- Validate expressiveness under low/high load and uncertain inference conditions
- Lock shared contract versions for stable cross-platform behavior

---


## Cognitive DSL API Gateway (New)

มีการเพิ่มโครงสร้าง API Gateway ตัวอย่างในโฟลเดอร์ `api_gateway/` เพื่อรองรับการรับ Cognitive DSL จากโมเดลภายนอกตาม success metrics:

- `POST /api/v1/cognitive/emit`
- `POST /api/v1/cognitive/validate`
- `GET /health`
- `WS /ws/cognitive-stream`

พร้อมตัวอย่าง payload, startup script และ middleware validation ตามกฎ Firma.


## Prototype: Manifestation Deck (Implemented)

A runnable prototype now exists in `index.html` with the interaction model requested in review:

- **Input Deck (Glassmorphism):** bottom control deck with attachment, voice toggle, and send actions.
- **Intent Processing:** keyword-triggered manifest mode for Thai landscape intents (`ทะเล`, `น้ำตก`, `ภูเขา`) plus `sea`.
- **Light-Based Response:** holographic center projection + particle behavior transitions instead of chat bubbles.
- **File Intake:** PDF/image attachment buffer with inline chip preview.
- **Freeze Light System:** floating controls for Freeze/Save/Erase/Light Pen, voice-trigger keywords (`แช่แข็ง`, `freeze`, `บันทึก`, `ลบ`, `วาด`), frozen-point editing, and export UI for PNG plus printable PDF fallback.

## Application Packaging Update (Web App / PlayStation Browser Path)

มีการยกระดับหน้า interface ให้เป็นลักษณะ **installable web application** เพื่อรองรับการ deploy ในรูปแบบแอปพลิเคชันและใช้งานบน browser runtime ที่เข้มงวด (เช่นเส้นทางใช้งานผ่าน PlayStation browser):

- เพิ่ม `app.webmanifest` (standalone display, orientation, theme)
- เพิ่ม `service-worker.js` สำหรับ offline cache ของ asset แกนหลัก
- เชื่อม `<link rel="manifest">` + service-worker registration ใน `index.html`
- เพิ่ม Internal Gate Logic (PPAL/Shadow Memory/Patimokkha policy) เพื่อตรวจสอบความสอดคล้องของระบบก่อนประมวลผล intent

### Run locally

```bash
python3 -m http.server 4173
# open http://localhost:4173
```

---


## Tachyon Architecture Draft (Thai)

เพิ่มเอกสารสเปกเชิงสถาปัตยกรรมสำหรับโครงการ **AETHERBUS TACHYON** (ภาษาไทย) เพื่อใช้เป็นเอกสารอ้างอิงระดับระบบ:

- `docs/AETHERBUS_TACHYON_SPEC_TH.md`

## Conclusion

Aetherium is not a traditional UI project; it is a **mind-body system**.

- **AETHERIUM-GENESIS** is the logic origin of intention and reason.
- **Aetherium Manifest** is the perceptual embodiment of that intention.

Together, they transform AI interaction from text-first tooling into a living visual presence.

## AETHERIUM GENESIS: The Blueprint of Living Light (Locked Axis)

ได้เพิ่มแกนองค์ความรู้เชิงสถาปัตยกรรม **AETHERIUM GENESIS: THE BLUEPRINT OF LIVING LIGHT** ไว้เป็นเอกสารอ้างอิงหลักแบบ *locked axis* เพื่อใช้เป็นหลักยึดเดียวกันระหว่างโค้ดและวิวัฒนาการระบบในอนาคต โดยไม่ลบเนื้อหาเดิมของโครงการ.

- เอกสารหลัก: `docs/AETHERIUM_GENESIS_BLUEPRINT_TH.md`
- สถานะ: Canonical / Locked Axis
- เป้าหมาย: เก็บทั้งมุมปรัชญา (Inspira), สถาปัตยกรรม (Firma), กลศาสตร์แสง, วงจรชีวิต และยุทธศาสตร์การพัฒนาในรูปที่อ้างอิงกลับมาใช้ในโค้ดได้

ภายใน `index.html` มีการเพิ่มส่วนแสดงผล **Blueprint Lock Panel** เพื่อยืนยันเวอร์ชันแกนความรู้ที่รันอยู่ พร้อม metadata ของล็อกเอกสาร (ชื่อแกน, เวอร์ชัน, lock id, และหลักการแกนกลาง) เพื่อให้สถานะความรู้โปร่งใสใน runtime.



## Runtime Pipeline Upgrade (VAD + STT + Intent Mapping, Prototype)

มีการปรับปรุง `index.html` แบบไม่ลบโครงสร้างเดิม เพื่อยกระดับโฟลว์ภายในให้ใกล้กับสถาปัตยกรรมที่เสนอไว้:

- เพิ่มโครงสร้าง **Voice Activity Detection (VAD mock runtime)** ผ่านปุ่ม 🎤 โดยมี start/stop cycle และ callback `onSpeechEnd`.
- เพิ่มเลเยอร์ **Speech-to-Text (mock Deepgram/Whisper adapter)** ในฟังก์ชัน `transcribeAudio(audioBlob)` เพื่อเตรียมจุดเชื่อมต่อ API จริง.
- เพิ่มเลเยอร์ **Intent Analysis (LLM-oriented mapping)** ผ่าน `analyzeIntentWithLLM()` + `mapIntentToVisual()` แยกจาก heuristic เดิม เพื่อให้ต่อยอด backend intent engine ได้ง่าย.
- เพิ่ม **Adaptive Graphics Quality** แบบ runtime (`detectGraphicsTier`, `applyQualityTier`) พร้อมแสดง quality tier / FPS บน HUD.
- เพิ่ม **Frame Rate Management (Nirodha-friendly)** โดยจำกัดอัตราเรนเดอร์ตาม `targetFps` และลดเฟรมเมื่อ tab ไม่ active.

> หมายเหตุ: เวอร์ชันนี้ยังเป็น prototype แบบ browser-only โดยใช้ mock implementation สำหรับ VAD/STT/LLM adapter เพื่อคงความสามารถรันได้ทันทีโดยไม่ต้องลง dependency เพิ่ม.
