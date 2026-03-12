# 📊 Lab: SIEM & Log Analysis with Elastic Stack

> Mục tiêu: dựng một pipeline thu thập log (Linux/Windows), gửi về Elasticsearch, viết rule phát hiện brute-force SSH và process injection.

---

## 1. Kiến trúc & Chuẩn bị

| Component | Vai trò |
| --- | --- |
| **Elasticsearch + Kibana** | Lưu trữ + visual log |
| **Filebeat / Winlogbeat** | Thu thập log hệ thống |
| **Elastic Agent (optional)** | Dễ cấu hình integration |

### **Prerequisites**
- Docker / Docker Compose (hoặc Elastic Cloud trial).
- 1 VM Linux (Ubuntu) và 1 VM Windows (hoặc WSL) để sinh log.

---

## 2. Triển khai Elastic Stack (Docker Compose)

`docker-compose.yaml`
```yaml
version: "3.2"
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - ELASTIC_PASSWORD=changeme
    ports:
      - "9200:9200"
  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    environment:
      - ELASTICSEARCH_HOSTS=https://elasticsearch:9200
      - ELASTICSEARCH_USERNAME=elastic
      - ELASTICSEARCH_PASSWORD=changeme
    ports:
      - "5601:5601"
```

```bash
docker compose up -d
```

Truy cập Kibana `http://localhost:5601`, nhập user `elastic` / `changeme` (đổi sau khi lab xong).

---

## 3. Thu thập log Linux với Filebeat

### **Cài đặt Filebeat (Ubuntu)**
```bash
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.11.0-amd64.deb
sudo dpkg -i filebeat-8.11.0-amd64.deb
```

### **Cấu hình output & module system**
`/etc/filebeat/filebeat.yml`
```yaml
output.elasticsearch:
  hosts: ["http://<SIEM_IP>:9200"]
  username: "elastic"
  password: "changeme"

setup.kibana:
  host: "http://<SIEM_IP>:5601"

filebeat.modules:
  - module: system
    syslog:
      enabled: true
    auth:
      enabled: true
```

```bash
sudo filebeat modules enable system
sudo filebeat setup
sudo systemctl enable --now filebeat
```

### **Tạo log bruteforce giả**
```bash
sudo apt install -y hydra
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://localhost -t 4
```
=> Sinh nhiều entry `sshd[xxx]: Failed password` trong `/var/log/auth.log`.

---

## 4. Thu thập log Windows với Winlogbeat

### **Cài đặt**
Tải `winlogbeat-8.11.0-windows-x86_64.zip`, giải nén `C:\Program Files\Winlogbeat`.

`winlogbeat.yml`
```yaml
output.elasticsearch:
  hosts: ["http://<SIEM_IP>:9200"]
  username: elastic
  password: changeme

winlogbeat.event_logs:
  - name: Security
  - name: Microsoft-Windows-Sysmon/Operational
```

Nếu chưa cài **Sysmon**, sử dụng config SwiftOnSecurity:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
Invoke-WebRequest https://download.sysinternals.com/files/Sysmon.zip -OutFile sysmon.zip
Expand-Archive sysmon.zip -DestinationPath .\sysmon
sysmon\Sysmon64.exe -accepteula -i sysmonconfig-export.xml
```

Chạy Winlogbeat service:
```powershell
.\install-service-winlogbeat.ps1
Start-Service winlogbeat
```

### **Sinh log process injection**
```powershell
Invoke-WebRequest https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1055/T1055.ps1 -OutFile atomics.ps1
.\atomics.ps1
# Chọn test T1055 - Process Injection (yêu cầu Sysmon)
```

---

## 5. Phân tích & Rule Detection

### **Kibana - Discover**
- Index pattern: `filebeat-*`, `winlogbeat-*`.
- Filter `event.dataset: system.auth` để xem SSH log.
- Filter `winlog.event_data.ImageLoaded: *ntdll.dll*` để tìm injection.

### **Saved Search: SSH Brute Force**
```
event.dataset:system.auth AND system.auth.ssh.event: Failed
```
Tạo visualization (Lens) hiển thị số lần failed theo IP. Nếu > 20 lần/5 phút → alert.

### **Detection Rule (Kibana Security)**
```
event.dataset: "system.auth" and system.auth.ssh.event: "Failed" and
event.module: "system" and event.action: "ssh_login" and 
event.outcome: "failure"
```
Action: gửi email/Slack khi `count() > 20` trong 5 phút.

### **Sysmon Process Injection Rule**
```
winlog.event_data.RuleName: "technique_id=T1055" OR winlog.event_data.ImageLoaded.keyword: "*\SysWow64\*"
```

---

## 6. Báo cáo & Hardening
- Xuất dashboard screenshot + mô tả nguồn log.
- Đề xuất chính sách: khóa tài khoản sau 5 lần thất bại, bật MFA SSH (e.g., Duo), EDR block injection.
- Thiết lập retention cho index (30 ngày) và snapshot backup.

---

> ✅ Kết thúc lab khi bạn có dashboard failed SSH + alert rule và phát hiện được event Sysmon injection.
