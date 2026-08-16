# Scripts — personal / work tracking

| Script | Việc |
| --- | --- |
| [`excel_tracking_style.py`](./excel_tracking_style.py) | Theme màu / zebra / conditional format dùng chung |
| [`create_tracking_templates.py`](./create_tracking_templates.py) | Excel Daily / Habits / Health / Nutrition → `tracking-YYYY-MM.xlsx` |
| [`create_work_tracking_templates.py`](./create_work_tracking_templates.py) | Excel trống dự án / OKR / timeline / productivity → `work-tracking-YYYY.xlsx` |
| [`import_farming_work_metrics.py`](./import_farming_work_metrics.py) | Đổ `Farming/Docs` WORK_METRICS (+ cột `story_id`/`priority`/`hours_actual`/`verify`/`deep_work`) + STATUS + epic + DAILY Metrics review → `work-tracking-farming-YYYY.xlsx` |

| [`../personal_week_summary.py`](../personal_week_summary.py) | Tóm tắt tuần + Lifestyle score từ `personal/` |

```powershell
pip install -r scripts/personal/requirements.txt
python scripts/personal/create_tracking_templates.py --month 2026-08
python scripts/personal/create_work_tracking_templates.py --year 2026
python scripts/personal/import_farming_work_metrics.py --year 2026
```
