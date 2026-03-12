# ⚖️ Risk-Adjusted Returns

## 1. Expected Value Framework
- `EV = (SuccessProbability * Revenue) - (FailureProbability * Cost)`.
- Với farm: Success = account survive + tạo revenue; Failure = bị ban/checkpoint.

## 2. Ban Rate Modeling
- Input: `ban_rate_weekly`, `recovery_cost`, `downtime`.
- Example: ban_rate 12%/tuần → expected lifetime `1/ban_rate ≈ 8.3 tuần`.
- Adjust ROI: `EffectiveRevenue = Revenue/account * (lifetime / target_lifetime)`.

## 3. Scenario Table
| Scenario | Ban Rate | Revenue/account | Effective Revenue | Failure Cost | Risk-adjusted ROI |
| --- | --- | --- | --- | --- | --- |
| Base | 10%/week | $8.0 | $6.4 | $1.2 | 32% |
| Spike | 18%/week | $7.2 | $4.0 | $2.0 | 5% |
| Optimized | 7%/week | $8.5 | $7.0 | $0.9 | 45% |

## 4. Monte Carlo Idea
- Simulate ban events (Bernoulli) → distribution ROI.
- Python pseudocode:
```python
import random

def simulate_roi(active_accounts, revenue, cost, ban_rate, days=30):
    survivors = 0
    for _ in range(active_accounts):
        alive = True
        for _ in range(days):
            if random.random() < ban_rate:
                alive = False
                break
        if alive:
            survivors += 1
    total_revenue = survivors * revenue
    roi = (total_revenue - cost) / cost
    return roi
```

## 5. Risk Mitigation
- Diversify proxy providers, fingerprint sets.
- Automate health check → early detect drop trust score.
- Insurance: giữ bank account dự phòng, fund reserve khi farm die.

## 6. Checklist
- [ ] Ban rate log theo tuần/tháng.
- [ ] ROI báo cáo kèm confidence interval.
- [ ] Mitigation plan cho spike scenario.