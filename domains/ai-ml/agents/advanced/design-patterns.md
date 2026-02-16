# 📐 Agentic Design Patterns: Chiến lược thiết kế

> [← Back to AI/ML Roadmap](../../README.md)

Để Agent thông minh hơn, đừng chỉ Prompt "Hãy làm X". Hãy thiết kế luồng suy nghĩ cho nó.

---

## 1. Reflection (Tự kiểm điểm)

Agent thường quá tự tin vào câu trả lời đầu tiên. Hãy bắt nó kiểm tra lại.

### **Reflexion Framework:**
1.  **Actor:** Sinh ra hành động/câu trả lời.
2.  **Evaluator:** Đánh giá chất lượng (Đúng/Sai).
3.  **Self-Reflection:** Nếu sai, Agent tự phân tích *tại sao sai* và lưu vào bộ nhớ ngắn hạn.
4.  **Retry:** Thử lại lần nữa với bài học kinh nghiệm vừa rút ra.

---

## 2. Planning Strategies (Chiến lược lập kế hoạch)

### **A. Chain of Thought (CoT)**
*   Suy nghĩ tuần tự: A -> B -> C.
*   Tốt cho bài toán logic đơn giản.

### **B. Tree of Thoughts (ToT)**
*   Suy nghĩ rẽ nhánh: Từ A có thể ra B1 hoặc B2.
*   Agent khám phá nhiều nhánh, đánh giá nhánh nào tiềm năng nhất và đi tiếp (giống thuật toán BFS/DFS).
*   Tốt cho bài toán sáng tạo hoặc giải đố phức tạp.

### **C. ReWOO (Reasoning without Observation)**
*   Tách biệt bước Suy luận (Planner) và Thực thi (Worker).
*   **Planner:** Viết ra toàn bộ kế hoạch: "Bước 1 tìm X, Bước 2 lấy X tính Y". (Không cần chờ kết quả bước 1).
*   **Worker:** Chạy song song các bước nếu có thể.
*   **Ưu điểm:** Giảm thời gian chờ và tiết kiệm Token.

---

## 3. Tool Use Strategies (Chiến lược dùng Tool)

### **A. Tool Selection (Chọn Tool)**
*   Khi có 100 Tools, làm sao Agent biết chọn cái nào?
*   **Giải pháp:** Dùng một LLM nhỏ (Classifier) để lọc ra Top 5 Tools liên quan nhất trước khi đưa cho Agent chính.

### **B. Robust Error Handling (Xử lý lỗi)**
*   Nếu Tool trả về lỗi (API timeout), Agent làm gì?
*   Đừng crash. Hãy dạy Agent đọc thông báo lỗi và tự sửa tham số input hoặc thử tool khác thay thế.
