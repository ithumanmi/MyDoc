---
title: "Code Review Playbook"
description: "Quy trình, checklist và template giúp team review hiệu quả mà không drama."
last_updated: 2026-03-04
---

# 👀 Code Review Playbook cho Web Team

> Review không chỉ là “bắt lỗi”, mà là hàng rào chất lượng cuối cùng trước production. Bài này giúp bạn chuẩn hóa quy trình, tiêu chí và kỹ năng giao tiếp để code review trở thành hoạt động nâng chuẩn, không phải bottleneck.

---

## 0. Mục tiêu & nguyên tắc

| Nguyên tắc | Ý nghĩa | Câu hỏi gợi ý |
| --- | --- | --- |
| **Focus on behavior** | Review behavior (feature, bug) trước, rồi mới bàn implementation | “Feature này đạt acceptance criteria chưa?” |
| **Actionable** | Comment phải rõ ràng, có đề xuất | “Nên dùng debounce tại đây để giảm call API.” |
| **Empathy** | Tấn công vấn đề, không tấn công người | “Chúng ta có thể tách hàm này để dễ test hơn?” |
| **Asynchronous first** | Dùng comment/ Loom/ screenshot trước khi gọi meeting | “Gửi video reproduction thay vì chat chung chung.” |

---

## 1. Quy trình chuẩn

1. **Author chuẩn bị**
   - Rebase, đảm bảo test local pass.
   - Viết PR description: context, ảnh, link Spec/Jira.
   - Liệt kê “Area cần review kỹ”.
2. **Reviewer đọc toàn cảnh**
   - Đọc PR description, chạy app nếu cần.
   - Đọc diff theo từng commit hoặc nhóm file.
3. **Đặt câu hỏi trước, phán xét sau**
   - Hỏi “intent” nếu chưa rõ tại sao code được viết vậy.
4. **Ưu tiên comment blocking trước**
   - Lỗi logic, security, performance → label `blocking`.
   - Style/cải thiện → `nit`/`optional`.
5. **Kết luận rõ ràng**
   - Approve / Request Changes / Comment.
   - Nhắc lại action items.

---

## 2. Checklist reviewer

- [ ] PR description, issue link đầy đủ?
- [ ] Test/Storybook/video demo có? (nếu UI)
- [ ] Naming rõ ràng, tránh viết tắt khó hiểu?
- [ ] Logic mới có test (unit/integration)?
- [ ] Breaking change đã cập nhật doc/config?
- [ ] Security: input validation, authz, secret?
- [ ] Performance: vòng lặp, query, render?
- [ ] Error handling rõ ràng, có fallback?
- [ ] Code reuse: DRY, tránh duplicate?
- [ ] Feature flag/rollback plan nếu cần?

> 💡 Team có thể biến checklist này thành PR template hoặc checklist GitHub.

---

## 3. Checklist author trước khi submit

- [ ] Chạy lint/test, CI local.
- [ ] PR diff < 400 dòng (chẻ nhỏ nếu lớn).
- [ ] Viết mô tả: What/Why/How, ảnh/video.
- [ ] Tự review lần cuối: xem diff như reviewer.
- [ ] Tag reviewer phù hợp domain.

---

## 4. Template comment & label

```md
**Blocking**: Bug hoặc requirement chưa đạt → cần fix trước khi merge.
**Major**: Đề xuất lớn cải thiện design/maintainability.
**Minor/Nit**: Có thể merge nhưng nên cân nhắc.
**Question**: Cần giải thích thêm.
```

Ví dụ:

```md
**Blocking** – Chưa validate role khi gọi API này. Nếu user không phải admin vẫn gọi được.

**Minor** – Có thể dùng `Promise.all` để chạy 2 request song song cho nhanh hơn.

**Question** – Sao mình cần clone object ở đây thay vì mutate trực tiếp?
```

---

## 5. Kỹ năng giao tiếp trong review

- **Mô tả observable fact**: “API trả về 500 khi input rỗng” thay vì “Code này tệ”.
- **Đề xuất hướng giải quyết**: “Chúng ta có thể dùng schema validation (Zod) để bắt case này”.
- **Giữ thread ngắn gọn**: Nếu >5 comment qua lại → hẹn call.
- **Chủ động nhận lỗi khi hiểu sai**: “Tớ hiểu nhầm context, cảm ơn đã giải thích”.

---

## 6. Metrics & automation

| Metric | Cách đo | Mục tiêu |
| --- | --- | --- |
| Lead time review | Thời gian từ mở PR đến approve đầu tiên | < 24h |
| Review depth | Số comment constructive / PR | ≥ 3 comment giá trị |
| Defect escape rate | Bug lọt qua review | Xu hướng giảm |

Automation gợi ý:
- Danger/Reviewdog để enforce PR template, lint.
- GitHub Action ping reviewer nếu 24h chưa phản hồi.
- Codeowners để tự tag reviewer phù hợp.

---

## 7. Anti-pattern & cách xử lý

| Anti-pattern | Triệu chứng | Giải pháp |
| --- | --- | --- |
| PR khổng lồ | 1000+ dòng, reviewer nản | Chia nhỏ theo feature/commit |
| Comment mơ hồ | “Fix đi”, không giải thích | Sử dụng template + mô tả lý do |
| Merge vội | Approve khi chưa đọc kỹ | Thiết lập rule 2 reviewer / CI bắt buộc |
| Defensive author | Reject mọi góp ý | Tổ chức retro, thống nhất mục tiêu chung |
## 8. Ví dụ review thực tế

### 8.1 Pull Request UI Form

**Context:** PR thêm tính năng “Save draft” trên form tạo bài viết. Diff chính:

```diff
 useEffect(() => {
-  if (autoSave) {
-    const id = setInterval(() => saveDraft(form), 5000);
-    return () => clearInterval(id);
-  }
+  if (!autoSave) return;
+  const controller = new AbortController();
+  const id = setInterval(() => saveDraft(form, controller.signal), 5000);
+  return () => {
+    controller.abort();
+    clearInterval(id);
+  };
 }, [autoSave, form]);
```

**Reviewer comment (Major):**

> “`saveDraft` chưa handle abort signal nên vẫn gửi request sau khi unmount → có risk race condition. Đề xuất truyền `controller.signal` vào fetch và check `signal.aborted` trước khi set state.”

**Author phản hồi:**

> “Đã cập nhật `saveDraft` để pass signal vào `fetch` + catch `DOMException`. Cũng thêm unit test cho hook auto save.”

### 8.2 API Endpoint Refactor

**Context:** PR chuyển logic export báo cáo sang service riêng bằng Command pattern.

```diff
-export async function handler(req: Request, res: Response) {
-  const data = await db.query(...);
-  const csv = toCsv(data);
-  await auditLog(user, 'export-report');
-  res.send(csv);
-}
+export async function handler(req: Request, res: Response) {
+  const command = new ExportReportCommand({
+    user: req.user,
+    filter: req.body.filter,
+    storage: new S3Storage(),
+  });
+  const csv = await command.execute();
+  res.send(csv);
+}


**Reviewer comment (Question):**

> “Vì sao mỗi request lại tạo `S3Storage` mới? Có cân nhắc inject qua DI container để reuse connection không?”

**Author phản hồi:**

> “S3 SDK nhẹ nhưng bạn nói đúng – mình đã chuyển qua `storageFactory` để tái sử dụng instance, đồng thời thêm integration test cho `ExportReportCommand`.”

> ✅ Bài học: luôn ghi rõ context, paste diff và gom quyết định vào thread để onboarding sau đọc hiểu được.

---

---

## 8. Bài tập team

1. Chọn 1 PR cũ → thực hành review lại, so sánh với bug đã xảy ra.
2. Viết PR template mới dựa trên checklist.
3. Thiết lập bot nhắc reviewer nếu quá hạn.
4. Tổ chức “Review Kata”: dev A tạo PR giả có bug, dev B review.

> 🎯 Mục tiêu: review trở thành kỹ năng có thể đo lường và cải thiện, giống như coding.

---

**Next Steps:**

- Thêm mục “Code Review” vào onboarding để dev mới hiểu kỳ vọng.
- Định kỳ retro (1 tháng) để cập nhật checklist/metric.

**Remember:** Review tốt không làm chậm team, mà giúp bạn ship nhanh hơn vì ít bug rollback.