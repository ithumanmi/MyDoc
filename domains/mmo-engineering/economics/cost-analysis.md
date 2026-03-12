# 💸 Cost Analysis

## 1. Cost Buckets
- **CapEx:** hardware (phone farm, PC controller, racks), amortized 12-18 tháng.
- **OpEx:** proxy, SIM data, điện + nhân sự vận hành, tool license, cloud infra.
- **Failure Cost:** account bị ban, checkpoint → chi phí làm lại.

## 2. Sample Breakdown (Phone Farm 50 máy)
| Item | Qty | Unit Cost | Cycle | Monthly Cost |
| --- | --- | --- | --- | --- |
| Galaxy Note 8 refurb | 50 | $80 | amortize 12m | $333 |
| Rack + PSU + cooling | 3 | $150 | amortize 12m | $38 |
| Control PC | 1 | $900 | amortize 18m | $50 |
| 4G proxy plan | 10 | $35 | monthly | $350 |
| SIM data (unlimited) | 50 | $5 | monthly | $250 |
| Electricity + cooling | - | - | monthly | $90 |
| Ops staffing (part-time) | 1 | $400 | monthly | $400 |
| Tool licenses (anti-detect, automation) | - | - | monthly | $120 |
| **Total** |  |  |  | **$1,631** |

## 3. Cost Formula
- `CapEx_monthly = sum(HardwareCost / amortization_months)`
- `OpEx_monthly = proxy + SIM + electricity + staffing + licenses`
- `CPA_farm = (CapEx_monthly + OpEx_monthly) / active_accounts`

## 4. Sensitivity Scenarios
- **Proxy surge:** giá proxy tăng 20% → update `OpEx` và tính lại ROI.
- **Ban spike:** active account giảm 15% → `CPA_farm` tăng.
- **Hardware failure:** 5 máy die/tháng → thêm `ReplacementCost`.

## 5. Dashboard Inputs
- Track cost per provider (proxy A vs B).
- Link tới [operations-monitoring.md](../operations-monitoring.md) để lấy số active account.

## 6. Checklist
- [ ] Amortization schedule cập nhật theo tuổi thọ thực tế.
- [ ] Proxy/SIM giá trị theo hợp đồng mới nhất.
- [ ] Failure cost được log riêng.