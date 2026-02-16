# 🧠 Critical Thinking & Logical Fallacies: The Developer's Mindset

> [← Back to Philosophy Roadmap](../README.md) | [Home](../../../README.md)

**Critical Thinking (Tư duy phản biện)** không phải là "thích tranh cãi" (argumentative).
Nó là khả năng **đánh giá khách quan** một thông tin để xem nó có đúng sự thật không, thay vì chấp nhận nó một cách mù quáng.

Trong kỷ nguyên AI và Fake News, đây là kỹ năng sinh tồn số 1.

---

## 🛠️ 1. The Socratic Method (Phương pháp Socrates)

Đây là công cụ Debugging cho tư duy. Thay vì đưa ra câu trả lời, hãy đặt câu hỏi để tìm ra lỗi sai (bug) trong suy nghĩ.

**Quy trình:**
1.  **Clarification:** Bạn định nghĩa X là gì? (VD: "Senior Developer là gì?")
2.  **Challenge Assumptions:** Tại sao bạn tin điều đó là đúng? (VD: "Tại sao Senior phải biết Kubernetes?")
3.  **Evidence:** Bằng chứng nào hỗ trợ điều này? (VD: "Có Data nào chứng minh điều đó không?")
4.  **Alternative:** Có cách giải thích nào khác không?
5.  **Consequences:** Nếu điều này sai thì sao?

**Ứng dụng:** Code Review, System Design Interview.

---

## 🚫 2. Top 10 Logical Fallacies trong Tech

Lỗi ngụy biện (Fallacies) là những "bug" trong logic. Hãy học cách spot chúng.

### 1. Ad Hominem (Tấn công cá nhân)
*   **Logic:** Tấn công người nói thay vì lập luận của họ.
*   **Tech Example:** "Thằng đó dùng PHP, ý kiến của nó về System Design không có giá trị." (Sai lầm: PHP dev vẫn có thể giỏi kiến trúc).

### 2. Straw Man (Người rơm)
*   **Logic:** Bóp méo lập luận của đối phương thành một phiên bản yếu ớt để dễ tấn công.
*   **Tech Example:**
    *   Dev A: "Chúng ta nên viết thêm Unit Test."
    *   Dev B: "A muốn chúng ta dành 100% thời gian viết test và không bao giờ ship tính năng mới à?" (A không hề nói thế).

### 3. Appeal to Authority (Dựa hơi quyền lực)
*   **Logic:** Tin điều gì đó chỉ vì một người nổi tiếng nói thế.
*   **Tech Example:** "Chúng ta phải dùng Microservices vì Netflix dùng nó." (Netflix có 1000 kỹ sư, team bạn có 3 người. Context khác nhau).

### 4. False Dichotomy (Nhị nguyên sai lầm)
*   **Logic:** Ép buộc chỉ có 2 lựa chọn (Trắng hoặc Đen), trong khi thực tế có nhiều hơn.
*   **Tech Example:** "Hoặc là chúng ta ship nhanh (nhưng code bẩn), hoặc là chúng ta ship chậm (code sạch)." (Thực tế: Code sạch giúp ship nhanh hơn về lâu dài).

### 5. Slippery Slope (Trượt dốc không phanh)
*   **Logic:** Cho rằng A sẽ dẫn đến Z (thảm họa) mà không có bằng chứng.
*   **Tech Example:** "Nếu cho phép remote 1 ngày, nhân viên sẽ lười biếng, rồi công ty sẽ phá sản."

### 6. Post Hoc Ergo Propter Hoc (Nhân quả sai lầm)
*   **Logic:** A xảy ra trước B → A là nguyên nhân của B. (Correlation ≠ Causation).
*   **Tech Example:** "Server sập ngay sau khi tôi deploy. Chắc chắn là do code của tôi." (Thực tế: Có thể do AWS sập cùng lúc).

### 7. Sunk Cost Fallacy (Chi phí chìm)
*   **Logic:** Tiếp tục làm cái sai vì đã lỡ đầu tư quá nhiều vào nó.
*   **Tech Example:** "Chúng ta đã bỏ 6 tháng code cái feature này rồi, phải release nó dù user không cần." (Giải pháp đúng: Kill it).

### 8. Confirmation Bias (Thiên kiến xác nhận)
*   **Logic:** Chỉ tìm kiếm thông tin ủng hộ niềm tin của mình và phớt lờ thông tin trái chiều.
*   **Tech Example:** Bạn thích React, nên bạn chỉ đọc bài viết khen React và bỏ qua bài viết chê nó chậm.

### 9. Bandwagon Fallacy (Hiệu ứng đoàn tàu)
*   **Logic:** Tin vì số đông đều tin.
*   **Tech Example:** "Mọi người đang đổ xô vào mua NFT, chắc chắn nó là tương lai." (FOMO).

### 10. Whataboutism (Đánh tráo chủ đề)
*   **Logic:** Phản bác bằng cách lôi một vấn đề khác ra để so sánh.
*   **Tech Example:** "Tại sao sếp chê code tôi bug? Code của thằng B còn nhiều bug hơn kìa!" (Lỗi của B không làm code bạn đúng hơn).

---

## ⚔️ 3. Razor Tools: Dao cạo tư duy

Những nguyên tắc giúp cắt bỏ sự nhiễu loạn (noise) để thấy sự thật.

### A. Occam’s Razor (Dao cạo Occam)
> "Giải thích đơn giản nhất thường là giải thích đúng nhất."

*   **Tech:** Nếu server lỗi, đừng nghĩ do Hacker Nga tấn công (phức tạp). Hãy nghĩ do ai đó quên cập nhật config (đơn giản).

### B. Hanlon’s Razor (Dao cạo Hanlon)
> "Đừng đổ lỗi cho ác ý những gì có thể giải thích bằng sự ngu dốt (hoặc lười biếng)."

*   **Tech:** PM đưa requirement sai không phải vì họ ghét bạn, mà vì họ không hiểu kỹ thuật. (Hãy educate họ thay vì giận dữ).

### C. Hitchens’s Razor
> "Cái gì được khẳng định không cần bằng chứng thì có thể bị bác bỏ không cần bằng chứng."

*   **Tech:** "Framework này nhanh hơn 10 lần!" - "Đâu? Benchmark đâu?" Không có → Bỏ qua.

---

## 📝 4. Action Plan: Rèn luyện mỗi ngày

1.  **Spot the Fallacy:** Trong cuộc họp tới, hãy thử (thầm) đếm xem có bao nhiêu lỗi ngụy biện được đưa ra.
2.  **Ask "Why?":** Khi nghe một khẳng định mạnh mẽ, hãy hỏi: "Dựa trên dữ liệu nào?"
3.  **Steel Man Argument:** Trước khi phản bác ai, hãy thử diễn giải lại ý của họ một cách tốt nhất có thể (Ngược với Straw Man). "Có phải ý bạn là...?"

> **Tư duy phản biện là khiên chắn bảo vệ não bộ của bạn khỏi sự thao túng.**

---

**Next Steps:**
*   [🏛️ Ancient Wisdom](../schools-and-thinkers/ancient-philosophy.md) - Học từ các bậc thầy tư duy cổ đại.
