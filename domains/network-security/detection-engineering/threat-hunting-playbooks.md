# 🕵️ Threat Hunting Playbooks

> Bộ playbook theo use case: pre-requisites, query mẫu, hành động tiếp theo.

---

## 1. Principles
- Hypothesis-driven: bắt đầu bằng câu hỏi (vd: "Có beacon HTTP bất thường không?").
- Data-first: xác nhận log có đủ sự kiện (EDR, Netflow, DNS...).
- Document loop: ghi lại kết quả, cập nhật detection/sigma rule.

---

## 2. Playbook mẫu

### 2.1 Suspicious PowerShell (Execution)
- **Data:** Windows Event 4104, Sysmon 1.
- **Query:**
```spl
index=win EventCode=4104 ScriptBlockText="Invoke-WebRequest" OR "IEX"
```
- **Steps:**
  1. Lọc user/service account bất thường.
  2. Kiểm tra network connection cùng thời gian.
  3. Nếu malicious -> enrich MITRE T1059.001, tạo detection rule.

### 2.2 Beaconing HTTP (C2)
- **Data:** Proxy/Zeek.
- **Query (Elastic):**
```kql
url.domain : "*.cloudfront.net" and http.response.status_code: 200
```
- **Steps:**
  1. Tính interval giữa request (StdDev thấp → beacon).
  2. Check JA3/JA3S fingerprint.
  3. Kết hợp DNS log để xác nhận domain mới đăng ký.

### 2.3 Lateral Movement via RDP
- **Data:** Windows Security 4624/4625, Sysmon 3.
- **Query (KQL):**
```kql
SecurityEvent
| where EventID == 4624 and LogonType == 10
| summarize count() by Account, Computer
| where count_ > 5
```
- **Steps:**
  1. Phát hiện account đăng nhập nhiều host trong thời gian ngắn.
  2. So sánh với asset inventory (admin hợp lệ?).
  3. Nếu bất thường -> isolate host, dump memory.

---

## 3. Template playbook
- Hypothesis:
- Data sources:
- Queries:
- Findings:
- Recommended detection/Sigma:

Lưu vào knowledge base, đo trạng thái (Open/Closed).

---

## 4. Checklist
- [ ] Có playbook cho tactic chính (Execution, Persistence, C2, Exfiltration).
- [ ] Log source validated trước khi hunt.
- [ ] Kết quả hunt được convert thành detection hoặc gap ticket.
- [ ] Share kết quả với SOC/IR team.