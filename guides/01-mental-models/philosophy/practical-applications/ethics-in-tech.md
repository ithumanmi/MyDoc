# 🤖 Ethics in Tech: Moral Code for the Digital Age

> [← Back to Philosophy Roadmap](../../../README.md) | [Home](../../../README.md)

Khi bạn viết code, bạn không chỉ viết hướng dẫn cho máy tính. Bạn đang viết **luật chơi cho xã hội**.
Thuật toán quyết định ai được vay tiền, ai được xem tin tức gì, và xe tự lái sẽ đâm vào ai.

Tech Workers không thể "trung lập về đạo đức" (morally neutral). Code của bạn có hệ quả.

---

## 🌪️ 1. Những câu hỏi khó (The Hard Questions)

### A. AI Bias (Thiên kiến thuật toán)
*   **Vấn đề:** AI học từ dữ liệu quá khứ. Nếu dữ liệu quá khứ phân biệt chủng tộc/giới tính, AI sẽ khuếch đại nó.
*   **Ví dụ:** Amazon AI Recruiting Tool bị hủy bỏ vì nó tự động loại hồ sơ ứng viên nữ (do học từ dữ liệu 10 năm trước toàn nam).
*   **Triết học:** Chúng ta có trách nhiệm sửa chữa quá khứ hay chỉ phản ánh nó? (Justice).

### B. Privacy vs Convenience (Quyền riêng tư vs Tiện ích)
*   **Vấn đề:** Để AI thông minh hơn, nó cần nhiều dữ liệu hơn. Nhưng dữ liệu đó là cuộc đời riêng tư của user.
*   **Ví dụ:** Google Maps biết bạn đi đâu. Facebook biết bạn thích gì.
*   **Triết học:**
    *   **Utilitarianism:** Nếu thu thập dữ liệu giúp chữa ung thư, có đáng hy sinh quyền riêng tư không?
    *   **Deontology:** Quyền riêng tư là quyền cơ bản, không được xâm phạm bất kể mục đích tốt đẹp.

### C. The Attention Economy (Kinh tế sự chú ý)
*   **Vấn đề:** Các thuật toán (TikTok, Facebook) được tối ưu để giữ chân user (Engagement). Cảm xúc giữ chân tốt nhất là **Giận dữ** và **Sợ hãi**.
*   **Hệ quả:** Phân cực xã hội, trầm cảm ở giới trẻ.
*   **Câu hỏi:** Là một kỹ sư, bạn có nên build một tính năng gây nghiện (addictive design) không?

---

## 🛠️ 2. Ethical Frameworks for Devs

Khi đứng trước quyết định khó, đừng dùng cảm tính. Hãy dùng Framework.

### Framework 1: The Utilitarian Test (Lợi ích tối đa)
> "Hành động này có mang lại hạnh phúc cho nhiều người nhất và giảm thiểu đau khổ không?"

*   **Áp dụng:** Xe tự lái. Nên lập trình để nó cứu hành khách trên xe (1 người) hay cứu người đi bộ (5 người)?
*   **Hạn chế:** Có thể biện minh cho việc hy sinh thiểu số (Minority).

### Framework 2: The Kantian Test (Quy tắc phổ quát)
> "Nếu tất cả mọi người đều làm như tôi, xã hội có tồn tại được không?" (Categorical Imperative).

*   **Áp dụng:** Dark Patterns (Lừa user click). Nếu mọi app đều lừa user, user sẽ mất niềm tin vào technology → Ngành tech sụp đổ. → Không được làm.
*   **Ưu điểm:** Bảo vệ quyền lợi cơ bản và lòng tin.

### Framework 3: The Grandma Test (Bài kiểm tra bà ngoại)
> "Nếu tôi phải giải thích tính năng này cho bà ngoại (hoặc báo chí), tôi có thấy xấu hổ không?"

*   **Áp dụng:** Nếu bạn đang lén lút thu thập danh bạ user mà không xin phép rõ ràng. Bạn có dám nói thẳng với bà không?

---

## 🛡️ 3. Trách nhiệm của Developer

Đừng dùng lời bào chữa **"Tôi chỉ làm theo lệnh"** (The Nuremberg Defense).

1.  **Quyền từ chối:** Bạn có quyền từ chối build những tính năng phi đạo đức. Thị trường lao động đang cần Dev giỏi, bạn có leverage.
2.  **Whistleblowing (Thổi còi):** Nếu công ty làm điều phạm pháp hoặc gây hại nghiêm trọng, bạn có nghĩa vụ đạo đức phải lên tiếng (như Frances Haugen vụ Facebook).
3.  **Humane Design:** Ưu tiên sức khỏe tinh thần của user hơn là metrics (Time on site).

---

## 📝 4. Checklist Đạo đức trước khi Deploy

Trước khi push code, hãy tự hỏi:

1.  [ ] **Transparency:** User có biết AI/Thuật toán đang quyết định thay họ không?
2.  **Fairness:** Thuật toán này có công bằng với các nhóm thiểu số không?
3.  **Privacy:** Mình có thu thập dữ liệu không cần thiết không?
4.  **Resilience:** Nếu kẻ xấu lợi dụng tính năng này, hậu quả tồi tệ nhất là gì? (Red Teaming).

> **Lời kết:** Technology là con dao. Triết học hướng dẫn bàn tay cầm con dao đó. Hãy là một **Ethical Technologist**.

---

**Next Steps:**
*   [🌟 Meaning & Purpose](./meaning-and-purpose.md) - Tìm ý nghĩa trong công việc.
*   [⚖️ Decision Making Frameworks](./decision-making-frameworks.md) - Cách ra quyết định.
