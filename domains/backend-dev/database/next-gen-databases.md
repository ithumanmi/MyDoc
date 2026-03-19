# 🚀 Next-Gen Databases: vector, graph, distributed SQL, time-series

> [← Back to Database Hub](./README.md)

Khi workload mới (AI, graph social, thanh toán đa region) xuất hiện, cần những database chuyên biệt. Dưới đây là 4 nhóm nổi bật.

---

## 🧭 1. Vector Databases
Đại diện: Pinecone, Milvus, Weaviate, Qdrant, `pgvector` (Postgres).

Giải quyết: tìm kiếm theo ngữ nghĩa/embedding (RAG, hình ảnh, audio) thay vì exact text.

Ý chính: LLM biến văn bản thành vector nhiều chiều, DB tối ưu nearest-neighbor (cosine/L2/inner product) để trả về kết quả gần nhất về nghĩa.

---

## 🕸️ 2. Graph Databases
Đại diện: Neo4j, Amazon Neptune, ArangoDB.

Giải quyết: phân tích quan hệ nhiều bậc (fraud ring, social graph, recommendation) với traversal nhanh hơn JOIN sâu trên RDBMS.

---

## 🌍 3. Distributed SQL
Đại diện: Google Cloud Spanner, CockroachDB, TiDB, YugabyteDB.

Giải quyết: mở rộng ngang mà vẫn ACID và SQL chuẩn, thay cho sharding thủ công của RDBMS truyền thống.

Ý chính: kiến trúc consensus (Raft/Paxos), auto-rebalancing, multi-region, giữ transaction semantics quen thuộc.

---

## 📈 4. Time-Series Databases
Đại diện: InfluxDB, TimescaleDB, Prometheus.

Giải quyết: ghi/đọc dữ liệu gắn timestamp với throughput cao (IoT, metrics, market data) nhờ storage append-only, nén và aggregation theo thời gian.

Ý chính: ưu tiên write nhanh, retention policy, downsampling, query theo window/time-bucket.

**Chọn đúng tool cho đúng bài toán:**
- Vector: tìm kiếm ngữ nghĩa/RAG.
- Graph: phân tích quan hệ sâu.
- Distributed SQL: ACID + scale ngang.
- Time-series: ingest/query dữ liệu theo thời gian.
