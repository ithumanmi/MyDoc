# 🧩 Sigma Rules Intro: Từ log thành detection đa nền tảng

> Mục tiêu: hiểu cấu trúc Sigma, cách viết rule chuẩn hóa log, convert sang SIEM (Elastic, Splunk, Sentinel).

---

## 1. Sigma là gì?
- Framework viết detection ở dạng YAML trung lập.
- Dùng converter (`sigmac`, `sigma-cli`) để xuất thành KQL, SPL, Lucene...
- Giúp share rule giữa team mà không phụ thuộc SIEM vendor.

---

## 2. Cấu trúc rule
```yaml
title: Suspicious PowerShell Download
id: 3b8f...
status: experimental
logsource:
  product: windows
  service: powershell
detection:
  selection:
    ScriptBlockText|contains: "Invoke-WebRequest"
    ScriptBlockText|contains: "http"
  condition: selection
level: high
tags:
  - attack.t1059.001
```

### Thành phần chính
- `logsource`: xác định loại log.
- `detection`: selection + condition (logic AND/OR).
- `level`: thông điệp severity.
- `tags`: mapping MITRE, compliance.

---

## 3. Workflow viết rule
1. **Thu thập log sample** (Windows Event, Sysmon, Zeek...).
2. **Xác định indicator** (command, registry path, TTP).
3. **Viết YAML** với selection rõ ràng, tránh false positive.
4. **Test bằng sigma-cli**: `sigma-cli validate rule.yml`.
5. **Convert**: `sigma-cli convert -t azure_sentinel rule.yml`.
6. **Triển khai** vào SIEM, theo dõi alert.

---

## 4. Tips giảm false positive
- Thêm `filter` block để loại hành vi hợp lệ.
- Sử dụng `1 of selection_*` cho nhiều indicator.
- Dùng wildcard/regex khi log format khác nhau.

```yaml
detection:
  selection_1:
    CommandLine|contains:
      - "certutil"
      - "-urlcache"
  selection_2:
    CommandLine|contains: "http"
  condition: selection_1 and selection_2
```

---

## 5. Tooling
- [sigmahq/sigma-cli](https://github.com/SigmaHQ/sigma-cli)
- VSCode extension "Sigma" + schema autocompletion.
- CI pipeline: validate rule trước khi merge.

---

## 6. Checklist
- [ ] Rule có `id` unique (UUID).
- [ ] Gắn tag MITRE & product.
- [ ] Có filter loại noise.
- [ ] Tested với log sample.
- [ ] Convertable sang SIEM target.