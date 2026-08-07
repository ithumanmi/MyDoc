---
title: "Network & Security Roadmap"
description: "Foundations through offense/defense security curriculum hub"
updated: "2026-08-07"
canonical: true
tags: [security, network, roadmap]
audience: [beginner, intermediate, advanced]
related:
  - ../../challenges/security/README.md
  - ../README.md
sensitivity: public
---

# 🛡️ Network & Security Roadmap

> [← Back to Chapter 1](../../chapters/01-xac-dinh-linh-vuc.md) | [Home](../../README.md)
>
> **Difficulty:** 🟢 Beginner → 🔴 Advanced (Progressive)
>
> **Prerequisites:** Basic Linux/Windows knowledge, Command line familiarity
>
> **Time to Master:** 18-36 months (Networking basics to Pentesting/Blue Team)

**📊 Difficulty levels:** See [DIFFICULTY-GUIDE.md](../../meta/ops/DIFFICULTY-GUIDE.md) to understand learning paths.
**🧩 Knowledge Audit:** Check [Cyber Security Knowledge Audit](../../case-studies/knowledge-audits/security-knowledge-audit.md) to test your skills!

---

"Amateurs hack systems, professionals hack people." - Bruce Schneier.
Hiểu về mạng và bảo mật không chỉ dành cho Hacker, mà là kỹ năng sinh tồn của mọi Developer trong thời đại số.

---

<!-- tech-career-nav -->
> **Tech vs Career:** this folder = technical how-to. **Security career / monetization:** [Security career / monetization](../../guides/03-career-skills/security/README.md). Full map: [`meta/domain-guide-map.md`](../../meta/domain-guide-map.md).

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

### **Foundations (Nền tảng bắt buộc)**
*   **[Networking Fundamentals](./foundations/networking-fundamentals.md):** Mô hình OSI 7 lớp, TCP/IP, cách Internet vận hành.
*   **[Security Fundamentals](./foundations/security-fundamentals.md):** CIA Triad, Cryptography (Mã hóa), Hashing (Băm), Digital Signature.
*   **[Cryptography Deep Dive](./foundations/cryptography-deep-dive.md):** PKI, TLS, thực hành OpenSSL.

### **Defense Operations (Blue Team)**
*   **[Network Defense & Operations](./defense-operations/network-defense.md):** Firewall, VPN, IDS/IPS, server hardening.
*   **[Cloud Security Basics](./defense-operations/cloud-security-basics.md):** Shared responsibility, IAM, monitoring.
*   **[Container Security](./defense-operations/container-security.md):** Runtime hardening, supply chain.
*   **[Forensics & Incident Response](./defense-operations/forensics-incident-response.md):** DFIR workflow.
*   **[Malware Analysis & Reverse Engineering (L3-L4) ✨](./defense-operations/malware-analysis-re.md):** (⭐ **NEW**) Thiết lập Sandbox Flare-VM, phân tích Tĩnh (Static) với Ghidra và Động (Dynamic) với Procmon/Wireshark.
*   **[Wireless Security](./defense-operations/wireless-hacking.md):** WPA2, Evil Twin, bảo vệ Wi-Fi.

### **Offensive Security (Red Team)**
*   **[Web Security & OWASP Top 10](./offensive-security/web-security-owasp.md):** SQLi, XSS, CSRF, SSRF.
*   **[Network Pentest & Metasploit](./offensive-security/network-pentest.md):** Nmap, Tấn công cơ bản.
*   **[C2 Infrastructure & EDR Evasion (Elite) ✨](./offensive-security/c2-edr-evasion.md):** (⭐ **NEW Khủng Lịch Sử**) Thiết kế Command & Control tàng hình (Domain Fronting, Direct Syscalls, Process Hollowing) để qua mặt AV/EDR.
*   **[Social Engineering](./offensive-security/social-engineering.md):** Phishing, OSINT, SET.

### **Governance & Strategy**
*   **[Anonymity & OpSec](./governance-strategy/anonymity-opsec.md):** Tor, OPSEC mindset.
*   **[Governance, Risk & Compliance](./governance-strategy/governance-risk-compliance.md):** ISO/NIST.
*   **[Threat Intelligence](./governance-strategy/threat-intelligence.md):** Cyber Kill Chain, ATT&CK mapping.

### **DevSecOps & Platform Security**
*   **[AppSec & DevSecOps](./devsecops/appsec-devsecops.md):** Shift-left pipeline.
*   **[API Security](./devsecops/api-security.md):** OWASP API Top 10.
*   **[Supply Chain Attacks](./devsecops/supply-chain-attacks.md):** Sigstore, artifact signing.
*   **[LLM Security](./devsecops/llm-security.md):** Prompt injection, jailbreak defense.

---

## 🧪 4. Labs (Thực hành)

Học Security là phải thực chiến. Hãy làm các bài lab này (trên máy ảo, KHÔNG làm trên máy thật của công ty).

### **Red Team (Tấn công)**
*   **[Virtual Lab Setup](./labs/virtual-lab-setup.md):** Hướng dẫn cài đặt Kali Linux & Metasploitable 2 an toàn.
*   **[SQL Injection Deep Dive](./labs/sql-injection-practice.md):** Thực hành tấn công Authentication Bypass và dump dữ liệu từ database.
*   **[XSS & CSRF Practice](./labs/xss-csrf-practice.md):** Tấn công phía Client-side, đánh cắp Cookie và chiếm quyền User.
*   **[Metasploit & Reverse Shell](./labs/metasploit-reverse-shell.md):** Sử dụng Framework khai thác lỗ hổng OS để chiếm quyền Root.
*   **[Khởi Trị C2 Sliver Framework Nhọn Hồi EDR ✨](./labs/lab-sliver-c2-evasion.md):** (⭐ **NEW**) Dùng Golang Tạc Tượng Sliver Build Implant Tàng Hình Vượt Sensor Dán Lệnh (mTLS Covert Channels).

#### Offensive Modules ↔ Tool Stack
| Offensive phase | Mô tả nhanh | Tool chính |
| --- | --- | --- |
| Recon & Discovery | Scan port/service, enum surface | Nmap, Masscan, Amass, Shodan |
| Web Exploitation | Proxy, payload crafting | Burp Suite, OWASP ZAP, sqlmap |
| Credential & Access | Brute-force, password spraying | Hydra, CrackMapExec, Responder |
| Exploitation & Payload | Tạo shell, khai thác CVE | Metasploit, Exploit-DB PoC, msfvenom |
| Post-Exploitation & Pivot | Duy trì quyền, lateral move | Covenant, Cobalt Strike (demo), BloodHound |
| Automation & Scripting | Glue task, custom exploit | Python, PowerShell, Bash |

### **Blue Team (Phòng thủ)**
*   **[Linux Hardening with UFW](./labs/linux-hardening-ufw.md):** Cấu hình Firewall chặn tất cả, chỉ mở SSH và Web.
*   **[Malware Analysis & Reverse Engineering Sandbox ✨](./labs/lab-malware-analysis.md):** (⭐ **NEW**) Nhốt Mã Độc Vào Flare-VM, Đo Bắt Cột Registry Run Của ProcMon & Tìm IP Gốc Bằng INetSim/Wireshark.
*   **[SIEM & Log Analysis (Elastic Stack)](./labs/siem-log-analysis.md):** Thu thập log Linux/Windows, phát hiện SSH brute-force & process injection.
*   **[Splunk Threat Hunting Basics](./labs/splunk-threat-hunting.md):** Dựng Splunk Enterprise + Universal Forwarder, viết SPL hunting brute-force & persistence.
*   **[Splunk Free SIEM Basics](./labs/siem-splunk-basics.md):** Build Splunk free tier, parse log và tạo alert cơ bản.
*   **[Microsoft Sentinel Threat Hunting](./labs/azure-sentinel-threat-hunting.md):** Kết nối Azure AD + Windows event, viết KQL rule impossible travel & PowerShell download detection.
*   **[Google Chronicle Detection Engineering](./labs/chronicle-detection-lab.md):** Ingest syslog/CloudTrail, viết YARA-L rule & UDM search DNS tunneling.
*   **[IBM QRadar Use Case Engineering](./labs/qradar-detection-lab.md):** Dựng QRadar CE, viết CRE rule lateral movement & beaconing.
*   **[QRadar Offense Automation](./labs/qradar-offense-automation.md):** Sử dụng API để block IP, tạo ticket và đóng offense tự động.
*   **[Chronicle BigQuery & Looker Lab](./labs/chronicle-detection-lab.md#-chronicle-advanced-lab-bigquery--looker-exploration):** Xuất log sang BigQuery, dựng dashboard Looker.
*   **[Chronicle BigQuery ML Add-on](./labs/chronicle-detection-lab.md#-bigquery-ml-anomaly-detection-add-on):** Train model ARIMA+ để phát hiện anomaly đăng nhập và tự động phản hồi.
*   **[Advanced Detection Use Cases](./labs/advanced-detection-usecases.md):** Bộ query nâng cao (Kerberos abuse, DNS beacon + JA3, container escape, ransomware kill chain).
*   **[ELK Detection with Sigma](./labs/elk-stack-detection.md):** Deploy Elastic Stack, convert Sigma rule sang KQL và tạo detection engine.
*   **[Wireshark Packet Analysis](./labs/wireshark-packet-analysis.md):** Bắt gói tin, phân tích TCP handshake, phát hiện port scan & slowloris.
*   **[Windows Event Forensics](./labs/windows-event-forensics.md):** Event ID hunting 4624/4625/4688/7045, xây timeline sự cố.
*   **[Home Lab Architecture Blueprint](./labs/home-lab-architecture.md):** Thiết kế lab Proxmox/ESXi đa VLAN cho SOC & pentest.
*   **[VulnHub & HTB Progression](./labs/vulnhub-htb-progression.md):** Lộ trình luyện box Easy → Insane, checklist kỹ thuật.
*   **[CTF Writeup Template](./labs/ctf-writeup-template.md):** Chuẩn hóa note/writeup, dễ chia sẻ và rút kinh nghiệm.

### **Advanced Topics (Nâng cao)**
*   **[Wireless Security (Wi-Fi Hacking)](./defense-operations/wireless-hacking.md):** Tấn công WPA2 Handshake, Evil Twin và cách phòng thủ.
*   **[Social Engineering (Hacking con người)](./offensive-security/social-engineering.md):** Phishing, OSINT và sử dụng SET (Social-Engineer Toolkit).

### **Lab Progression Checklist**

| Level | Focus | Labs |
| --- | --- | --- |
| **Level 1 – Foundation** | Thiết lập môi trường, hiểu attack surface | Virtual Lab Setup, Linux Hardening |
| **Level 2 – Offensive** | Web/app exploitation, privilege escalation | SQLi Deep Dive, XSS/CSRF, Metasploit |
| **Level 3 – Specialized** | Wireless, Social engineering, hybrid ops | Wireless Security, Social Engineering, tùy chọn MMO automation |

> ✅ Đánh dấu hoàn thành từng level trước khi lên level cao hơn để đảm bảo nắm vững kỹ năng.

### **Security Modules ↔ Lab Playbook**
| Module phòng thủ | Mục tiêu | Lab khuyến nghị |
| --- | --- | --- |
| SIEM & Detection | Thu thập log, viết rule | [SIEM Elastic](./labs/siem-log-analysis.md), [Splunk Hunting](./labs/splunk-threat-hunting.md), [Microsoft Sentinel](./labs/azure-sentinel-threat-hunting.md), [Chronicle Detection](./labs/chronicle-detection-lab.md) |
| Incident Response | Điều tra, phản hồi | [QRadar Use Case](./labs/qradar-detection-lab.md), [QRadar Offense Automation](./labs/qradar-offense-automation.md) |
| Host/Network Hardening | Gia cố OS, firewall | [Linux Hardening UFW](./labs/linux-hardening-ufw.md), [Virtual Lab Setup](./labs/virtual-lab-setup.md) |
| Advanced Threat Analytics | JA3, DNS beacon, cloud log | [Advanced Detection](./labs/advanced-detection-usecases.md), [Chronicle BigQuery Lab](./labs/chronicle-detection-lab.md#-chronicle-advanced-lab-bigquery--looker-exploration) |

### **Mastery & Specialized Fields (Chuyên sâu)**
*   **[Cryptography Deep Dive](./foundations/cryptography-deep-dive.md):** Mã hóa đối xứng/bất đối xứng, Hashing, PKI và thực hành OpenSSL.
*   **[Cloud Security](./defense-operations/cloud-security-basics.md):** Bảo mật AWS/Azure, Mô hình trách nhiệm chia sẻ, IAM và S3 Leaks.
*   **[Digital Forensics & Incident Response](./defense-operations/forensics-incident-response.md):** Quy trình ứng cứu sự cố, phân tích Malware và điều tra số.
*   **[Anonymity & OpSec](./governance-strategy/anonymity-opsec.md):** Nghệ thuật ẩn danh, Tor, Dark Web và bảo vệ danh tính.

#### Cloud Security ↔ Labs/Guides
| Chủ đề | Nội dung | Tài liệu/Lab |
| --- | --- | --- |
| IAM & Least Privilege | Chính sách IAM, MFA, key rotation | [Cloud Security Basics](./defense-operations/cloud-security-basics.md#iam--identity-architecture), [Azure Sentinel Lab](./labs/azure-sentinel-threat-hunting.md) |
| Logging & Detection | CloudTrail, Azure Monitor | [Chronicle Detection Lab](./labs/chronicle-detection-lab.md), [Advanced Detection](./labs/advanced-detection-usecases.md#5-cloudtrail-suspicious-console-login) |
| Network Segmentation | VPC, Security Group, WAF | [Network Defense](./defense-operations/network-defense.md), [Virtual Lab Setup](./labs/virtual-lab-setup.md) |
| Incident Response | Forensics, automation | [QRadar Offense Automation](./labs/qradar-offense-automation.md), [Chronicle BigQuery Lab](./labs/chronicle-detection-lab.md#-chronicle-advanced-lab-bigquery--looker-exploration) |

### **InfoSec Strategy & Management (Quản lý & Chiến lược)**
*   **[Governance, Risk & Compliance (GRC)](./governance-strategy/governance-risk-compliance.md):** ISO 27001, NIST Framework và quản lý rủi ro doanh nghiệp.
*   **[AppSec & DevSecOps](./devsecops/appsec-devsecops.md):** Bảo mật ứng dụng hiện đại (SAST/DAST) và tích hợp vào CI/CD.
*   **[Threat Intelligence](./governance-strategy/threat-intelligence.md):** Tình báo mối đe dọa, Cyber Kill Chain và MITRE ATT&CK.

#### DevSecOps ↔ Toolchain Mapping
| DevSecOps stage | Mục tiêu bảo mật | Tool/Resource |
| --- | --- | --- |
| Plan & Requirements | Threat modeling, policy-as-code | [AppSec & DevSecOps guide](./devsecops/appsec-devsecops.md#1-threat-modeling), IriusRisk, Threat Dragon |
| Code & Build | Static scan, dependency audit | SonarQube, Semgrep, GitHub Advanced Security |
| Test & Validate | DAST, API scanning, IaC checks | OWASP ZAP, Burp CI, Checkov, tfsec |
| Deploy & Release | Secrets management, supply chain | HashiCorp Vault, SOPS, Sigstore/Cosign |
| Operate & Monitor | Runtime protection, drift detection | Falco, AWS GuardDuty, Azure Defender |
| Respond & Improve | Feedback loop, RCA | Jira/YouTrack + Playbook trong [AppSec & DevSecOps](./appsec-devsecops.md#6-incident-response--continuous-improvement) |

### **Network Internals & Deep Dive (Kiến thức Mạng chuyên sâu)**
*   **[Network Layer](./deep-dive/network-layer.md):** IP addressing, subnetting workflow, ICMP/MTU, OSPF/BGP khái quát + bài tập Path MTU.
*   **[Routing Protocols](./deep-dive/routing-protocols.md):** Hướng dẫn multi-area OSPF, eBGP/iBGP design, anti BGP hijack + lab GNS3 chi tiết.
*   **[Application Layer](./deep-dive/application-layer.md):** HTTP/2 vs HTTP/3, Proxy, Load Balancer & API Gateway.
*   **[Transport Layer](./deep-dive/transport-layer.md):** TCP Handshake, Flow Control, UDP & QUIC.
*   **[Security Protocols](./deep-dive/security-protocols.md):** TLS 1.3 Handshake, PKI, Certificate Pinning & MITM.
*   **[Infrastructure](./deep-dive/infrastructure-networking.md):** CDN, NAT, Modern Firewall & Zero Trust Architecture.

### **Deep Dive ↔ Lab Mapping**
| Deep-dive topic | Kiến thức chính | Lab liên quan |
| --- | --- | --- |
| Network Layer & Routing | Subnetting workflow, PMTUD, OSPF/BGP fundamentals | [Netflow & BGP Monitoring](./labs/netflow-bgp-monitoring.md), [Wireshark Packet Analysis](./labs/wireshark-packet-analysis.md), [Virtual Lab Setup](./labs/virtual-lab-setup.md) |
| Application Layer | HTTP evolution, proxy patterns, API gateway | [SQL Injection](./labs/sql-injection-practice.md), [XSS/CSRF](./labs/xss-csrf-practice.md), [Azure Sentinel](./labs/azure-sentinel-threat-hunting.md) |
| Transport Layer | TCP handshake, congestion, QUIC | [SIEM Elastic](./labs/siem-log-analysis.md), [Splunk Hunting](./labs/splunk-threat-hunting.md), [Advanced Detection](./labs/advanced-detection-usecases.md#2-dns-beacon--ja3-ssl-fingerprinting) |
| Security Protocols | TLS 1.3, PKI, MITM defense | [Advanced Detection](./labs/advanced-detection-usecases.md#2-dns-beacon--ja3-ssl-fingerprinting), [Azure Sentinel](./labs/azure-sentinel-threat-hunting.md), [Chronicle Detection](./labs/chronicle-detection-lab.md) |
| Infrastructure Networking | NAT, CDN, Zero Trust, firewall | [Linux Hardening UFW](./labs/linux-hardening-ufw.md), [Virtual Lab Setup](./labs/virtual-lab-setup.md), [QRadar Use Case](./labs/qradar-detection-lab.md) |

### **MMO & Automation Engineering (Kỹ thuật MMO)**
*   **[Browser Fingerprinting](./mmo-engineering/browser-fingerprinting.md):** Cách các ông lớn theo dõi bạn và cách sử dụng Anti-Detect Browser.
*   **[Proxy Infrastructure](./mmo-engineering/proxy-infrastructure.md):** Xây dựng Farm 4G, phân biệt Residential vs Datacenter Proxy.
*   **[Automation Tools](./mmo-engineering/automation-tools.md):** Selenium, ZennoPoster, Phone Farm và bypass OTP.
*   **[Crypto Sybil Attack](./mmo-engineering/crypto-sybil.md):** Chiến lược cheat Airdrop, quản lý 1000 ví và tránh bị phát hiện on-chain.
*   **[MMO Engineering README](./mmo-engineering/README.md):** Scope, risk & ethics checklist, roadmap.
*   **[Tool Development (Python)](./mmo-engineering/tool-dev/python-foundation.md):** Lộ trình tự viết Tool từ API Automation, GUI đến Anti-Detect.

## 🎯 6. Certification & Career Mapping

| Track | Junior Goal | Advanced Goal | Content Mapping |
| --- | --- | --- | --- |
| Networking | **CCNA**, Network+ | **CCNP**, JNCIP | Modules 1 & Deep-dive Infrastructure |
| Offensive Security | **OSCP**, eJPT | **OSEP**, CRTO | Web Security, Labs Offensive, Threat Intel |
| Blue Team / Defense | **Security+**, **CySA+** | **GCIA**, **GCIH**, **CISSP** | Security Foundations, Network Defense, Forensics, GRC |
| Cloud Security | **AWS SAA/Security Specialty** | **CCSP**, **Azure Security Engineer** | Cloud Security, Zero Trust, Automation/SOC add-ons |

> Sử dụng bảng này để chọn chứng chỉ phù hợp với giai đoạn hiện tại và nội dung cần ôn luyện.

---

## 🛠️ 7. Tools & Lab Setup

Để học Security, bạn KHÔNG THỂ chỉ đọc sách. Bạn cần thực hành.
1.  **Kali Linux:** Hệ điều hành dành cho Hacker (cài trên VirtualBox/VMware).
2.  **Wireshark:** Bắt và phân tích gói tin mạng.
3.  **Burp Suite:** Proxy để chặn và sửa đổi request web.
4.  **Metasploit:** Framework để khai thác lỗ hổng.
5.  **TryHackMe / HackTheBox:** Các phòng lab ảo để luyện tập an toàn.

---

> **Last Updated:** March 2026
