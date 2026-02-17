# 🔐 OAuth 2.0 & OpenID Connect (OIDC): Deep Dive

> [← Back to Backend Roadmap](../README.md)

Bạn có bao giờ thắc mắc nút **"Log in with Google/Facebook"** hoạt động như thế nào? Đó chính là OAuth 2.0 và OIDC.
Đây là chuẩn mực xác thực (Authentication) và ủy quyền (Authorization) của thế giới Internet hiện đại.

---

## 1. OAuth 2.0 vs OIDC: Khác nhau chỗ nào? 🤔

Đây là sự nhầm lẫn phổ biến nhất.

### OAuth 2.0 (Authorization Framework)
*   **Mục tiêu:** Cấp **QUYỀN** truy cập.
*   **Ví dụ:** Bạn cho phép ứng dụng in ảnh truy cập vào Google Photos của bạn để in ảnh. Ứng dụng in ảnh không cần biết bạn là ai, chỉ cần quyền lấy ảnh.
*   **Key Artifact:** `Access Token`.

### OpenID Connect (OIDC) (Authentication Protocol)
*   **Mục tiêu:** Xác định **DANH TÍNH** người dùng.
*   **Là gì:** Một lớp mỏng chạy trên nền OAuth 2.0.
*   **Ví dụ:** Bạn đăng nhập vào Tiki bằng Google. Tiki muốn biết bạn là ai (Email, Tên, Avatar).
*   **Key Artifact:** `ID Token` (JWT).

👉 **Tóm lại:** OAuth 2.0 để **Access API**. OIDC để **Log in**.

---

## 2. The Actors (Các vai diễn) 🎭

1.  **Resource Owner (User):** Bạn - chủ sở hữu dữ liệu.
2.  **Client (App):** Ứng dụng muốn truy cập dữ liệu (Web, Mobile App).
3.  **Authorization Server (Auth Server):** Hệ thống cấp quyền (Google, Auth0, Keycloak). Nơi bạn nhập password.
4.  **Resource Server (API):** Nơi chứa dữ liệu (Google Photos API, Your Backend API).

---

## 3. Các Luồng Hoạt Động (Grant Types) Phổ Biến flow

### 3.1. Authorization Code Flow + PKCE (Chuẩn Vàng) 🏆
Dùng cho **Mobile Apps** và **SPA (React/Vue)**. An toàn nhất hiện nay.

**Quy trình:**
1.  **Client** tạo một mã bí mật ngẫu nhiên (`Code Verifier`) và mã hóa nó (`Code Challenge`).
2.  **Client** chuyển hướng User đến **Auth Server** kèm `Code Challenge`.
3.  **User** đăng nhập và đồng ý cấp quyền.
4.  **Auth Server** trả về một `Authorization Code` (dùng 1 lần).
5.  **Client** gửi `Authorization Code` + `Code Verifier` gốc lên **Auth Server**.
6.  **Auth Server** kiểm tra khớp mã -> Trả về `Access Token` và `ID Token`.

✅ **Tại sao an toàn?** Ngay cả khi hacker chặn được `Authorization Code` ở bước 4, họ không có `Code Verifier` (đang nằm trong RAM của Client) để đổi lấy Token ở bước 5.

### 3.2. Client Credentials Flow 🤖
Dùng cho **Machine-to-Machine** (Service A gọi Service B). Không có người dùng.

**Quy trình:**
1.  **Service A** gửi `Client ID` + `Client Secret` lên **Auth Server**.
2.  **Auth Server** trả về `Access Token`.
3.  **Service A** dùng token gọi API của **Service B**.

---

## 4. Giải Phẫu Token 🧬

### 4.1. Access Token
*   **Mục đích:** Giấy thông hành để gọi API.
*   **Định dạng:** Thường là JWT (JSON Web Token) hoặc Reference Token (chuỗi ngẫu nhiên).
*   **Chứa gì:** Scopes (quyền hạn), Expiry time.
*   **Lưu ý:** Không nên chứa thông tin nhạy cảm.

### 4.2. ID Token (Chỉ có trong OIDC)
*   **Mục đích:** Chứng minh danh tính.
*   **Định dạng:** Luôn là JWT.
*   **Chứa gì:** `sub` (User ID), `email`, `name`, `picture`.
*   **Lưu ý:** Client đọc token này để hiển thị "Hello, [Name]".

### 4.3. Refresh Token
*   **Mục đích:** Lấy Access Token mới khi cái cũ hết hạn mà không cần user đăng nhập lại.
*   **Đặc điểm:** Sống lâu (vài ngày/tuần). Cần lưu trữ cực kỳ cẩn mật.

---

## 5. Security Checklist (Đừng Bỏ Qua!) 🛡️

1.  [ ] **State Parameter:** Luôn dùng `state` để chống tấn công CSRF trong quá trình redirect.
2.  [ ] **Redirect URI:** Đăng ký chính xác URL callback trên Auth Server (Tuyệt đối không dùng wildcard `*`).
3.  [ ] **PKCE (Proof Key for Code Exchange):** BẮT BUỘC cho mọi ứng dụng public client (Mobile, SPA).
4.  [ ] **Client Secret:** Không bao giờ để `Client Secret` trong code frontend/mobile app. Nếu lộ, hacker có thể giả mạo app của bạn.
5.  [ ] **Token Storage:**
    *   **Web:** Lưu Access Token trong memory. Lưu Refresh Token trong `HttpOnly Cookie`.
    *   **Mobile:** Lưu trong Secure Storage (iOS Keychain, Android Keystore).

---

## 6. Khi Nào Dùng Cái Gì?

| Loại Ứng Dụng | Flow Nên Dùng |
| :--- | :--- |
| **Server-side Web (MVC)** | Authorization Code Flow |
| **SPA (React/Vue/Angular)** | Authorization Code Flow + PKCE |
| **Mobile App (iOS/Android)** | Authorization Code Flow + PKCE |
| **Backend Service (Microservice)** | Client Credentials Flow |
| **TV/Device (No Keyboard)** | Device Flow |

> **Lời khuyên:** Đừng tự viết OAuth Server trừ khi bạn là Google. Hãy dùng các giải pháp có sẵn như **Keycloak** (Open Source), **Auth0**, **Okta**, hoặc **AWS Cognito**.
