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
├── README.md
├── SCORE.md               ← rubric Lifestyle /100
├── config.yaml            ← targets & weights
├── dashboard.md
├── daily/YYYY/YYYY-MM-DD.md
├── nutrition/YYYY/YYYY-MM-DD.md
├── body/metrics.csv
├── habits/
├── weekly/YYYY/YYYY-Www.md
└── monthly/YYYY-MM.md
```

## ⏱️ Routine gợi ý (10–15 phút/ngày)

| Khi | Làm gì | File |
| --- | --- | --- |
| Sáng (2′) | Goals + sleep từ đêm qua | `daily/…` + 1 dòng `body/metrics.csv` |
| Mỗi bữa (1′) | Ghi meal + ước lượng | `nutrition/…` |
| Tối (5–8′) | Energy, deep work, habits, mood | `daily/…` + `habits/YYYY-MM.md` |
| Chủ nhật (20′) | Week summary + score + dashboard | `python scripts/personal_week_summary.py --week YYYY-Www --write` |
| Cuối tháng (30′) | Monthly review | `monthly/YYYY-MM.md` |

## Lifestyle score

- Rubric: [`SCORE.md`](./SCORE.md)
- Targets: [`config.yaml`](./config.yaml)
- Dashboard: [`dashboard.md`](./dashboard.md)

```powershell
python scripts/personal_week_summary.py --week 2026-W32 --write
```

## ➕ Tạo ngày mới

```powershell
.\personal\new-day.ps1
# hoặc
.\personal\new-day.ps1 -Date 2026-08-08
```

## 🔗 Theory ↔ Data

| Muốn tối ưu | Đọc (guides) | Ghi (personal) |
| --- | --- | --- |
| Ngủ / HRV | [sleep-optimization](../guides/04-lifestyle-os/health/sleep-optimization.md) | `body/metrics.csv` |
| Glucose / ăn | [glucose-insulin](../guides/04-lifestyle-os/health/glucose-insulin-system.md) | `nutrition/` |
| **Toàn map hormone** | **[endocrine-hormone-map](../guides/04-lifestyle-os/health/endocrine-hormone-map.md)** | daily mood/energy + sleep + craving |
| Energy / deep work | [energy-management](../guides/04-lifestyle-os/life-os/energy-management.md) | `daily/` |
| Weekly reflection | [weekly-review template](../templates/personal/weekly-review-personal.md) | `weekly/` + score script |
| Monthly eval | [monthly-review](../templates/personal/monthly-review.md) | `monthly/` |

## Quy ước

- **Tên file ngày:** `YYYY-MM-DD.md` (ISO, sort được).
- **Số liệu body:** ưu tiên 1 dòng/ngày trong CSV (dễ chart sau bằng Sheets/Python).
- **Không nhét secrets** (password, OTP, địa chỉ chi tiết người khác) vào đây nếu repo từng public.
- **Thang điểm mặc định:** 1–10 trừ khi file ghi khác.

> **Last Updated:** August 2026
