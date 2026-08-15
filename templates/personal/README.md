# Personal entry templates

Blank forms. Copy vào `personal/` — đừng ghi data thật ở đây.

| Template | Dùng cho |
| --- | --- |
| [daily-entry.md](./daily-entry.md) | `personal/daily/YYYY/` |
| **[Giải thích từng phần daily](../../personal/daily/README.md)** | Đọc hiểu Meta / Scores / Deep work / Habits… |
| [nutrition-day.md](./nutrition-day.md) | `personal/nutrition/YYYY/` |
| [skincare-day.md](./skincare-day.md) | `personal/skincare/YYYY/` · link từ daily |
| [weekly-review-personal.md](./weekly-review-personal.md) | `personal/weekly/YYYY/` |
| [monthly-review.md](./monthly-review.md) | `personal/monthly/YYYY-MM.md` |
| [habit-month.md](./habit-month.md) | `personal/habits/YYYY-MM.md` |
| [learning-session.md](./learning-session.md) | Log 1 phiên Learning OS / Topic Attack |

Body metrics → append 1 dòng vào [`personal/body/metrics.csv`](../../personal/body/metrics.csv).

**Lifestyle score:** config [`personal/config.yaml`](../../personal/config.yaml) · rubric [`personal/SCORE.md`](../../personal/SCORE.md) · script:

```powershell
python scripts/personal_week_summary.py --week YYYY-Www --write
```

Related: [`../daily-log.md`](../daily-log.md), [`../well-being/daily-performance-tracker.md`](../well-being/daily-performance-tracker.md).
