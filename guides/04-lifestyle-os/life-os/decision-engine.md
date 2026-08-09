# 1️⃣ Decision Engine (Động cơ Ra quyết định)

> **"Cuộc đời là tổng hợp của các quyết định bạn đưa ra."**

## 🎯 Mission & Outcomes
- **Mục tiêu:** Tạo hệ thống ra quyết định có thể tái sử dụng, giảm cảm tính, tăng độ chính xác.
- **Output chính:** Decision Memo, EV Dashboard, Checklist OODA, Lessons Learned Log.
- **Success Metrics:**
  - % quyết định đạt mục tiêu kỳ vọng (hit rate) ≥ 60%.
  - Thời gian ra quyết định cho case lớn < 14 ngày.
  - Feedback loop được cập nhật ít nhất 1 lần/tháng.

## 🧠 Mental Model Stack
1. **Expected Value (Giá trị Kỳ vọng)**
   - Công thức: $EV = (P_{win} \times V_{win}) - (P_{lose} \times V_{lose})$.
   - Đừng đánh giá dựa trên outcome đơn lẻ (Outcome Bias). Tập trung vào EV dài hạn.
2. **Bayesian Updating (Cập nhật Bayes)**
   - Không có gì 100% chắc chắn. Mọi niềm tin đều là xác suất.
   - Khi có dữ liệu mới, cập nhật Prior → Posterior thay vì bảo vệ Ego.
3. **Kelly Criterion (Quản lý vốn)**
   - Ngay cả cơ hội tốt cũng không được all-in. Kelly sizing giúp tối ưu hóa tăng trưởng log-utility.
4. **Opportunity Cost (Chi phí cơ hội)**
   - Mỗi lựa chọn đều loại trừ lựa chọn khác. Luôn hỏi “Nếu làm việc này, tôi bỏ lỡ điều gì?”
5. **Sunk Cost Fallacy (Chi phí chìm)**
   - Những gì đã mất không nên ảnh hưởng tới quyết định tương lai.
   - Audit câu hỏi: “Nếu bắt đầu lại, tôi có chọn dự án này không?”
6. **Optionality (Tính tùy chọn)**
   - Ưu tiên quyết định có capped downside nhưng mở thêm lựa chọn tương lai.
7. **Second-order Effects (Hệ quả bậc 2)**
   - Đánh giá chuỗi phản ứng sau quyết định. Dùng systems thinking để map hiệu ứng dây chuyền.

## 🔍 Diagnostic Questions
1. **Thông tin:** Tôi đang ra quyết định dựa trên dữ liệu hay cảm xúc? Evidence nào thiếu?
2. **EV:** EV đã dương chưa? Downsides có thể giết tôi không?
3. **Optionality:** Quyết định này mở thêm bao nhiêu lựa chọn trong tương lai?
4. **Opportunity Cost:** Nếu nói “Có” với lựa chọn này, tôi nói “Không” với điều gì quan trọng hơn?
5. **Sunk Cost:** Tôi có giữ dự án chỉ vì đã đầu tư quá nhiều thời gian/tiền?
6. **Feedback:** Tôi đo lường hiệu quả quyết định cũ ra sao? Có học được gì?

## 🛠️ Execution Playbook (OODA + EV loop)
1. **Observe:** Thu thập dữ liệu, quan sát tín hiệu, định nghĩa vấn đề. Tạo `Assumption log`.
2. **Orient:** Áp dụng EV, Bayes, Opportunity cost để mô hình hóa. Chạy mô phỏng (Monte Carlo khi cần).
3. **Decide:** Chọn phương án có EV dương, trừ Ruin scenario. Ghi rõ “Why now? Why this?”
4. **Act:** Commit, triển khai plan. Thiết lập trigger cho Plan B.
5. **Review:** Sau khi outcome rõ, ghi lại lesson vào Decision Journal.

## 📈 Metrics & Rituals
- **Decision Scorecard:** Liệt kê 5-10 quyết định lớn/ quý, đánh giá EV kỳ vọng vs kết quả.
- **Cadence:** Weekly micro-decisions review, Monthly strategic decisions sync, Quarterly Deep Review.
- **Leading indicators:** % giả định có dữ liệu, thời gian thu thập dữ liệu, số lượng pre-mortem hoàn thành.

## 🧪 Examples & Templates

### ⚙️ Ví dụ nhanh: EV + Pre-mortem

| Quyết định | Các kịch bản (xác suất) | EV ước tính | Pre-mortem – Điều gì khiến thất bại? |
| --- | --- | --- | --- |
| **Đổi việc sang Big Tech** | `P_offer 60% × (Lương +30% + RSU 50k)` vs `P_fail 40% × (mất 2 tháng không lương)` | `EV ≈ 0.6 × 50k - 0.4 × 10k = +26k` (chấp nhận vì không phá sản) | Không luyện DSA hằng ngày, không network nội bộ, bị đóng băng headcount → Study plan 30-60-90 + sponsor nội bộ. |
| **Đầu tư dự án fintech Series A** | `Upside 25% × (10× vốn)` vs `Downside 75% × (mất 50% vốn)` | `EV ≈ 0.25 × 10 - 0.75 × 0.5 = +1.75×` nhưng Kelly chỉ cho phép 15-20% vốn | Founder bỏ cuộc, regulatory ban, không tìm được PMF → Yêu cầu runway ≥18 tháng, clause thoát vốn, theo sát product metric. |

> **Cách dùng:** Đặt giả định vào bảng, tính EV sơ bộ, viết 3-5 tình huống dẫn tới thất bại để tạo hành động phòng ngừa (timeline, owner, trigger).

### 📝 Templates & Tools
- [Decision Journal Template](../../templates/decision-journal.md)
- [Risk Radar Template](../../templates/productivity/risk-radar.md) – dùng để check ruin trước khi commit.
- [Pre-mortem Worksheet](../../../templates/productivity/project-pre-mortem.md)
- Guide: [Pre-mortem Technique](../../03-career-skills/innovation/pre-mortem-technique.md) — chống Groupthink & Confirmation Bias.

## 🔗 Related Engines
- **Risk Engine:** Dùng checklist `SPOF / Margin of Safety` trước khi all-in EV cao → [Risk Engine](./risk-engine.md#🛠️-quy-trình-quản-trị-rủi-ro-checklist).
- **Alignment Engine:** Khi phân vân giữa 2 offer gần nhau về EV, dùng `vector dài hạn + regret minimization` để chọn hướng → [Alignment Engine](./alignment-engine.md#🧭-framework-vector-pca).

---

## 📚 Further Reading
- [Systems Thinking](../01-mental-models/systems-thinking.md)
- [Probability & Bayes](../01-mental-models/probability-calculus.md)
- [Mental Models – Decision Making](../01-mental-models/README.md)
