# Personal life & work tracking (Excel)

> Excel trống để ghi nhanh. Markdown trong [`personal/`](../../personal/README.md) vẫn là nguồn Lifestyle score.

| Script | Output |
| --- | --- |
| [`create_tracking_templates.py`](../../scripts/personal/create_tracking_templates.py) | `tracking-YYYY-MM.xlsx` — Daily / Habits / Health / Nutrition |
| [`create_work_tracking_templates.py`](../../scripts/personal/create_work_tracking_templates.py) | `work-tracking-YYYY.xlsx` — Dự án / Mục tiêu / Timeline / Productivity |

## Health & habit (theo tháng)

```powershell
python scripts/personal/create_tracking_templates.py --month 2026-08
```

| Sheet | Nội dung |
| --- | --- |
| **Cot_y_nghia** | Tra cứu ý nghĩa cột (tiếng Việt) |
| Daily_* / Habits / Health / Nutrition | Theo dõi đời sống ngày |

## Dự án · mục tiêu · productivity (theo năm)

```powershell
python scripts/personal/create_work_tracking_templates.py --year 2026
```

| Sheet | Nội dung |
| --- | --- |
| **Cot_y_nghia** | Giải thích mọi cột |
| Projects | Danh sách dự án + next action |
| Goals | Mục tiêu / Objective (năm · quý · tháng) |
| Key_Results | KR đo được gắn Goal_ID |
| Timeline | Mốc / deliverable |
| Prod_Daily | Năng suất từng ngày trong năm |
| Prod_Weekly | Review từng tuần |
| Prod_Monthly | Review 12 tháng |
| Prod_Quarterly | Review 4 quý |
| Prod_Yearly | Review năm |

Trên mỗi sheet data: **dòng 1** = tên cột · **dòng 2 (vàng)** = giải thích · hover tên cột = chú thích.

File `.xlsx` gitignore. Chỉ commit README này.

## Liên kết template

- [`templates/personal/daily-entry.md`](../../templates/personal/daily-entry.md)
- [`templates/okr-planning.md`](../../templates/okr-planning.md)
- [`templates/weekly-review.md`](../../templates/weekly-review.md)
- [`templates/productivity/monthly-review-template.md`](../../templates/productivity/monthly-review-template.md)

```powershell
python scripts/personal_week_summary.py --week YYYY-Www --write
```
