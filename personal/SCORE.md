# Lifestyle score — rubric (/100)

> Config: [`config.yaml`](./config.yaml) · Script: `python scripts/personal_week_summary.py`  
> Điền weekly rồi chép điểm vào [`dashboard.md`](./dashboard.md).  
> Daily guide: [`daily/README.md`](./daily/README.md)

## Components (health-leaning v2)

| Component | Max | Cách tính |
| --- | ---: | --- |
| **Sleep** | 25 | Trung bình điểm ngày: giờ trong `[sleep_h_min, sleep_h_max]` + quality ≥ min → 1.0; lệch nhẹ → 0.5; không data → 0; rồi `× 25` trên 7 ngày |
| **Habits** | 20 | `%` ô habit: `x`=1, `~`=0.5, `-`=0 |
| **Workouts** | 15 | `min(1, workouts / workouts_week) × 15` — đếm dòng CSV có `training` non-empty trong tuần |
| **Deep work** | 15 | `min(1, total_h / deep_work_h_week) × 15` (parse daily) |
| **Nutrition days** | 15 | `(số ngày có nutrition file) / 7 × 15` |
| **Metrics days** | 10 | `(số ngày CSV có sleep_h hoặc weight) / 7 × 10` |

**Tổng = Lifestyle score /100.**

### Có / chưa trong score

| Đã đo trong `/100` | Theo dõi daily, **chưa** auto-score |
| --- | --- |
| Sleep, habits, workouts, deep work, nutrition files, metrics rows | Anxiety, Recovery, Social, Soreness, Mood/Stress raw |

Mind scores đọc ở weekly review thủ công (v1 tránh overfit).

## Bands

| Score | Label |
| ---: | --- |
| 85–100 | 🟢 Strong week |
| 70–84 | 🟡 Solid |
| 50–69 | 🟠 Needs focus |
| <50 | 🔴 Reset week |

## Loop

1. Mỗi tối: daily (kể cả **mind scores**) + CSV (`training` nếu tập) + habit + nutrition.  
2. Chủ nhật: `python scripts/personal_week_summary.py --week YYYY-Www --write`  
3. Dán output vào `weekly/YYYY/YYYY-Www.md` + dashboard; **đọc thêm** Anxiety/Recovery/Social trend.  
4. Cuối tháng: [`templates/personal/monthly-review.md`](../templates/personal/monthly-review.md) → `monthly/YYYY-MM.md`.
