# 🏠 Home Lab Architecture Blueprint (Proxmox / VMware)

> Mục tiêu: xây dựng lab đa hypervisor (Proxmox hoặc VMware ESXi) phục vụ SOC, Pentest, DevSecOps.

---

## 1. Topology Overview
- **Layer 0 (Host):** Server mini (Intel NUC, Dell R730) -> cài Proxmox hoặc ESXi.
- **Layer 1 (Network):** pfSense/OPNsense làm router + VLAN (Mgmt, DMZ, Lab, Storage).
- **Layer 2 (Services):** AD/DC, Linux jumpbox, SIEM stack, vulnerable targets.

```
ISP → pfSense (VLAN trunk)
  ├── VLAN10 Mgmt (Proxmox/ESXi mgmt)
  ├── VLAN20 Lab (Kali, Attacker)
  ├── VLAN30 Server (AD, File, DB)
  └── VLAN40 DMZ (Web, Honeypot)
```

---

## 2. Hardware tối thiểu
| Thành phần | Gợi ý |
| --- | --- |
| CPU | 8 core (Xeon E5, Ryzen) |
| RAM | 64GB+ |
| Storage | 1TB NVMe (VM), 4TB HDD (NAS) |
| Network | 2x1GbE (WAN/LAN) |

---

## 3. Proxmox Blueprint
1. Install Proxmox VE → cập nhật repo (community).
2. Tạo bridge `vmbr0` (LAN), `vmbr1` (DMZ).
3. Enable VLAN aware + tag theo pfSense.
4. Template VM (Cloud-Init) cho Ubuntu/Windows.

### VMware ESXi variation
- Sử dụng vSwitch Standard/Distributed.
- VCSA để quản lý cluster.
- vCenter + DRS để mô phỏng enterprise.

---

## 4. Core Services
- **pfSense firewall:** IDS/IPS (Suricata), VPN.
- **Active Directory:** Windows Server + DNS.
- **SOC Stack:** Elastic/Splunk container.
- **Attack box:** Kali/Parrot.
- **Targets:** Metasploitable2, vulnerable web (DVWA, Juice Shop).

---

## 5. Automation & Backup
- Infrastructure as Code: Terraform + Ansible (Proxmox provider) để tạo VM.
- Backup: Proxmox backup server hoặc Veeam Community.
- Snapshot lab trước khi demo.

---

## 6. Checklist
- [ ] Segmentation rõ ràng (VLAN, firewall rule).
- [ ] Có license phù hợp (ESXi free vs Proxmox open-source).
- [ ] Monitoring cơ bản (Zabbix/Netdata) cho host.
- [ ] Backup/snapshot định kỳ.
- [ ] Documentation topo + credential vault (Bitwarden).