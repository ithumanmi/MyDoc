# 🤝 Human-in-the-loop: Tương tác Người - Máy

> [← Back to AI/ML Roadmap](../../README.md)

Agent không nên là hộp đen. Nó cần sự hợp tác của con người để hoàn thành nhiệm vụ khó.

---

## 1. Interruptibility (Cơ chế Ngắt lời)

Khi Agent đang chạy một tác vụ dài (ví dụ: Viết code, chạy test, deploy), người dùng có thể muốn can thiệp.

### **Use Cases:**
*   Agent đi sai hướng -> User bấm "Stop" và sửa lại yêu cầu.
*   Agent cần xác nhận (Approval) trước khi thực hiện hành động nguy hiểm (Xóa file, Chuyển tiền).

### **Kỹ thuật:**
*   **Checkpointing:** Lưu trạng thái Agent sau mỗi bước. User có thể "Rewind" (Tua lại) về quá khứ và chọn ngã rẽ khác.
*   **Human Node:** Trong LangGraph, thêm một node đặc biệt chỉ làm nhiệm vụ chờ User Input.

---

## 2. Streaming (Hiển thị thời gian thực)

Đừng để User chờ 30 giây rồi mới hiện kết quả.

*   **Token Streaming:** Hiện từng chữ ngay khi LLM sinh ra (giống ChatGPT).
*   **Activity Streaming:** Hiện các hành động nội bộ: "Đang tìm kiếm Google...", "Đang đọc tài liệu...", "Đang viết code...".
*   *Lợi ích:* Tăng tính tin cậy (Transparency) và giảm cảm giác chờ đợi (Perceived Latency).

---

## 3. UX Patterns for Agents (Giao diện)

### **A. Chat UI (Truyền thống)**
*   Dòng thời gian tuyến tính.
*   Phù hợp cho hỏi đáp đơn giản.

### **B. Canvas UI (Hiện đại - OpenAI Canvas / Cursor)**
*   Agent và User cùng làm việc trên một văn bản/code editor.
*   Agent có thể highlight, sửa đổi trực tiếp nội dung.
*   User có thể comment vào từng đoạn cụ thể để ra lệnh.

### **C. Generative UI (Vercel AI SDK)**
*   Agent không chỉ trả về text, mà trả về cả Component React (Biểu đồ, Bảng giá, Form điền thông tin).
*   Ví dụ: Hỏi "Giá cổ phiếu Apple", Agent vẽ luôn biểu đồ nến tương tác được.
