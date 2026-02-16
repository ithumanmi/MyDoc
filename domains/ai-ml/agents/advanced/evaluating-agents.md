# 🧪 Agent Evaluation: Đo lường trí tuệ

> [← Back to AI/ML Roadmap](../../README.md)

Làm sao biết Agent A thông minh hơn Agent B?
Làm sao biết bản cập nhật mới không làm Agent "ngu" đi?

---

## 1. Benchmarks (Bài thi chuẩn hóa)

*   **AgentBench:** Tập hợp các bài test đa dạng (OS, Database, Knowledge Graph, Card Game, House-holding).
*   **GAIA (General AI Assistants benchmark):** Các câu hỏi yêu cầu khả năng suy luận, dùng tool và xử lý đa phương thức (Multimodal). Khó hơn nhiều so với MMLU.
*   **HumanEval:** Bài test khả năng viết code (Python).

---

## 2. RAGAS (Evaluation for RAG)

Đánh giá hệ thống RAG dựa trên 3 tiêu chí chính (Tam giác RAG):

1.  **Faithfulness (Độ trung thực):** Câu trả lời có bịa đặt không? Có dựa trên tài liệu được cung cấp không?
2.  **Answer Relevance (Độ liên quan):** Câu trả lời có đúng trọng tâm câu hỏi không?
3.  **Context Precision (Độ chính xác ngữ cảnh):** Tài liệu tìm được (Retrieve) có chứa thông tin cần thiết không?

-> **Cách dùng:** Dùng GPT-4 làm giám khảo (LLM-as-a-Judge) để chấm điểm cho các LLM nhỏ hơn.

---

## 3. Debugging & Tracing (Gỡ lỗi)

Khi Agent chạy sai, bạn cần biết nó sai ở bước nào (Suy nghĩ sai? Chọn tool sai? Hay Tool lỗi?).

### **Tools:**
*   **LangSmith (LangChain):** Ghi lại toàn bộ Log (Input/Output) của từng bước trong Chain.
*   **Arize Phoenix:** Open-source observability cho LLM.
*   **WandB Weave:** Theo dõi luồng thực thi và đánh giá.

### **Quy trình Debug:**
1.  Nhìn vào Trace.
2.  Tìm bước mà LLM trả về output lạ.
3.  Sửa Prompt hoặc Context tại bước đó.
4.  Thêm Test Case đó vào bộ Evaluation Set để tránh lặp lại lỗi (Regression Testing).
