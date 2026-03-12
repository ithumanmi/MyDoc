# 🪂 Case Study: Crypto Airdrop Postmortem (LayerZero, ZKSync)

## 1. Bối cảnh
- Tham gia chiến dịch LayerZero + ZKSync 2024 với 1.200 ví.
- Mục tiêu: maximize allocation, limit Sybil detection.

## 2. Strategy
- **Wallet Hygiene:** mỗi ví có funding route riêng (CEX → mixer → ví), rotation 7 ngày.
- **Activity Mix:** bridge, swap, LP, vote governance.
- **Automation:** script Rust dùng RPC + relayers, rate limit 30 tx/phút.

## 3. Metrics
| Metric | LayerZero | ZKSync |
| --- | --- | --- |
| Survival Rate | 88% | 91% |
| Checkpoint Flag | 9% | 6% |
| Revenue/account | $420 | $280 |

## 4. Alert & Logs
- Alert nếu `gas fee spike > 50%` hoặc RPC error tăng.
- Log aggregator (ClickHouse) lưu transaction hash + fingerprint.
- Auto-remediation: chuyển sang RPC dự phòng, giảm tốc độ nếu flagged.

## 5. Lessons
- LayerZero phát hiện ví có pattern giống nhau → cần random hóa schedule (cron jitter ±45 phút).
- ZKSync reward ưu tiên ví đã vote governance → thêm automation “vote bot”.
- ROI cao nhưng chi phí gas tăng 25% do spam → cần gas budgeting dashboard.