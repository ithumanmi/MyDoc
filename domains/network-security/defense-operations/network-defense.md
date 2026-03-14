# 🛡️ Network Defense & Operations: Phòng thủ mạng

> [← Back to Network Security](./README.md)

Tấn công (Offense) là nghệ thuật. Phòng thủ (Defense) là kỹ thuật.
Để phòng thủ tốt, bạn phải xây dựng hệ thống "Defense in Depth" (Phòng thủ nhiều lớp).

---

## 1. Network Security Devices (Thiết bị an ninh)

### **A. Firewall (Tường lửa)**
*   **Chức năng:** "Người gác cổng". Kiểm soát traffic ra/vào dựa trên Rules.
*   **Loại:**
    *   **Packet Filtering:** Chặn theo IP/Port (Layer 3/4).
    *   **Next-Gen Firewall (NGFW):** Chặn theo App, User, Content (Layer 7).
    *   **WAF (Web Application Firewall):** Chuyên chặn tấn công Web (SQLi, XSS).

### **B. VPN (Virtual Private Network)**
*   **Chức năng:** Tạo đường hầm bí mật (Encrypted Tunnel) qua Internet công cộng.
*   **Ứng dụng:**
    *   **Site-to-Site:** Kết nối 2 văn phòng ở xa nhau.
    *   **Remote Access:** Nhân viên làm việc tại nhà truy cập mạng công ty an toàn.

### **C. IDS / IPS (Phát hiện & Ngăn chặn Xâm nhập)**
*   **IDS (Intrusion Detection System):** Camera quan sát. Thấy kẻ trộm -> Hú còi (Alert).
*   **IPS (Intrusion Prevention System):** Bảo vệ. Thấy kẻ trộm -> Đấm luôn (Block).

---

## 2. Security Operations (Vận hành)

### **A. SIEM (Security Information and Event Management)**
*   **Vấn đề:** Có hàng nghìn thiết bị (Server, Router, Firewall) sinh ra log mỗi giây. Làm sao đọc hết?
*   **Giải pháp:** SIEM gom log về một chỗ, phân tích và cảnh báo khi có dấu hiệu bất thường.
*   **Tools:** Splunk, ELK Stack, Wazuh.

### **B. Incident Response (Ứng cứu sự cố)**
Quy trình 6 bước khi bị hack:
1.  **Preparation:** Chuẩn bị tools, nhân sự.
2.  **Identification:** Xác định xem có bị hack thật không? Hack cái gì?
3.  **Containment:** Khoanh vùng (Rút dây mạng, cô lập server).
4.  **Eradication:** Diệt virus, vá lỗ hổng.
5.  **Recovery:** Khôi phục dữ liệu từ backup.
6.  **Lessons Learned:** Rút kinh nghiệm.

---

## 3. System Hardening (Gia cố hệ thống)

### **Linux Hardening Checklist:**
1.  **SSH:** Đổi port mặc định (22), tắt root login, dùng Key thay cho Password.
2.  **Firewall:** Cấu hình `ufw` hoặc `iptables` chỉ mở port cần thiết.
3.  **Updates:** Luôn chạy `apt update && apt upgrade`.
4.  **Least Privilege:** Chỉ chạy service với user thường, không chạy với root.

### **Windows Hardening Checklist:**
1.  **GPO (Group Policy Object):** Ép buộc chính sách mật khẩu mạnh.
2.  **Anti-virus:** Luôn bật Windows Defender hoặc Endpoint Protection.
3.  **Disable Unused Services:** Tắt các service không dùng (Print Spooler nếu không in).
