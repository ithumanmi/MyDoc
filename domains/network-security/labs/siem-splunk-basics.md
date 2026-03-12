# 📘 Lab: Splunk Free SIEM Basics

> Mục tiêu: dựng Splunk Free trên máy ảo, thu thập log Linux/Windows, parse với field extractor và viết SPL detection cơ bản.

---

## 1. Chuẩn bị

| Thành phần | Ghi chú |
| --- | --- |
| Splunk Enterprise Free (trial 500MB/ngày) | Tải từ splunk.com, cài trên Linux hoặc Windows |
| Universal Forwarder | Thu thập log từ endpoint |
| VM Linux + VM Windows | Sinh log SSH, PowerShell |

### 1.1 Cài Splunk Enterprise (Linux)
```bash
wget -O splunk.tgz 'https://download.splunk.com/products/splunk/releases/9.2.0/linux/splunk-9.2.0-linux-2.6-x86_64.tgz'
tar -xvf splunk.tgz
sudo ./splunk/bin/splunk start --accept-license
```

Đăng nhập `http://<IP>:8000` user/password tạo lần đầu.

---

## 2. Universal Forwarder & Input

### 2.1 Linux UF
```bash
wget -O splunkforwarder.tgz 'https://download.splunk.com/products/universalforwarder/releases/9.2.0/linux/splunkforwarder-9.2.0.tgz'
tar -xvf splunkforwarder.tgz
sudo ./splunkforwarder/bin/splunk set deploy-poll <splunk-ip>:8089 -auth admin:changeme
```

`inputs.conf`
```conf
[monitor:///var/log/auth.log]
disabled = false
[monitor:///var/log/syslog]
disabled = false
```

### 2.2 Windows UF
1. Tải `.msi`, cài và trỏ tới deployment server.
2. `inputs.conf`
```conf
[WinEventLog://Security]
index = wineventlog
[WinEventLog://System]
index = wineventlog
```

Sinh log brute-force: `hydra -l root -P rockyou.txt ssh://<ip>` và `Invoke-WebRequest` trên Windows.

---

## 3. Field Extraction & CIM
- Trong Splunk Web → `Settings > Fields > Field Extractions`.
- Dùng `regex` để parse `sshd` log: `Failed password for (?<user>\S+) from (?<src_ip>\S+)`.
- Áp dụng `Splunk Common Information Model (CIM)` bằng cách cài add-on `Splunk Add-on for Unix and Linux`.

---

## 4. SPL Detection mẫu

### 4.1 SSH Brute Force
```spl
index=linux_auth sourcetype=linux_secure "Failed password"
| stats count by src_ip, user
| where count > 20
```

### 4.2 PowerShell Download
```spl
index=wineventlog source="WinEventLog:Microsoft-Windows-PowerShell/Operational" EventCode=4104
| search ScriptBlockText="*Invoke-WebRequest*"
```

### 4.3 Dashboard nhanh
- Sử dụng `Visualization > Line chart` hiển thị failed login theo thời gian.
- Panel `Top Source IP` với `stats count by src_ip | sort - count`.

---

## 5. Alert & Report
- Tạo alert khi truy vấn SSH brute force > 20 lần / 5 phút → gửi email/webhook.
- Export dashboard PDF kèm mô tả log source.

> ✅ Hoàn thành lab khi thu thập log từ 2 host, có dashboard và alert SPL cơ bản.