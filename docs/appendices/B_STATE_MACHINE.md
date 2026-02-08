# Appendix B — State Machine (Light-Centric)

## Canonical States
1. `IDLE` — แสงสงบ คงที่
2. `LISTENING` — แสงรับสัญญาณ การเต้นช้าและชัด
3. `THINKING` — เกิด turbulence และการรวมตัวของอนุภาค
4. `RESPONDING` — การแผ่รูปทรงหลัก/จังหวะตอบสนอง
5. `STABILIZED` — การผ่อนแรงกลับสู่สมดุล
6. `NIRODHA` — minimal activity เพื่อประหยัดพลังงานและลด noise

## Transition Rule
การย้ายสถานะต้องอิง input/state จริงจาก contract ไม่ใช่ animation script ล้วน
