# 🧠 First Principles Thinking in Data Analytics

> Thay vì làm theo template cũ, hãy quay về bản chất: vấn đề thật là gì, biến số nào quan trọng, và kiểm chứng giả định ra sao?

## 1. Khung tư duy 3 tầng

1. **Reality** – Sự kiện quan sát được (dữ liệu thô, hành vi người dùng).
2. **Model** – KPI, metric, thuật toán mà bạn thiết kế.
3. **Decision** – Hành động cuối cùng và tác động kinh doanh.

Luôn kiểm tra xem mỗi tầng có đang phản ánh tầng trước trung thực hay không.

## 2. Quy trình First Principles (W.H.Y.)

| Bước | Câu hỏi | Deliverable |
| --- | --- | --- |
| **W – What is the real problem?** | KPI nào thực sự bị ảnh hưởng? Ai chịu tác động? | Problem Statement 1 câu |
| **H – How does the system work?** | Dòng dữ liệu/Business flow như thế nào? Giả định nào đang có? | System Diagram, list assumptions |
| **Y – Yes/No experiments** | Có cách nào kiểm chứng nhanh? Nếu sai thì sao? | Hypothesis + test/analysis plan |

## 3. Toolkit câu hỏi

- **Facts:** Data này được thu thập thế nào? Có bị delay/hole không?
- **Forces:** Cấu phần nào kéo KPI lên/xuống? (input vs output metric)
- **Constraints:** Thời gian, ngân sách, privacy?
- **Proof:** Cần bằng chứng mức nào để ra quyết định?

## 4. Applied example (Retention drop)

1. **Reality:** DAU giảm 12%, retention D30 từ 22% → 17%.
2. **Model:** Cohort cho thấy người dùng gói “Free Trial” churn cao.
3. **Decision:** Đề xuất redesign onboarding + push campaign.

Trước khi triển khai, thử “Yes/No experiment”: gửi survey nhanh + kiểm tra event tracking.

## 5. Kết hợp với decision frameworks

- Sau khi có insight, dùng **ICE Scoring** hoặc **Impact vs Effort** để ưu tiên.
- OODA Loop: Observe (dữ liệu) → Orient (First Principles) → Decide → Act.

## 6. Practice routine

- **Daily:** Chọn 1 dashboard đang dùng, viết lại problem statement và assumption.
- **Weekly:** Post-mortem 1 dự án: điều gì là assumption chưa validate?
- **Retro:** Ghi vào [Weekly Review](../../templates/weekly-review.md) về insight mới.

> 📝 *Remember:* First Principles không phải phản biện mọi thứ vô lý, mà là đảm bảo mỗi bước phân tích đều có căn cứ gốc rễ.