# 🧪 Lộ trình nghiên cứu & thử nghiệm Micro-SaaS / Side Project

> “Làm sao để biết ý tưởng micro-SaaS đáng theo đuổi?” – Bắt đầu từ việc hiểu vấn đề, thử nghiệm microskill nhanh, scale dần theo dữ liệu.

## 1. Cài đặt tư duy & KPI

| Khung | Mô tả | Gợi ý |
| --- | --- | --- |
| **Global Problem First** | Chọn ngách có nhu cầu thực, tốt hơn là nhu cầu tăng trưởng (ví dụ: automation cho creator, workflow AI) | Đọc [`product-market-fit.md`](./product-market-fit.md), [`indie-hacker-roadmap.md`](../career/indie-hacker-roadmap.md) |
| **Micro-Learning** | Cố định 6-8 tuần thử nghiệm, chia nhỏ thành sprint 2 tuần | KPI: 30 cuộc phỏng vấn / 2 sprint, 2 thử nghiệm MVP nhỏ |
| **Revenue Target** | Micro-SaaS: ~1-5k$/tháng trong 12 tháng đầu | Theo dõi MRR, số user trả tiền, payback period |

## 2. Roadmap 6 bước

1. **Scan nhu cầu (2 tuần)**
   - Thu thập “job to be done” từ niche (Reddit, cộng đồng Discord, IndieHackers).
   - Lưu bảng Pain-Metric: vấn đề, tần suất, mức sẵn sàng trả.
2. **Phỏng vấn người dùng (2 tuần)**
   - Mẫu câu hỏi mở: “Lần cuối bạn gặp vấn đề X là khi nào? Bạn giải quyết ra sao? Điều gì làm bạn khó chịu nhất?”
   - Kết quả: chọn 1 vấn đề có tần suất cao + willingness to pay rõ.
3. **Bản đồ giải pháp (1 tuần)**
   - Vẽ customer journey, highlight step gây friction.
   - Xác định micro “win” có thể demo trong 3 ngày.
4. **Prototype & Smoke Test (2 tuần)**
   - Dùng no-code/automation/LLM để tạo bản demo (video, Figma, bubble).
   - Đặt landing page + waitlist (dùng [`landing-page-copy-template.md`](../../../templates/landing-page-copy-template.md)).
5. **MVP Launch (2-4 tuần)**
   - Ship phiên bản nhỏ: script, extension, API wrapper.
   - Thu feedback qua in-app form + user interview follow-up.
6. **Grow / Kill / Pivot (2 tuần)**
   - Grow: nếu >20% user trả lời “rất thất vọng nếu không dùng được”.
   - Kill/Pivot: nếu retention <10% sau 2 tuần → học từ feedback, chọn pain khác.

## 3. Bảng Research Log

| Sprint | Vấn đề đang kiểm chứng | Số user phỏng vấn | Insight chính | Quyết định |
| --- | --- | --- | --- | --- |
| S1 | Social media automation cho agency nhỏ | 12 | Quá nhiều tool, họ muốn “1-click reporting” | Chuyển sang xây reporting micro-service |
| S2 | Reporting micro-service | 18 | Họ cần template + export nhanh | Làm plugin Google Slides + API |

> Dùng bảng này trong Notion/Airtable để không lặp lại insight cũ.

## 4. Checklist điều kiện trước khi code

- [ ] Có ít nhất 15 user nói “tôi sẽ trả tiền cho giải pháp X nếu nó làm được Y/Z”.
- [ ] Hiểu rõ workflow từ đầu đến cuối (có thể vẽ được diagram).
- [ ] Có kênh phân phối dự kiến (community, newsletter, partner).
- [ ] Đặt được pricing / mô hình thu tiền cơ bản.
- [ ] Có KPI cho MVP (ví dụ: 20 user đầu tiên, 5 người trả tiền).

## 5. Kit thử nghiệm nhanh

- **Landing page:** [`landing-page-copy-template.md`](../../../templates/landing-page-copy-template.md)
- **Email sequence:** [`cold-email-mentor.md`](../../../templates/cold-email-mentor.md) (biến thể cho khách hàng)
- **Product feedback:** dùng [`weekly-review.md`](../../../templates/weekly-review.md) để reflective sau mỗi sprint.

## 6. Liên kết trong repo

- [`../career/indie-hacker-roadmap.md`](../career/indie-hacker-roadmap.md) – Tổng quan xây indie business.
- [`product-market-fit.md`](./product-market-fit.md) – Framework PMF.
- [`templates/`](./templates/) – Canvas: value proposition, user story map.
- [`../sales-telesales/negotiation-mastery-roadmap.md`](../sales-telesales/negotiation-mastery-roadmap.md) – Kỹ năng chốt deal early adopter.

> Làm micro-SaaS không cần team lớn. Điều quan trọng là phải có nhịp thử nghiệm đều, học từ user nhanh và không ngại kill ý tưởng để nhường chỗ cho giải pháp phù hợp hơn.