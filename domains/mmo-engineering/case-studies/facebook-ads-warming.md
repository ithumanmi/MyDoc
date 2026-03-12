# 📣 Case Study: Facebook Ads Warm-up 30 ngày

## 1. Mục tiêu
- Kéo tài khoản mới lên mức chi tiêu $500/day trong 30 ngày mà không bị review hoặc limit.

## 2. Timeline & Workflow
| Day | Action |
| --- | --- |
| 1-3 | Profile hygiene (manual browse 45 phút/ngày, join group). Payment test $5. |
| 4-7 | Boost post engagement $10/day, giữ CTR >2%. |
| 8-14 | Chạy campaign traffic nhỏ, target rộng, tăng ngân sách 15%/ngày. |
| 15-21 | Conversion campaign (Add to cart), implement server-side events. |
| 22-30 | Scale lên $500/day, maintain ROAS mục tiêu. |

## 3. Trust Scoring
- Score dựa trên: account age, payment success, policy compliance, feedback.
- Threshold: Score <70 → tạm dừng tăng ngân sách, log incident.

## 4. Metrics & Dashboard
- **Checkpoint Rate:** <2%/tuần.
- **Event Match Quality:** >6/10.
- **Revenue/account:** theo dõi qua Metabase.
- Grafana alert nếu `Rejected Ads > 3/24h` hoặc `Spend drop >25%`.

## 5. Automation Guardrails
- Playwright automation **max 3 actions/phút**.
- IP pinning theo profile; mismatch → auto-pause.
- Payment rotation: list 3 bank cards, rotate mỗi 10 ngày.

## 6. Lessons
- Đăng nhập từ IP mới làm fail 40% warm-up → enforce proxy pinning.
- Payment mismatch quốc gia → add local bank BIN để giảm review.
- Trust score log + screenshot giúp appeal nhanh khi bị hạn chế.