# 📙 Lab: ELK Stack Detection với Sigma Rules

> Mục tiêu: dựng Elastic Stack (Elasticsearch + Logstash + Kibana), ingest log hệ điều hành và áp dụng Sigma rule để tạo detection rule tự động.

---

## 1. Kiến trúc

| Component | Vai trò |
| --- | --- |
| Elasticsearch/Kibana | Lưu trữ + visualize log |
| Logstash + Beats | Thu thập log Linux/Windows |
| Sigma CLI | Convert rule → KQL/ES Query |

### 1.1 Docker Compose mẫu
`docker-compose.yml`
```yaml
version: "3"
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - ELASTIC_PASSWORD=changeme
    ports: ["9200:9200"]
  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    environment:
      - ELASTICSEARCH_HOSTS=https://elasticsearch:9200
      - ELASTICSEARCH_USERNAME=elastic
      - ELASTICSEARCH_PASSWORD=changeme
    ports: ["5601:5601"]
```

```bash
docker compose up -d
```

---

## 2. Thu thập log

### 2.1 Filebeat (Linux)
```bash
sudo filebeat modules enable system
sudo filebeat setup -E output.elasticsearch.hosts=['https://localhost:9200'] \
  -E output.elasticsearch.username=elastic -E output.elasticsearch.password=changeme \
  -E setup.kibana.host=https://localhost:5601
sudo systemctl start filebeat
```

### 2.2 Winlogbeat (Windows)
- Thu thập Event ID Security + Sysmon.
- Khuyến khích cài Sysmon config SwiftOnSecurity.

---

## 3. Áp dụng Sigma Rules

### 3.1 Install Sigma CLI
```bash
git clone https://github.com/SigmaHQ/sigma.git
python3 -m venv venv && source venv/bin/activate
pip install -r sigma/tools/requirements.txt
```

### 3.2 Convert rule → KQL
```bash
sigma/tools/sigmac -t es-qs -c sigma/tools/config/elk-windows.yml \
  -r rules/windows/process_creation/win_susp_powershell_download.yml > powershell.kql
```

### 3.3 Import vào Kibana Detection
- Security → Rules → Create → Query.
- Dán KQL từ file `powershell.kql`.

---

## 4. Rule Labs

| Rule | Log source | Trigger |
| --- | --- | --- |
| `win_susp_powershell_download` | Sysmon Event ID 1/4104 | `powershell -enc`, `Invoke-WebRequest` |
| `proc_creation_win_susp_cmd_web_request` | Sysmon | `cmd /c bitsadmin` |
| `linux_susp_netcat_reverse_shell` | Filebeat system module | `nc -e /bin/bash` |

Sinh log thử: chạy scripts từ Atomic Red Team hoặc tạo netcat reverse shell.

---

## 5. Alerting & Dashboard
- Dùng Kibana Detection engine tạo rule (Schedule 5 phút).
- Kích hoạt action: email, Slack webhook.
- Dashboard: Lens hiển thị số rule trigger theo ngày, pie chart top host.

---

## 6. Automation idea
- Dùng Fleet/Elastic Agent để scale.
- Implement `sigma-cli` trong CI/CD, convert rule batch → push via Kibana API.
- Map rule ↔ MITRE ATT&CK trong dashboard để tracking coverage.

> ✅ Hoàn thành lab khi deploy được ít nhất 2 Sigma rule và nhận alert trong Kibana.