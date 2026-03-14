# 🔒 Security Fundamentals: Bảo mật căn bản

> [← Back to Network Security](./README.md)

Bảo mật không phải là một sản phẩm, nó là một quá trình.
Bạn không thể "cài" bảo mật, bạn chỉ có thể "làm" bảo mật.

---

## 1. CIA Triad (Tam giác Bảo mật)

Mọi hệ thống bảo mật đều xoay quanh 3 trụ cột này:

1.  **Confidentiality (Tính Bí mật):** Chỉ người được phép mới xem được dữ liệu.
    *   *Cách làm:* Mã hóa (Encryption), Phân quyền (Access Control).
    *   *Ví dụ:* Chỉ bạn mới biết mật khẩu Facebook của bạn.
2.  **Integrity (Tính Toàn vẹn):** Dữ liệu không bị chỉnh sửa trái phép.
    *   *Cách làm:* Hashing (Băm), Digital Signature (Chữ ký số).
    *   *Ví dụ:* File bạn tải về giống hệt file gốc, không bị cài virus.
3.  **Availability (Tính Sẵn sàng):** Hệ thống luôn hoạt động khi cần.
    *   *Cách làm:* Redundancy (Dự phòng), Load Balancing, DDoS Protection.
    *   *Ví dụ:* Facebook không bị sập khi có hàng tỷ người truy cập.

---

## 2. Cryptography (Mật mã học)

### **A. Encryption (Mã hóa - 2 chiều)**
Biến Plaintext -> Ciphertext (để giấu). Có thể giải mã lại.
*   **Symmetric (Đối xứng):** Dùng 1 chìa khóa (Key) để khóa và mở. Nhanh nhưng khó chia sẻ Key an toàn. (VD: AES).
*   **Asymmetric (Bất đối xứng):** Dùng 1 cặp khóa: Public Key (để khóa) và Private Key (để mở). Chậm nhưng an toàn. (VD: RSA, ECC).

### **B. Hashing (Băm - 1 chiều)**
Biến Plaintext -> Hash cố định (VD: chuỗi 256 ký tự). KHÔNG THỂ giải mã lại.
*   **Dùng để:** Kiểm tra tính toàn vẹn (Integrity) hoặc lưu mật khẩu.
*   **Salt & Pepper:** Thêm chuỗi ngẫu nhiên vào password trước khi hash để chống tấn công Rainbow Table.

---

## 3. Identity (Định danh)

### **Authentication (AuthN - Bạn là ai?)**
*   **Something you know:** Password, PIN.
*   **Something you have:** OTP (điện thoại), Smart card.
*   **Something you are:** Vân tay, FaceID.
*   **MFA (Multi-Factor Authentication):** Kết hợp ít nhất 2 loại trên -> Bảo mật gấp bội.

### **Authorization (AuthZ - Bạn được làm gì?)**
*   Sau khi biết bạn là ai, hệ thống phân quyền.
*   **Admin:** Full quyền.
*   **User:** Chỉ xem bài viết.
