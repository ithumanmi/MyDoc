# 🛰️ Lab: IBM QRadar Use Case Engineering

> Mục tiêu: triển khai QRadar Community Edition hoặc Appliance, thu thập log Windows & NetFlow, viết Custom Rule Engine (CRE) phát hiện lateral movement và beaconing.

---

## 1. Chuẩn bị
- **QRadar Community Edition** (OVA) – giới hạn 50 EPS.
- 1 Windows server + WinCollect agent hoặc syslog forwarder.
- NetFlow exporter (pfSense, nProbe) để feed lưu lượng.

### **Triển khai QRadar CE (VMware/VirtualBox)**
1. Import OVA, allocate 8GB RAM, 4 CPU, 250GB disk.
2. Đăng nhập UI `https://<ip>` → user `admin`.

---

## 2. Ingest Data Sources

### **Windows via WinCollect**
1. Tải WinCollect agent từ QRadar console (`Admin > WinCollect > Install Wizard`).
2. Cài trên Windows:
```powershell
msiexec /i WinCollect-10.1.0.0-x64.msi TRANSFORM=WinCollectConfig.mst /qn
```
3. Add log source type `Microsoft Windows Security Event Log`.

### **NetFlow**
- Trên pfSense: `Services > NetFlow` → gửi tới `QRadar_IP:2055`.
- QRadar: `Log Sources > Add > Flow > External Flow Source`.

---

## 3. CRE Rule: Lateral Movement via Service Control

1. `Offenses > Rules > Actions > New Event Rule`.
2. Condition:
   - When event(s) were detected by the **Microsoft Windows Security Event Log** log source 
   - and when the event name equals `Service Control Manager`.
   - and when the event description contains `sc.exe create` or `PsExec`.
   - and when at least 5 events are seen with the same Source IP in 10 minutes.
3. Response: **Create Offense on Source IP**.

### **Test**
```powershell
sc.exe \TARGET create EvilSvc binPath=cmd.exe
```
Quan sát offense xuất hiện.

---

## 4. CRE Rule: Beaconing via NetFlow

Condition:
```
when the same source IP has flows to the same destination IP
every 60 seconds
and total bytes per flow < 2000
in at least 8 flows within 10 minutes
```

Rule wizard → Flow rule.

Test: dùng `c2` (e.g., `cobalt strike` demo) hoặc script cron ping.

---

## 5. Dashboards & Reporting
- Create custom dashboard widget: Top Offenses by Category.
- Flow analytics chart: `Reports > Flow > Custom`.

---

## 6. Advanced Use Case Ideas
- Correlate Winlog event 4624 (logon) với NetFlow outbound unusual port.
- Use Reference Set to track suspicious hashes.

---

> ✅ Hoàn thành khi bạn tạo được 2 rule (service lateral + beaconing), offense raise, và báo cáo flow hiển thị pattern.
