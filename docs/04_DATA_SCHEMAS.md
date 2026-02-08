# 04 — Data Schemas

ไฟล์นี้อธิบายเหตุผลของ schema โดย JSON canonical อยู่ใน `docs/schemas/`.

## AkashicEnvelope V2
ฟิลด์สำคัญ:
- `sync_id`: ordering เชิงตรรกะ
- `intent_vector`: embedding สำหรับ prediction-aware routing
- `entropy_seed`: deterministic simulation seed
- `payload_ptr` + `rkey`: zero-copy RDMA payload access
- `ghost_flag`: แยก speculative message ออกจาก canonical flow

## Embodiment Contract V1
แยกเป็นบล็อกสำคัญ:
- intent
- cognitive_state
- temporal_state
- visual_manifestation

เหตุผล: ทำให้ rendering logic ซื่อสัตย์ต่อสถานะการคิดจริง ไม่ผูกติด model vendor

## IPW V1
- predictions เป็น probability distribution เหนือ action space
- collapse threshold ใช้ตัดสิน match/mismatch
- evidence ช่วยอธิบายที่มาของการทำนาย

## ABI Governance
- schema ถือเป็น ABI ระหว่าง cognition ↔ manifestation
- การเปลี่ยน schema ต้อง version และระบุ migration impact
