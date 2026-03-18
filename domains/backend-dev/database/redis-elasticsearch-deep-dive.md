# Giải Phẫu Động Cơ Dữ Liệu Thời Gian Thực: Redis & ElasticSearch Internals

> [← Back to Database Guides](./README.md)

Khi scale hệ thống Backend lên đáp ứng hàng chục nghìn Request/s (RPS), PostgreSQL/MySQL truyền thống (Dùng thuật toán B-Tree trên Ổ Disk) bị thắt cổ chai vòng quay Read/I/O. Giải pháp bắt buộc cho Senior Engineer là kết hợp bộ giáp đệm: **Redis** và **ElasticSearch**.

Tuy nhiên, đừng dừng lại ở mức "Set/Get" hay "Match Keyword". Hãy cùng mổ xẻ "Bộ Lòng" của chúng để biết tại sao chúng lại nhanh như điện!

---

## ⚡ 1. Redis Internals (Quái Vật In-Memory Bộ Nhớ Trong)

Tại sao Redis xử lý được 100,000+ RPS trên một nhân CPU Duy Nhất (Single Thread)? 

### A. I/O Multiplexing (Ma Thuật Đơn Luồng)
NodeJS Single-Thread bị nghẽn Event Loop. Redis Singe-Thread thì dùng `epoll/kqueue` Của Linux Cực Sát Tầng Máy. Thay vì tốn Ram Mở Khung Hàng Trăm Thread Tranh Giành CPU (Context Switch), 1 Nhân CPU Của Redis quét vòng cực sốc tất cả các Request Network, làm thay đổi cấu trúc RAM liền mạch không kẹt Lock!

### B. Mất Điện Có Bay Dữ Liệu Không? (RDB vs AOF Persistence)
Mọi dữ liệu Redis ráng Cắm Trong RAM, Tắt Máy Mất Data Trắng! 
Để Chống Chết, Redis Gắn 2 Ống Cứu Sinh:
*   **RDB (Redis Database Snapshots):** Cắt Dịch File Dump Ra Đĩa Cứ 5 Phút 1 Lần. Nén Cực Nhanh Nhưng Dễ Bay Text Vừa Viết Trong 4 Phút Quá Nhanh Chờ Lưu!
*   **AOF (Append Only File):** Trận Chiến Như Kafka Log! Cứ Gõ `SET Tên Nam`, Redis Cầm Lệnh Đó Ghi Vào Cuối 1 Cuộn File Sổ Chỉ Dài Chữ Chú Text. Khôi Cạn Nhanh Cực Không Sợ Sai Sót Nhưng Cực Tốn Dung Lượng Disk Quen Tốc Ghi Cắt Chân IO Tức Thời Giây 1 Lần Nhịp (fsync).
-> *Thực Hành Senior:* Thường Mix Bật Cả 2: Lấy RDB Load Nhanh Nhất, Giật Khoảng Cuối Dò Móc AOF Lại Bù!

### C. Đầy RAM Thì Nó Vứt Data Ai Trước? (Eviction Policies)
Khoảng Hở Cache Gắn Cục:
Khi Cache Đụng Nóc MaxMemory, Redis Có Khả Năng Diệt Data Theo Mệnh:
- `noeviction`: Báo Lỗi Chết Đứng Trả Báo Lỗi Kính OOM!
- `allkeys-lru` (Least Recently Used): Data Mốc Cũ, Ít Truy Cập Cuối Cùng Dạt Bỏ Đầu Tiên! Thuật Toán Sống Còn Của Session Và Caching Cache-Aside Vĩ Đại. 

---

## 🔍 2. ElasticSearch Internals (Ma Thuật Phân Rã Ngữ Nghĩa)

Cú pháp SQL `LIKE '%iPhone Pro Max%'` Trên Bảng 10 Triệu Sản Phẩm Sẽ Quét Toàn Bộ Bảng (Full Table Scan), Treo DB Cổ 10 Giây!
Đó Là Lúc Động Cơ ElasticSearch (Luật Java Lucene Engine) Phóc Dậy Và Xé Xác Kết Quả Trong **Tuyệt Đối 15ms**. Tại Sao?

### A. Inverted Index (Chỉ Mục Ma Cận Cắt Giấy)
Khi bạn Nạp Chữ: `Sách Code Dạo Ở Lâu` Vào Elastic. Nó Không Lưu Nguyên Cục Chữ Nhau SQL B-Tree.
Nó Cho Vào Máy Tán Xé Thành Hạt (Analyzer):
- Bỏ Chữ Thừa (Stop words): Sách, Code, Dạo, Ở, Lâu.
- Đổi Cận (Lowercase).
- Gom Xây Điểm Nghịch Đảo Theo Chữ, Gắn ID Bản Record Phía Sau:
  - Đầu Sách Chữ `code` -> Nằm Mảnh Text Của Document ID: `[1, 15, 30]`
  - Đầu Sách Chữ `dạo` ->  Nằm Mảnh Text Của Document ID: `[1, 5, 8]`

Gõ Tìm: "Code Khung". Tìm Vào Array Nhanh Khung Cáp Báo Hash O(1) Báo Gặp Chữ Cũ Giao Tập Array O(1) Lấy Giao Document Chồng Đỉnh Score Chặn O(N)!

### B. Sharding Đầu Dữ Liệu Luôn Nhanh 
Mảnh Index Quá Lớn Chứa Không Nổi RAM Quật Tìm Máy Java Bóp Kén. Elasticsearch Tách Nát Gốc Bụi Căn Index Bỏ Cho X Shards Phóng Rải Rác 10 Máy Node (Scale-Out Horizontal). Node Nào Tìm Cũng Trả Data Chạy Nhanh Xong Vào Nút Trưởng Node Gút Đưa Quá List Sách Frontend (Scatter-Gather Phase). Tốc Đỉnh Thuật Kiến Phân Tán Đẳng Cấp Ngã Làng!
