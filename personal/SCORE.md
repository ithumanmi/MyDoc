# Lifestyle score — rubric (/100)

> Config: [`config.yaml`](./config.yaml) · Script: `python scripts/personal_week_summary.py`  
> Điền weekly rồi chép điểm vào [`dashboard.md`](./dashboard.md).

## Components (mặc định)

| Component | Max | Cách tính |
| --- | ---: | --- |
| **Sleep** | 25 | Trung bình điểm ngày: giờ trong `[sleep_h_min, sleep_h_max]` + quality ≥ min → 1.0; lệch nhẹ → 0.5; không data → 0 |
| **Habits** | 25 | `%` ô habit trong tuần: `x`=1, `~`=0.5, `-`/空白 đã qua=0 |
| **Deep work** | 20 | `min(1, total_h / deep_work_h_week) × 20` (parse từ daily) |
| **Nutrition days** | 15 | `(số ngày có nutrition file) / 7 × 15` |
| **Metrics days** | 15 | `(số ngày CSV có sleep_h hoặc weight) / 7 × 15` |

**Tổng = Lifestyle score /100.**

## Bands

| Score | Label |
| ---: | --- |
| 85–100 | 🟢 Strong week |
| 70–84 | 🟡 Solid |
| 50–69 | 🟠 Needs focus |
| <50 | 🔴 Reset week |

## Loop

1. Mỗi tối: daily + CSV + habit tick + nutrition.  
2. Chủ nhật: `python scripts/personal_week_summary.py --week YYYY-Www`  
3. Dán output vào `weekly/YYYY/YYYY-Www.md` + cập nhật dashboard.  
4. Cuối tháng: copy [`templates/personal/monthly-review.md`](../templates/personal/monthly-review.md) → `monthly/YYYY-MM.md`.
