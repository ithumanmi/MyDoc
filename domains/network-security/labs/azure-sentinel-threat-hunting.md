# ☁️ Lab: Microsoft Sentinel Threat Hunting

> Mục tiêu: kết nối Windows Security Event, Azure AD log vào Sentinel, viết KQL truy vấn phát hiện impossible travel và PowerShell download script.

---

## 1. Chuẩn bị
- Azure subscription (trial) + quyền tạo Log Analytics Workspace & Sentinel.
- Windows 10/11 máy thật hoặc VM để cài **Azure Monitor Agent (AMA)**.
- Quyền Global Reader trong Azure AD để xem sign-in log.

### **Tạo Log Analytics + Sentinel**
1. `Log Analytics Workspace` → chọn region (East Asia/Southeast Asia).
2. Vào workspace → `Microsoft Sentinel` → `+ Create` → attach workspace.

---

## 2. Kết nối dữ liệu

### **Windows Event Logs (via AMA)**
1. Tải `AzureMonitorAgentInstaller.exe`.
2. Cài bằng PowerShell:
```powershell
Start-Process AzureMonitorAgentInstaller.exe /quiet
```
3. Trong portal: `Azure Monitor` → `Data Collection Rules` → `Create` → chọn workspace + resource (máy Windows).
4. Chọn **Windows Security Events** (Common schema) + System logs.

### **Azure AD Sign-in Logs**
- Trong Sentinel → `Content Hub` → cài `Azure AD` connector.
- Enable log forwarding (Sign-in, Audit) vào workspace.

---

## 3. KQL Queries

### **SSH/PowerShell Download Detection**
```kql
SecurityEvent
| where EventID == 4104 // PowerShell script block
| where ScriptBlockText has_any ("Invoke-WebRequest", "iwr", "curl")
| project TimeGenerated, Computer, Account, ScriptBlockText
```

### **Impossible Travel (Azure AD)**
```kql
SigninLogs
| where ResultType == 0
| extend IsoTime = TimeGenerated, User = UserPrincipalName, IP = IPAddress
| project IsoTime, User, IP, Location
| make-series count() on IsoTime step 1h by User, Location
| evaluate pivottable(User, Location, count_)
```
Hoặc dùng built-in analytic rule template `Impossible travel activity`.

### **Suspicious Service Creation**
```kql
SecurityEvent
| where EventID == 7045
| project TimeGenerated, ServiceName, ServiceFileName, Account
| where ServiceFileName contains "AppData"
```

---

## 4. Analytics Rule & Automation
1. `Analytics` → `+ Create` → Scheduled query rule.
2. Query: PowerShell download detection, schedule every 5 minutes.
3. Actions: gửi email/Azure DevOps ticket.
4. Có thể tạo `Logic App` chạy khi alert để disable user hoặc reset password.

---

## 5. Workbook Dashboard
- Dùng template `Security Operations Efficiency` hoặc tự tạo workbook:
  - Chart sign-in theo location.
  - Table top PowerShell commands.
- Pin workbook vào Sentinel overview.

---

## 6. Báo cáo & Cleanup
- Xuất report: screenshot analytic rule, query, incident detail.
- Delete workspace để tránh tốn phí (nhớ export log nếu cần).

> ✅ Hoàn thành khi bạn có ít nhất 1 analytic rule chạy, 1 workbook hiển thị sign-in + alert, và sự kiện test (PowerShell) tạo incident trong Sentinel.
