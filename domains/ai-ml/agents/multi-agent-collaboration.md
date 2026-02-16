# 🤖 Multi-Agent Systems: Sức mạnh của Đội nhóm

> [← Back to AI/ML Roadmap](../README.md)

Tại sao dùng 1 Agent khi bạn có thể dùng cả một **Team**?
Một Agent duy nhất (GPT-4) dễ bị quá tải Context và làm sai các nhiệm vụ phức tạp.

---

## 1. Hierarchy (Phân cấp) - Mô hình Công ty

### **Cấu trúc:**
*   **Manager (Quản lý):** Nhận yêu cầu từ User. Chia nhỏ thành các Task. Giao việc cho các Agent con.
*   **Workers (Nhân viên):** Thực hiện Task cụ thể (Code, Search, Review). Báo cáo lại cho Manager.

### **Lợi ích:**
*   **Specialization (Chuyên môn hóa):** Mỗi Agent chỉ cần giỏi một việc (Coder chỉ biết code, Writer chỉ biết viết).
*   **Parallelization (Song song):** Các Worker có thể làm việc cùng lúc.

---

## 2. Joint Collaboration (Bàn tròn) - Mô hình Nhóm

Tất cả Agent đều bình đẳng và có thể nói chuyện với nhau.

### **Cơ chế:**
*   **Round Robin:** Lần lượt từng Agent phát biểu ý kiến.
*   **Shared Memory:** Các Agent chia sẻ chung một bộ nhớ (Bảng trắng) để cập nhật tiến độ.

### **Ví dụ (Code Review):**
1.  **Coder:** Viết hàm tính giai thừa.
2.  **Tester:** Chạy thử hàm với input âm -> Lỗi.
3.  **Coder:** Nhận feedback -> Sửa code.
4.  **Reviewer:** Kiểm tra style code -> Duyệt.

---

## 3. Debate (Tranh luận) - Mô hình Phản biện

Để tìm ra giải pháp tốt nhất, hãy cho các Agent cãi nhau.

### **Cơ chế:**
*   **Proposer (Người đề xuất):** Đưa ra giải pháp A.
*   **Opponent (Người phản biện):** Tìm ra điểm yếu của giải pháp A. Đưa ra giải pháp B.
*   **Judge (Trọng tài):** Lắng nghe tranh luận và chọn giải pháp tối ưu.

### **Lợi ích:**
*   Giảm ảo giác (Hallucination). Agent thứ 2 sẽ phát hiện ra lỗi sai của Agent thứ 1.
*   Tăng tính sáng tạo (Diversity).

---

## 4. Challenges (Thách thức)

Không phải cứ nhiều Agent là tốt.
*   **Communication Overhead:** Tốn quá nhiều token để các Agent nói chuyện với nhau -> Tốn tiền.
*   **Infinite Loop:** Các Agent cãi nhau mãi không hồi kết. (Cần cơ chế Timeout hoặc Max Turns).
*   **Coordination:** Khó đồng bộ trạng thái giữa các Agent.
