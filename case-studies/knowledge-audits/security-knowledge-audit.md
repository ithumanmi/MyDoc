# 🛡️ Cyber Security Knowledge Audit: Thử thách "The Guardian of Nexus"

> **Mục đích:** Đo lường năng lực thực chiến trong việc bảo vệ hệ thống, phát hiện xâm nhập, phản ứng sự cố và tư duy tấn công (Red Team) để củng cố phòng thủ (Blue Team).
> **Phiếu trả lời:** [Tải mẫu tại đây](../answer-templates/security-answer-template.md)
> 
> **Kịch bản:** Bạn là **Security Operations Center (SOC) Lead** của tập đoàn "NexusCloud" - một nhà cung cấp dịch vụ hạ tầng đám mây cho các ngân hàng lớn. Vào lúc 2:00 sáng Chủ Nhật, hệ thống giám sát SIEM của bạn đồng loạt báo động đỏ: Có dấu hiệu của một cuộc tấn công APT (Advanced Persistent Threat) đang nhắm vào máy chủ chứa dữ liệu nhạy cảm nhất.

---

## 🛠️ Thử thách 1: Network Forensics & Protocol Deep Dive (Phân tích mạng)
*Đo lường sự am hiểu về cách dữ liệu di chuyển và cách tin tặc ẩn mình.*

**Tình huống:** Bạn bắt được một tệp tin `.pcap` từ gateway chính. Bạn thấy hàng ngàn request HTTP lạ lùng nhắm vào một endpoint nội bộ, kèm theo đó là các gói tin DNS có dung lượng lớn bất thường hướng ra một IP lạ tại nước ngoài.

**Câu hỏi:**
1.  Dấu hiệu "DNS có dung lượng lớn bất thường" gợi cho bạn kỹ thuật tấn công hoặc exfiltration (rút trích dữ liệu) nào? Bạn sẽ dùng công cụ gì (ví dụ: **Wireshark**, **Zeek**) để trích xuất nội dung bị nghi ngờ?
2.  Làm thế nào để phân biệt một request **SQL Injection** với một request hợp lệ chỉ bằng cách nhìn vào log Raw của Web Server? Nêu 3 từ khóa (keywords) thường xuất hiện trong một cuộc tấn công SQLi.

**Thước đo:**
*   **🟢 Beginner:** Biết dùng Wireshark xem gói tin cơ bản, hiểu mô hình OSI.
*   **🔴 Expert:** Thành thạo kỹ thuật **DNS Tunneling**, phân tích được luồng traffic mã hóa (TLS Fingerprinting) và giải mã được các payload phức tạp.

---

## ⚔️ Thử thách 2: Web Security & Exploitation (An toàn ứng dụng Web)
*Đo lường tư duy Red Team để tìm ra lỗ hổng trước khi tin tặc làm điều đó.*

**Tình huống:** NexusCloud vừa ra mắt một dashboard quản lý mới. Dashboard này có tính năng "Import Profile from URL". Hacker đã lợi dụng tính năng này để truy cập vào metadata server của Cloud (169.254.169.254) và lấy cắp IAM Role của Admin.

**Câu hỏi:**
1.  Đây là lỗ hổng bảo mật nào trong danh mục **OWASP Top 10**? Làm thế nào để cấu hình "Whitelist" hoặc "Metadata Shield" để ngăn chặn nó?
2.  Phân biệt giữa **Stored XSS** và **Reflected XSS**. Tại sao lỗ hổng **Insecure Direct Object Reference (IDOR)** thường bị bỏ qua bởi các công cụ scan tự động nhưng lại cực kỳ nguy hiểm?

**Thước đo:**
*   **🟢 Beginner:** Biết dùng Burp Suite chặn request, hiểu về SQLi và XSS cơ bản.
*   **🔴 Expert:** Thành thạo các kỹ thuật **SSRF (Server-Side Request Forgery)** nâng cao, **Deserialization attacks**, và có khả năng chaining (xâu chuỗi) nhiều lỗ hổng nhỏ thành một đòn tấn công chiếm quyền điều khiển server (RCE).

---

## 🛡️ Thử thách 3: System Hardening & Defense (Phòng thủ hệ thống)
*Đo lường năng lực xây dựng "Pháo đài" kỹ thuật số.*

**Tình huống:** Sau khi đẩy lùi cuộc tấn công, bạn cần cấu hình lại toàn bộ cụm server Linux để đảm bảo hacker không thể quay lại qua các "Backdoor" thông thường.

**Câu hỏi:**
1.  Nêu 5 bước quan trọng nhất để **Harden (Gia cố)** một server Linux mới cài đặt (ví dụ: SSH configuration, Firewall, OS Update, v.v.).
2.  **Zero Trust Architecture (ZTA)** khác gì so với mô hình bảo mật truyền thống "Lâu đài và Hào nước" (Castle and Moat)? Tại sao việc sử dụng VPN truyền thống không còn đủ an toàn trong kỷ nguyên Cloud?

**Thước đo:**
*   **🟢 Beginner:** Biết đổi port SSH, cài UFW/iptables cơ bản.
*   **🔴 Expert:** Triển khai được mô hình **Identity-Aware Proxy**, quản lý được **Secrets** (HashiCorp Vault), và áp dụng tư duy **Defense in Depth** ở mọi tầng của hệ thống.

---

## 🧠 Thử thách 4: Identity & Cryptography (Định danh & Mật mã)
*Đo lường năng lực bảo vệ "Chìa khóa" của vương quốc.*

**Tình huống:** Hacker đã lấy được một bản dump của bảng `users` chứa mật khẩu đã được băm (hashed). Tuy nhiên, team Dev cũ chỉ dùng `MD5` mà không có `Salt`.

**Câu hỏi:**
1.  Tại sao `MD5` hoặc `SHA1` (kể cả có Salt) vẫn bị coi là không an toàn cho việc lưu trữ mật khẩu ngày nay? Bạn sẽ đề xuất thuật toán nào thay thế (**Argon2**, **bcrypt**, **scrypt**)? Giải thích khái niệm **Work Factor**.
2.  **Multi-Factor Authentication (MFA)** dựa trên SMS có rủi ro gì (ví dụ: **SIM Swapping**)? Tại sao **FIDO2/WebAuthn (Hardware Key)** được coi là tiêu chuẩn vàng của xác thực hiện nay?

**Thước đo:**
*   **🟢 Beginner:** Phân biệt được Encryption (Mã hóa) và Hashing (Băm). Biết dùng 2FA App.
*   **🔴 Expert:** Hiểu sâu về **Public Key Infrastructure (PKI)**, biết cách thiết kế hệ thống **Single Sign-On (SSO)** an toàn với **OAuth2/OIDC**, và hiểu về các rủi ro của mật mã học trong kỷ nguyên máy tính lượng tử.

---

## 🚀 Thử thách 5: Incident Response & GRC (Ứng cứu & Tuân thủ)
*Đo lường năng lực quản lý khủng hoảng và quy trình chuyên nghiệp.*

**Tình huống:** Dữ liệu của 10.000 khách hàng đã bị rò rỉ. Bạn phải báo cáo sự việc cho Ban giám đốc và các cơ quan quản lý.

**Câu hỏi:**
1.  Nêu 6 bước trong quy trình ứng cứu sự cố của **SANS** (Preparation -> Identification -> Containment -> Eradication -> Recovery -> Lessons Learned). Tại sao bước "Lessons Learned" lại thường bị bỏ qua nhưng lại là quan trọng nhất?
2.  Sự khác biệt giữa **Risk Assessment** (Đánh giá rủi ro) và **Vulnerability Assessment** (Đánh giá lỗ hổng) là gì?

**Thước đo:**
*   **🟢 Beginner:** Biết báo cáo khi thấy lỗi, hiểu tầm quan trọng của backup.
*   **🔴 Expert:** Có khả năng điều phối toàn bộ chiến dịch ứng cứu, hiểu rõ các khung tiêu chuẩn quốc tế (**ISO 27001**, **NIST**, **SOC2**) và biết cách cân bằng giữa bảo mật và hiệu quả kinh doanh.

---

## 📊 Bảng tự chấm điểm (Scoring Rubric)

| Lĩnh vực | Thang điểm (1-10) | Gợi ý tự vấn |
| :--- | :---: | :--- |
| **Network & Forensics** | ____ / 10 | Bạn có thể "thấy" hacker đang làm gì chỉ qua các gói tin không? |
| **AppSec (Red Team)** | ____ / 10 | Bạn có thể tìm ra lỗ hổng trước khi nó được công bố không? |
| **Defensive (Blue Team)** | ____ / 10 | Hệ thống bạn dựng lên có thể trụ vững trước một cuộc tấn công DDoS lớn không? |
| **Identity & Crypto** | ____ / 10 | Bạn có đang dùng "ổ khóa" của thập niên 90 để bảo vệ tài sản năm 2026 không? |
| **Strategy & IR** | ____ / 10 | Khi mọi thứ sụp đổ, bạn có phải là người giữ được cái đầu lạnh để giải quyết không? |

### 🏆 Xếp hạng năng lực Security:
*   **0 - 15 điểm:** **Security Enthusiast**. Bạn mới bắt đầu hành trình. Hãy học kỹ Module 1 & 2 tại `domains/network-security/`.
*   **16 - 30 điểm:** **Junior Security Analyst / SOC Tier 1**. Bạn có thể vận hành các công cụ bảo mật cơ bản.
*   **31 - 45 điểm:** **Security Engineer / Senior Pentester**. Bạn là trụ cột bảo mật của tổ chức.
*   **46 - 50 điểm:** **CISO / Chief Security Architect**. Bạn không chỉ hiểu kỹ thuật mà còn định hình chiến lược bảo mật cho cả tập đoàn.

---

## 🔑 Answer Key: Góc nhìn Chuyên gia (Expert Guidelines)

### Thử thách 1: Network & Forensics
*   **DNS Tunneling:** Kỹ thuật giấu dữ liệu trong các record DNS (như TXT) để vượt qua Firewall/Proxy.
*   **Keywords SQLi:** `' OR 1=1--`, `UNION SELECT`, `information_schema`, `sleep()`.

### Thử thách 2: Web Security
*   **SSRF:** Lỗ hổng cho phép hacker ép server thực hiện các request đến các tài nguyên nội bộ mà hacker không truy cập trực tiếp được. Cách chống: Whitelist IP/Domain, chặn truy cập metadata IP của Cloud providers.

### Thử thách 3: System Hardening
*   **Hardening:** Disable Root login, dùng SSH Key, cài Fail2ban, tắt các service không cần thiết, cấu hình SELinux/AppArmor.
*   **Zero Trust:** "Never trust, always verify". Mọi request (dù là nội bộ hay bên ngoài) đều phải được định danh và kiểm tra quyền hạn.

### Thử thách 4: Identity & Crypto
*   **Argon2/bcrypt:** Là các thuật toán "chậm" có chủ đích (Iterative hashing) để chống lại các cuộc tấn công brute-force bằng GPU/ASIC.

### Thử thách 5: Incident Response
*   **Containment:** Là bước quan trọng nhất để khoanh vùng "Blast Radius" (bán kính thiệt hại), ngăn hacker lan rộng sang các server khác.

---

## 🚀 Tài liệu bổ trợ để "Level Up"
*   **Lộ trình kỹ thuật:** [Network & Security Roadmap](../../domains/network-security/README.md)
*   **Luyện tập (Tấn công):** [TryHackMe](https://tryhackme.com/)
*   **Luyện tập (Phòng thủ):** [LetsDefend](https://letsdefend.io/)
*   **Tiêu chuẩn quốc tế:** [OWASP Top 10](https://owasp.org/www-project-top-ten/)
