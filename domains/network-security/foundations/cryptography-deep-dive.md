# 🔐 Cryptography Deep Dive: Mật mã học Ứng dụng

> [← Back to Network Security](./README.md)

"Cryptography is the ultimate form of non-violent direct action." - Julian Assange.
Mật mã học không chỉ là toán học, nó là nền tảng của tự do và riêng tư trên Internet.

---

## 1. Các loại mã hóa (Encryption Types)

### **A. Symmetric Encryption (Mã hóa Đối xứng)**
*   **Cơ chế:** Dùng **MỘT** chìa khóa (Key) duy nhất để Khóa (Encrypt) và Mở (Decrypt).
*   **Đặc điểm:** Rất nhanh. Dùng để mã hóa dữ liệu lớn (File, Disk).
*   **Thuật toán:** AES-256 (Chuẩn quân đội), ChaCha20.
*   **Vấn đề:** Làm sao để gửi Key cho người nhận mà không bị lộ? (Key Distribution Problem).

### **B. Asymmetric Encryption (Mã hóa Bất đối xứng)**
*   **Cơ chế:** Dùng **CẶP** chìa khóa:
    *   **Public Key:** Công khai cho mọi người. Dùng để **Khóa**.
    *   **Private Key:** Giữ bí mật tuyệt đối. Dùng để **Mở**.
*   **Đặc điểm:** Chậm hơn nhiều. Dùng để trao đổi Key đối xứng an toàn.
*   **Thuật toán:** RSA, ECC (Elliptic Curve Cryptography).

---

## 2. Hashing (Băm) - Không phải là Mã hóa!

Hashing là một chiều (One-way). Bạn biến con bò thành xúc xích, nhưng không thể biến xúc xích thành con bò.

*   **Đặc điểm:**
    *   Cùng đầu vào -> Luôn ra cùng đầu ra.
    *   Đổi 1 ký tự đầu vào -> Đầu ra thay đổi hoàn toàn (Avalanche Effect).
*   **Thuật toán:**
    *   **MD5, SHA-1:** Đã bị phá (Collision). KHÔNG DÙNG.
    *   **SHA-256:** An toàn. Dùng cho Bitcoin, SSL.
    *   **bcrypt, Argon2:** Dùng để lưu mật khẩu (Chậm để chống Brute-force).

---

## 3. PKI & SSL/TLS (Hạ tầng khóa công khai)

Làm sao bạn biết `google.com` bạn đang truy cập là thật?

1.  **CA (Certificate Authority):** Tổ chức uy tín (Let's Encrypt, DigiCert) xác thực danh tính Google.
2.  **Digital Certificate:** "Chứng minh thư" điện tử của Google, do CA ký (Sign).
3.  **SSL Handshake:**
    *   Browser kiểm tra Certificate.
    *   Browser dùng Public Key của Google để mã hóa một Session Key (Symmetric).
    *   Hai bên dùng Session Key để nói chuyện (cho nhanh).

---

## 4. Lab Thực hành: OpenSSL & John the Ripper

### **Bài 1: Tạo CA và Tự ký chứng chỉ (Self-Signed)**
Biến máy bạn thành một CA (Certificate Authority).

```bash
# 1. Tạo Private Key cho CA
openssl genrsa -out ca.key 2048

# 2. Tạo Certificate cho CA (Self-signed)
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1825 -out ca.crt

# 3. Tạo Private Key cho Server (Web)
openssl genrsa -out server.key 2048

# 4. Tạo CSR (Certificate Signing Request)
openssl req -new -key server.key -out server.csr

# 5. Dùng CA ký cho Server
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

### **Bài 2: Cracking Hash (Dò mật khẩu)**
Giả sử bạn hack được database và lấy được hash mật khẩu.

1.  Tạo file `hash.txt` chứa hash MD5 của "password123":
    `echo "482c811da5d5b4bc6d497ffa98491e38" > hash.txt`
2.  Dùng **John the Ripper** để crack:
    ```bash
    john --format=Raw-MD5 hash.txt
    ```
3.  Nếu mật khẩu nằm trong wordlist mặc định, John sẽ tìm ra ngay!

> **Kết luận:** Đừng bao giờ dùng MD5. Hãy dùng bcrypt + Salt.
