---
title: "VN Law Map"
description: "Bản đồ ngành luật Việt Nam và chỗ tra cứu trong repo"
updated: "2026-08-14"
canonical: true
tags: [vn-law, map]
audience: [beginner, intermediate]
related:
  - README.md
  - catalog.yaml
  - legal-hierarchy.md
sensitivity: public
---

# Bản đồ Luật Việt Nam

> [← Hub](./README.md) · Database: [catalog.yaml](./catalog.yaml)

<!-- agent-summary -->
**Agent SUMMARY**
- Map ngành luật → id `branches` trong catalog → note nếu đã seed.
- Câu “luật nào chi phối X?” bắt đầu ở bảng dưới, rồi lọc `catalog.yaml` theo `branches`.
<!-- /agent-summary -->

## Ngành luật (filter catalog)

| Branch id | Ngành | Seed note / pointer |
| --- | --- | --- |
| `hien-phap` | Hiến pháp, tổ chức nhà nước | [notes/hien-phap-2013.md](./notes/hien-phap-2013.md) |
| `dan-su` | Dân sự, hợp đồng, sở hữu, bồi thường | [notes/bo-luat-dan-su-2015.md](./notes/bo-luat-dan-su-2015.md) |
| `hinh-su` | Hình sự, tội phạm, hình phạt | [notes/bo-luat-hinh-su-2015.md](./notes/bo-luat-hinh-su-2015.md) |
| `to-tung` | Tố tụng dân sự / hình sự / hành chính | catalog `bl-tt-*` |
| `lao-dong` | Lao động, BHXH, hợp đồng lao động | [notes/bo-luat-lao-dong-2019.md](./notes/bo-luat-lao-dong-2019.md) · thực hành [`legal/employment/`](../02-wealth-business/legal/employment/labor-contract.md) |
| `dat-dai` | Đất đai, nhà ở, kinh doanh BĐS | [notes/luat-dat-dai-2024.md](./notes/luat-dat-dai-2024.md) |
| `doanh-nghiep` | Doanh nghiệp, đầu tư | [notes/luat-doanh-nghiep-2020.md](./notes/luat-doanh-nghiep-2020.md) |
| `hon-nhan-gia-dinh` | Hôn nhân, gia đình, nuôi con | catalog `luat-hn-gd-2014` · thực hành [`marriage-family.md`](../02-wealth-business/legal/personal/marriage-family.md) |
| `hanh-chinh` | Xử lý VPHC, khiếu nại, tố cáo | catalog `luat-xlvphc-2012` |
| `thue` | Thuế (GTGT, TNDN, TNCN) — chỉ mục, không thay tư vấn thuế | thực hành [`tax-compliance.md`](../02-wealth-business/legal/business/tax-compliance.md) |
| `shtt` | Sở hữu trí tuệ | catalog `luat-shtt` · thực hành [`intellectual-property.md`](../02-wealth-business/legal/business/intellectual-property.md) |
| `so` | An ninh mạng, giao dịch điện tử, dữ liệu | catalog `luat-an-ninh-mang-2018`, `luat-giao-dich-dt-2023` |
| `moi-truong` | Bảo vệ môi trường | catalog `luat-bvmt-2020` |
| `giao-thong` | Trật tự ATGT, đường bộ | catalog `luat-ttatgt-2024`, `luat-duong-bo-2024` |
| `tieu-dung` | Bảo vệ người tiêu dùng | catalog `luat-nt-2023` |

## Câu hỏi → chỗ mở

```text
"Luật VN / catalog / số hiệu đạo luật?"
  → guides/06-vn-law/README.md → catalog.yaml

"Văn bản nào cao hơn / NĐ có được trái Luật?"
  → legal-hierarchy.md

"HĐLĐ / BHXH / NDA / thuế doanh nghiệp thực hành?"
  → guides/02-wealth-business/legal/

"Quốc hội làm luật thế nào / Tòa án / Viện kiểm sát?"
  → guides/04-lifestyle-os/politics/vietnam/
```
