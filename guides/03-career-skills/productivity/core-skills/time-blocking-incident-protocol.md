# 🧯 Time-Block Incident Protocol (Runbook 3 tầng)

> Dùng khi “time block” liên tục bị phá (interruptions, energy mismatch, dependency delay), và troubleshooting thông thường không đủ.

## 1) Khi nào coi là “time-block incident”?
- Block bị phá/tách khỏi planned schedule **> 1 lần** trong cùng một ngày.
- Energy mismatch kéo dài: block deep work bị cạn pin hoặc tụt focus rõ rệt.
- Dependency delay: công việc phụ thuộc bị kẹt làm block không thể tiến tới outcome.
- Planned vs done lệch: bạn ghi “đã xong” nhưng thực tế chỉ xong một phần/khác kỳ vọng.

## 2) Root Cause Taxonomy (gắn nhãn nhanh)
- **Interruption:** bị ngắt giữa chừng (chat, họp đến trễ, fire request).
- **EnergyMismatch:** thời điểm sai với nhịp năng lượng; deep block ở lúc “pin thấp”.
- **DependencyDelay:** thiếu input/permission/data; không có đường đi tiếp.
- **Overplanning:** lên lịch quá chặt, không chừa buffer hoặc WIP không thực tế.
- **ContextSwitchLeak:** bạn “bước ra” khỏi block quá dễ và bị kéo vào việc khác.

Mẹo: mỗi incident chỉ chọn **1 root cause chính** (tối đa 2) để xử lý rõ.

## 3) Runbook 3 tầng (2–5 phút / 20–30 phút / sau ngày)

### Tầng 1: Trong block (2–5 phút) - STOP & Router
1. **STOP:** dừng làm trong 30–60 giây để ngắt vòng phản xạ.
2. **Ghi 1 dòng reason tag:** `Interruption` / `EnergyMismatch` / `DependencyDelay` / `Overplanning` / `ContextSwitchLeak`.
3. **Chọn route:**
   - **Salvage:** vẫn tiến được một phần deliverable (micro-outcome).
   - **Swap:** đổi sang task cùng “mức shallow” phù hợp năng lượng/context hiện tại.
   - **Abort:** dừng block, chuyển phần còn lại sang lịch/hệ thống để tránh phí thêm.
4. **Update immediate next action:** viết 1 câu “làm gì tiếp trong 10 phút tới”.

### Tầng 2: Cùng ngày (20–30 phút) - Regroup & Replan
1. **Xác định remaining work:** còn lại bao nhiêu phần và phần nào không còn phụ thuộc?
2. **Replan block remaining:** chọn 1 trong:
   - kéo dài block,
   - chia thành 2 block (deep → shallow),
   - chuyển thành task với deadline cụ thể.
3. **Update owner / input status (nếu phụ thuộc):** gửi 1 ping có ngữ cảnh + câu hỏi chốt.
4. **Gắn “done definition” cho phần có thể xong hôm nay:** tránh mập mờ khiến incident lặp.

### Tầng 3: Sau ngày (10 phút) - Planned vs Done & Guardrail
1. Điền **Planned vs Done sheet** (mục 4) cho block bị phá.
2. Chọn 1 guardrail sẽ thay đổi cho lần sau:
   - thêm buffer,
   - đổi khung giờ,
   - thiết lập “dependency check” trước khi bắt đầu block,
   - thiết kế lại tên block = outcome.
3. Nếu incident thuộc hệ thống (root cause lặp lại 2+ lần/tuần): thêm vào IA “Change Log” hoặc decision note.

## 4) Planned vs Done block sheet (copy/paste)
Điền sau mỗi incident để biến “cảm giác” thành dữ liệu.

| Field | Value |
|---|---|
| Block name |  |
| Planned start/end |  |
| Actual start/end |  |
| Done (planned) |  |
| Done (actual) |  |
| Root cause tags | (Interruption / EnergyMismatch / DependencyDelay / Overplanning / ContextSwitchLeak) |
| Salvage route | Salvage / Swap / Abort |
| Next action | (1 việc vật lý tiếp theo + link/spec) |
| Next review date | (ngày xem lại) |

## 5) Drills (7 ngày) - tạo nhịp phản hồi nhanh
- **Mỗi ngày 1 lần:** ghi 1 incident nếu block bị phá (hoặc giả lập nếu ngày đó “suôn”).
- **Mỗi ngày 1 lần:** chọn 1 guardrail thay đổi nhỏ và áp dụng ngay cho block tiếp theo.
- Cuối ngày 7: nhìn tần suất root cause chính để biết guardrail nào “đáng tiền”.

## 6) Tham chiếu chéo
- Time blocking troubleshooting cơ bản: `time-blocking.md`
- Cách biến decision lớn thành note có cấu trúc: `templates/decision-journal.md`

