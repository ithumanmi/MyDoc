# 🤖 Autonomous Agents: Trí tuệ Tự chủ

> [← Back to AI/ML Roadmap](../README.md)

Đây là giấc mơ của mọi nhà phát triển AI: Một Agent có thể tự làm việc mà không cần sự can thiệp của con người.
Chỉ cần đưa ra mục tiêu: "Kiếm cho tôi 1 triệu đô". Agent sẽ tự tìm cách.

---

## 1. AutoGPT (Ông tổ của Agent Tự chủ)

Dự án mã nguồn mở đình đám nhất năm 2023.

### **Cơ chế:**
1.  **Goal:** Người dùng nhập mục tiêu.
2.  **Think:** Agent suy nghĩ các bước cần làm.
3.  **Plan:** Lên kế hoạch chi tiết.
4.  **Execute:** Thực hiện từng bước (Search, Code, Write File).
5.  **Review:** Đánh giá kết quả. Nếu chưa đạt -> Quay lại bước 2 (Vòng lặp vô tận).

### **Vấn đề:**
*   **Infinite Loop:** Agent thường bị kẹt trong vòng lặp luẩn quẩn mà không thoát ra được.
*   **Hallucination:** Bịa đặt thông tin sai sự thật để hoàn thành task.
*   **Cost:** Tốn cực nhiều tiền API (GPT-4) vì suy nghĩ liên tục.

---

## 2. BabyAGI (Task-driven Autonomous Agent)

Phiên bản đơn giản hơn của AutoGPT. Tập trung vào việc quản lý Task List.

### **Cơ chế:**
1.  **Task Creation:** Tạo danh sách các việc cần làm dựa trên mục tiêu.
2.  **Prioritization:** Sắp xếp thứ tự ưu tiên các task.
3.  **Execution:** Thực hiện task đầu tiên.
4.  **Result Storage:** Lưu kết quả vào Vector DB.
5.  **New Task Generation:** Tạo thêm task mới dựa trên kết quả vừa làm được.

---

## 3. Devin (AI Software Engineer)

Sản phẩm thương mại đầu tiên thực sự hoạt động ổn định (Cognition Labs).
*   Có khả năng tự sửa lỗi (Self-healing).
*   Tự đọc tài liệu API mới để học cách sử dụng.
*   Tự deploy ứng dụng lên Cloud.

> **Bài học:** Để Agent hoạt động tốt, cần giới hạn phạm vi (Scope).
> AutoGPT thất bại vì cố gắng làm mọi thứ. Devin thành công vì chỉ tập trung vào việc **Code**.

---

## 4. Challenges (Thách thức lớn nhất)

### **A. Safety & Alignment (An toàn & Căn chỉnh)**
*   Làm sao đảm bảo Agent không làm điều xấu? (Ví dụ: Hack server để hoàn thành mục tiêu "Lấy dữ liệu").
*   Cần cơ chế **Human-in-the-loop** để kiểm soát các hành động nguy hiểm.

### **B. Reliability (Độ tin cậy)**
*   Agent hiện tại vẫn hay làm sai hoặc bịa đặt.
*   Cần cơ chế **Self-Reflection** (Tự kiểm điểm) mạnh mẽ hơn.
