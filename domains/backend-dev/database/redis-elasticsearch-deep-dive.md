# Redis & ElasticSearch internals: tại sao nhanh, dùng khi nào

> [← Back to Database Guides](./README.md)

PostgreSQL/MySQL có thể nghẽn I/O khi RPS cao. Redis và Elasticsearch bổ sung: cache in-memory và search full-text/distributed.

---

## ⚡ 1. Redis internals

Vì sao Redis xử lý 100,000+ RPS trên một CPU?

### A. I/O multiplexing
Single-thread + `epoll/kqueue` giảm context switch, tránh lock contention, quét request mạng liên tục.

### B. Persistence: RDB vs AOF
- **RDB snapshot:** ghi định kỳ, khôi phục nhanh, có thể mất dữ liệu mới nhất.
- **AOF:** ghi append-only, ít mất dữ liệu hơn, dung lượng lớn hơn; có chế độ fsync.
- Thực tế thường bật cả hai.

### C. Eviction policies
Khi hết RAM: `noeviction`, `allkeys-lru`, `volatile-lru`, LFU, random. Chọn theo use case cache.

---

## 🔍 2. Elasticsearch internals

Cú pháp SQL `LIKE '%iPhone Pro Max%'` Trên Bảng 10 Triệu Sản Phẩm Sẽ Quét Toàn Bộ Bảng (Full Table Scan), Treo DB Cổ 10 Giây!
Đó Là Lúc Động Cơ ElasticSearch (Luật Java Lucene Engine) Phóc Dậy Và Xé Xác Kết Quả Trong **Tuyệt Đối 15ms**. Tại Sao?

### A. Inverted index
Analyzer tách token, chuẩn hóa, lưu token → danh sách document ID để search nhanh theo từ khóa (TF/IDF/BM25).

### B. Sharding & replication
Index gồm nhiều shard, phân tán node, search theo scatter-gather. Có replica shard để HA và tăng throughput read.

Khi dùng Elastic:
- Full-text search, aggregations, autocomplete.
- Log/metrics search (ELK), phân tích semi-structured data.
