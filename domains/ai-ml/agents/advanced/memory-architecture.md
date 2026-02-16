# 🧠 Advanced Memory Systems: Bộ nhớ vô hạn cho Agent

> [← Back to AI/ML Roadmap](../../README.md)

Làm sao để Agent nhớ được thông tin về bạn sau hàng tháng trời nói chuyện, mà không bị tràn Context Window?

---

## 1. MemGPT (Memory-GPT)

Lấy cảm hứng từ Hệ điều hành (OS). Xem Context Window như RAM (nhanh, đắt, giới hạn) và Vector DB như ổ cứng (chậm, rẻ, vô hạn).

### **Cơ chế:**
*   **Virtual Context:** Tự động quản lý việc nạp/xả thông tin từ "ổ cứng" vào "RAM".
*   **System Instructions:** Agent có thể tự gọi hàm `core_memory_append` hoặc `archival_memory_search` để lưu/lấy ký ức.
*   **Kết quả:** Tạo ra ảo giác về bộ nhớ vô hạn (Infinite Context).

---

## 2. Memory Types (Phân loại bộ nhớ)

Không phải mọi ký ức đều giống nhau.

### **A. Semantic Memory (Kiến thức)**
*   Lưu trữ sự thật, khái niệm.
*   Ví dụ: "Thủ đô của Pháp là Paris", "User thích ăn phở".
*   Lưu trong **Vector Database**.

### **B. Episodic Memory (Sự kiện)**
*   Lưu trữ chuỗi sự kiện theo thời gian.
*   Ví dụ: "Hôm qua User hỏi về iPhone", "Tuần trước User phàn nàn về lỗi X".
*   Lưu trong **Time-series DB** hoặc Graph.

### **C. Procedural Memory (Kỹ năng)**
*   Lưu trữ cách làm việc.
*   Ví dụ: "Cách dùng tool Calculator", "Quy trình debug code".
*   Lưu trong **Prompt Templates** hoặc Fine-tuned Weights.

---

## 3. Memory Optimization (Nén ký ức)

Lưu tất cả hội thoại vào Vector DB là lãng phí và nhiễu.

### **Kỹ thuật:**
*   **Summarization:** Sau mỗi phiên chat, Agent tự tóm tắt lại các điểm chính và chỉ lưu tóm tắt.
*   **Entity Extraction:** Chỉ trích xuất thông tin quan trọng (Sở thích, Lịch hẹn) để lưu vào Profile User.
*   **Forgetting Curve:** Xóa bớt các ký ức cũ không quan trọng (như con người quên chuyện vặt vãnh).
