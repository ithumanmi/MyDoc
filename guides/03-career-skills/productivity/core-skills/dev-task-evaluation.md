# 🧮 Dev Task Evaluation & Measurement

> [← Back to Productivity Core Skills](./README.md) | [Tech KPI Framework](../../../02-wealth-business/entrepreneurship/operations/tech-kpi-framework.md)

**Mục tiêu:** Giúp Technical Lead/PM/Dev đánh giá và đo lường tasks một cách định lượng, cân bằng giữa tốc độ và chất lượng.

---

## 1. Tại sao phải đo?

| Hệ quả nếu chỉ “ước lượng cảm tính” | Lợi ích khi đo lường chuẩn |
| --- | --- |
| Deadline vỡ do scope creep | Biết rõ effort vs impact, ưu tiên chính xác |
| Dev kiệt sức, burn-out | Phân bổ nguồn lực hợp lý 70/20/10 |
| Tech debt tăng, bug leak | Có cảnh báo sớm qua Stability KPI |

---

## 2. Framework đánh giá Task

### 2.1 Impact × Effort Grid
- **Impact:** Lợi ích kinh doanh/khách hàng (Revenue, Retention, Risk giảm...).
- **Effort:** Thời gian + độ phức tạp kỹ thuật (Story Points/Person-days).
- Ưu tiên theo 4 nhóm: **Quick Win**, **Strategic Bets**, **Fill-in**, **Drop**.

### 2.2 Definition of Done (DoD)
Tạo checklist DoD cho từng loại task:
- Code review chéo? ✅
- Unit test/Integration test? ✅
- Tài liệu cập nhật? ✅
- Monitoring/Alert cấu hình? ✅

### 2.3 Risk Score
- **Complexity:** số service ảnh hưởng, logic business.
- **Dependency:** chạm module core hay không.
- **Rollback difficulty:** dễ/khó revert.
> Dùng thang 1-5, task >12 điểm yêu cầu Tech Lead review trước khi start.

---

## 3. Đo lường tiến độ & chất lượng

### 3.1 Throughput & Flow Metrics
- **Cycle Time:** Từ lúc “In Progress” đến “Done”.
- **Lead Time:** Từ khi task được yêu cầu đến khi deliver.
- **WIP Limit:** Mỗi dev không quá 2 task đang làm để tránh context switching.

### 3.2 Stability Metrics
- **Bug Leak Rate** = Bugs Prod / Total Bugs.
- **Mean Time to Recovery (MTTR).**
- **Change Failure Rate:** % deployments phải rollback.

### 3.3 Value Metrics
- % task đóng góp vào mục tiêu OKR (ví dụ Revenue Growth, giảm churn).
- Customer feedback score sau khi tính năng live.

---

## 4. Dashboard mẫu (Notion/Jira/Linear)

| Cột | Nội dung |
| --- | --- |
| Task | Link Jira/Linear + mô tả ngắn |
| Impact (1-5) | Từ nhận định PM/Product |
| Effort (Story Points) | Đánh giá bởi dev chịu trách nhiệm |
| Risk Score | Complexity + Dependency + Rollback |
| Owner | Dev chính |
| Status | Backlog / In progress / Review / Done |
| Cycle Time | Auto tính từ status change |
| Notes | Blockers, quyết định quan trọng |

> **Automation:** Sync status từ Jira → Notion/Trello bằng Zapier/Make để lãnh đạo theo dõi real-time.

---

## 5. Ritual đo lường hằng tuần

1. **Sprint Planning:**
   - Review Impact × Effort.
   - Chốt WIP theo capacity thực tế (trừ buffer bug/ops).
2. **Daily Standup + Flow Review:**
   - So sánh Cycle Time từng task với benchmark.
   - Nếu task đứng yên >2 ngày ⇒ escalated.
3. **Sprint Review/Retrospective:**
   - Report DORA metrics.
   - Chốt hành động giảm tech debt/ cải thiện quy trình.

---

## 6. Checklist triển khai

- [ ] Có template DoD cho từng loại task (feature, bug, infra)?
- [ ] Dashboard đo Impact / Effort / Cycle Time cập nhật tự động?
- [ ] KPI Stability (Bug Leak, MTTR) gắn vào thưởng/phạt?
- [ ] Lịch review Tech Debt tối thiểu 1 lần/tháng?
- [ ] Team hiểu cách phân bổ 70/20/10 giữa Feature – Debt – R&D?

---

**Next Step:** Embed dashboard vào workspace, bật cảnh báo khi task vượt cycle time chuẩn, và align với Product/Business để mọi người nói chung “ngôn ngữ số”.