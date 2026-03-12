# 🎯 MITRE ATT&CK Mapping cho Detection Engineer

> Hướng dẫn map detection/use case vào tactic/technique MITRE ATT&CK để tạo coverage matrix và report.

---

## 1. Vì sao cần mapping?
- Đo lường coverage: tactic nào mạnh/yếu.
- Giao tiếp với business/CISO (ngôn ngữ chuẩn).
- Ưu tiên roadmap detection theo threat model.

---

## 2. Quy trình mapping
1. **Xác định hành vi** (vd: Powershell download file).
2. **Tra MITRE**: tactic `Execution`, technique `T1059.001`.
3. **Gán tag** vào rule (Sigma, YARA, KQL dashboard).
4. **Ghi log coverage matrix** (Excel, ATT&CK Navigator).

---

## 3. Công cụ
- **ATT&CK Navigator**: layer, heatmap.
- **MITRE CTI CSV/ STIX**: import/upsert data.
- **OpenCTI / Vectr**: quản lý detection vs test case.

---

## 4. Ví dụ mapping
| Use Case | Rule | Tactic | Technique |
| --- | --- | --- | --- |
| PowerShell download suspicious | Sigma `powershell_download.yaml` | Execution | T1059.001 |
| LSASS dump | YARA `lsass_dump` | Credential Access | T1003 |
| Suspicious RDP lateral movement | KQL query | Lateral Movement | T1021.001 |

---

## 5. Reporting
- Xây dashboard `% coverage` theo tactic.
- Highlight detection gap (vd: thiếu Phishing T1566).
- Liên kết với red team/purple team plan.

---

## 6. Checklist
- [ ] Mỗi detection có tag tactic/technique.
- [ ] Coverage matrix cập nhật hàng quý.
- [ ] Mapping align với threat model thực tế.
- [ ] Gap có owner và timeline remediation.