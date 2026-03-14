# Challenge: REST API với Auth JWT, Rate Limit, Pagination

- **Loại:** project
- **Mảng:** backend
- **Mức:** Intermediate
- **Ước lượng thời gian:** 2-4 ngày
- **Prerequisites (tùy chọn):** [`domains/backend-dev/README.md`](../../domains/backend-dev/README.md) · [`domains/backend-dev/testing-guide.md`](../../domains/backend-dev/testing-guide.md)

## Mục tiêu học tập
- Thiết kế REST API chuẩn với auth JWT, pagination, rate limiting.
- Viết test (unit/integration) cho auth, pagination, error cases.
- Logging/metrics cơ bản cho API.

## Đề bài
Xây dựng API cho 1 resource (ví dụ: `articles` hoặc `products`):
- Đăng ký/đăng nhập (JWT), refresh token (tùy chọn).
- CRUD resource, với pagination + filter cơ bản.
- Rate limit trên IP hoặc user (ví dụ 100 req/10 phút).

## Đầu vào (Input)
- REST endpoints: `/auth/register`, `/auth/login`, `/items` (CRUD + GET list with `page`, `page_size`).
- DB tùy chọn (Postgres khuyến khích).

## Đầu ra (Output)
- API chạy được với JWT bảo vệ endpoints (trừ đăng ký/đăng nhập).
- Pagination trả về `items`, `page`, `page_size`, `total`.
- Rate limit trả 429 khi vượt ngưỡng.

## Tiêu chí chấm (Acceptance)
- **Đúng chức năng:** CRUD hoạt động, pagination đúng, auth bảo vệ, rate limit hoạt động.
- **Test:** Có test cho auth (login sai/đúng), pagination, rate limit (hoặc mock), error handling.
- **Code quality:** Cấu trúc rõ (routes/handlers/service/repo), .env mẫu, hướng dẫn chạy.

## Gợi ý / Hint
- Sử dụng middleware cho auth + rate limit.
- Trả về `X-RateLimit-*` headers nếu tiện.
- Seed 5-10 bản ghi để kiểm tra pagination.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Thêm link repo mẫu hoặc ghi chú test kịch bản.