# 🗣️ NLP & LLMs: Xử lý Ngôn ngữ Tự nhiên (Level 5)

> [← Back to AI/ML Roadmap](../README.md)

Trước 2017, NLP là một lĩnh vực khó nhằn với LSTM/RNN.
Sau 2017 (Transformer), NLP bùng nổ với BERT và GPT.
Ngày nay, chúng ta có ChatGPT (LLM) viết code giỏi hơn Junior Dev.

---

## 1. Transformer Architecture ("Attention Is All You Need")

Mô hình thay đổi thế giới AI mãi mãi (Google Brain - 2017).

### **A. Self-Attention (Cơ chế chú ý)**
*   Khi đọc từ "Bank", máy phải biết nó đang nói về "Ngân hàng" hay "Bờ sông".
*   Attention giúp mô hình nhìn vào các từ xung quanh (Context) để hiểu nghĩa từ hiện tại.
*   **Parallelization:** Không cần đọc tuần tự từ trái sang phải như RNN -> Huấn luyện song song cực nhanh trên GPU -> Scale mô hình lên hàng tỷ tham số.

### **B. Encoder vs Decoder**
*   **Encoder (BERT):** Hiểu ngôn ngữ (NLU). Tốt cho bài toán phân loại, tìm kiếm.
*   **Decoder (GPT):** Sinh ngôn ngữ (NLG). Tốt cho bài toán Chatbot, viết văn.
*   **Encoder-Decoder (T5/BART):** Tốt cho bài toán dịch máy (Translation), tóm tắt văn bản.

---

## 2. Large Language Models (LLM)

Mô hình ngôn ngữ lớn (Billions parameters) học từ hàng Terabyte dữ liệu văn bản.

### **A. Pre-training (Học vẹt)**
*   Đọc hết Internet (Wikipedia, Github, Reddit...).
*   Học cách điền từ vào chỗ trống: "Hôm nay trời [MASK]".
*   Kết quả: Mô hình hiểu ngữ pháp, kiến thức thế giới, nhưng chưa biết làm theo lệnh.

### **B. Fine-tuning (Học chuyên sâu)**
*   Dạy mô hình làm nhiệm vụ cụ thể (Instruction Tuning).
*   **RLHF (Reinforcement Learning from Human Feedback):** Dùng con người chấm điểm câu trả lời để dạy mô hình cư xử đúng mực (Helpful, Honest, Harmless).

### **C. Efficient Fine-tuning (PEFT/LoRA)**
*   Thay vì train lại cả tỷ tham số (tốn tiền triệu đô), chỉ train một lớp nhỏ (Adapter) chèn vào giữa.
*   Tốn ít VRAM, chạy được trên GPU cá nhân (RTX 3090/4090).
*   👉 Xem chi tiết hands-on trong **[PEFT & LoRA Guide](./peft-lora-guide.md)** (chuẩn bị môi trường, code mẫu QLoRA, evaluation, deployment).

---

## 3. RAG (Retrieval-Augmented Generation)

LLM có 2 vấn đề lớn:
1.  **Hallucination (Ảo giác):** Bịa đặt thông tin sai sự thật.
2.  **Outdated Knowledge:** Kiến thức dừng ở năm 2021 (Cut-off date).

**Giải pháp RAG:**
1.  User hỏi: "Doanh thu công ty X quý vừa rồi là bao nhiêu?"
2.  Hệ thống tìm kiếm trong Database nội bộ (Vector DB) tài liệu liên quan.
3.  Gửi câu hỏi + Tài liệu tìm được cho LLM.
4.  LLM trả lời dựa trên tài liệu đó (có trích dẫn). -> Chính xác tuyệt đối.
