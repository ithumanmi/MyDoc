# Scripts — personal / work tracking

| Script | Việc |
| --- | --- |
| [`create_tracking_templates.py`](./create_tracking_templates.py) | Excel Daily / Habits / Health / Nutrition → `data/personal/tracking-YYYY-MM.xlsx` |
| [`create_work_tracking_templates.py`](./create_work_tracking_templates.py) | Excel dự án / OKR / timeline / productivity ngày→năm → `work-tracking-YYYY.xlsx` |
| [`../personal_week_summary.py`](../personal_week_summary.py) | Tóm tắt tuần + Lifestyle score từ `personal/` |

```powershell
pip install -r scripts/personal/requirements.txt
python scripts/personal/create_tracking_templates.py --month 2026-08
python scripts/personal/create_work_tracking_templates.py --year 2026
```
