# 🧠 AI Agent Architecture: Giải phẫu một Agent

> [← Back to AI/ML Roadmap](../README.md)

AI Agent không chỉ là LLM. Agent là một **Hệ thống** có khả năng suy luận, lập kế hoạch và hành động để đạt mục tiêu.

$$ Agent = LLM + Memory + Planning + Tools $$

---

## 1. The Core (Bộ não) - LLM

LLM (GPT-4, Claude 3, Llama 3) đóng vai trò bộ xử lý trung tâm.
*   **Chức năng:** Hiểu yêu cầu (Intent Understanding), suy luận logic và ra quyết định.
*   **Thách thức:** LLM bị ảo giác (Hallucination) và giới hạn độ dài (Context Window).

---

## 2. Memory (Bộ nhớ)

Agent cần nhớ những gì đã làm.

### **A. Short-term Memory (Bộ nhớ ngắn hạn)**
*   Toàn bộ lịch sử chat (Conversation History) trong Context Window hiện tại.
*   *Hạn chế:* Khi chat quá dài, Agent sẽ quên đoạn đầu.

### **B. Long-term Memory (Bộ nhớ dài hạn)**
*   Lưu trữ kiến thức vĩnh viễn trong **Vector Database** (Pinecone, ChromaDB).
*   **Retrieval (RAG):** Khi cần thông tin cũ, Agent tìm kiếm trong Vector DB và lôi ra.

---

## 3. Planning (Lập kế hoạch)

Trước khi làm, Agent phải biết nghĩ.

### **A. Chain of Thought (CoT)**
*   Chia nhỏ vấn đề thành từng bước suy luận.
*   *Prompt:* "Let's think step by step."

### **B. ReAct (Reason + Act)**
*   Mô hình phổ biến nhất hiện nay.
*   **Loop:**
    1.  **Thought:** Mình cần làm gì? -> Cần tìm giá iPhone 15.
    2.  **Action:** Gọi tool `Google Search`.
    3.  **Observation:** Kết quả trả về là 25 triệu.
    4.  **Thought:** Đã có giá, giờ cần so sánh với Samsung S24...

---

## 4. Tools (Công cụ)

LLM chỉ biết chữ. Tools giúp Agent tương tác với thế giới thực.

*   **Search:** Google Search, Bing Search.
*   **Calculator:** Tính toán chính xác (LLM tính toán rất dốt).
*   **Code Interpreter:** Viết và chạy code Python (để vẽ biểu đồ, xử lý file).
*   **Function Calling:** Gọi API của bên thứ 3 (Gửi mail, Đặt vé máy bay).
