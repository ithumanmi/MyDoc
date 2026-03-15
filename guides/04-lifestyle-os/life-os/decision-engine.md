# 1️⃣ Decision Engine (Động cơ Ra quyết định)

> **"Cuộc đời là tổng hợp của các quyết định bạn đưa ra."**

## Core Mental Models

### 1. Expected Value (Giá trị Kỳ vọng)
*   **Công thức:** $EV = (P_{win} \times V_{win}) - (P_{lose} \times V_{lose})$
*   **Tư duy:** Đừng đánh giá quyết định dựa trên kết quả (Outcome Bias). Hãy đánh giá dựa trên EV. Nếu EV dương và rủi ro phá sản thấp -> Làm tới.

### 2. Bayesian Updating (Cập nhật Bayes)
*   **Tư duy:** Không có gì là chắc chắn 100%. Mọi thứ chỉ là xác suất.
*   **Hành động:** Khi có thông tin mới, hãy cập nhật niềm tin cũ. Đừng cố chấp bảo vệ ý kiến (Ego). "Tôi có thể sai, và đây là xác suất tôi sai."

### 3. Kelly Criterion (Quản lý vốn)
*   **Tư duy:** Ngay cả khi cơ hội ngon ăn nhất, không bao giờ được All-in.
*   **Hành động:** Luôn giữ lại một phần vốn (tiền, sức khỏe, uy tín) để làm lại nếu thất bại.

### 4. Opportunity Cost (Chi phí cơ hội)
*   **Tư duy:** Mọi sự lựa chọn đều có giá. Giá của A là việc không được chọn B.
*   **Hành động:** "Nếu tôi làm việc này, tôi sẽ KHÔNG làm được việc gì khác?"

### 5. Second-order Effects (Hệ quả bậc 2)
*   **Tư duy:** Quyết định tốt không chỉ xét kết quả trực tiếp mà còn chuỗi phản ứng phía sau (Systems Thinking).
*   **Ví dụ:** Nhận freelance thêm giờ = tiền tăng (bậc 1) nhưng ngủ ít → hiệu suất ngày mai giảm, mất cơ hội thăng tiến (bậc 2). Luôn hỏi “Điều này kéo theo phản ứng dây chuyền nào?”
*   **Đọc thêm:** [Systems Thinking](../01-mental-models/systems-thinking.md) *(cập nhật link chính xác nếu khác).* 

---

## 🛠️ Quy trình Ra quyết định (Checklist)

Trước mỗi quyết định lớn (Đổi việc, Đầu tư, Mua nhà):

1.  **Tính EV:** Kịch bản tốt nhất là gì? Kịch bản tệ nhất là gì? Xác suất mỗi cái?
2.  **Check Ruin:** Nếu kịch bản tệ nhất xảy ra, tôi có "chết" (phá sản, mất danh dự vĩnh viễn) không? Nếu có -> Bỏ qua ngay lập tức.
3.  **Check Opportunity:** Tôi có đang bỏ lỡ cơ hội nào tốt hơn không?
4.  **Pre-mortem:** Tưởng tượng 1 năm sau dự án này thất bại thảm hại. Lý do là gì? (Tìm ra điểm mù).

### ⚙️ Ví dụ nhanh: EV + Pre-mortem

| Quyết định | Các kịch bản (xác suất) | EV ước tính | Pre-mortem – Điều gì khiến thất bại? |
| --- | --- | --- | --- |
| **Đổi việc sang Big Tech** | `P_offer 60% × (Lương +30% + RSU 50k)` vs `P_fail 40% × (mất 2 tháng không lương)` | `EV ≈ 0.6 × 50k - 0.4 × 10k = +26k` (chấp nhận vì không phá sản) | Không luyện DSA hằng ngày, không network nội bộ, bị đóng băng headcount → Giải pháp: Study plan 30-60-90 + sponsor nội bộ. |
| **Đầu tư dự án fintech Series A** | `Upside 25% × (10× vốn)` vs `Downside 75% × (mất 50% vốn)` | `EV ≈ 0.25 × 10 - 0.75 × 0.5 = +1.75×` nhưng Kelly chỉ cho phép 15-20% vốn | Founder bỏ cuộc, regulatory ban, không tìm được PMF → Thiết lập pre-mortem: yêu cầu runway ≥18 tháng, clause thoát vốn, theo sát product metric. |

> **Cách dùng:** Đặt các giả định vào bảng, tính EV sơ bộ, rồi viết 3-5 tình huống dẫn tới thất bại để tạo hành động phòng ngừa (timeline, người chịu trách nhiệm, tín hiệu cảnh báo).

---

### 🔗 Related Engines
- **Risk Engine:** Dùng checklist `SPOF / Margin of Safety` để đo xác suất "chết" trước khi all-in EV cao → [Risk Engine](./risk-engine.md#🛠️-quy-trình-quản-trị-rủi-ro-checklist).
- **Alignment Engine:** Khi phân vân giữa 2 offer gần nhau về EV, dùng kỹ thuật `vector dài hạn + regret minimization` để xem quyết định nào giữ bạn trên hướng đi đã chọn → [Alignment Engine](./alignment-engine.md#🧭-framework-vector-pca).

### 📝 Templates & Tools
- **Decision Log:** Lưu lại giả định, EV, pre-mortem để học từ feedback loop → [Decision Journal Template](../../templates/decision-journal.md)
