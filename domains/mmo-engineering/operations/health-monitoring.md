# ❤️ Account Health Monitoring

> Chấm điểm sức khỏe account để auto-pause profile rủi ro trước khi bị ban.

## 1. Health Score Model
- `Score = w1*age + w2*engagement + w3*checkpoint_history + w4*proxy_quality + w5*revenue`
- Normalize 0-100; threshold:
  - **80-100:** Green → chạy full scripts.
  - **50-79:** Yellow → hạn chế action, tăng nghỉ.
  - **<50:** Red → auto-pause + review thủ công.

## 2. Metrics Input
- **Account Survival Rate:** rolling 7 ngày.
- **Checkpoint Rate:** số checkpoint/tuần.
- **Revenue per Account:** trung bình 7 ngày.
- **Behavior Signals:** session length, randomization score.
- **Proxy Health:** latency, ASN rotation.

## 3. Auto-Remediation
- Khi `score < 50` → script gửi event tới queue `pause_account`.
- Reset proxy + cookies aging lại 48h, sau đó chấm điểm lại.
- Nếu checkpoint xảy ra 2 lần/tuần → move vào “rehab pool”.

## 4. Alert Thresholds
| Metric | Threshold | Action |
| --- | --- | --- |
| Survival rate | < 85%/24h | Notify ops, check farm hardware |
| Checkpoint rate | > 8%/6h | Auto-pause batch + rotate proxy |
| Revenue/account | < target -20% | Kiểm tra script mới hoặc ads rejection |

## 5. Data Flow
`Agent heartbeat → Kafka → Stream processor (Flink) → State table (Redis/Postgres) → Score job (hourly)`

## 6. Dashboard Tiles
- Scatter plot (Score vs Revenue) để ưu tiên team review.
- Table “Red Accounts” với nút trigger manual actions.

## 7. Checklist
- [ ] Score function versioned (git tag) để audit.
- [ ] Auto-pause có fallback manual.
- [ ] Logs lưu lại quyết định (score, action) để giải thích.