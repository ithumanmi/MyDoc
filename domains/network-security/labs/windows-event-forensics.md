# 📕 Lab: Windows Event Forensics & Event ID Hunting

> Mục tiêu: phân tích Windows Security Event Log (4624, 4625, 4672, 4688, 7045...), xây dựng kỹ năng hunting với PowerShell/Log Parser và lập báo cáo timeline sự cố.

---

## 1. Chuẩn bị môi trường

| Thành phần | Mô tả |
| --- | --- |
| Windows 10/11 hoặc Server | Dùng để sinh log |
| Sysmon (khuyến nghị) | Bổ sung chi tiết process |
| Tools | Event Viewer, PowerShell, Log Parser, Chainsaw |

### 1.1 Enable Audit Policy
```powershell
AuditPol /set /category:"Logon" /success:enable /failure:enable
AuditPol /set /category:"Account Logon" /success:enable /failure:enable
```

### 1.2 Cài Sysmon (optional)
```powershell
.
\Sysmon64.exe -accepteula -i sysmonconfig-export.xml
```

---

## 2. Sinh dữ liệu

| Hoạt động | Event ID | Cách thực hiện |
| --- | --- | --- |
| Successful logon | 4624 | Đăng nhập bằng user domain/local |
| Failed logon | 4625 | Nhập sai password nhiều lần |
| Privileged logon | 4672 | Đăng nhập user thuộc Administrators |
| Process creation | 4688 | Chạy `powershell.exe -enc ...` |
| Service creation | 7045 | `sc.exe create backdoor binPath= "cmd /c net user"` |

---

## 3. Phân tích log bằng PowerShell

### 3.1 Export log
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624} -MaxEvents 1000 | Export-Csv logon.csv
```

### 3.2 Query example
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} |
  Where-Object { $_.Properties[19].Value -eq "%%2313" } |
  Select-Object TimeCreated, @{n='Account';e={$_.Properties[5].Value}}, @{n='IP';e={$_.Properties[18].Value}}
```

### 3.3 Chainsaw (optional)
```powershell
chainsaw hunt Security.evtx --rules sigma/rules/windows
```

---

## 4. Detection Playbook

| Use case | Event ID | Logic |
| --- | --- | --- |
| Brute-force | 4625 | Count thất bại > 10/5 phút theo IP |
| Pass-the-hash | 4624 LogonType=9 + 4672 | Logon từ account admin, source IP nghi ngờ |
| Persistence Service | 7045 + 4688 | Service tạo xong chạy script đáng nghi |
| LOLBin Execution | 4688 | Command line chứa `certutil`, `mshta`, `powershell -enc` |

Tạo script PowerShell/Splunk query tương ứng.

---

## 5. Báo cáo Timeline

1. Sử dụng `Get-WinEvent` hoặc `LogParser` để xuất sự kiện theo thời gian.
2. Tạo bảng:

| Time | Event ID | Account | Detail |
| --- | --- | --- | --- |
| 10:01 | 4625 | user1 | Failed logon từ 10.0.0.5 |
| 10:02 | 4625 | user1 | Repeated failure |
| 10:03 | 4624 | user1 | Success từ IP khác |
| 10:04 | 4672 | user1 | Admin privileges assigned |
| 10:05 | 4688 | user1 | powershell.exe -enc ... |

3. Viết kết luận + đề xuất khoá account, reset password, bật MFA.

---

## 6. Automation
- Export log → SIEM (Splunk/Elastic) theo định kỳ.
- Dùng PowerShell Scheduled Task gửi email khi 4672 xuất hiện ngoài giờ.
- Mapping MITRE: `T1110`, `T1078`, `T1543`, `T1059`.

> ✅ Hoàn thành khi bạn tạo được timeline sự cố với ít nhất 3 event loại khác nhau và đề xuất khắc phục.