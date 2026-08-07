---
title: "Personal Life Data"
description: "Private life records: daily, nutrition, body, habits, weekly — not curriculum"
updated: "2026-08-07"
canonical: true
tags: [personal, life-data, hub]
audience: [beginner, intermediate, advanced]
related:
  - dashboard.md
  - ../templates/personal/README.md
  - ../guides/04-lifestyle-os/README.md
  - ../guides/04-lifestyle-os/health/README.md
sensitivity: private
---

# 🧬 Personal Life Data

> **Đây là lớp dữ liệu cá nhân** — khác với `domains/` / `guides/` (library kiến thức).
>
> [← Home](../README.md) | [Lifestyle OS](../guides/04-lifestyle-os/README.md) | [Health theory](../guides/04-lifestyle-os/health/README.md) | [Templates](../templates/personal/)

Repo này vừa là **knowledge library**, vừa là **personal OS data store** của bạn.

| Layer | Folder | Commit? |
| --- | --- | --- |
| Knowledge (dạy / học) | `domains/`, `guides/`, `chapters/`… | Yes |
| **Health / hormone theory** | [`guides/04-lifestyle-os/health/`](../guides/04-lifestyle-os/health/README.md) | Yes |
| **Records (đời sống thật)** | `personal/` | Yes (bạn chọn commit hết) |
| Blank forms | `templates/personal/` | Yes |

**Không ghi protocol dài vào `personal/`** — link sang `health/` rồi chỉ log số liệu/ngày.

**Học kiến thức mới?** Dùng [Learning OS Framework](../guides/03-career-skills/productivity/meta-skills/learning-os-framework.md) + template [`templates/personal/learning-session.md`](../templates/personal/learning-session.md); ghi deep work vào `daily/`.

## 📂 Cấu trúc

```
personal/
├── README.md              ← bạn đang ở đây
├── dashboard.md           ← nhìn nhanh tuần/tháng
├── daily/YYYY/YYYY-MM-DD.md
├── nutrition/YYYY/YYYY-MM-DD.md
├── body/metrics.csv       ← trọng số, ngủ, steps…
├── habits/
│   ├── definitions.md     ← danh sách habit + vì sao
│   └── YYYY-MM.md         ← grid tháng
└── weekly/YYYY/YYYY-Www.md
```

## ⏱️ Routine gợi ý (10–15 phút/ngày)

| Khi | Làm gì | File |
| --- | --- | --- |
| Sáng (2′) | Goals + sleep từ đêm qua | `daily/…` + 1 dòng `body/metrics.csv` |
| Mỗi bữa (1′) | Ghi meal + ước lượng | `nutrition/…` |
| Tối (5–8′) | Energy, deep work, habits, mood | `daily/…` + `habits/YYYY-MM.md` |
| Chủ nhật (20′) | Weekly review từ data tuần | `weekly/…` + cập nhật `dashboard.md` |

## ➕ Tạo ngày mới

```powershell
# từ root repo
$d = Get-Date -Format 'yyyy-MM-dd'
$y = Get-Date -Format 'yyyy'
Copy-Item templates/personal/daily-entry.md "personal/daily/$y/$d.md"
Copy-Item templates/personal/nutrition-day.md "personal/nutrition/$y/$d.md"
# mở file và sửa tiêu đề ngày
```

Hoặc duplicate file hôm qua rồi xóa nội dung cụ thể.

## 🔗 Theory ↔ Data

| Muốn tối ưu | Đọc (guides) | Ghi (personal) |
| --- | --- | --- |
| Ngủ / HRV | [sleep-optimization](../guides/04-lifestyle-os/health/sleep-optimization.md) | `body/metrics.csv` |
| Glucose / ăn | [glucose-insulin](../guides/04-lifestyle-os/health/glucose-insulin-system.md) | `nutrition/` |
| **Toàn map hormone** | **[endocrine-hormone-map](../guides/04-lifestyle-os/health/endocrine-hormone-map.md)** | daily mood/energy + sleep + craving |
| Energy / deep work | [energy-management](../guides/04-lifestyle-os/life-os/energy-management.md) | `daily/` |
| Weekly reflection | [weekly-review template](../templates/weekly-review.md) | `weekly/` |

## Quy ước

- **Tên file ngày:** `YYYY-MM-DD.md` (ISO, sort được).
- **Số liệu body:** ưu tiên 1 dòng/ngày trong CSV (dễ chart sau bằng Sheets/Python).
- **Không nhét secrets** (password, OTP, địa chỉ chi tiết người khác) vào đây nếu repo từng public.
- **Thang điểm mặc định:** 1–10 trừ khi file ghi khác.

> **Last Updated:** August 2026
