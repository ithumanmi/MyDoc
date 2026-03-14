# Challenge: Fix & Hardening OWASP Issues in a Sample App

- **Loại:** project
- **Mảng:** security
- **Mức:** Intermediate
- **Ước lượng thời gian:** 2-4 ngày
- **Prerequisites (tùy chọn):** [`domains/network-security/README.md`](../../domains/network-security/README.md) · [`domains/backend-dev/backend-security.md`](../../domains/backend-dev/backend-security.md)

## Mục tiêu học tập
- Nhận diện và khai thác các lỗi phổ biến OWASP (SQLi, XSS, broken auth).
- Hardening: input validation, escaping, auth/session/JWT an toàn, security headers.
- Viết checklist phòng thủ và verify lại sau khi fix.

## Đề bài
Có một app web mẫu (có thể tự tạo hoặc dùng skeleton) với 3 lỗi:
- **SQL injection** ở search/query.
- **XSS** ở phần hiển thị nội dung user nhập.
- **Broken auth** (ví dụ: JWT không verify đúng, thiếu expiration/refresh, hoặc session không httpOnly/secure).

Nhiệm vụ: (1) Mô tả cách khai thác, (2) Fix triệt để, (3) Thêm kiểm soát/hardening, (4) Viết checklist.

## Đầu vào (Input)
- Source code app mẫu (hoặc scaffold tự tạo) với 3 lỗi trên.
- Môi trường chạy local.

## Đầu ra (Output)
- Báo cáo ngắn: mô tả lỗi + PoC (curl/screenshot) + root cause.
- Bản code đã fix + security headers + cấu hình auth/session an toàn.
- Checklist phòng thủ (md) để kiểm lại.

## Tiêu chí chấm (Acceptance)
- **PoC rõ ràng:** chứng minh được khai thác 3 lỗi.
- **Fix đúng:** SQLi được parameterized, XSS được escape/CSP, auth/session/JWT được bảo vệ.
- **Hardening:** bật headers (CSP, HSTS, X-Frame-Options…), secure cookies/CSRF token nếu dùng session.
- **Checklist:** ngắn gọn, actionable, có bước verify.

## Gợi ý / Hint
- Dùng prepared statements/ORM, encode/escape output, validate input.
- JWT: verify signature, expiry, audience; hoặc session: httpOnly, secure, sameSite.
- CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Đính kèm link repo trước/sau khi fix và checklist.