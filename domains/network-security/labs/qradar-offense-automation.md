# 🤖 Lab: QRadar Offense Automation

> Mục tiêu: sử dụng QRadar API (Ariel, REST) + app integrations để tự động tạo ticket, block IP, và đồng bộ status khi offense được xử lý.

---

## 1. Prerequisites
- QRadar 7.4+ với quyền admin.
- API token (`Admin > User Management > Authorized Services`).
- SIEM server có thể chạy Python/Ansible.

### **API Token**
- Create Authorized Service → chọn role Admin, ghi nhớ token.
- REST endpoint: `https://<qradar_ip>/api/`.

---

## 2. Fetch Offenses via REST

```bash
curl -k -H "SEC: <TOKEN>" \
  "https://qradar/api/siem/offenses?filter=status='OPEN'&fields=id,description,source_ips"
```

### **Python Script**
```python
import requests

BASE = "https://qradar/api"
TOKEN = "YOUR_TOKEN"

resp = requests.get(
    f"{BASE}/siem/offenses",
    headers={"SEC": TOKEN}, verify=False,
    params={"filter": "status='OPEN'", "fields": "id,source_ips"}
)
offenses = resp.json()
for o in offenses:
    print(o["id"], o["source_ips"])
```

---

## 3. Automate Response (Blocking IP)

### **Integration Options**
1. **QRadar Network Hierarchy → Reference Set**
   - Create reference set `Blocked_IPs`.
   - API call to add IP.
```bash
curl -k -H "SEC: <TOKEN>" -H "Content-Type: application/json" \
  -X POST "https://qradar/api/reference_data/sets/Blocked_IPs" \
  -d '{"value": "203.0.113.5"}'
```
   - Firewall automation đọc reference set để block.

2. **AQL Query + Script**
   - Query offense detail: `SELECT sourceip FROM events WHERE INOFFENSE(12345)`.

### **Playbook Example (Python)**
```python
import requests

def block_ip(ip):
    requests.post(
        f"{BASE}/reference_data/sets/Blocked_IPs",
        headers={"SEC": TOKEN}, verify=False,
        json={"value": ip}
    )

for offense in offenses:
    for ip in offense["source_ips"]:
        block_ip(ip)
        requests.post(
            f"{BASE}/siem/offenses/{offense['id']}",
            headers={"SEC": TOKEN}, verify=False,
            json={"status": "CLOSED", "closing_user": "Automation"}
        )
```

---

## 4. Ticketing Integration

### **ServiceNow**
- Use QRadar connector or custom script:
```python
sn_resp = requests.post(
    "https://instance.service-now.com/api/now/table/incident",
    auth=("user", "pass"),
    json={
        "short_description": f"QRadar Offense {offense['id']}",
        "description": offense['description']
    }
)
ticket = sn_resp.json()["result"]["number"]
requests.post(f"{BASE}/siem/offenses/{offense['id']}", json={"closing_reason_id": 1, "closing_user": ticket}, headers={"SEC": TOKEN}, verify=False)
```

### **JIRA**
- Use webhooks or JIRA REST API to create issue, store issue key in offense notes.

---

## 5. Automation Platforms
- **QRadar SOAR (ex-Resilient)**: build workflow to call API block IP, update offense.
- **Ansible**: playbook run `uri` module to call QRadar + firewall.
- **IBM Cloud Pak for Security**: orchestrate multi-step response.

### QRadar SOAR Workflow Example
1. In SOAR (Resilient) create new rule `When incident created from QRadar`.
2. Playbook steps:
   - **Function:** Fetch offense detail via QRadar app (inputs: offense_id).
   - **Decision:** If severity > 7 → call firewall block (e.g., Palo Alto integration).
   - **Action:** Update QRadar offense status to Closed + attach SOAR incident link.

```python
# Pseudocode function in SOAR
inputs.qradar_offense_id = artifact.value
client = resilient_lib.AppFunctionComponent(QRADAR_APP)
offense = client.get_offense(inputs.qradar_offense_id)
if offense['severity'] > 7:
    firewall.block(offense['source_ip'])
    client.close_offense(offense['id'], note='Blocked via SOAR')
```

3. Optional: Create ticket in ServiceNow via SOAR integration, keep status synced.

---

## 6. Testing
1. Trigger offense (e.g., run `sc.exe` lateral movement lab).
2. Run automation script.
3. Verify IP added to reference set / firewall blocked.
4. Check offense status closed with note.

---

> ✅ Hoàn thành khi script/automation có thể đọc offense mở, block IP hoặc tạo ticket, và cập nhật status offense tự động.
