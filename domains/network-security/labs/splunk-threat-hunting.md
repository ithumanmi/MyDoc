# 🔍 Lab: Splunk Threat Hunting Basics

> Mục tiêu: thu thập log từ Linux/Windows vào Splunk, viết SPL truy vấn phát hiện brute-force và persistence registry changes.

---

## 1. Chuẩn bị
- Splunk Enterprise trial (docker hoặc local install) – free 60 ngày.
- 1 máy Linux cài `splunkforwarder`, 1 máy Windows cài Universal Forwarder.
- Tài khoản admin Splunk (mặc định `admin/changeme`).

### **Splunk Enterprise (Docker)**
```bash
docker run -d --name splunk \
  -p 8000:8000 -p 8089:8089 -p 9997:9997 \
  -e SPLUNK_START_ARGS='--accept-license' \
  -e SPLUNK_PASSWORD='changeme123' \
  splunk/splunk:9.1
```

---

## 2. Forwarder Linux

```bash
wget -O splunkforwarder.tgz https://download.splunk.com/products/universalforwarder/releases/9.1.0/linux/splunkforwarder-9.1.0.tgz
sudo tar -xvf splunkforwarder-9.1.0.tgz -C /opt
sudo /opt/splunkforwarder/bin/splunk start --accept-license

sudo /opt/splunkforwarder/bin/splunk add forward-server <SPLUNK_IP>:9997 -auth admin:changeme123

sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log -index security -sourcetype linux:auth
sudo /opt/splunkforwarder/bin/splunk restart
```

Tạo brute-force log như lab Elastic (hydra). Log sẽ đẩy vào index `security`.

---

## 3. Forwarder Windows

1. Download: `splunkforwarder-9.1.0-x64-release.msi`
2. Cài bằng PowerShell:
```powershell
msiexec.exe /i splunkforwarder-9.1.0-x64-release.msi AGREETOLICENSE=Yes DEPLOYMENT_SERVER="" RECEIVING_INDEXER="<SPLUNK_IP>:9997" SPLUNKUSERNAME=admin SPLUNKPASSWORD=changeme123 LAUNCHSPLUNK=1 /quiet
```
3. Cấu hình inputs `C:\Program Files\SplunkUniversalForwarder\etc\system\local\inputs.conf`
```ini
[default]
host = win-lab

[WinEventLog://Security]
disabled = 0

[WinRegMon://Persistence]
disabled = 0
baseline = 0
registry = HKLM\Software\Microsoft\Windows\CurrentVersion\Run\*
type = rename
```
4. Restart forwarder:
```powershell
& "C:\Program Files\SplunkUniversalForwarder\bin\splunk.exe" restart
```

---

## 4. Hunting Queries (SPL)

### **SSH Brute Force**
```spl
index=security sourcetype=linux:auth "Failed password" \
| stats count by host, user, src \
| where count > 20
```

### **Persistence Registry**
```spl
index=security sourcetype=WinRegMon \
| stats latest(_time) as last_seen, values(registry_type) by key, host \
| search key="*\\run\\*"
```

### **Process Execution via WinEventLog**
```spl
index=security sourcetype=WinEventLog:Security EventCode=4688 \
| stats values(New_Process_Name) by Creator_Process_Name
```

Tạo dashboard hiển thị số lượng brute-force theo IP và registry modification timeline.

---

## 5. Alert & Response
- Đặt alert frequency 5 phút, trigger khi brute-force > 20.
- Gửi webhook tới Slack hoặc chạy script block IP.
- Lưu ý license Splunk: 500 MB/day free – clean index sau lab.

---

> ✅ Hoàn thành lab khi có dashboard brute-force, registry monitor, và ít nhất một alert rule chạy được.
