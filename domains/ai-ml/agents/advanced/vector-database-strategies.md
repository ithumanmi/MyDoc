# Chiến lược Vector Database & Advanced RAG (Retrieval-Augmented Generation)

> [← Back to Agents Module](../README.md) | [Home](../../../README.md)

RAG cơ bản (Naïve RAG) rất dễ làm: Cắt tài liệu ra -> Đưa qua Embedding Model -> Lưu vào Vector DB -> Lấy Document tương đồng nhất -> Ném vào LLM.
Nhưng hệ thống **RAG Production-ready** lại cực kỳ khó. Nó sẽ trả về rác nếu Chunking sai, hoặc không thể tìm thấy kết nối nhân quả giữa các văn bản bị cắt vỡ. Bài viết này đào sâu vào lớp dữ liệu (Vector Data Layer) và các chiến lược RAG nâng cao.

---

## 🗄️ 1. Lựa chọn "Vũ khí": Landscape Vector Databases 2026

Bạn không thể dùng SQLite bình thường để truy vấn thuật toán HNSW (Hierarchical Navigable Small World) hay IVF (Inverted File) với tốc độ mili-giây. Bạn cần một Vector DB thực thụ.

| Database | Điểm mạnh (Superpower) | Điểm yếu / Khi nào tránh | Use Case lí tưởng |
| :--- | :--- | :--- | :--- |
| **Pinecone**| Serverless 100%, dễ setup nhất trần đời, quản lý vận hành Zero. | Khép kín, có thể đắt khi Scale lớn dữ liệu cực khủng. | Các Startup SaaS muốn go-to-market nhanh, ít kỹ sư Ops. |
| **Qdrant** | Lõi Rust siêu nhanh, mã nguồn mở, hỗ trợ Local/Docker rất tốt, Metadata Filtering cực tối ưu. | Cần hiểu chút kiến trúc nếu self-host clustering. | Ứng dụng Hybrid (Cloud+Local), cần Lọc (Filter) siêu tốc. |
| **Milvus** | Vua của hệ sinh thái khổng lồ, Scale lên hàng tỷ Vectors. Mở rông bằng kiến trúc phân tán. | Setup phức tạp (nhiều microservices, ZooKeeper...). | Enterprise, System tập đoàn lớn, GenAI Search Scale khủng. |
| **pgvector / pgvectorscale**| Mở rộng (Extension) của PostgreSQL. Tận dụng hạ tầng RDBMS có sẵn. Dễ dàng Join dữ liệu quan hệ với embeddings.| Xử lý chậm hơn các Native VectorDB khi khối lượng vector lên hàng trăm triệu. | Indie hackers dùng Supabase, hoặc hệ thống đã có sẵn Postgres mạnh. |

> **Lời khuyên thực chiến:** Bắt đầu bằng **Supabase (pgvector)** nếu dự án là Micro-SaaS. Nếu chuyên thuần túy NLP/Search và tốc độ là trên hết, dùng **Qdrant**.

---

## 🔪 2. Nghệ thuật Cắt Nhỏ Dữ Liệu (Advanced Chunking)

Chia text ra mỗi 500 từ (Fixed-size chunking) là thảm họa. Câu văn có thể bị cắt làm đôi ở giữa, hoặc bảng biểu bị vỡ vụn làm mất hoàn toàn ngữ nghĩa.

### 2.1. Semantic Chunking (Phân đoạn Ngữ Nghĩa)
Máy tính tự nhận diện khi nào chủ đề trong văn bản thay đổi, và cắt ở "ranh giới" chủ đề đó.
*   **Cách làm:** Dùng NLP để cắt thành các câu, embed từng câu vào Vector space. Tính Distance (Khoảng cách cosine) giữa các câu liên tiếp. Nếu khoảng cách tăng đột ngột -> Chứng tỏ đoạn văn chuyển ý sang chủ đề khác -> Cắt ở đó.

### 2.2. Document Hierarchy (Cấu trúc phân tầng cha-con)
Khi tìm kiếm, đôi khi một đoạn nhỏ (Child chunk) là thứ khớp sát nhất với câu hỏi. 
Nhưng đoạn nhỏ đó lại nằm trơ trọi, thiếu ngữ cảnh.
*   **Giải pháp (Parent-Child Retriever):** Cắt tài liệu gốc thành các chunk khổng lồ (Parent - 2000 tokens), rồi chia Parent đó thành các chunk bé (Child - 200 tokens). Khớp embeddings với Child, nhưng khi trả kết quả cho LLM thì lấy toàn bộ Parent để LLM có "bức tranh toàn cảnh" (Context Injection).

### 2.3. Markdown & Structural Chunking
Xử lý tài liệu code, danh sách, hay bảng biểu.
*   Sử dụng thư viện (như Unstructured.io hoặc LlamaParse) để bóc tách DOM/Markdown. Các thẻ Headers (`##`, `###`) sẽ được nhúng làm Metadata của chunk, giúp thuật toán Search hiểu "Đoạn text này nằm trong chương nào của cuốn sách".

---

## 🔍 3. Nâng Cấp Hệ Thống Truy Xuất (Advanced Retrieval)

Tìm kiếm Vector (Dense Search) rất tệ ở việc tìm chính xác từ khóa (ví dụ: Tìm số Seri, tên Mã Sản Phẩm đặc biệt). Đó là khi ta cần Reranking và Hybrid Search.

### 3.1. Hybrid Search (Kho vũ khí kép)
Kết hợp hai phương thức tìm kiếm lại với nhau để tạo ra kết quả xuất sắc:
*   **Dense Search (Vector Embeddings):** Tìm nghĩa tiềm ẩn, khái niệm tương đồng.
*   **Sparse Search (Keyword - BM25):** Vua của tìm kiếm theo cụm từ khóa chính xác y chang.
*   **Thực thi:** Tìm top 50 từ Vector, top 50 từ BM25. Trộn chúng lại (vd dùng thuật toán Reciprocal Rank Fusion - RRF) để lấy lại top 10 ngon nhất. Hệ thống RAG thực thụ nào hiện nay cũng phải dùng Hybrid Search.

### 3.2. Reranking Model (Cross-Encoder Bước Nhảy Vọt)
Mô hình Embedding ban đầu (Bi-Encoder) tìm kiếm cực nhanh trên hàng triệu tài liệu nhưng độ tinh tế (Accuracy) không "sâu", do thiết kế tính cosin riêng rẽ.
*   **Giải pháp:** Lấy Top 20 tài liệu thô ban đầu -> Ném qua một Mô Hình Reranker đặc dụng (như **Cohere Rerank**, hoặc BGE-Reranker mã nguồn mở). Mô hình này sẽ chấm điểm (Scoring) chi tiết sự tương quan giữa *Câu hỏi* và *Từng tài liệu*, sắp xếp lại thứ tự từ cao xuống thấp cực kì chính xác. Lấy lại Top 3 đưa cho LLM.
*   *Kết quả: Nâng độ chính xác của RAG lên đáng ngạc nhiên với thời gian tốn thêm rất ngắn (~100ms).*

### 3.3. Query Transformation: Tự "Nắn" Câu Hỏi (Tưởng tượng trước khi Tìm)
Đôi khi user hỏi một câu quá ngắn gọn hoặc tối nghĩa. LLM có thể định hình lại (Transform) trước khi móc mũi nhọn vào Database.
*   **Quý Ngài Giả Thuyết (HyDE - Hypothetical Document Embeddings):** User tạo query. Ta cho LLM tạo ra một câu trả lời (giả tưởng, có thể sai lè - hallucinated answer) dựa trên query đó. Xong ta lấy *Câu lời giải giả tưởng* đó đi Embed rồi Search trong Database! Kỹ thuật này tìm ra kết quả xuất sắc vi diệu khi user mô tả triệu chứng thay vì gọi đích danh tên bệnh.
*   **Multi-Query:** LLM "sinh lời đồn", xào chẻ câu hỏi gốc của user thành 3-5 phiên bản câu hỏi khác nhau nhưng chung nghĩa -> Query DB cả 5 bản -> Gộp kết quả. Nó quét DB được nhiều ngóc ngách hơn một câu đơn thuần.

---

## 💡 4. Ứng Dụng Thực Chiến (Checklist)

> [!TIP]
> **Checklist trước khi Deploy RAG:**
>
> ✓ Bỏ ngay RAG cơ bản! Tối thiểu phải bật **Hybrid Search (BM25 + Semantic)**.
> ✓ Thêm thư viện gọi **Reranker API (ví dụ Cohere Rerank model)**. Nếu chi phí cao thì tự chạy local BGE-Reranker.
> ✓ Log lại các câu hỏi RAG không ra được kết quả (Null/Hallucinations) vào một bảng. Phân tích do Chunking sai (thiếu data) hay LLM bị Ngu, từ đó tinh chỉnh chiến lược.
