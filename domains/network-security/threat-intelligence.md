# 🧠 Threat Intelligence: Tình báo Mối đe dọa

> [← Back to Network Security](./README.md)

"Biết người biết ta, trăm trận trăm thắng."
Threat Intelligence (CTI) là việc thu thập và phân tích thông tin về Hacker để dự đoán và ngăn chặn tấn công.

---

## 1. Cyber Kill Chain (Chuỗi tiêu diệt)

Mô hình 7 bước tấn công của Lockheed Martin. Để ngăn chặn Hacker, bạn chỉ cần phá vỡ **MỘT** mắt xích.

1.  **Reconnaissance (Thám thính):** Hacker thu thập email, IP, công nghệ mục tiêu.
    *   *Chặn:* Ẩn thông tin nhạy cảm, đào tạo nhân viên chống Phishing.
2.  **Weaponization (Vũ khí hóa):** Tạo mã độc (Malware) nhúng vào file PDF/Word.
    *   *Chặn:* Antivirus, Email Gateway.
3.  **Delivery (Vận chuyển):** Gửi email hoặc USB chứa mã độc đến nạn nhân.
    *   *Chặn:* Firewall, Spam Filter.
4.  **Exploitation (Khai thác):** Mã độc chạy, khai thác lỗ hổng phần mềm.
    *   *Chặn:* Vá lỗ hổng (Patching), DEP/ASLR.
5.  **Installation (Cài đặt):** Cài Backdoor để duy trì truy cập.
    *   *Chặn:* HIPS (Host Intrusion Prevention System).
6.  **Command & Control (C2):** Mã độc kết nối về máy chủ Hacker nhận lệnh.
    *   *Chặn:* Firewall chặn Outbound Traffic, DNS Sinkhole.
7.  **Actions on Objectives (Hành động):** Ăn cắp dữ liệu, mã hóa tống tiền (Ransomware).
    *   *Chặn:* DLP (Data Loss Prevention), Backup dữ liệu.

---

## 2. MITRE ATT&CK Framework

Bảng tuần hoàn các kỹ thuật tấn công thực tế. Chi tiết hơn Kill Chain.
*   **Tactics (Chiến thuật):** Mục tiêu của Hacker (VD: Leo thang đặc quyền).
*   **Techniques (Kỹ thuật):** Cách thực hiện (VD: Process Injection).
*   **Procedures (Quy trình):** Tool cụ thể (VD: Mimikatz).

> **Sử dụng:** Dùng MITRE ATT&CK để kiểm tra xem hệ thống phòng thủ của bạn có phát hiện được các kỹ thuật cụ thể không (Red Teaming Simulation).

---

## 3. Pyramid of Pain (Kim tự tháp Đau đớn)

Các loại IoC (Indicators of Compromise) gây khó khăn cho Hacker ở mức độ nào khi bị chặn?

| Level (Đỉnh xuống Đáy) | Loại IoC | Mức đau đớn cho Hacker |
| :--- | :--- | :--- |
| **TTPs** | Tactics, Techniques, Procedures (Hành vi) | **Tough (Rất đau):** Hacker phải học lại từ đầu. |
| **Tools** | Công cụ tấn công (Cobalt Strike) | **Challenging:** Phải viết lại tool mới. |
| **Network Artifacts** | User-Agent, C2 Protocol | **Annoying:** Phải cấu hình lại tool. |
| **Domain Names** | `evil.com` | **Simple:** Mua domain mới. |
| **IP Addresses** | `1.2.3.4` | **Easy:** Đổi IP (Proxy/VPN). |
| **Hash Values** | SHA256 của file malware | **Trivial (Không đau):** Đổi 1 bit file là Hash đổi. |

> **Chiến lược:** Đừng chỉ chặn IP/Hash (dễ thay đổi). Hãy tập trung phát hiện hành vi (TTPs).

---

## 4. Các nguồn tình báo (Feeds)

*   **Commercial:** FireEye, CrowdStrike (Đắt tiền, dữ liệu chất lượng).
*   **Open Source (OSINT):** AlienVault OTX, MISP (Cộng đồng chia sẻ).
*   **Dark Web Monitoring:** Theo dõi xem data công ty có bị rao bán trên chợ đen không.
