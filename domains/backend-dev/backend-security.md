# 🔒 Backend Security Best Practices: Defense in Depth

> [← Back to Backend Roadmap](./README.md) | [Home](../../README.md)

Bảo mật không phải là một "tính năng" thêm vào sau cùng. Nó là tư duy xuyên suốt quá trình code. Một lỗi bảo mật nhỏ có thể xóa sổ cả công ty. Hướng dẫn này cover OWASP Top 10 và các thực hành tốt nhất để bảo vệ Backend của bạn.

---

## 📋 Mục lục

1. [OWASP Top 10 (Backend Perspective)](#1-owasp-top-10-hiểm-họa-hàng-đầu)
2. [Secure Coding Practices](#2-secure-coding-practices-code-an-toàn)
3. [Infrastructure Security](#3-infrastructure-security-bảo-vệ-hạ-tầng)
4. [Compliance & Regulations](#4-compliance-tuân-thủ-luật-pháp)
5. [Security Checklist](#5-security-checklist-trước-khi-deploy)
6. [Action Plan](#6-action-plan-bắt-tay-vào-làm)

---

## 1. OWASP Top 10: Hiểm họa hàng đầu

Danh sách 10 lỗ hổng bảo mật phổ biến nhất thế giới web.

### 1.1. Injection (SQL Injection, Command Injection)

**Nguy hiểm:** Attacker chèn code độc hại vào input để server thực thi.

*   ❌ **Vulnerable Code:**
    ```javascript
    const query = `SELECT * FROM users WHERE name = '${req.body.name}'`;
    // Input: "admin' --" -> SELECT * FROM users WHERE name = 'admin' --'
    ```
*   ✅ **Fix (Parameterized Query):**
    ```javascript
    // Node.js (pg)
    const query = 'SELECT * FROM users WHERE name = $1';
    await client.query(query, [req.body.name]);
    ```

### 1.2. Broken Authentication

**Nguy hiểm:** Cho phép attacker giả mạo user khác.

*   **Nguyên nhân:** Weak password, Session không hết hạn, URL chứa Session ID.
*   **Fix:**
    *   Dùng **MFA (Multi-Factor Authentication)**.
    *   Giới hạn số lần login sai (Rate Limiting).
    *   Password Complexity (Min 8 chars, special chars).
    *   Không tự viết Crypto! Dùng thư viện chuẩn (bcrypt, Argon2).

### 1.3. Sensitive Data Exposure

**Nguy hiểm:** Lộ password, thẻ tín dụng, thông tin cá nhân (PII).

*   **Fix:**
    *   **Encryption at Rest:** Mã hóa DB, Backup.
    *   **Encryption in Transit:** Luôn dùng **HTTPS (TLS 1.2+)**.
    *   **Hashing:** Không bao giờ lưu plain-text password.

### 1.4. Broken Access Control (IDOR)

**Nguy hiểm:** User A xem/sửa được dữ liệu của User B.

*   **Scenario:** `GET /invoices/123` (User A đổi ID thành 124 để xem hóa đơn User B).
*   **Fix:** Luôn check quyền sở hữu.
    ```javascript
    if (invoice.userId !== currentUser.id && !currentUser.isAdmin) {
      throw new ForbiddenError();
    }
    ```

### 1.5. Security Misconfiguration

**Nguy hiểm:** Để default password, lộ stack trace, mở port không cần thiết.

*   **Fix:**
    *   Disable directory listing.
    *   Tắt verbose error messages trên Production.
    *   Đổi default admin password.

---

## 2. Secure Coding Practices: Code an toàn

### 2.1. Input Validation (Sanitization)

"Never Trust User Input". Coi mọi dữ liệu từ Client là độc hại.

*   **Allow-list (Tốt):** Chỉ chấp nhận ký tự a-z, 0-9.
*   **Block-list (Kém):** Cấm ký tự `<script>`. (Hacker sẽ tìm cách bypass như `<SCRIPT>`).
*   **Tools:** `zod`, `joi`, `class-validator`.

### 2.2. CSRF (Cross-Site Request Forgery)

**Kịch bản:** User đang login ngân hàng. Bấm vào link lạ → Link đó gửi lệnh chuyển tiền ngầm dưới danh nghĩa User.

*   **Fix:**
    *   Dùng **SameSite Cookie Attribute** (`SameSite=Strict` hoặc `Lax`).
    *   Dùng **Anti-CSRF Tokens** (Double Submit Cookie).

### 2.3. Secrets Management

Tuyệt đối không hardcode API Key, DB Password trong code!

*   ❌ `const dbPass = "secret123";`
*   ✅ Dùng Environment Variables (`.env`).
*   ✅ Dùng Secret Manager (AWS Secrets Manager, HashiCorp Vault).
*   **Git:** Thêm `.env` vào `.gitignore`.

---

## 3. Infrastructure Security: Bảo vệ hạ tầng

### 3.1. Network Segmentation

Chia mạng thành các vùng (Zones).
*   **Public Subnet:** Load Balancer (Internet access).
*   **Private Subnet:** App Server (No direct Internet access).
*   **Data Subnet:** Database (Locked down).

### 3.2. DDoS Protection

*   Dùng Cloudflare/AWS Shield để chặn volumetric attacks.
*   Rate Limiting ở API Gateway.

### 3.3. Dependency Scanning

Code của bạn an toàn, nhưng thư viện bạn dùng thì sao? (Vụ `event-stream` bị inject bitcoin miner).

*   **Tool:** `npm audit`, `Snyk`, `GitHub Dependabot`.
*   **Action:** Chạy scan trong CI/CD pipeline.

---

## 4. Compliance: Tuân thủ luật pháp

### 4.1. GDPR (Châu Âu) & PDPA (Việt Nam)

*   **Right to be forgotten:** User yêu cầu xóa account → Phải xóa sạch (hoặc anonymize) data của họ.
*   **Data Minimization:** Chỉ thu thập dữ liệu cần thiết.
*   **Consent:** Phải xin phép trước khi thu thập.

### 4.2. PCI DSS (Thanh toán)

Nếu xử lý thẻ tín dụng:
*   Đừng tự lưu số thẻ! Dùng Payment Gateway (Stripe, PayPal).
*   Nếu bắt buộc lưu: Phải tuân thủ chuẩn PCI DSS cực nghiêm ngặt.

---

## 5. Security Checklist: Trước khi Deploy

1.  [ ] **HTTPS Everywhere:** Redirect HTTP → HTTPS.
2.  [ ] **Headers:** Set security headers (Helmet.js).
    *   `Strict-Transport-Security`
    *   `X-Content-Type-Options: nosniff`
    *   `X-Frame-Options: DENY`
3.  [ ] **Secrets:** Check xem có lộ key trong git history không (Dùng `git-secrets`).
4.  [ ] **Dependencies:** Run `npm audit fix`.
5.  [ ] **Logging:** Đảm bảo không log password/token ra file log.
6.  [ ] **Error Handling:** Check error response không lộ stack trace.

---

## 6. Action Plan: Bắt tay vào làm

### 6.1. Immediate Actions
1.  Cài **Snyk** hoặc bật **Dependabot** cho repo.
2.  Review code tìm **SQL Injection** và fix ngay.
3.  Kiểm tra auth logic: Có check quyền sở hữu resource (IDOR) không?

### 6.2. Weekly Habits
1.  Check log xem có dấu hiệu tấn công (Brute force, error 500 bất thường) không.
2.  Update dependencies.

> **Tư duy:** "Hacker chỉ cần đúng 1 lần. Bạn phải đúng mọi lần." Hãy luôn cảnh giác.
