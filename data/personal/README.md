# Personal life & work tracking (Excel)

> Excel trống để ghi nhanh. Markdown trong [`personal/`](../../personal/README.md) vẫn là nguồn Lifestyle score.

| Script | Output |
| --- | --- |
| [`create_tracking_templates.py`](../../scripts/personal/create_tracking_templates.py) | `tracking-YYYY-MM.xlsx` — Daily / Habits / Health / Nutrition |
| [`create_work_tracking_templates.py`](../../scripts/personal/create_work_tracking_templates.py) | `work-tracking-YYYY.xlsx` — Dự án / Mục tiêu / Timeline / Productivity (trống) |
| [`import_farming_work_metrics.py`](../../scripts/personal/import_farming_work_metrics.py) | `work-tracking-farming-YYYY.xlsx` — đổ từ `Farming/Docs` (WORK_METRICS, STATUS, epic) |

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

Workbook trống. Để **đổ data từ game Farming**:

```powershell
python scripts/personal/import_farming_work_metrics.py --year 2026
# mặc định đọc C:\Projects\Game\Games\Farming\Docs
```

| Sheet (farming import) | Nguồn |
| --- | --- |
| Metrics_Log | `WORK_METRICS.md` (1 hàng = 1 cụm; gồm `story_id` · `priority` · `hours_actual` · `verify` · `deep_work`) |
| Prod_Daily…Yearly | Roll-up metrics (`est_hours` = `hours_actual` nếu có, không thì map effort S/M/L/XL) |
| Projects | `STATUS.md` systems + `P-farming` |
| Timeline | Epic Sequence stories + `BACKLOG.md` Open |
| Perf_Weekly…Yearly | Snapshot metrics + block `### Metrics review` từ `DAILY.md` (nếu có); còn trống điền tay |
| Perf_Rubric | Rubric thang 1–10 |

Narrative chi tiết vẫn đọc `DAILY.md` trong Docs game — Excel không thay nhật ký.

Trên mỗi sheet data: **dòng 1** = tên cột · **dòng 2 (vàng)** = giải thích · hover tên cột = chú thích.

**Format màu** (tự áp khi generate/import qua `excel_tracking_style.py`):
- Tab sheet theo nhóm (Daily teal · Habits tím · Health xanh · Metrics indigo…)
- Hàng data zebra; tắt gridlines
- Status / Priority / effort / type / outcome / habit `x~-` tô màu (+ conditional format khi chọn dropdown)
- Điểm 1–10: thấp đỏ → cao xanh
- **Wrap text**: chữ dài xuống dòng trong ô, cột text dài ≤ ~22 ký tự rộng — không tràn ô cạnh

File `.xlsx` gitignore. Chỉ commit README này.

## Liên kết template

- [`templates/personal/daily-entry.md`](../../templates/personal/daily-entry.md)
- [`templates/okr-planning.md`](../../templates/okr-planning.md)
- [`templates/weekly-review.md`](../../templates/weekly-review.md)
- [`templates/productivity/monthly-review-template.md`](../../templates/productivity/monthly-review-template.md)

```powershell
python scripts/personal_week_summary.py --week YYYY-Www --write
```
