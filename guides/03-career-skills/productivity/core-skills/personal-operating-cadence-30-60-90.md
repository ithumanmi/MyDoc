# 🗓️ Personal Operating Cadence 30/60/90 (Operating Loop có nhịp)

> Mục tiêu: vận hành bền bằng cách biến “plan → execute → review → adjust” thành một lịch cố định theo mốc 30/60/90 ngày.

## 0) Operating unit: “Incident → Guardrail”
Quy tắc xương sống: mọi lần hệ thống bị phá (block bị phá, planned vs done lệch, note không ra action, decision mơ hồ) đều phải trả về:
- 1 incident sheet
- 1 planned vs done update
- 1 change/guardrail nhỏ (đổi điều kiện nền hoặc quy tắc xử lý)

## 1) Tuần 0 (Baseline chung cho cả 30/60/90)
- Chọn 1–2 chỉ số baseline:
  - Deep work hours/tuần
  - Planned vs Done rate (%)
  - Tần suất incident theo taxonomy (root cause tags)
- Chuẩn hóa nơi lưu:
  - Incident sheet: theo quy ước ở `time-blocking-incident-protocol.md`
  - Decision/change note: `templates/decision-journal.md`

## 2) 30 ngày: Audit + Incident taxonomy (làm rõ hệ thống đang “gãy” ở đâu)
### Mục tiêu
- Biết incident nào xảy ra nhiều nhất.
- Có 1 protocol tối thiểu để xử lý trong 5 phút (runbook 3 tầng).

### Deliverables (kết thúc ngày 30)
1. Incident taxonomy sheet (top root cause 1–2 cái).
2. 1 guardrail update đã áp dụng (ví dụ đổi route Salvage/Swap/Abort, thêm dependency check).
3. Bộ planned vs done sheet copy/paste để ghi chuẩn.

### Checklist 30 ngày (nhanh)
- [ ] ≥ 7 incident entries (hoặc giả lập nếu ngày ổn).
- [ ] ≥ 3 guardrail changes đã áp dụng.
- [ ] Weekly review có so sánh Planned vs Done.

## 3) 60 ngày: Cải guardrails + chuẩn hóa templates (giảm tần suất “gãy”)
### Mục tiêu
- Tối ưu điều kiện nền (guardrails) để incident giảm.
- Encoding templates vào workflow hằng ngày (startup/shutdown + planned vs done).

### Deliverables (kết thúc ngày 60)
1. Update template daily shutdown (Planned vs Done + next guardrail).
2. 1 quyết định hệ thống được ghi bằng Decision Journal (để biến học thành quy tắc).
3. Một phần IA được “đủ để tìm <30s” (Global Index 3 lớp).

### Checklist 60 ngày
- [ ] Incident frequency giảm (so với baseline).
- [ ] Mỗi tuần có tối thiểu 1 protocol tweak (guardrail/procedure).
- [ ] Không còn “note-only” cho những thay đổi có tác động.

## 4) 90 ngày: Systematize (SOP hóa 1–2 việc lặp)
### Mục tiêu
- Biến quy trình xử lý incident thành SOP.
- Liên kết operating cadence với IA: decision/change log và incident sheet đều có lifecycle.

### Deliverables (kết thúc ngày 90)
1. Operating Manual dạng 1 trang/1 repo page:
   - Protocol incident 3 tầng
   - Planned vs Done template + nơi ghi
   - Weekly review checklist
   - Global Index rule + convention linking
2. SOP 1–2 việc lặp:
   - Ví dụ: “Weekly planning + scheduled regroup khi dependency delay”

### Checklist 90 ngày
- [ ] Hệ thống chạy “ít cần ý chí” hơn.
- [ ] Có SOP/Operating Manual để onboarding (hoặc tự kiểm).

## 5) Cadence: lịch mẫu (có thể copy)
### Mỗi tuần (30–45 phút)
- Weekly review (PARA/Projects tùy bạn dùng) + planned vs done snapshot.
- Chọn 1 guardrail để thay đổi nhỏ tuần tới.

### Mỗi ngày (1 phút)
- Startup 60 giây: 1–3 MITs + sync planned block names.
- Shutdown 60 giây: planned vs done 1 dòng/block + next guardrail.

### Mỗi mốc (30/60/90)
- Viết 1 page “System Delta”:
  - cái gì giảm/gãy ít hơn
  - cái gì vẫn gãy
  - thay đổi guardrail tiếp theo

## 6) Tham chiếu nhanh
- Runbook incident 3 tầng: `time-blocking-incident-protocol.md`
- Daily startup/shutdown + planned vs done: `personal-work-framework.md`
- IA Decision/Change Log + Global Index: `information-architecture-playbook.md`

> Nhắc mình: Operating cadence không phải để kiểm soát, mà để tạo điều kiện cho hiệu suất bền vững.

