# Challenge: Web App Security Review + Threat Model

- **Loại:** interview/project hybrid
- **Mảng:** security
- **Mức:** Intermediate
- **Ước lượng thời gian:** 3-5 ngày
- **Prerequisites:** [`domains/network-security/README.md`](../../domains/network-security/README.md) · [`domains/backend-dev/backend-security.md`](../../domains/backend-dev/backend-security.md)

## Mục tiêu học tập
- Nhận diện và mô tả rủi ro theo OWASP Top 10.
- Viết threat model (STRIDE) và đề xuất biện pháp giảm thiểu.
- Thiết kế kiểm soát: authN/Z, secrets, logging/audit, HTTPS/mTLS.

## Đề bài
Bạn nhận được một web app (giả lập) gồm: auth bằng JWT, form nhập dữ liệu, upload file, và một API nội bộ cho admin. Nhiệm vụ:
1) **Review bảo mật**: liệt kê rủi ro top 10-15 theo OWASP Top 10.
2) **Threat model**: vẽ sơ đồ luồng (text hoặc diagram) và áp dụng STRIDE cho các thành phần chính.
3) **Mitigation plan**: đề xuất biện pháp và ưu tiên (High/Medium/Low).
4) **Bonus**: demo 1-2 PoC khai thác (có thể mô tả thay vì code).

## Đầu vào (Input)
- Mô tả app (có thể tự giả lập) với các thành phần: web frontend, backend API, DB, file storage, admin endpoint.
- Giả định JWT, form, upload, và một endpoint nội bộ.

## Đầu ra (Output)
- Tài liệu ngắn (md/pdf) gồm: rủi ro, threat model, mitigations; kèm hình hoặc ASCII diagram.
- (Tuỳ chọn) PoC script/link nếu có.

## Tiêu chí chấm (Acceptance)
- **Đúng trọng tâm:** Rủi ro map được vào OWASP Top 10; có STRIDE trên các flow chính.
- **Mitigation khả thi:** Biện pháp cụ thể (input validation, CSP, rate limit, mTLS, secret rotation, audit).
- **Ưu tiên:** Có bảng High/Med/Low, giải thích tác động.
- **Rõ ràng:** Tài liệu dễ đọc; có checklist hành động.

## Gợi ý / Hint
- Kiểm tra: auth/session/JWT, CSRF/XSS, SSRF/RFI, file upload, broken access control, secrets, logging.
- STRIDE: Spoofing/Tampering/Repudiation/Information disclosure/DoS/Elevation.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Tham khảo các checklist OWASP hoặc mô hình mẫu; nếu bạn có repo demo, link vào đây.