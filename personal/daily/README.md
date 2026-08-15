---
title: "Daily entry — giải thích từng phần"
description: "Meta, Scores state/mind, Deep work, Body, Nutrition, Skincare, Habits, SCORE mapping."
updated: "2026-08-14"
canonical: true
tags: [personal, daily, guide]
audience: [beginner]
related:
  - ../../templates/personal/daily-entry.md
  - ../../templates/personal/skincare-day.md
  - ../habits/definitions.md
  - ../SCORE.md
  - ../config.yaml
  - ../../guides/04-lifestyle-os/life-os/energy-management.md
  - ../../guides/04-lifestyle-os/health/sns-cortisol-brake-playbook.md
sensitivity: private
---

# Daily entry — đọc hiểu từng phần

> Template trống: [`templates/personal/daily-entry.md`](../../templates/personal/daily-entry.md)  
> File thật: `personal/daily/YYYY/YYYY-MM-DD.md` · tạo nhanh: `.\personal\new-day.ps1`

Mỗi tối ~5–8′. **Không** viết essay — số + gạch đầu dòng ngắn.

---

## Tổng quan (map 30 giây)

| Phần | Trả lời câu hỏi | Feed Lifestyle score? |
| --- | --- | --- |
| Meta | Ngủ / dậy / 1 việc | Sleep (qua CSV) |
| Scores — state | Energy Focus Mood Stress Motivation | Review thủ công (Energy parse optional) |
| Scores — mind | Anxiety · Recovery · Social · Soreness | **Chưa auto** — theo dõi tinh thần |
| Deep work | Block sâu thật? | **Deep work** pts |
| Wins / Friction | Ship / kẹt | Weekly narrative |
| Body + CSV | Ngủ/cân/tập | **Metrics** + **Workouts** (cột `training`) |
| Nutrition link | Có file ăn? | **Nutrition days** |
| Skincare link | AM/PM + state da? | **Chưa auto** — track only |
| Habits H1–H5 | Tick | **Habits** |
| Compliance | Đóng ngày | Chất lượng data |
| Note / MIT | Học + ngày mai | — |

Rubric: [`../SCORE.md`](../SCORE.md) · [`../config.yaml`](../config.yaml).

**Thể chất vs tinh thần:** CSV + H4 + nutrition ≈ thể chất proxy. Mind block ≈ tinh thần proxy. Deep work = career, không thay mental health.

---

## Meta

| Field | Ý nghĩa | Cách điền |
| --- | --- | --- |
| **Wake** | Giờ thức | `07:30` hoặc “bình thường” |
| **Sleep last night** | Giờ ngủ | Khớp CSV `sleep_h` |
| **Sleep quality (1–10)** | Cảm nhận ngủ | Target mặc định ≥6 |
| **One thing hôm nay** | Theme / ưu tiên 1 câu | Không list việc |

---

## Scores — state (1–10)

| Cột | Nghĩa | Thang gợi ý |
| --- | --- | --- |
| **Energy** | Thể lực / tỉnh | 1 kiệt · **5–6 BT** · 10 đầy |
| **Focus** | Giữ chú ý | Thấp nếu reactive cả ngày |
| **Mood** | Cảm xúc nền | 1 xuống · **5–6 BT** · 10 tốt |
| **Stress** | Áp lực việc/đời (acute) | 1 êm · **8–9 rất stress** |
| **Motivation** | Muốn tiến / làm | Độc lập với Energy |

Theory: [energy-management](../../guides/04-lifestyle-os/life-os/energy-management.md).

---

## Scores — mind / recovery

| Field | Nghĩa | Cách điền |
| --- | --- | --- |
| **Anxiety (1–10)** | Lo lan tỏa, khó “tắt” — **khác Stress** | Stress cao + Anxiety thấp = áp lực việc nhưng đầu ổn |
| **Recovery / rest** | Có downtime thật (walk, nằm, hobby không doomscroll) | Yes/No — ngủ chưa đủ nếu cả ngày on |
| **Social** | Nói chuyện **người thật** (không chỉ Slack việc) | Yes/No |
| **Soreness / ốm (0–10)** | Đau cơ / bệnh | 0 = bình thường · tách stress tâm lý |

Khi Stress/Anxiety cao: xem [sns-cortisol-brake-playbook](../../guides/04-lifestyle-os/health/sns-cortisol-brake-playbook.md) (không thay lời khuyên y khoa).

**Score tuần:** mind block **chưa** vào `/100` (tránh phức tạp v1) — vẫn **bắt buộc điền** để tuần review đọc được sức khỏe tinh thần.

---

## Deep work

| Field | Ý nghĩa |
| --- | --- |
| Block / Time / Task / Focus | Phiên có chủ đích, ít interrupt |
| **Deep work total (h)** | Chỉ giờ deep thật |

Không deep: mail/meeting/reactive 10→21 → total **0**. Habit H3: ≥90′ ([definitions](../habits/definitions.md)).

---

## Wins / Friction

- **Wins:** output đã ship (kể cả gym).  
- **Friction:** stress, không deep, tool… → 1 thí nghiệm tuần sau.

---

## Body

| Dòng | Ý nghĩa |
| --- | --- |
| CSV checkbox | 1 dòng `body/metrics.csv` |
| Movement / training | gym, walk, rest — **điền `training` trên CSV** để Workouts score đếm |
| RHR / HRV | Optional; theory [hrv-tracking](../../guides/04-lifestyle-os/health/hrv-tracking.md) |

Có `sleep_h` hoặc `weight_kg` → Metrics days. Có `training` non-empty → Workouts.

---

## Nutrition link

Chi tiết bữa → `nutrition/YYYY/YYYY-MM-DD.md`. Có file → Nutrition days.  
[glucose-insulin](../../guides/04-lifestyle-os/health/glucose-insulin-system.md).

---

## Skincare link

Chi tiết routine → `skincare/YYYY/YYYY-MM-DD.md` · blank: [`templates/personal/skincare-day.md`](../../templates/personal/skincare-day.md).

| Phần | Điền gì |
| --- | --- |
| **Skin state** | Oil / dry / breakouts / redness — cảm nhận nhanh |
| **AM / PM** | Tick bước thật làm; ghi **1** treat chính (không list 10 product mỗi tối) |
| **SPF** | Tick nếu ra ngoài ban ngày |
| **Triggers** | Gym muộn, nắng no-SPF, product mới, gãi… |
| **Product change** | Chỉ khi đổi — tránh “routine hop” |

**Không** vào Lifestyle `/100` (v1). Compliance: optional.  
Da đỏ / dị ứng / mụn nặng kéo dài → da liễu (log chỉ hỗ trợ nhớ pattern).

---

## Habits (H1–H5)

| ID | Done khi (mặc định) |
| --- | --- |
| H1 | Giường trước **23:00** |
| H2 | Sáng ≥ **30g** protein |
| H3 | ≥1 block **90′** deep |
| H4 | Walk ≥20′ hoặc gym |
| H5 | Không caffeine sau **14:00** |

---

## Compliance

CSV · Nutrition · Habit tháng · **Mind scores** · Skincare (optional) — đủ data cho review.

---

## Note 3 dòng · Tomorrow MIT (≤3)

3 quan sát ngắn · ≤3 MIT (ưu tiên ngủ / recovery / 1 deep block).

---

## Workflow tối

1. State + **mind** scores (2′)  
2. Deep work total (1′)  
3. Body/CSV + nutrition (2′)  
4. Skincare AM/PM tick nếu chưa (1′)  
5. Habits + Compliance (1′)  
6. Note + MIT (2′)  

```powershell
python scripts/personal_week_summary.py --week YYYY-Www --write
```

---

## Ví dụ

- [`2026-08-13.md`](./2026/2026-08-13.md) — stress cao, anxiety điền, recovery No, social TBD, gym 22h, 0h deep
