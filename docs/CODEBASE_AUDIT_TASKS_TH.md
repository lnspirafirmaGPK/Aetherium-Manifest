# Codebase Audit: ข้อเสนอแผนงานแก้ไข (Thai)

เอกสารนี้สรุปผลการตรวจสอบโค้ดเบื้องต้น และเสนอ "งานแก้ไข" อย่างละ 1 งาน ตามหมวดที่ร้องขอ

## 1) งานแก้ไขข้อความพิมพ์ผิด (Typo Fix)

**ปัญหาที่พบ**
- ใน `README.md` มีข้อความผิดรูปแบบ/ผิดพิมพ์จากการตัดข้อความค้างกลางประโยค:
  - `**installable web application**…245 chars truncated…ง asset แกนหลัก`
- ข้อความลักษณะนี้ทำให้เอกสารไม่เป็นมืออาชีพ และอ่านบริบทส่วนอัปเดตแพ็กเกจแอปไม่รู้เรื่อง

**หลักฐานอ้างอิง**
- `README.md` (ช่วงหัวข้อ Application Packaging Update)

**งานที่เสนอ**
- แก้ข้อความให้เป็นประโยคสมบูรณ์ เช่น:
  - "มีการยกระดับหน้า interface ให้เป็นลักษณะ installable web application พร้อมการตั้งค่า manifest, service worker และ asset แกนหลักสำหรับการใช้งานแบบ PWA"
- ตรวจทั้งไฟล์ `README.md` รอบเดียวเพื่อกำจัดอาการข้อความตัด/encoding เพี้ยนเพิ่มเติม

---

## 2) งานแก้ไขบั๊ก (Bug Fix)

**ปัญหาที่พบ**
- WebSocket endpoint (`/ws/cognitive-stream`) ไม่มีการตรวจสอบ `X-API-Key` ขณะที่ REST endpoints ใช้ `_ensure_api_key(...)` บังคับคีย์
- ส่งผลให้ช่องทางสตรีมสามารถเชื่อมต่อได้โดยไม่ผ่านการยืนยันตัวตน ซึ่งเป็นช่องโหว่ด้านการควบคุมสิทธิ์

**หลักฐานอ้างอิง**
- มีการบังคับ API key ใน `emit` และ `validate`
- ไม่มีการเช็ก API key ใน `cognitive_stream`

**งานที่เสนอ**
- เพิ่มการตรวจ API key ใน WebSocket handshake (เช่น อ่านจาก header/query แล้ว reject connection เมื่อไม่มีคีย์)
- กำหนดรูปแบบ error response ของ websocket ให้สอดคล้องกับ REST (`401` semantics)

---

## 3) งานแก้ความคลาดเคลื่อนของเอกสาร (Documentation Discrepancy)

**ปัญหาที่พบ**
- ใน `api_gateway/README.md` มีตัวอย่างรันด้วย `uvicorn ...` โดยตรง แต่ในสคริปต์ `start_cognitive_api.sh` ใช้ `uv run uvicorn ...` และมีเงื่อนไขว่าต้องมี API key อย่างน้อยหนึ่งตัว
- ผู้ใช้ใหม่ที่ทำตาม README อาจรันได้ แต่ไม่รู้เงื่อนไขความพร้อมของ environment แบบเดียวกับ production/start script

**หลักฐานอ้างอิง**
- `api_gateway/README.md` ส่วน "ตัวอย่างรัน"
- `api_gateway/start_cognitive_api.sh` ส่วนตรวจ API key + คำสั่ง `uv run uvicorn`

**งานที่เสนอ**
- ปรับ README ให้บอกทั้ง 2 โหมดอย่างชัดเจน:
  1) โหมดพัฒนาแบบเร็ว (`uvicorn`)
  2) โหมดใกล้ production (`./api_gateway/start_cognitive_api.sh`)
- เพิ่มโน้ตเรื่อง environment variables ที่จำเป็นก่อนสตาร์ต

---

## 4) งานปรับปรุงการทดสอบ (Test Improvement)

**ปัญหาที่พบ**
- ปัจจุบันยังไม่มี automated test สำหรับ security behavior ของ WebSocket endpoint (`/ws/cognitive-stream`)
- ทดสอบส่วน `AetherBusExtreme` มีอยู่แล้ว แต่ฝั่ง API ยังขาดเคส auth ที่สำคัญ

**หลักฐานอ้างอิง**
- มีชุดทดสอบใน `api_gateway/test_aetherbus_extreme.py`
- ยังไม่พบไฟล์ทดสอบสำหรับ FastAPI endpoints/websocket auth

**งานที่เสนอ**
- เพิ่ม `pytest` + `fastapi.testclient` test อย่างน้อย 2 เคส:
  - websocket connection แบบไม่มี API key ต้องถูกปฏิเสธ
  - websocket connection แบบมี API key ต้องเชื่อมต่อได้และได้ response ตามสัญญา
- เพิ่ม test สำหรับ `POST /api/v1/cognitive/emit` เคส header ไม่ครบ เพื่อป้องกัน regression

