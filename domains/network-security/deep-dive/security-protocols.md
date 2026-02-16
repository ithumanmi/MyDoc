# 🔒 Security Protocols: TLS & PKI Deep Dive

> [← Back to Network Security](../README.md)

Lớp bảo mật nằm giữa Transport và Application. Nó đảm bảo Hacker dù bắt được gói tin cũng chỉ thấy một mớ ký tự vô nghĩa.

---

## 1. TLS/SSL Handshake (Cái bắt tay bảo mật)

Trước khi gửi dữ liệu HTTP, Client và Server phải thiết lập kênh mã hóa.

### **TLS 1.2 (Cũ): 2-RTT (2 vòng khứ hồi)**
1.  **Client Hello:** Gửi danh sách thuật toán hỗ trợ.
2.  **Server Hello:** Chọn thuật toán, gửi Certificate.
3.  **Key Exchange:** Client và Server trao đổi khóa.
4.  **Finished:** Xác nhận.

### **TLS 1.3 (Mới - Siêu nhanh): 1-RTT**
*   Gộp bước Key Exchange ngay vào Hello. Giảm 50% thời gian kết nối.
*   **0-RTT (Zero Round Trip Time):** Nếu Client đã từng kết nối Server trước đó, nó gửi dữ liệu mã hóa NGAY trong gói tin đầu tiên (Resumption).

---

## 2. PKI (Public Key Infrastructure)

Hệ thống niềm tin của Internet.

### **Chain of Trust (Chuỗi tin cậy):**
1.  **Root CA (Certificate Authority):** Tổ chức uy tín nhất (VD: DigiCert, Let's Encrypt). Certificate của họ được cài sẵn trong Window/Browser của bạn.
2.  **Intermediate CA:** Root CA ủy quyền cho các CA con.
3.  **Server Certificate:** Certificate của trang web (`google.com`), được ký bởi Intermediate CA.

> Nếu Browser không tin Root CA, nó sẽ hiện cảnh báo đỏ: "Your connection is not private".

### **Certificate Pinning:**
*   Ứng dụng Mobile (App) ghim cứng (Hardcode) Public Key của Server vào code.
*   Nếu Hacker dùng Charles Proxy để bắt gói tin (MITM) và đưa ra Certificate giả -> App từ chối kết nối ngay lập tức.

---

## 3. Các cuộc tấn công phổ biến

### **A. MITM (Man-in-the-Middle)**
*   Hacker đứng giữa Client và Server.
*   Client nghĩ Hacker là Server. Server nghĩ Hacker là Client.
*   **Phòng chống:** Dùng HTTPS (TLS) xác thực Server thật.

### **B. SSL Stripping**
*   Hacker chặn gói tin chuyển hướng `http://` -> `https://`.
*   Hacker lừa Client dùng bản HTTP (không mã hóa) trong khi Hacker dùng HTTPS với Server.
*   **Phòng chống:** HSTS (HTTP Strict Transport Security). Server ép buộc Browser chỉ được dùng HTTPS.

### **C. Downgrade Attack**
*   Hacker lừa 2 bên dùng phiên bản TLS cũ (TLS 1.0) có lỗ hổng.
*   **Phòng chống:** Server tắt hỗ trợ các phiên bản cũ.
