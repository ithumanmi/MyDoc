# Tech Day 69: Tech Interview Question – Design A/B Test for ML

**Câu hỏi:** “Thiết kế A/B test để đánh giá mô hình ML mới (hoặc rule-based mới) như thế nào?”

## 1) Ý chính cần nhấn mạnh
- Xác định **mục tiêu & metric**: business metric (conversion/retention/CTR) + guardrail (latency/error).
- Chia traffic công bằng, tránh bias; thời gian chạy đủ để đạt power.
- Kế hoạch rollout/rollback và giám sát.

## 2) Flow trả lời gợi ý
1) **Define mục tiêu**: primary metric + guardrail; giả thuyết H0/H1.
2) **Chia traffic**: random split, stratify nếu cần (theo geo/device); tránh leakage giữa group.
3) **Size & thời gian**: tính sample size/power (ước lượng baseline + uplift kỳ vọng); chạy đủ dài để qua chu kỳ theo ngày/tuần.
4) **Instrumentation**: log event thống nhất, dán experiment id vào request/response.
5) **Monitoring**: dashboard p95 latency/error, business metric theo thời gian; alert nếu vượt ngưỡng.
6) **Rollout**: canary nhỏ → 50/50 → full; rollback nếu guardrail vi phạm.
7) **Analysis**: kiểm định thống kê (t-test/chi-square), check peeking; segment analysis.

## 3) Bullet trả lời ngắn gọn (template 30-60s)
- “Tôi xác định primary metric (ví dụ CTR) và guardrail (latency/error). Chia traffic ngẫu nhiên/stratify, tính sample size/power, chạy đủ chu kỳ. Log event kèm experiment id, giám sát p95 latency + error. Rollout canary→50/50, rollback nếu guardrail xấu. Phân tích với kiểm định thống kê và segment.”

## 4) Đi sâu nếu bị hỏi thêm
- **Peeking & sequential test:** tránh dừng sớm; cân nhắc sequential/SPRT hoặc bayesian nếu muốn theo dõi liên tục.
- **Cold-start/learning:** nếu là bandit, cần giải thích exploration/exploitation; nếu A/B thuần thì giữ allocation cố định.
- **Bias:** cookie/device vs user-level; bot/abuse filtering.
- **Metric pitfalls:** chọn metric nhạy nhưng không dễ bị nhiễu; dùng guardrail latency/error.

## 5) Đoạn kết thúc nhấn mạnh (1 câu)
- “A/B test cho ML cần metric rõ, chia traffic chuẩn, power đủ, giám sát guardrail, rollout an toàn và phân tích đúng thống kê.”

## Reference / Solution (tùy chọn)
- Checklist: sample size calculator, metric definition doc, dashboard layout, rollback rule.