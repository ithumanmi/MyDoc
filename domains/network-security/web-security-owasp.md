# 🌐 Web Security & OWASP Top 10

> [← Back to Network Security](./README.md)

Developer thường tập trung vào "làm cho nó chạy" mà quên mất "làm cho nó an toàn".
OWASP Top 10 là danh sách 10 lỗ hổng web nguy hiểm nhất thế giới. Thuộc lòng nó!

---

## 1. Injection (SQL Injection - SQLi)

*   **Là gì:** Hacker chèn mã độc vào câu lệnh SQL thông qua input form.
*   **Ví dụ:** Login form. User nhập: `' OR '1'='1`.
    *   Query gốc: `SELECT * FROM users WHERE user = '$user'`
    *   Query bị hack: `SELECT * FROM users WHERE user = '' OR '1'='1'` (Luôn đúng -> Login thành công mà không cần password).
*   **Phòng chống:**
    *   KHÔNG bao giờ nối chuỗi (String Concatenation).
    *   Dùng **Parameterized Queries** (Prepared Statements) hoặc ORM.

---

## 2. Broken Authentication

*   **Là gì:** Quản lý đăng nhập/phiên làm việc kém, cho phép hacker giả mạo người dùng.
*   **Ví dụ:**
    *   Cho phép mật khẩu yếu (123456).
    *   Không có giới hạn số lần thử login (Brute-force).
    *   Session ID lộ trong URL.
*   **Phòng chống:**
    *   Bắt buộc mật khẩu mạnh.
    *   Dùng MFA (Multi-Factor Authentication).
    *   Rate Limiting (Giới hạn 5 lần sai -> Khóa 10 phút).

---

## 3. Sensitive Data Exposure

*   **Là gì:** Để lộ dữ liệu nhạy cảm (Password, Credit Card, PII) do không mã hóa.
*   **Ví dụ:**
    *   Lưu password dạng plain-text trong DB.
    *   Truyền dữ liệu qua HTTP (không phải HTTPS).
*   **Phòng chống:**
    *   Luôn dùng HTTPS (TLS).
    *   Hash password bằng bcrypt/Argon2.
    *   Mã hóa dữ liệu nhạy cảm khi lưu trữ (Encryption at Rest).

---

## 4. XML External Entities (XXE)

*   **Là gì:** Lợi dụng lỗ hổng trong trình xử lý XML để đọc file hệ thống hoặc tấn công DoS.
*   **Phòng chống:** Tắt tính năng xử lý external entities trong XML parser.

---

## 5. Broken Access Control

*   **Là gì:** User thường truy cập được trang Admin hoặc dữ liệu của user khác.
*   **Ví dụ:** Đổi ID trên URL `example.com/app/accountInfo?id=123` thành `id=456` và xem được thông tin của người khác (IDOR - Insecure Direct Object References).
*   **Phòng chống:** Kiểm tra quyền (Authorization) chặt chẽ ở phía Server (Backend), không tin tưởng Frontend.

---

## 6. Security Misconfiguration

*   **Là gì:** Cấu hình server/app mặc định, thiếu an toàn.
*   **Ví dụ:**
    *   Để nguyên password mặc định của Admin (admin/admin).
    *   Bật chế độ Debug trên Production (lộ stack trace).
    *   Mở port không cần thiết.

---

## 7. Cross-Site Scripting (XSS)

*   **Là gì:** Hacker chèn mã JavaScript độc vào trang web để chạy trên trình duyệt của nạn nhân.
*   **Phân loại:**
    *   **Stored XSS:** Mã độc lưu trong DB (VD: Comment bẩn). Ai vào xem cũng bị dính.
    *   **Reflected XSS:** Mã độc trong URL. Gửi link lừa nạn nhân click.
*   **Hậu quả:** Ăn cắp Cookie, Session ID -> Chiếm quyền tài khoản.
*   **Phòng chống:** Escape tất cả dữ liệu đầu vào và đầu ra. Dùng Content Security Policy (CSP).

---

## 8. Insecure Deserialization

*   **Là gì:** Hacker chỉnh sửa dữ liệu object đã được serialize để thực thi mã độc khi server deserialize.

---

## 9. Using Components with Known Vulnerabilities

*   **Là gì:** Dùng thư viện/framework cũ có lỗ hổng đã được công bố.
*   **Ví dụ:** Dùng phiên bản cũ của Log4j.
*   **Phòng chống:** Thường xuyên update dependencies. Dùng tool quét (Snyk, npm audit).

---

## 10. Insufficient Logging & Monitoring

*   **Là gì:** Không ghi log hoặc không theo dõi log, khiến hacker tấn công mà không ai biết trong thời gian dài.
