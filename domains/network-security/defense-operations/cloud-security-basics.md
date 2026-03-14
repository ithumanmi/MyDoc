# ☁️ Cloud Security: Bảo mật Đám mây (AWS/Azure)

> [← Back to Network Security](./README.md)

"There is no cloud, it's just someone else's computer."
Khi bạn đưa dữ liệu lên Cloud, bạn không còn lo về phần cứng, nhưng bạn phải lo gấp đôi về cấu hình.

---

## 1. Shared Responsibility Model (Mô hình Trách nhiệm Chia sẻ)

Ai chịu trách nhiệm khi bị hack?

| Layer | Trách nhiệm của AWS/Azure | Trách nhiệm của BẠN |
| :--- | :--- | :--- |
| **Physical** | Server, Datacenter, Cables (Bạn không được đụng vào). | |
| **Network** | Hạ tầng mạng Backbone toàn cầu. | Cấu hình Firewall (Security Group), VPN. |
| **OS** | (Nếu dùng RDS/Lambda) Patching OS. | (Nếu dùng EC2) Bạn phải tự update Windows/Linux. |
| **Data** | Bảo vệ ổ cứng vật lý. | Mã hóa dữ liệu (Encryption), Backup, IAM. |

> **Quy tắc:** Nếu bạn có thể cấu hình nó, bạn phải chịu trách nhiệm bảo mật nó.

---

## 2. IAM: Identity & Access Management (Quản lý Danh tính)

Đây là bức tường lửa mới trong kỷ nguyên Cloud.

### **Nguyên tắc "Least Privilege" (Quyền tối thiểu)**
*   Đừng bao giờ dùng tài khoản **Root** để làm việc hàng ngày.
*   Chỉ cấp quyền vừa đủ. (Ví dụ: App chỉ cần đọc S3 thì chỉ cấp `s3:GetObject`, không cấp `s3:*`).

### **MFA (Multi-Factor Authentication)**
*   BẮT BUỘC bật MFA cho tài khoản Root và tất cả Admin.

---

## 3. Các lỗi bảo mật phổ biến (Cloud Misconfiguration)

### **A. S3 Bucket Leaks**
*   **Lỗi:** Cấu hình S3 Bucket ở chế độ "Public Read/Write".
*   **Hậu quả:** Bất kỳ ai trên Internet cũng có thể tải về dữ liệu khách hàng hoặc upload malware lên web của bạn.
*   **Khắc phục:** Luôn bật "Block Public Access" trừ khi thực sự cần thiết (VD: Web tĩnh).

### **B. Security Group quá lỏng lẻo**
*   **Lỗi:** Mở port SSH (22) hoặc RDP (3389) cho toàn thế giới (`0.0.0.0/0`).
*   **Hậu quả:** Bị Brute-force hoặc khai thác lỗ hổng.
*   **Khắc phục:** Chỉ cho phép IP văn phòng hoặc dùng VPN/Bastion Host.

### **C. Hardcoded Secrets**
*   **Lỗi:** Lưu Access Key (`AWS_ACCESS_KEY_ID`) trực tiếp trong Code và push lên GitHub.
*   **Hậu quả:** Hacker scan GitHub -> Lấy Key -> Đào Bitcoin trên tài khoản của bạn -> Bạn nợ AWS 50.000$.
*   **Khắc phục:** Dùng IAM Role cho EC2/Lambda.

---

## 4. Tools & Auditing

1.  **AWS Trusted Advisor:** Công cụ có sẵn check lỗi bảo mật cơ bản.
2.  **ScoutSuite:** Tool mã nguồn mở audit bảo mật đa nền tảng (AWS, Azure, GCP).
    ```bash
    pip install scoutsuite
    scout aws
    ```
    -> Nó sẽ xuất ra một báo cáo HTML chi tiết các lỗi cấu hình.
3.  **CloudTrail:** Camera giám sát. Ghi lại mọi hành động API (Ai đã làm gì, lúc nào).
4.  **Prowler / Steampipe Dashboards:** Kiểm tra compliance (CIS, NIST) tự động.

---

## 5. Advanced Topics & Next Steps

### **Zero Trust & Network Segmentation**
- Sử dụng AWS PrivateLink/VPC Endpoint để dịch vụ private không cần Internet.
- Áp dụng Security Group + NACL như “defense-in-depth” (Lớp SG per workload, NACL per subnet).
- Triển khai Zero Trust Access (ZTA) với AWS Verified Access hoặc Cloudflare Access.

### **Container & Serverless Security**
- **ECR Image Scanning:** Tự động quét CVE trước khi deploy.
- **Lambda least privilege:** IAM role chỉ cấp quyền cần thiết, bật runtime monitoring (Lambda Inspector).
- **Kubernetes (EKS/AKS):** Dùng OPA/Gatekeeper để enforce policy, bật audit logs, RBAC.

### **Detection & Response**
- Kết hợp CloudTrail + GuardDuty + Security Hub để có alert pipeline.
- Thiết lập log centralization (S3 + Athena/CloudWatch Logs Insight) để truy vấn nhanh khi incident.
- Run **chaos security drills**: simulate credential leak, S3 data exfil để test playbook.

### **Practice Checklist**
- [ ] Bật MFA + rotation cho tất cả IAM User/Admin.
- [ ] Tạo Config Rules kiểm tra S3 public, SG mở quá mức.
- [ ] Thiết lập CloudTrail multi-region + log integrity validation.
- [ ] Chuẩn bị Incident Response Runbook cho Cloud (triage, isolation, forensics).

**Next:** Làm lab tự động hóa compliance bằng Terraform + Prowler, và dựng môi trường detection với Security Hub + custom Lambda remediation.
