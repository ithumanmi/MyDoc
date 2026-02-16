# 🏠 Local Agents: AI chạy trên máy nhà

> [← Back to AI/ML Roadmap](../../README.md)

Tại sao phải tốn tiền API cho OpenAI khi bạn có thể chạy Agent miễn phí, riêng tư ngay trên laptop?

---

## 1. Local LLM Runners (Công cụ chạy model)

### **A. Ollama (Dễ nhất)**
*   Cài đặt 1 click.
*   Lệnh: `ollama run llama3`.
*   Tự động quản lý API server local.

### **B. Llama.cpp (Tối ưu nhất)**
*   Chạy LLM trên CPU (nếu không có GPU xịn).
*   Hỗ trợ Apple Silicon (Macbook M1/M2/M3) cực tốt.

### **C. LM Studio (Giao diện đẹp)**
*   GUI thân thiện, dễ tải model từ HuggingFace.

---

## 2. Quantization (Nén mô hình)

Model gốc (FP16) rất nặng. Ví dụ Llama-3-70B cần 140GB VRAM.
Quantization nén số thực 16-bit xuống 4-bit (GGUF, AWQ, GPTQ).

*   **Q4_K_M:** Mất rất ít độ chính xác, giảm dung lượng 4 lần.
*   **Kết quả:** Chạy Llama-3-8B trên máy 8GB RAM mượt mà.

---

## 3. Function Calling với Local Model

Các model nhỏ (7B, 8B) thường dốt khoản gọi Tool (Function Calling).
Chúng hay viết sai cú pháp JSON hoặc quên đóng ngoặc.

### **Giải pháp:**
*   **Fine-tuned Models:** Dùng các model chuyên dụng cho tool như **Gorilla LLM**, **NexusRaven**, hoặc **Hermes-2-Pro**.
*   **Grammar Sampling (Llama.cpp):** Ép buộc model chỉ được xuất ra output tuân theo cấu trúc ngữ pháp JSON định sẵn. (Nếu model định viết text linh tinh, engine sẽ chặn lại).

---

## 4. Privacy & Security

*   **Offline 100%:** Dữ liệu không bao giờ rời khỏi máy bạn. An toàn tuyệt đối cho dữ liệu nhạy cảm (Code công ty, Hồ sơ bệnh án).
*   **No Rate Limit:** Chạy bao nhiêu tùy thích, không lo bị chặn API.
