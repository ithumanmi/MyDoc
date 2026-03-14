# Challenge: CQRS + Outbox + Idempotency API

- **Loại:** project
- **Mảng:** backend
- **Mức:** Intermediate
- **Ước lượng thời gian:** 1-2 tuần
- **Prerequisites:** [`domains/backend-dev/README.md`](../../domains/backend-dev/README.md) · [`domains/backend-dev/system-design-guide.md`](../../domains/backend-dev/system-design-guide.md)

## Mục tiêu học tập
- Thiết kế API ghi/đọc tách biệt (CQRS) cho throughput cao.
- Đảm bảo **exactly-once** effect bằng **outbox pattern** + idempotency key.
- Thiết lập quan sát hệ thống: metrics, tracing, structured logs.

## Đề bài
Xây dựng service **Orders**:
- **Write model (command):** create/update order, thanh toán giả lập.
- **Read model (query):** trả về trạng thái order, lịch sử event.
- **Event delivery:** dùng **outbox table** để publish events sang message broker giả lập (có thể dùng background job + local queue).
- **Idempotency:** mọi request tạo/cập nhật đều dùng idempotency key (header) và trả cùng response nếu lặp lại.

## Đầu vào (Input)
- REST/gRPC endpoints cho create/update/get order.
- DB: Postgres (khuyến nghị) với bảng orders + outbox.
- Idempotency-Key header cho các lệnh ghi.

## Đầu ra (Output)
- API hoạt động với idempotency (request lặp không tạo bản ghi trùng).
- Outbox job xuất events (in-memory queue/log hoặc file) có đánh dấu delivered.
- Query model trả kết quả nhất quán.

## Tiêu chí chấm (Acceptance)
- **Đúng chức năng:**
  - Create/update trả 200/201, lặp lại cùng idempotency key trả cùng response, không nhân bản side-effects.
  - Read trả đúng trạng thái sau khi event được xử lý.
- **Độ tin cậy:**
  - Outbox retry được khi publish fail (có trạng thái pending → success/failed).
- **Quan sát:**
  - Metrics: số request, latency, error rate; queue length.
  - Logs có correlation id / trace id.
- **Code quality:** cấu trúc rõ ràng (domain/service/repo), test cơ bản cho idempotency + outbox.

## Gợi ý / Hint
- Idempotency store: bảng idempotency (key, request hash, response body, status, expiry).
- Outbox: insert trong cùng transaction với command; worker đọc theo batch, đánh dấu delivered.
- Có thể dùng một queue đơn giản (Redis list / local file) nếu không có Kafka/RabbitMQ.

## Reference solution (tùy chọn)
- Ghi lại kiến trúc + lược đồ DB + cách test trong README của bạn.
- (Tuỳ chọn) Public repo: thêm link tại đây.