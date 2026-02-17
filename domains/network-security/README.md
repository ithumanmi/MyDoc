# 🛡️ Network & Security Roadmap

> [← Back to Chapter 1](../../chapters/01-xac-dinh-linh-vuc.md) | [Home](../../README.md)
>
> **Difficulty:** 🟢 Beginner → 🔴 Advanced (Progressive)
>
> **Prerequisites:** Basic Linux/Windows knowledge, Command line familiarity
>
> **Time to Master:** 18-36 months (Networking basics to Pentesting/Blue Team)

**📊 Difficulty levels:** See [DIFFICULTY-GUIDE.md](../../DIFFICULTY-GUIDE.md) to understand learning paths.

---

"Amateurs hack systems, professionals hack people." - Bruce Schneier.
Hiểu về mạng và bảo mật không chỉ dành cho Hacker, mà là kỹ năng sinh tồn của mọi Developer trong thời đại số.

---

## 📊 1. Reality Check: Security Engineer

| Tiêu chí | 🛡️ Security Engineer | 💻 Network Engineer | 🕵️ Pentester (Ethical Hacker) |
| :--- | :--- | :--- | :--- |
| **Độ khó** | ⭐⭐⭐⭐⭐ (Rất khó - Cần kiến thức rộng) | ⭐⭐⭐⭐ (Khó - Cần chứng chỉ CCNA/CCNP) | ⭐⭐⭐⭐⭐ (Cực khó - Tư duy Out-of-the-box) |
| **Cơ hội việc làm** | ⭐⭐⭐⭐ (Nhu cầu cao, lương khủng) | ⭐⭐⭐ (Ổn định, bảo trì hệ thống) | ⭐⭐⭐ (Niche market, lương rất cao) |
| **Mức lương (Junior)** | 💰 $800 - $1,500 | 💰 $600 - $1,000 | 💰 $1,000 - $2,000 |
| **Mức lương (Senior)** | 📈 $3,000 - $10,000+ | 📈 $2,000 - $4,000 | 📈 $5,000 - $15,000+ |
| **Tech Stack** | Python, Linux, Bash, SIEM, Firewalls | Cisco IOS, Juniper, Wireshark | Burp Suite, Metasploit, Kali Linux |

> **Verdict:** Đây là con đường chông gai nhất nhưng cũng "ngầu" nhất. Bạn cần am hiểu cả Code, System, Network và Psychology.

---

## 🗺️ 2. Visual Roadmap

```mermaid
graph TD
    A[Start Here] --> B[🌐 Networking Foundations]
    B --> B1(OSI Model & TCP/IP)
    B --> B2(DNS, HTTP, DHCP)
    B --> B3(Subnetting, Routing)
    
    B --> C[🔒 Security Foundations]
    C --> C1(CIA Triad)
    C --> C2(Cryptography: Encryption, Hashing)
    C --> C3(Identity: AuthN vs AuthZ)

    C --> D{Choose Your Path}
    
    D --> E[🛡️ Blue Team (Defense)]
    E --> E1(Firewalls, VPN, IDS/IPS)
    E --> E2(SIEM, Log Analysis)
    E --> E3(Hardening Linux/Windows)

    D --> F[⚔️ Red Team (Offense)]
    F --> F1(Web Security: OWASP Top 10)
    F --> F2(Network Pentest: Nmap, Metasploit)
    F --> F3(Social Engineering)
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
```

---

## 📚 3. Detailed Roadmap (Mục lục chi tiết)

### **Module 1: Networking Foundations (Mạng căn bản)**
*   **[Networking Fundamentals](./networking-fundamentals.md):** Mô hình OSI 7 lớp, TCP/IP, cách Internet vận hành.
*   **Key Concepts:** IP Address, Subnet mask, Mac Address, Port, Protocol (TCP vs UDP).

### **Module 2: Security Foundations (Bảo mật căn bản)**
*   **[Security Fundamentals](./security-fundamentals.md):** CIA Triad, Cryptography (Mã hóa), Hashing (Băm), Digital Signature.
*   **Key Concepts:** Public/Private Key, SSL/TLS Handshake, Salt & Pepper.

### **Module 3: Web Security (Dành cho Web Dev)**
*   **[Web Security & OWASP Top 10](./web-security-owasp.md):** Các lỗ hổng web phổ biến nhất và cách phòng chống.
*   **Attacks:** SQL Injection, XSS, CSRF, DDoS.

### **Module 4: Network Defense (Phòng thủ)**
*   **[Network Defense & Operations](./network-defense.md):** Firewall, VPN, IDS/IPS, Hardening Server.

---

## 🧪 4. Labs (Thực hành)

Học Security là phải thực chiến. Hãy làm các bài lab này (trên máy ảo, KHÔNG làm trên máy thật của công ty).

### **Red Team (Tấn công)**
*   **[Virtual Lab Setup](./labs/virtual-lab-setup.md):** Hướng dẫn cài đặt Kali Linux & Metasploitable 2 an toàn.
*   **[SQL Injection Deep Dive](./labs/sql-injection-practice.md):** Thực hành tấn công Authentication Bypass và dump dữ liệu từ database.
*   **[XSS & CSRF Practice](./labs/xss-csrf-practice.md):** Tấn công phía Client-side, đánh cắp Cookie và chiếm quyền User.
*   **[Metasploit & Reverse Shell](./labs/metasploit-reverse-shell.md):** Sử dụng Framework khai thác lỗ hổng OS để chiếm quyền Root.

### **Blue Team (Phòng thủ)**
*   **[Linux Hardening with UFW](./labs/linux-hardening-ufw.md):** Cấu hình Firewall chặn tất cả, chỉ mở SSH và Web.

### **Advanced Topics (Nâng cao)**
*   **[Wireless Security (Wi-Fi Hacking)](./wireless-hacking.md):** Tấn công WPA2 Handshake, Evil Twin và cách phòng thủ.
*   **[Social Engineering (Hacking con người)](./social-engineering.md):** Phishing, OSINT và sử dụng SET (Social-Engineer Toolkit).

### **Mastery & Specialized Fields (Chuyên sâu)**
*   **[Cryptography Deep Dive](./cryptography-deep-dive.md):** Mã hóa đối xứng/bất đối xứng, Hashing, PKI và thực hành OpenSSL.
*   **[Cloud Security](./cloud-security-basics.md):** Bảo mật AWS/Azure, Mô hình trách nhiệm chia sẻ, IAM và S3 Leaks.
*   **[Digital Forensics & Incident Response](./forensics-incident-response.md):** Quy trình ứng cứu sự cố, phân tích Malware và điều tra số.
*   **[Anonymity & OpSec](./anonymity-opsec.md):** Nghệ thuật ẩn danh, Tor, Dark Web và bảo vệ danh tính.

### **InfoSec Strategy & Management (Quản lý & Chiến lược)**
*   **[Governance, Risk & Compliance (GRC)](./governance-risk-compliance.md):** ISO 27001, NIST Framework và quản lý rủi ro doanh nghiệp.
*   **[AppSec & DevSecOps](./appsec-devsecops.md):** Bảo mật ứng dụng hiện đại (SAST/DAST) và tích hợp vào CI/CD.
*   **[Threat Intelligence](./threat-intelligence.md):** Tình báo mối đe dọa, Cyber Kill Chain và MITRE ATT&CK.

### **Network Internals & Deep Dive (Kiến thức Mạng chuyên sâu)**
*   **[Application Layer](./deep-dive/application-layer.md):** HTTP/2 vs HTTP/3, Proxy, Load Balancer & API Gateway.
*   **[Transport Layer](./deep-dive/transport-layer.md):** TCP Handshake, Flow Control, UDP & QUIC.
*   **[Security Protocols](./deep-dive/security-protocols.md):** TLS 1.3 Handshake, PKI, Certificate Pinning & MITM.
*   **[Infrastructure](./deep-dive/infrastructure-networking.md):** CDN, NAT, Modern Firewall & Zero Trust Architecture.

### **MMO & Automation Engineering (Kỹ thuật MMO)**
*   **[Browser Fingerprinting](./mmo-engineering/browser-fingerprinting.md):** Cách các ông lớn theo dõi bạn và cách sử dụng Anti-Detect Browser.
*   **[Proxy Infrastructure](./mmo-engineering/proxy-infrastructure.md):** Xây dựng Farm 4G, phân biệt Residential vs Datacenter Proxy.
*   **[Automation Tools](./mmo-engineering/automation-tools.md):** Selenium, ZennoPoster, Phone Farm và bypass OTP.
*   **[Crypto Sybil Attack](./mmo-engineering/crypto-sybil.md):** Chiến lược cheat Airdrop, quản lý 1000 ví và tránh bị phát hiện on-chain.
*   **[Tool Development (Python)](./mmo-engineering/tool-dev/python-foundation.md):** Lộ trình tự viết Tool từ API Automation, GUI đến Anti-Detect.

---

## 🛠️ 5. Tools & Lab Setup

Để học Security, bạn KHÔNG THỂ chỉ đọc sách. Bạn cần thực hành.
1.  **Kali Linux:** Hệ điều hành dành cho Hacker (cài trên VirtualBox/VMware).
2.  **Wireshark:** Bắt và phân tích gói tin mạng.
3.  **Burp Suite:** Proxy để chặn và sửa đổi request web.
4.  **Metasploit:** Framework để khai thác lỗ hổng.
5.  **TryHackMe / HackTheBox:** Các phòng lab ảo để luyện tập an toàn.

---

> **Last Updated:** February 2026
