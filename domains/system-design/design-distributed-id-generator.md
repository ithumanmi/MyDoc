# 🔑 Deep Dive: Design Distributed ID Generator (Snowflake, UUID, KGS)

> **"Mục tiêu: Tạo ID duy nhất toàn hệ thống với độ trễ thấp, không bị trùng khi scale đa region."**

---

## 1. Clarify Requirements

### Functional Requirements
*   **Uniqueness:** Mọi bản ghi trong hệ thống phải có ID không trùng.
*   **Sortable (Optional):** ID tăng dần theo thời gian để hỗ trợ pagination.
*   **High Throughput:** Hàng triệu ID/giây.
*   **Low Latency:** < 1ms per ID generation.

### Non-Functional Requirements
*   **High Availability:** Không được downtime, dễ mở rộng node.
*   **Multi-region:** Hỗ trợ nhiều datacenter mà không trùng ID.
*   **Observability:** Theo dõi sequence, đồng hồ lệch, node health.

---

## 2. Candidate Approaches

| Phương pháp | Ưu điểm | Nhược điểm | Khi dùng |
| --- | --- | --- | --- |
| **UUID v4** | Random, không cần coordination | Không sortable, 36 ký tự, tốn storage/index | Thích hợp cho distributed cache, không cần order |
| **UUID v7/v8** | Có timestamp component → sortable | Chuẩn mới, cần lib hỗ trợ | Khi muốn keep globally unique + approximate order |
| **Database Auto Increment** | Đơn giản, có order | Bị bottleneck khi scale (single DB) | Monolith nhỏ |
| **KGS (Key Generation Service)** | Trung tâm tạo ID tăng dần | Single point of failure nếu không HA | Khi cần kiểm soát chặt chẽ format ID |
| **Snowflake (Twitter)** | Sortable, phân tán, throughput cao | Cần đồng bộ clock, quản lý worker ID | Hầu hết hệ thống scale lớn |
| **Hi/Lo Allocation** | DB cấp `hi`, app tự tăng `lo` | Cần quản lý expiry hi block | Khi vẫn dùng SQL nhưng muốn giảm contention |

---

## 3. Snowflake Style ID

```text
| 1 bit (sign) | 41 bits timestamp | 5 bits datacenter | 5 bits worker | 12 bits sequence |
```

*   **Timestamp:** Milliseconds since custom epoch (ví dụ 2020-01-01).
*   **Datacenter & Worker ID:** Cho phép tối đa 32 DC × 32 worker = 1024 node.
*   **Sequence:** 4096 ID mỗi ms cho mỗi worker.

### Flow
1.  Client gọi ID service.
2.  Service đọc đồng hồ hiện tại (millisecond).
3.  Nếu cùng millisecond → tăng `sequence`. Nếu sequence vượt 4095 → chờ 1ms tiếp theo.
4.  Ghép bit -> trả ID dạng số 64-bit.

### Handling Clock Drift
*   **NTP sync** tất cả node.
*   Nếu phát hiện clock lùi (timestamp < last_timestamp) →
    *   Chờ đến khi đồng hồ catch-up.
    *   Hoặc bật `clock_backwards_tolerance` (cho phép lùi X ms, map sang sequence region).

---

## 4. Key Generation Service (KGS)

### Kiến trúc

```mermaid
flowchart LR
    App --> LoadBalancer --> KGSCluster
    KGSCluster --> DB[(ID Blocks Table)]
```

*   DB giữ bảng `id_blocks` với cột `next_id`.
*   Mỗi node lấy block (ví dụ 10k ID). Khi block sắp hết → lấy block mới (optimistic lock).
*   Đảm bảo HA bằng replication + leader election.

### Trade-offs
*   Đơn giản nhưng vẫn có shared state (DB).
*   Phù hợp nếu muốn ID có format đặc biệt (prefix theo entity).

---

## 5. Hi/Lo Pattern

*   DB cấp `hi = next_block`. Ứng dụng tạo ID = `hi * block_size + local_counter`.
*   Ví dụ block_size=1000 → app tạo được 1000 ID tại chỗ trước khi cần DB.
*   Ưu điểm: Giảm load DB, vẫn đảm bảo order tương đối.
*   Nhược điểm: Mất ID nếu node chết (có thể chấp nhận nếu ID chỉ cần unique, không liên tục).

---

## 6. Interview Pro-tips

1.  **ID collision:** Giải thích vì sao UUID v4 hầu như không trùng (2^122 space).
2.  **Hotspot index:** ID tăng dần có thể gây hotspot ở DB (B-Tree). Cần shard theo hash hoặc dùng UUID.
3.  **Storage format:** 64-bit integer < 16 bytes vs 36-char UUID (text) → ảnh hưởng size index.
4.  **Data privacy:** ID tuần tự dễ bị đoán (order_id). Có thể encode Base62 hoặc thêm salt để tránh lộ số lượng đơn hàng.
5.  **Multi-region:** Worker ID mapping theo region để tránh trùng khi cross-region replication.

---

## 7. Monitoring & Operations

*   **Metrics:** `ids_generated_per_sec`, `sequence_exhausted_count`, `clock_skew_ms`.
*   **Alert:** Khi sequence full liên tục (>500ms) → cần scale thêm worker hoặc tăng bits allocation.
*   **Deployment:** Rolling restart phải giữ nguyên worker ID (persist config) để tránh overlap.

---

## 8. Quick Estimation Template

| Thông số | Ví dụ | Ghi chú |
| --- | --- | --- |
| Max QPS | 5 triệu ID/s | Chọn số worker & sequence bits phù hợp |
| Sequence bits | 12 | 4096 ID/ms mỗi node |
| Worker count | 256 | 8 bits worker + datacenter |
| Epoch | 2024-01-01 | Cho phép 69 năm nếu dùng 41 bits timestamp |

---

## 📚 Bài tiếp theo
*   [Design URL Shortener](./design-url-shortener.md) – cần ID generator cho slug.
*   [Design Chat System](./design-chat-system.md) – tạo `message_id` đảm bảo order.
