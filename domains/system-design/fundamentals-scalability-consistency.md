# ⚖️ Scalability & Consistency Fundamentals

> [← Back to System Design](./README.md) | [Glossary](../../GLOSSARY.md)

Tài liệu này tập trung vào ba trụ cột khi thiết kế hệ thống phân tán: **CAP & consistency**, **replication** và **sharding**. Đây là những câu hỏi phỏng vấn kinh điển cho mọi cấp độ.

---

## 1. CAP Theorem & Consistency Spectrum

### CAP nhắc lại
- **Consistency (C):** Mọi replica thấy cùng dữ liệu ngay sau khi ghi.
- **Availability (A):** Hệ thống trả lời mọi request (thành công hoặc lỗi) ngay cả khi một số replica gặp sự cố.
- **Partition tolerance (P):** Hệ thống vẫn hoạt động khi mạng bị phân mảnh (lossy link, split brain).

> Trong môi trường phân tán, P là bắt buộc. Do đó bạn phải chọn thiên về **CP** (ưu tiên tính nhất quán) hoặc **AP** (ưu tiên luôn trả lời).

### Strong vs Eventual Consistency
| Model | Ưu điểm | Hạn chế | Ví dụ / Khi dùng |
| --- | --- | --- | --- |
| **Strong** | Đọc luôn thấy dữ liệu mới nhất → UX rõ ràng | Latency cao, khó scale toàn cầu | Banking, isomorphic counter, metadata quan trọng |
| **Eventual** | Latency thấp, hấp thụ partition tốt | Có thể thấy dữ liệu cũ ⇒ cần UX xử lý | News feed, counters, analytics |
| **Bounded Staleness / Tunable** | Kiểm soát stale bằng số replica hoặc thời gian | Phải tinh chỉnh, phức tạp | Cassandra (tunable, CL=QUORUM) |

**Khi nào chấp nhận eventual?**
- Khi dữ liệu có thể tạm thời lệch mà không gây thiệt hại (ví dụ: lượt like, số lượt xem).
- Khi cần ưu tiên Availability (AP) trong CAP, ví dụ hệ thống global cần chống partition.
- Khi có thể bổ sung cơ chế *read-your-writes* hoặc *per-user cache* để che giấu độ trễ đồng bộ.

---

## 2. Replication Patterns

### Primary-Replica (Master-Slave)
- **Write**: Gửi vào Primary → replicate sang Replica.
- **Read**: Có thể đọc từ Replica để scale throughput.
- **Sync vs Async**: Sync giữ dữ liệu Strong nhưng chậm; Async nhanh nhưng có RPO > 0 (mất dữ liệu nếu Primary chết).

### Quorum & Tunable Consistency
- Tham số **W** (write quorum) và **R** (read quorum). Nếu `W + R > N` (N = tổng replica) → đảm bảo Strong cho key đó.
- Ví dụ Cassandra/Dynamo: chọn Consistency Level = ONE, QUORUM, ALL tùy trường hợp.
- **Trade-off**: QUORUM tăng latency nhưng giảm khả năng đọc dữ liệu cũ.

### Conflict Resolution (Multi-leader / Eventually Consistent)
- **Last-write-wins (timestamp)**: đơn giản nhưng lệ thuộc clock, có thể mất dữ liệu.
- **Version vector / Vector clock**: Lưu lịch sử để phát hiện concurrent updates → yêu cầu merge.
- **CRDT / OT**: Cho phép merge không xung đột cho dữ liệu đặc biệt (counter, set, text).

---

## 3. Sharding Essentials

### Partition Key
- Chọn dựa trên `user_id`, `tenant_id`, geo hoặc hash. Mục tiêu: phân phối đều và dễ suy luận.
- Tránh shard key có hot spot (ví dụ timestamp tăng dần) nếu throughput cao.

### Hot Partition
- Khi một shard nhận quá nhiều traffic so với phần còn lại.
- **Biện pháp:**
  - Sử dụng **hash-based** key hoặc thêm *salt* vào key.
  - **Hierarchical partition:** shard theo quốc gia rồi hash trong quốc gia đó.
  - **Autosplit:** tự động chia shard khi vượt ngưỡng (MongoDB, Bigtable).

### Rebalancing & Metadata
- **Consistent Hashing:** giảm số key phải di chuyển khi thêm node.
- **Central Shard Map:** Dịch vụ lookup (config server, placement driver) → cache ở client để giảm latency.
- **Live migration:** Read/write song song 2 shard trong thời gian chuyển đổi, dùng dual-write + checksum để đảm bảo an toàn.

### Checklist khi thiết kế sharding
1. Shard key là gì? Có đảm bảo truy vấn chính nằm trong cùng shard?
2. Làm sao cập nhật shard map cho hàng triệu client?
3. Chiến lược reshard (scale-out) và scale-in như thế nào?
4. Backup/restore per shard ra sao?

---

## 4. Cheat Sheet phỏng vấn

| Câu hỏi | Ý chính cần trả lời |
| --- | --- |
| Nếu xảy ra partition? | Chọn Strong (CP) hay Available (AP) và giải thích theo domain. |
| Làm sao tránh đọc stale khi eventual consistency? | Lamda architecture: ghi log, cache per-user, read repair. |
| Replication conflict giải quyết thế nào? | Timestamp, vector clock, CRDT, hoặc merge manual. |
| Shard key và hot partition? | Dùng hash + salt, autosplit, hoặc dedicated cluster cho tenant lớn. |

---

## 5. Tiếp tục học gì?
- [System Design Fundamentals (tổng quan)](./system-design-fundamentals.md)
- [Design Distributed Cache](./design-distributed-cache.md) để thấy replication/chia shard trong thực tế.
- [Design Rate Limiter](./design-rate-limiter.md) cho ví dụ multi-dimensional quota.