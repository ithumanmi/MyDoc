# 🌐 Advanced RAG for Agents: Vượt xa tìm kiếm từ khóa

> [← Back to AI/ML Roadmap](../../README.md)

RAG cơ bản (Vector Search) chỉ tìm được những gì "giống nhau về mặt ngữ nghĩa".
Nhưng nếu câu trả lời nằm rải rác ở nhiều tài liệu khác nhau? Hoặc yêu cầu tư duy bắc cầu? -> Cần **Advanced RAG**.

---

## 1. GraphRAG (Knowledge Graphs)

Khi Vector DB là chưa đủ. GraphRAG kết hợp Vector Search với **Knowledge Graph (Đồ thị tri thức)**.

### **Vấn đề của Vector Search:**
*   Hỏi: "Mối quan hệ giữa nhân vật A và nhân vật B trong truyện là gì?"
*   Vector Search: Tìm đoạn văn có tên A và B -> Thường rời rạc, không thấy bức tranh toàn cảnh.

### **Giải pháp GraphRAG:**
1.  **Extract Entities:** Trích xuất thực thể (Người, Nơi chốn, Sự kiện) từ văn bản.
2.  **Build Graph:** Xây dựng đồ thị kết nối các thực thể (A --kẻ thù--> B).
3.  **Graph Traversal:** Khi user hỏi, Agent duyệt đồ thị để tìm mối quan hệ ẩn.

> **Ví dụ:** Microsoft GraphRAG dùng LLM để tóm tắt các cụm (Community Summary) trên đồ thị -> Trả lời câu hỏi tổng hợp cực tốt.

---

## 2. Hybrid Search (Tìm kiếm lai)

Đừng bỏ quên từ khóa (Keyword).

*   **Dense Retrieval (Vector):** Hiểu ngữ nghĩa. (Tìm "Con chó" ra "Golden Retriever").
*   **Sparse Retrieval (BM25):** Khớp chính xác từ khóa. (Tìm mã số "SKU-12345" phải ra đúng sản phẩm đó).
*   **Hybrid:** Kết hợp cả 2 điểm số (Weighted Sum) để có kết quả tốt nhất.

---

## 3. Reranking (Sắp xếp lại)

Tìm được 100 tài liệu rồi, nhưng tài liệu nào quan trọng nhất?

*   **Bi-Encoder (Vector Search):** Nhanh nhưng kém chính xác. Dùng để lọc sơ bộ (Retrieve top 100).
*   **Cross-Encoder (Reranker):** Chậm nhưng cực chính xác. Đọc kỹ từng cặp (Câu hỏi, Tài liệu) để chấm điểm lại.
*   **Quy trình:** Retrieve 100 -> Rerank lấy Top 5 -> Gửi cho LLM.

---

## 4. Self-RAG (Agent tự suy ngẫm)

Agent không chỉ nhận tài liệu một cách thụ động.

1.  **Retrieval:** Tìm tài liệu.
2.  **Critic (Phê bình):** Agent tự hỏi: "Tài liệu này có liên quan không?". Nếu không -> Tìm lại.
3.  **Generate:** Trả lời câu hỏi.
4.  **Verify:** Agent tự hỏi: "Câu trả lời này có đúng với tài liệu không?". Nếu bịa đặt -> Viết lại.
