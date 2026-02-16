# 🔌 API Design Guide: The Interface of Your Backend

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)

API là "bộ mặt" của hệ thống Backend. API tồi = Client khổ, bugs nhiều, khó maintain. API tốt = Developer Experience (DX) tuyệt vời. Hướng dẫn này giúp bạn thiết kế API chuẩn mực như Stripe hay GitHub.

---

## 📋 Mục lục

1. [RESTful API Design](#1-restful-api-design-nguyên-tắc-cốt-lõi)
2. [API Versioning](#2-api-versioning-quản-lý-thay-đổi)
3. [Request & Response Format](#3-request--response-format-chuẩn-hóa-giao-tiếp)
4. [Authentication & Authorization](#4-authentication--authorization-bảo-mật-api)
5. [Rate Limiting & Throttling](#5-rate-limiting--throttling-bảo-vệ-hệ-thống)
6. [Documentation](#6-documentation-tài-liệu-là-nhất)
7. [GraphQL vs REST](#7-graphql-vs-rest-khi-nào-dùng-gì)
8. [Action Plan](#8-action-plan-checklist-thiết-kế)

---

## 1. RESTful API Design: Nguyên tắc cốt lõi

### 1.1. Resource Naming (Danh từ, không phải Động từ)

*   ❌ **Sai:** `/getUsers`, `/createUser`, `/deleteUser?id=1`
*   ✅ **Đúng:**
    *   `GET /users` (Lấy danh sách)
    *   `POST /users` (Tạo mới)
    *   `GET /users/1` (Lấy chi tiết)
    *   `PUT /users/1` (Update toàn bộ)
    *   `PATCH /users/1` (Update một phần)
    *   `DELETE /users/1` (Xóa)

**Quy tắc:** Dùng **Số nhiều (Plural)** cho resource name (`/users`, không phải `/user`).

### 1.2. HTTP Methods Semantic

| Method | Ý nghĩa | Idempotent? | Safe? |
| :--- | :--- | :--- | :--- |
| **GET** | Lấy dữ liệu. Không thay đổi server state. | ✅ Yes | ✅ Yes |
| **POST** | Tạo resource mới. | ❌ No | ❌ No |
| **PUT** | Thay thế resource (ghi đè toàn bộ). | ✅ Yes | ❌ No |
| **PATCH** | Sửa đổi một phần resource. | ❌ No (thường là yes) | ❌ No |
| **DELETE** | Xóa resource. | ✅ Yes | ❌ No |

*Idempotent: Gọi 1 lần hay 10 lần thì kết quả server state vẫn giống nhau.*

### 1.3. Status Codes Masterclass

Đừng chỉ dùng `200` cho mọi thứ!

*   **Success:**
    *   `200 OK`: Thành công chung.
    *   `201 Created`: Tạo thành công (Trả về sau POST).
    *   `204 No Content`: Xử lý xong, không trả về body (Thường dùng cho DELETE).
*   **Client Error:**
    *   `400 Bad Request`: Input sai format (thiếu field, sai type).
    *   `401 Unauthorized`: Chưa login (thiếu token).
    *   `403 Forbidden`: Đã login nhưng không có quyền (User thường đòi xóa Admin).
    *   `404 Not Found`: Resource không tồn tại.
    *   `422 Unprocessable Entity`: Format đúng nhưng logic sai (VD: Email đã tồn tại).
    *   `429 Too Many Requests`: Bị rate limit.
*   **Server Error:**
    *   `500 Internal Server Error`: Code lỗi, DB sập (Developer fix gấp).

### 1.4. Pagination, Filtering, Sorting

Đừng bao giờ trả về toàn bộ DB (`SELECT * FROM users`).

*   **Pagination:**
    *   **Offset-based:** `GET /users?page=2&limit=10` (Dễ implement, nhưng chậm khi offset lớn).
    *   **Cursor-based:** `GET /users?cursor=xyz&limit=10` (Nhanh, dùng cho infinite scroll).
*   **Filtering:** `GET /users?role=admin&status=active`
*   **Sorting:** `GET /users?sort=-created_at` (Dấu `-` là DESC).
*   **Field Selection:** `GET /users?fields=id,name` (Giảm payload size).

---

## 2. API Versioning: Quản lý thay đổi

API là contract. Đừng phá vỡ contract mà không báo trước.

### 2.1. Strategies

1.  **URL Versioning (Phổ biến nhất):**
    *   `https://api.example.com/v1/users`
    *   Dễ nhìn, dễ cache.
2.  **Header Versioning (REST chuẩn):**
    *   `Accept: application/vnd.example.v1+json`
    *   URL sạch, nhưng khó test trên browser.

### 2.2. Breaking vs Non-breaking Changes

*   **Non-breaking:** Thêm field mới vào response, thêm optional parameter. → *Không cần tăng version.*
*   **Breaking:** Đổi tên field (`userId` → `id`), xóa field, đổi data type, đổi logic validation. → *Bắt buộc tăng version (v1 → v2).*

### 2.3. Deprecation Strategy

Khi ra v2, đừng xóa v1 ngay.
1.  Thông báo deprecation (Email, Blog).
2.  Thêm header vào response v1: `Warning: 299 - "This API is deprecated"`.
3.  Support v1 thêm 6-12 tháng.

---

## 3. Request & Response Format: Chuẩn hóa giao tiếp

### 3.1. Naming Convention

*   **JSON Fields:** Chọn 1 và nhất quán.
    *   `camelCase`: Chuẩn JavaScript/Node.js (`userId`, `createdAt`). **Khuyên dùng.**
    *   `snake_case`: Chuẩn Python/Database (`user_id`, `created_at`).
*   **Enveloping:** Có nên bọc data không?
    *   Option 1 (Envelope): `{ "data": [...], "meta": { "page": 1 } }`
    *   Option 2 (Direct): `[...]` (Kèm headers cho metadata).

### 3.2. Error Response Structure (RFC 7807)

Đừng trả về string "Lỗi rồi". Hãy trả về JSON có cấu trúc.

```json
// HTTP 422
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Validation failed",
    "details": [
      { "field": "email", "message": "Email is invalid" },
      { "field": "password", "message": "Too short" }
    ]
  }
}
```

### 3.3. Date & Time

Luôn dùng **ISO 8601** và **UTC**.
*   ✅ `2026-02-16T14:30:00Z`
*   ❌ `16/02/2026` (Mỹ hay VN?), Timestamp (khó đọc).

---

## 4. Authentication & Authorization: Bảo mật API

### 4.1. JWT Best Practices

*   **Stateless:** Server không lưu session.
*   **Storage:**
    *   Web: `HttpOnly Cookie` (Chống XSS).
    *   Mobile: `Secure Storage` (iOS Keychain).
*   **Expiry:**
    *   Access Token: Ngắn (15-30 phút).
    *   Refresh Token: Dài (7-30 ngày) - Dùng để lấy Access Token mới.

### 4.2. OAuth 2.0 Flows

1.  **Authorization Code Flow:** Chuẩn cho Web/Mobile apps (Cần server backend trao đổi token).
2.  **Client Credentials Flow:** Server-to-Server (VD: Backend gọi PayPal API).

### 4.3. CORS (Cross-Origin Resource Sharing)

Chỉ cho phép domain tin cậy gọi API.

```javascript
// Node.js (Express)
app.use(cors({
  origin: ['https://myapp.com', 'https://admin.myapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));
```

---

## 5. Rate Limiting & Throttling: Bảo vệ hệ thống

Ngăn chặn abuse và DDoS.

### 5.1. Headers

Trả về headers để client biết tình trạng:
*   `X-RateLimit-Limit`: 1000 (Requests/hour)
*   `X-RateLimit-Remaining`: 900
*   `X-RateLimit-Reset`: 1678888888 (Unix timestamp khi reset)

### 5.2. Algorithms

*   **Token Bucket:** Cho phép burst traffic ngắn hạn.
*   **Fixed Window:** Reset mỗi giờ.
*   **Sliding Window:** Chính xác hơn Fixed Window.

---

## 6. Documentation: Tài liệu là nhất

API không có doc = API chết.

### 6.1. OpenAPI (Swagger)

Viết file YAML/JSON mô tả API, tự generate UI.

```yaml
paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: OK
```

### 6.2. Tools

*   **Swagger UI:** Standard, dễ setup.
*   **Postman Collection:** Share collection cho Frontend dev test.
*   **Redoc:** Giao diện đẹp hơn Swagger UI.

---

## 7. GraphQL vs REST: Khi nào dùng gì?

### 7.1. REST
*   **Ưu điểm:** Đơn giản, caching tốt (HTTP caching), tools phong phú.
*   **Nhược điểm:** Over-fetching (lấy thừa data), Under-fetching (phải gọi nhiều API).
*   **Use case:** Public API, Microservices communication, Simple apps.

### 7.2. GraphQL
*   **Ưu điểm:** Client lấy chính xác data cần (`{ user { name } }`), 1 request duy nhất.
*   **Nhược điểm:** Caching khó, Complexity cao (N+1 query), Security khó hơn (Query depth limit).
*   **Use case:** Mobile apps phức tạp (Facebook), Frontend cần flexible data requirements.

---

## 8. Action Plan: Checklist thiết kế

Trước khi code API endpoint đầu tiên:

1.  **Define Resources:** Liệt kê các nouns (`products`, `orders`).
2.  **Design URL:** Map resources vào URL (`/products`).
3.  **Choose Methods:** Map actions vào HTTP verbs (`POST`, `GET`).
4.  **Design Payload:** Request body gửi gì? Response trả gì?
5.  **Error Handling:** List các lỗi có thể xảy ra và mã lỗi tương ứng.
6.  **Security:** Endpoint này ai được gọi? (Public/User/Admin).
7.  **Write Docs:** Viết Swagger spec trước (API First Approach) hoặc code xong generate (Code First).

### 🛠️ Recommended Stack
*   **Node.js:** Express + Zod (Validation) + Swagger JSDoc.
*   **C#:** ASP.NET Core Web API (Built-in Swagger & Validation).

> **Lời khuyên:** Hãy nghĩ về người dùng API (Frontend dev) như khách hàng. Làm cho cuộc sống của họ dễ dàng hơn bằng API rõ ràng và document xịn.
