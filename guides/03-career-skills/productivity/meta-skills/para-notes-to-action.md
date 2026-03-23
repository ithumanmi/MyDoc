# 🗂️ Ghi chú nhiều CHƯA CHẮC nhớ lâu – Dùng PARA để biến note thành hành động

> Hết cảnh “note chất đầy nhưng không dùng được”. PARA xoay quanh **actionability**: mọi ghi chú phải gắn với dự án, trách nhiệm, hoặc quyết định sắp tới.

## 1) Vấn đề thường gặp
- Ghi chép dày nhưng không quay lại xem → kiến thức chết.
- Lưu theo **chủ đề** (topic) nên khó tìm khi cần **ra quyết định/hành động**.
- Không có cầu nối từ note → task → lịch → deliverable.

## 2) PARA: cấu trúc tối giản (Projects · Areas · Resources · Archives)
- **Projects:** Đang làm, có deadline/output rõ (ví dụ: “Ship demo cho publisher”, “Viết postmortem”).
- **Areas:** Trách nhiệm dài hạn (Sức khỏe, Tài chính, Career Growth, Team Ops).
- **Resources:** Tham khảo/ý tưởng, không áp lực phải dùng ngay (Shader tips, UX patterns, Funding models).
- **Archives:** Đã xong/không còn ưu tiên.

### Quy tắc gán nhanh
1) Câu hỏi: “Note này phục vụ **Project** nào?” → nếu không, chuyển xuống **Area** (nếu thuộc trách nhiệm) → nếu vẫn không, để **Resources**.
2) Nếu 30 ngày không đụng tới, cân nhắc **Archive**.

## 3) Biến ghi chú thành hành động (Note → Task → Lịch → Deliverable)
1) **Capture:** Ghi ngắn, 1-3 bullet, kèm context (link, ảnh). Không cần sạch đẹp.
2) **Classify:** Ngay khi xong buổi đọc/họp, gán PARA + tag **Next Action? (Y/N)**.
3) **Distill:** 3 gạch đầu dòng “Essence / How to use / Where to apply”.
4) **Express:**
   - Nếu có action trong 7 ngày → tạo task (có chủ, deadline). 
   - Nếu cần slot sâu → block lịch (90’ deep work) và link note vào calendar entry.
   - Nếu cần quyết định nhóm → đưa vào agenda họp, đính note.

**Template 1 note → 1 action:**
- Essence: …
- How to use: …
- Next Action: [task/tool/link] + deadline + owner.

## 3.5) Decision Tree: Next Action? (task / calendar / meeting / wait)
Quy tắc: hỏi “Trong 7 ngày tới, note này cần tạo ra gì để giảm khổ/đẩy dự án/ra quyết định?”

```text
Trong 7 ngày tới note này cần ra output gì?
├─ Làm được một việc cụ thể (<= 2h), kết thúc rõ -> Task
├─ Cần một block sâu (ít bị gián đoạn), cần tập trung cao -> Calendar block
├─ Cần quyết định/align với người khác -> Meeting agenda (pre-read + câu hỏi chốt)
└─ Chưa đủ dữ liệu hoặc chưa đúng thời điểm -> Waiting / Reference
```

Phrasing ngắn để bạn dùng ngay:
- `Task:` “Trong tuần này, mình sẽ hoàn thành ___ để ___.”
- `Calendar block:` “Mình dành ___ phút để tạo ___ (input: ___; output: ___).”
- `Meeting agenda:` “Agenda: ___ (quyết định cần ra: ___). Pre-read: ___.”
- `Waiting/Reference:` “Chờ đến khi ___ vì hiện tại thiếu ___ / chưa tới ngưỡng thời điểm.”

## 3.6) Next Action Templates (copy/paste)
### Task:
- `Next Action:` ___
- `Owner:` (ai làm)
- `Deadline:` (ngày/giờ)
- `Done when:` (tiêu chí hoàn tất 1 câu)
- `Inputs/Links:` ___

### Calendar block:
- `Block:` ___ phút vào (ngày giờ)
- `Goal:` (1 câu)
- `Inputs:` (note/link/spec)
- `Output:` (deliverable cụ thể)
- `Exit criteria:` (ví dụ: xong prototype / xong outline / xong draft)

### Meeting agenda:
- `Meeting goal:` (quyết định gì)
- `Question(s) to answer:` 1–3 câu
- `Pre-reading:` link note + 3 gạch đầu dòng “cái gì cần biết trước”
- `Owner of decision:` ai chịu trách nhiệm chốt

### Waiting / Reference:
- `Waiting for:` ___ (điều kiện cần xảy ra)
- `Trigger to resume:` khi có ___ thì quay lại
- `Reason:` thiếu dữ liệu gì / chưa đúng timing nào
- `Next check:` ngày hẹn (để khỏi treo vĩnh viễn)

## 3.7) Mini failure modes (và cách sửa nhanh)
- `Note -> Action mơ hồ:` Next Action không nói rõ deliverable -> sửa bằng cách viết lại “Done when” 1 câu.
- `Action -> late:` Task tạo ra nhưng không có deadline/owner rõ -> gắn owner + deadline + lý do ưu tiên 1 dòng.
- `Bloat resources:` Note để Resources nhưng không có “Where to use?” -> quay về rule: nếu 30 ngày không dùng, Archive.

## 4) Dashboard PARA (tuỳ công cụ)
- **Notion/Obsidian:** 4 database/folder: Projects, Areas, Resources, Archives. View chính = Projects (Kanban/Board), mỗi card link note liên quan.
- **Calendar:** Với task quan trọng, tạo event “Deep Work: <Project>” 90-120’ và attach note.
- **Task app:** Sync từ Projects → task (chỉ giữ 1 inbox chính). 

## 5) Nghi thức hằng tuần (30’)
- Duyệt **Projects**: chọn 3 mục tiêu tuần; mỗi mục tiêu 1-2 task cụ thể.
- Duyệt **Areas**: có trách nhiệm nào xuống cấp? (Health, Finance, Team). Tạo 1 task bảo trì.
- Duyệt **Resources**: chọn 1-2 note áp dụng ngay vào Project/Area; còn lại Archive dần.
- Gom note rời → distill 3 dòng hoặc liên kết sang Projects.

## 6) Anti-bloat (chống phình note)
- Chỉ giữ thứ **gây ấn tượng mạnh** (resonate). 
- Mỗi note phải có **“Where to use?”**; nếu không trả lời được → Archive.
- Mỗi tuần xóa/dọn 10-20% Resources cũ hoặc di chuyển vào Archives.

## 7) Ví dụ thực chiến (Game Dev)
- Đọc bài “LiveOps event cadence”: Distill 3 bullet → gán Project “Seasonal event Q2” → tạo task “Mock event metrics” (deadline thứ Sáu) và block lịch 90’.
- Học shader mới: Note vào Resources + tag “rendering”; khi có Project “VFX cho boss fight”, kéo note vào Projects và tạo subtask “Prototype shader”.

## 8) Quick start (10 phút thiết lập)
1) Tạo 4 folder/DB: Projects, Areas, Resources, Archives.
2) Bốc 5 note quan trọng nhất → gán vào Projects/Areas.
3) Chọn 1 Project, tạo 2 task + 1 block lịch. Đính note vào calendar.
4) Lên lịch Weekly Review 30’ (nhắc lặp).

> Nhắc mình: Ghi chú chỉ có giá trị khi dẫn tới quyết định, hành động, hoặc sản phẩm. PARA = cầu nối từ tri thức → output.