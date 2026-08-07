# 🧮 Thuật Toán Backend Nâng Cao

> [← Quay lại Backend Development](../README.md)

Ở quy mô rất lớn, các cấu trúc dữ liệu chuẩn (List, Set, HashMap) tốn quá nhiều bộ nhớ. Ta cần các **cấu trúc dữ liệu xác suất** và thuật toán hiệu quả hơn.

---

## 1. Cấu trúc dữ liệu xác suất
Đánh đổi một phần độ chính xác để tiết kiệm bộ nhớ. "Có lẽ đúng" còn hơn "hết bộ nhớ".

### **Bloom Filter**
*   **Câu hỏi:** "Phần tử này có trong tập không?"
*   **Trả lời:** "Có thể có" hoặc "Chắc chắn không" (không có false negative).
*   **Cách làm:** Băm (hash) nhiều lần và đặt bit trong mảng bit.
*   **Ứng dụng:**
    *   **Database:** Kiểm tra tồn tại trước khi truy vấn đĩa (Postgres/Cassandra dùng).
    *   **Username:** Kiểm tra "username123" đã được dùng chưa mà không cần truy vấn DB.
    *   **Crawler:** Kiểm tra URL đã thăm chưa.
*   **Ưu:** O(1), bộ nhớ rất nhỏ (MB cho hàng tỷ phần tử).
*   **Nhược:** Có thể false positive. Không xóa được phần tử.

### **HyperLogLog (HLL)**
*   **Câu hỏi:** "Có bao nhiêu phần tử duy nhất trong dòng dữ liệu lớn?" (độ hiếm/độ phong phú).
*   **Trả lời:** Xấp xỉ, sai số ~0.81% với chỉ ~12KB bộ nhớ.
*   **Cách làm:** Hash phần tử và đếm số bit 0 liên tiếp ở đầu.
*   **Ứng dụng:**
    *   Đếm unique visitor (DAU/MAU) trong Redis (`PFADD`, `PFCOUNT`).
    *   Đếm IP duy nhất trong tấn công DDoS.

### **Count-Min Sketch**
*   **Câu hỏi:** "X xuất hiện bao nhiêu lần?" (tần suất).
*   **Trả lời:** "Ít nhất N lần" (có thể ước lượng cao hơn thực tế).
*   **Ứng dụng:**
    *   Top K video được xem nhiều.
    *   Hashtag đang trending.

---

## 2. Thuật toán không gian địa lý
Tìm kiếm hiệu quả trên bản đồ.

### **GeoHash**
*   **Khái niệm:** Mã hóa Lat/Long thành chuỗi (Base32).
*   **Tính chất:** Chung tiền tố => Gần nhau.
    *   `u4pruydqqv` (London)
    *   `u4pruydqqw` (lân cận London)
*   **Ứng dụng:** Tìm tài xế gần (Uber). Truy vấn: `SELECT * WHERE geohash LIKE 'u4pru%'`.
*   **Ưu:** So khớp chuỗi đơn giản.
*   **Nhược:** Biên ô lưới có thể lệch (hàng xóm khác tiền tố).

### **QuadTree**
*   **Khái niệm:** Chia không gian 2D thành 4 phần tư đệ quy.
*   **Cấu trúc:** Node chứa điểm dữ liệu hoặc 4 node con.
*   **Ứng dụng:** Vẽ bản đồ, phát hiện va chạm.
*   **Ưu:** Độ phân giải thích ứng (vùng dày đặc có cây sâu hơn).

---

## 3. Thuật toán giới hạn tốc độ (Rate Limiting)

### **Token Bucket**
*   **Khái niệm:** Một xô chứa `N` token. Token được thêm với tốc độ `R` mỗi giây.
*   **Hành vi:** Mỗi request tiêu thụ 1 token. Hết token -> từ chối.
*   **Ưu:** Cho phép **burst** (người dùng rảnh 10s, sau đó gửi 10 request cùng lúc).
*   **Triển khai:** Redis Lua script (atomic `GET` + `DECR`).

### **Leaky Bucket**
*   **Khái niệm:** Xô có lỗ rò. Request đi vào xô, nước rò ra với tốc độ cố định.
*   **Hành vi:** Xô đầy -> tràn -> từ chối.
*   **Ưu:** Làm phẳng lưu lượng (tốc độ ra cố định). Bảo vệ dịch vụ nội bộ.
*   **Nhược:** Không cho burst.

---

## 4. Thuật toán băm
Mục tiêu tốc độ và phân phối, không phải bảo mật.

### **Consistent Hashing**
*   **Bài toán:** Cân bằng lại cache khi thêm/bớt node.
*   **Giải pháp:** Map cả Node và Key lên vòng tròn (0-360°). Key thuộc node kế tiếp theo chiều kim đồng hồ.
*   **Virtual Nodes:** Mỗi node vật lý có nhiều điểm trên vòng tròn để phân phối đều.
*   **Ứng dụng:** Phân vùng trong DynamoDB, Cassandra, Memcached.

### **MurmurHash / xxHash**
*   **Mục tiêu:** Nhanh và phân phối đều (không phải bảo mật).
*   **Hiệu năng:** Nhanh hơn SHA-256/MD5 khoảng 10-100 lần.
*   **Ứng dụng:** Hash map, Bloom filter, cân bằng tải, sharding key.

---

## ✅ Apply it
- [ ] Tích hợp Bloom Filter hoặc Cuckoo Filter trước database query để giảm IO, đo tỷ lệ false positive.
- [ ] Dùng HyperLogLog (Redis `PFADD`) để tính DAU/MAU và so sánh với số liệu từ warehouse.
- [ ] Viết thử Count-Min Sketch trong service ghi log để suy đoán top URL truy cập mà không cần full aggregation.
- [ ] Benchmark token bucket vs leaky bucket trong API Gateway với cùng traffic pattern.
- [ ] Tạo PoC consistent hashing bằng 3 node Redis cache, đo thời gian rebalance khi thêm node thứ 4.

## 🔗 Cross-reference
- [Scaling Strategy](./scaling-strategy.md) – chiến thuật tổng thể khi cần cache/sharding.
- [Monitoring & Observability](../monitoring-observability.md) – theo dõi tỉ lệ lỗi của probabilistic structure.
- [System Design Universe](../system-design/system-design-universe.md) – layer Performance & Storage.
