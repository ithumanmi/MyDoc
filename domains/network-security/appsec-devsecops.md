# 🛡️ Application Security & DevSecOps

> [← Back to Network Security](./README.md)

"Security at the speed of DevOps."
Ngày xưa, Dev code xong mới ném cho Security kiểm tra (làm chậm tiến độ).
Ngày nay, Security được nhúng thẳng vào quy trình Dev (DevSecOps).

---

## 1. Shift Left (Dịch chuyển sang trái)

Trong quy trình SDLC (Software Development Life Cycle), timeline đi từ Trái (Design/Code) sang Phải (Deploy/Monitor).
*   **Truyền thống:** Test bảo mật ở cuối (Phải). Lỗ hổng phát hiện muộn -> Sửa tốn kém.
*   **Shift Left:** Test bảo mật ngay từ lúc Code (Trái). Lỗ hổng phát hiện sớm -> Sửa rẻ bèo.

---

## 2. Các công cụ kiểm thử tự động (Automated Testing)

### **A. SAST (Static Application Security Testing)**
*   **Là gì:** Quét **Source Code** tĩnh (chưa chạy) để tìm lỗi logic, hardcoded password.
*   **Ưu điểm:** Tìm lỗi sớm, chỉ chính xác dòng code bị lỗi.
*   **Nhược điểm:** Nhiều báo động giả (False Positive). Không tìm được lỗi cấu hình runtime.
*   **Tools:** SonarQube, CodeQL, Checkmarx.

### **B. DAST (Dynamic Application Security Testing)**
*   **Là gì:** Tấn công thử nghiệm vào ứng dụng **Đang Chạy** (như một Hacker).
*   **Ưu điểm:** Tìm được lỗi thực tế (Runtime), không phụ thuộc ngôn ngữ lập trình.
*   **Nhược điểm:** Chậm, cần môi trường chạy được.
*   **Tools:** OWASP ZAP, Burp Suite Enterprise.

### **C. SCA (Software Composition Analysis)**
*   **Là gì:** Quét các thư viện/dependencies (Open Source) xem có lỗ hổng đã biết (CVE) không.
*   **Tại sao:** 90% code của bạn là thư viện open source. Log4j là ví dụ điển hình.
*   **Tools:** Snyk, Dependabot (GitHub), OWASP Dependency-Check.

---

## 3. Bảo mật CI/CD Pipeline

Biến Pipeline thành chốt chặn bảo mật (Security Gate).

1.  **Commit Code:**
    *   Chạy **Secret Scanning** (TruffleHog) để chặn commit chứa API Key.
2.  **Build:**
    *   Chạy **SCA** để kiểm tra thư viện lỗi thời.
    *   Chạy **SAST** để kiểm tra chất lượng code.
3.  **Test:**
    *   Deploy lên môi trường Staging -> Chạy **DAST** scan tự động.
4.  **Deploy:**
    *   Nếu có lỗi High/Critical -> **Block Build** ngay lập tức. Không cho ra Production.

---

## 4. Container Security (Docker/K8s)

1.  **Image Scanning:** Quét Docker Image tìm lỗ hổng OS (Alpine, Ubuntu) trước khi deploy. (Tool: Trivy, Clair).
2.  **Runtime Security:** Giám sát hành vi bất thường của Container (VD: Container web server tự nhiên spawn ra shell). (Tool: Falco).
