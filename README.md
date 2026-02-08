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

มีการยกระดับหน้า interface ให้เป็นลักษณะ **installable web application** พร้อมการตั้งค่า manifest, service worker และ asset แกนหลัก เพื่อรองรับการ deploy ในรูปแบบแอปพลิเคชันและใช้งานบน browser runtime ที่เข้มงวด (เช่นเส้นทางใช้งานผ่าน PlayStation browser):

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

## Canonical Documentation Architecture (New)

เพื่อให้ repo อ่านและพัฒนาได้ระยะยาว มีการจัดโครงสร้างเอกสาร Canon ใน `docs/` แบบแยกหมวดมาตรฐาน:

- `docs/README.md` (ศูนย์กลาง Canon)
- `docs/00_PURPOSE_AND_SCOPE.md`
- `docs/01_SYSTEM_OVERVIEW.md`
- `docs/02_COMPONENTS.md`
- `docs/03_INTERFACES.md`
- `docs/04_DATA_SCHEMAS.md`
- `docs/05_ALGORITHMS.md`
- `docs/06_POLICIES.md`
- `docs/07_SAFETY_AND_GOVERNANCE.md`
- `docs/08_TEST_PLAN.md`
- `docs/schemas/*.json` (ABI contracts)
- `docs/appendices/*.md` (glossary/state machine/roadmap)

แนวทางบังคับใช้:
- Canonical docs มีลำดับความสำคัญเหนือ implementation details
- Schema ใดๆ ใน `docs/schemas/` ให้ถือเป็น versioned ABI
- การเปลี่ยน behavior สำคัญต้องอิง `Manifestation Gate`, `Embodiment Contract`, และ `Goal-Lock`

## คำแนะนำการต่อยอดเชิงประสิทธิภาพและความท้าทายเชิงสร้างสรรค์

1. สร้าง `contract-checker` CI step เพื่อ validate payload จริงกับ schema (`akashic_envelope_v2`, `embodiment_v1`, `ipw_v1`) ทุก PR
2. เพิ่ม deterministic replay harness (seed + event log) เพื่อเทียบผล lockstep ระหว่างโหนด
3. ทำ latency perception benchmark แยกจาก raw RTT เพื่อวัดผลตามเป้าหมาย GunUI จริง
4. เพิ่ม “creative stress scenarios” เช่น high-emotion burst / rapid intent switching เพื่อทดสอบ Manifestation Gate ว่าไม่ spam และไม่โกหก state
5. สร้าง knowledge graph ของ intent-to-light mapping จากข้อมูล production anonymized เพื่อปรับ calibration ให้แม่นขึ้นโดยไม่ละเมิด privacy

## Runtime Validation & Calibration Expansion (PR Guardrails)

เพิ่มชุดงานสำหรับยกระดับคุณภาพก่อน merge ทุก PR และต่อยอดการคาลิเบรตเชิง perception:

- **Contract-checker CI:** เพิ่ม workflow `.github/workflows/contract-and-runtime-checks.yml` ให้รันบน `pull_request` เพื่อ validate payload จริงกับ schema ทั้ง `akashic_envelope_v2`, `embodiment_v1`, `ipw_v1` ผ่าน `tools/contracts/contract_checker.py`.
- **Deterministic replay harness:** เพิ่ม `api_gateway/deterministic_replay.py` รองรับ `seed + event log` เพื่อตรวจ lockstep consistency ระหว่างหลายโหนด (state hash ต้องตรงกัน).
- **Latency perception benchmark:** เพิ่ม `tools/benchmarks/latency_perception_benchmark.py` แยกการวัดผล `perceived latency` ออกจาก `raw RTT` เพื่อวัดตามเป้าหมาย GunUI ที่สะท้อนประสบการณ์ผู้ใช้จริง.
- **Creative stress scenarios:** เพิ่ม `tools/benchmarks/creative_stress_scenarios.py` สำหรับกรณี `high-emotion burst` และ `rapid intent switching` เพื่อตรวจ Manifestation Gate ว่าไม่ spam และไม่โกหก state.
- **Intent-to-light knowledge graph (privacy-preserving):** เพิ่ม `tools/benchmarks/intent_light_knowledge_graph.py` เพื่อสร้างกราฟคาลิเบรตจาก production data แบบ anonymized พร้อม k-anonymity threshold.

### Suggested next extensions (for higher performance + creative challenge)

1. เพิ่ม online calibration loop โดย feed edge weights จาก knowledge graph กลับเข้า runtime mapping แบบรายสัปดาห์ พร้อม drift alert เมื่อ mapping เปลี่ยนเกิน threshold.
2. เพิ่ม synthetic adversarial stream generator (เช่น intent oscillation 20Hz) เพื่อ stress-test gate และ benchmark stability envelope.
3. เก็บ perceptual telemetry แบบ privacy-safe (aggregated buckets, no raw text/session IDs) เพื่อเชื่อม metric “felt latency” เข้ากับ release gates ใน CI/CD.
4. ใช้ multi-objective tuning (latency, coherence, truthfulness) สำหรับ auto-calibration เพื่อเลี่ยง optimize เฉพาะ RTT อย่างเดียว.

## Contract Hardening Update (Cadence + Probability Distribution)

อัปเดตเพิ่มเติมเพื่อแก้จุดเสี่ยงจากรีวิวล่าสุดให้พร้อมใช้งานใน PR gate จริง:

- ค่าแนะนำการใช้งาน: `python tools/contracts/contract_checker.py --strict` สำหรับ CI และ `python tools/contracts/contract_checker.py --legacy` สำหรับ compatibility migration.

- เพิ่ม `visual_manifestation.cadence` ใน `embodiment_v1` พร้อมเงื่อนไข `bpm(20-240), phase(0-1), jitter(0-1)` เพื่อคุมจังหวะแสง/แอนิเมชันไม่ให้ drift.
- แยกโหมด contract checker ชัดเจน: **Strict mode (CI/PR gate)** ต้องมี cadence มิฉะนั้น fail ทันที, และ **Legacy mode (runtime/migration)** อนุญาต deterministic cadence injection ตาม phase (`nirodha`, `awakened`, `processing`) พร้อม audit log.
- เพิ่ม `probability_policy` ใน `ipw_v1` เพื่อบังคับ semantics ว่า `predictions[].p` ต้องเป็น probability mass จริง (ไม่ใช่ confidence ลอย ๆ).
- เพิ่ม runtime validation ของผลรวมความน่าจะเป็น (`sum(p)`) พร้อม `epsilon` และ policy `on_violation` (`error` หรือ `normalize`) โดยเมื่อ normalize จะมี audit key เช่น `ipw_validation.audit.normalized=true` และ `ipw_validation.audit.original_sum=...`.

### Suggested next extensions (performance + creative challenge)

1. ต่อ knowledge graph ให้เป็น **phase-aware cadence recommender** (intent + context → cadence profile) เพื่อจูน rhythm แบบ adaptive โดยยังคง deterministic fallback.
2. เพิ่ม **probability drift dashboard** (เช่น KL divergence ของ IPW distribution ราย build) เพื่อจับ quality regression ก่อนขึ้น production.
3. สร้าง **scenario fuzzer** สำหรับ edge cases เช่น extreme jitter, burst reconnect, และ one-action collapse เพื่อยกระดับ challenge ของ Manifestation Gate.
4. ผูก audit trail ของ normalization/cadence injection เข้ากับ release note อัตโนมัติ เพื่อให้ governance ตรวจสอบย้อนหลังได้ง่าย.
5. เพิ่มชุดข้อมูลทดสอบแบบ edge-case library (empty samples, malformed probability vectors, cadence out-of-range) เพื่อให้ regression tests จับบั๊กได้เร็วขึ้นก่อนเข้าระบบจริง.
