# 🧠 Advanced Detection Use Cases

> Tập hợp kịch bản hunting nâng cao cho SIEM/SOAR (Elastic, Splunk, Sentinel, Chronicle, QRadar). Mục tiêu: đa tầng phát hiện, kết hợp log hệ điều hành, network, cloud và identity.

---

## 1. Lateral Movement via Remote Service Creation + SMB

### **Ý tưởng**
- Correlate EventID 7045 (Service creation) + SMB session (network logs) từ cùng IP.

### **Elastic Query**
```kql
event.category: driver AND winlog.event_id:7045
| join [
  event.dataset: network AND network.transport: tcp AND destination.port:445
  | stats count by source.ip, host.name
]
on source.ip
```

### **Splunk SPL**
```spl
search index=winlog EventCode=7045
| stats values(Service_File_Name) by dest, user
| join dest [ search index=netflow dest_port=445 | stats count by dest, src ]
```

Alert khi service tạo xong và có SMB session > 3 trong 5 phút.

---

## 2. Golden Ticket / Kerberos Abuse

### **Detection logic**
- Event 4769 với encryption type 0x17 (RC4) cho account high privilege.
- Hoặc ticket lifetime bất thường.

```kql
SecurityEvent
| where EventID == 4769 and TicketEncryptionType == "0x17"
| where Account contains "$" == false // loại trừ computer accounts
```

Trong Splunk: `source=WinEventLog:Security EventCode=4769 Ticket_Encryption_Type=0x17`.

---

## 3. Cloud Impossible Token + Suspicious OAuth App

### **Sentinel KQL**
```kql
SigninLogs
| where ResultType == 0
| summarize min(TimeGenerated), max(TimeGenerated), dcount(Location) by UserPrincipalName
| where dcount_Location > 2 and max_TimeGenerated - min_TimeGenerated < 1h

AuditLogs
| where OperationName == "Add service principal"
| summarize by InitiatedBy.user.userPrincipalName, TargetResources
```
Cross-check user trùng nhau → alert.

---

## 4. DNS Beacon + JA3 Fingerprint

### **Chronicle**
```sql
FETCH threat FROM dns_lookup
  WHERE udf.length(target.domain) > 45 AND target.domain matches "(.*)\.cloudfront\.net"
  WINDOW 10 MINUTES
  GROUP BY src.ip, target.domain

FETCH threat FROM network_connection
  WHERE metadata.product_name = "zeek" AND network.tls.ja3 = "72a589da586844d7f0818ce684948eea"
```
Join 2 kết quả theo src.ip.

### **Elastic**
```kql
fields.ja3: "72a589da586844d7f0818ce684948eea"
```

---

## 5. Suspicious PowerShell Over WebProxy

### **QRadar CRE**
- Condition: log source = `Web Proxy` AND URL contains `Invoke-WebRequest`.
- Co-occurrence: same source IP has Windows Event ID 4104 within 2 minutes.

Implementation: Use AQL rule referencing Event ID 4104.

---

## 6. Container Escape Attempt

### **Elastic**
```kql
event.module: auditd and auditd.data.syscall: "setns"
| where process.args: ("/proc/1/ns/mnt")
```

### **Splunk**
`index=auditd syscall=setns command="*nsenter*"`.

Alert + trigger SOAR playbook (pause container, snapshot).

---

## 7. Ransomware Kill Chain
- Volume shadow copy deletion (Event 524) + high file encryption I/O + ransom note drop.
- Use EDR log (SentinelOne, CrowdStrike) + Windows events.

### **Elastic Detection**
```kql
event.code: VSSADMIN_DELETE_SHADOW_COPY AND 
process.command_line: "*delete shadows*"
```
Combine with filebeat module `filebeat-*` path matches `*\README_RECOVER_FILES.txt`.

---

> Tip: Tạo bảng mapping giữa use case ↔ SIEM có thể triển khai. Lưu queries thành templates để tái dùng.
