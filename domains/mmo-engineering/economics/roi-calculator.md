# 📈 ROI Calculator

## 1. Template Spreadsheet
- Columns: `Month`, `Active Accounts`, `Revenue/account`, `CapEx`, `OpEx`, `Failure Cost`, `ROI`.
- Formula: `TotalRevenue = ActiveAccounts * RevenuePerAccount`.
- `TotalCost = CapEx_monthly + OpEx + FailureCost`.
- `ROI = (TotalRevenue - TotalCost) / TotalCost`.
- Add scenario toggles (Best/Base/Worst) cho ban rate và proxy cost.

## 2. Python Script (sample)
```python
import pandas as pd

def roi_report(active_accounts, revenue_per_account, capex_monthly, opex_monthly, failure_cost):
    total_revenue = active_accounts * revenue_per_account
    total_cost = capex_monthly + opex_monthly + failure_cost
    roi = (total_revenue - total_cost) / total_cost
    return {
        "active_accounts": active_accounts,
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "roi": roi
    }

scenarios = [
    {"name": "Base", "active": 300, "revenue": 8.0, "capex": 420, "opex": 1211, "failure": 120},
    {"name": "Ban Spike", "active": 250, "revenue": 7.5, "capex": 420, "opex": 1250, "failure": 200},
    {"name": "High ROI", "active": 320, "revenue": 9.2, "capex": 420, "opex": 1180, "failure": 80},
]

df = pd.DataFrame([{
    "Scenario": s["name"],
    **roi_report(s["active"], s["revenue"], s["capex"], s["opex"], s["failure"])
} for s in scenarios])

print(df)
```

## 3. Usage
- Plug từ [cost-analysis.md](./cost-analysis.md) vào script để cập nhật thực tế.
- Export CSV → gửi ops/finance.

## 4. Sample ROI Framework (Airdrop Farm)
| Cost Item | Monthly | Notes |
| --- | --- | --- |
| Residential Proxy (10GB) | $50 | @$5/GB |
| SIM 4G x 20 | $40 | @$2/SIM data |
| Anti-detect license | $100 | Gologin/Multilogin |
| VPS/Server | $50 |  |
| **Total** | **$240** |  |

- Revenue assumptions:
  - `Expected payout per wallet = X`
  - `Success rate (post-Sybil) = Y%`
  - `Active wallets = N`
- Net profit per month:
  `Net = (X * Y * N) - 240`
- ROI:
  `ROI = Net / 240`

- Track ROI theo tuần/tháng để quyết định scale hay pause.

## 4. Checklist
- [ ] Số active account lấy từ monitoring.
- [ ] Revenue/account cập nhật theo chiến dịch.
- [ ] Scenario analysis chạy ít nhất 3 case.