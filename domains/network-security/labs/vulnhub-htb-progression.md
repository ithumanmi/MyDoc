# 🎯 VulnHub / HackTheBox Progression

> Lộ trình luyện box từ Easy → Insane, tập trung build kỹ năng liên tục.

---

## 1. Strategy
- Xen kẽ VulnHub (offline) và HackTheBox (online) để đa dạng.
- Mỗi box phải viết note + flag command, convert thành detection idea.
- Revisit sau 3-6 tháng với phương pháp mới (automation, scripting).

---

## 2. Roadmap by Difficulty

### Easy
- **VulnHub:** Kioptrix 1-3, DC-1.
- **HTB:** Lame, Legacy, OpenAdmin.
- **Focus:** Recon cơ bản (nmap, dirb), misconfig obvious.

### Medium
- **VulnHub:** DC-5, RickdiculouslyEasy.
- **HTB:** Optimum, Blunder, Physician.
- **Focus:** Privilege escalation (Linux capabilities, Windows services), scripting.

### Hard
- **VulnHub:** PrimeSeries 1-2.
- **HTB:** Sauna, Arctic, Ransom.
- **Focus:** AD exploitation, Kerberoast, custom exploit, AV evasion.

### Insane
- **HTB:** Oouch, APT, MonitorsTwo.
- **Focus:** Chaining nhiều bug, code review, pivot network.

---

## 3. Tracking Template
| Box | Platform | Difficulty | Key technique | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Lame | HTB | Easy | Samba exploit | ✅ | CVE-2007-2447 |
| Optimum | HTB | Easy | Rejetto HFS | ✅ | Powershell privesc |

---

## 4. Tips
- Dùng `autorecon`/`nmapAutomator` để tiết kiệm thời gian.
- Lưu script exploit vào repo riêng.
- Tạo detection idea: sau mỗi box, nghĩ xem SOC phát hiện thế nào.

---

## 5. Checklist
- [ ] Có nhật ký progression (Notion/Obsidian).
- [ ] Mỗi box có writeup (public/private).
- [ ] Review box cũ với kỹ thuật mới.
- [ ] Tham gia team event (HTB Team, CTF).