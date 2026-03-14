# ⚖️ Governance, Risk & Compliance (GRC): Quản trị An toàn Thông tin

> [← Back to Network Security](./README.md)

"An toàn thông tin không chỉ là vấn đề kỹ thuật (IT Problem), mà là vấn đề kinh doanh (Business Problem)."
GRC là cầu nối giữa Hacker mũ trắng và Ban giám đốc.

---

## 1. Governance (Quản trị) - Chiến lược

Quản trị đảm bảo chiến lược bảo mật phù hợp với mục tiêu kinh doanh.

### **Các Framework tiêu chuẩn quốc tế:**
1.  **ISO/IEC 27001:** Tiêu chuẩn vàng về ISMS (Information Security Management System).
    *   Yêu cầu các quy trình (Process), chính sách (Policy) và kiểm soát (Control).
    *   Chứng chỉ ISO 27001 giúp tăng uy tín với khách hàng doanh nghiệp.
2.  **NIST Cybersecurity Framework (CSF):** Tiêu chuẩn của Mỹ, phổ biến toàn cầu.
    *   5 chức năng cốt lõi: **Identify -> Protect -> Detect -> Respond -> Recover**.
3.  **CIS Controls:** Danh sách 18 kiểm soát kỹ thuật ưu tiên (VD: Inventory tài sản, Quản lý tài khoản Admin).

---

## 2. Risk Management (Quản lý Rủi ro) - Chiến thuật

Bạn không thể bảo vệ tất cả mọi thứ. Bạn phải bảo vệ những thứ quan trọng nhất.

### **Quy trình đánh giá rủi ro (Risk Assessment):**
1.  **Identify Assets:** Xác định tài sản quý giá (Dữ liệu khách hàng, Source code).
2.  **Identify Threats:** Xác định mối đe dọa (Hacker, Nhân viên bất mãn, Thiên tai).
3.  **Identify Vulnerabilities:** Xác định lỗ hổng (Server chưa patch, Quy trình lỏng lẻo).
4.  **Calculate Risk:**
    $$ Rủi ro = (Khả năng xảy ra) \times (Mức độ ảnh hưởng) $$

### **4 Chiến lược xử lý rủi ro:**
1.  **Risk Mitigation (Giảm thiểu):** Cài Firewall, Vá lỗ hổng.
2.  **Risk Transfer (Chuyển giao):** Mua bảo hiểm an ninh mạng (Cyber Insurance).
3.  **Risk Acceptance (Chấp nhận):** Rủi ro thấp, chi phí sửa quá cao -> Kệ nó.
4.  **Risk Avoidance (Né tránh):** Ngừng cung cấp dịch vụ rủi ro đó (VD: Đóng server FTP cũ).

---

## 3. Compliance (Tuân thủ) - Luật pháp

Không tuân thủ luật = Phạt tiền + Mất uy tín + Đi tù.

### **Các quy định quan trọng:**
1.  **GDPR (Châu Âu):** Bảo vệ dữ liệu cá nhân. Phạt tới 4% doanh thu toàn cầu nếu để lộ dữ liệu.
2.  **PCI DSS:** Dành cho các công ty xử lý thẻ tín dụng (Visa/Mastercard).
3.  **HIPAA (Mỹ):** Bảo vệ dữ liệu y tế bệnh nhân.
4.  **Luật An ninh mạng (Việt Nam):** Yêu cầu lưu trữ dữ liệu tại Việt Nam (Data Localization).

> **Lời khuyên:** Đừng chờ đến khi bị kiểm toán (Audit) mới lo làm bảo mật. Hãy biến nó thành văn hóa công ty.
