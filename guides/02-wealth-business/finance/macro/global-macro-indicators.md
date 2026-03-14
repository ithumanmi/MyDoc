# 🌐 Global Macro Indicators Dashboard

> "What gets measured gets managed." – Peter Drucker

Framework tập hợp các chỉ báo chủ chốt (PMI, yield curve, employment, credit spreads) để xây dựng bảng điều khiển macro.

---

## 1. Indicator Stack

| Bucket | Indicator | Source | Frequency | Interpretation |
| --- | --- | --- | --- | --- |
| Growth | Global PMI (Manufacturing/Services) | S&P Global | Monthly | >50 = expansion, rate of change quan trọng |
| Growth | OECD CLI | OECD | Monthly | Dẫn dắt 6-9 tháng |
| Inflation | CPI, PCE Core | BLS/BEA | Monthly | Watch MoM annualized |
| Inflation | ISM Prices Paid | ISM | Monthly | Early pressure input |
| Liquidity | Fed Net Liquidity (Fed BS - TGA - RRP) | FRED/Treasury | Weekly | <0 → tightening |
| Liquidity | Cross-currency basis (JPY/USD) | Bloomberg | Daily | Negative sâu = USD shortage |
| Credit | HY & IG spreads | ICE/Bloomberg | Daily | > 600bps (HY) = stress |
| Employment | Initial jobless claims | DOL | Weekly | <200k = nóng, >300k = stress |
| Housing | Building permits, NAHB | Census/NAHB | Monthly | Leading US growth |

---

## 2. Yield Curve & Term Premium

### 2.1 Yield Curve Signals
- 3m-10y, 2y-10y inversion depth.
- Steepening after inversion thường báo recession trong 12-18 tháng.

### 2.2 Tools
- FRED API, TradingView spreads.
- Alert khi 3m-10y > +50bps (steepener) sau khi inverted.

---

## 3. Employment Dashboard

| Indicator | Threshold | Action |
| --- | --- | --- |
| Initial claims | < 210k | Labor tight → Fed hawkish |
| Initial claims | > 280k | Growth slowing → defensive tilt |
| Payrolls vs ADP | Divergence lớn | Question data quality, focus on trend |
| JOLTS openings | < 8M | Demand hạ nhiệt |

Include wage trackers (Atlanta Fed Wage Growth, Average Hourly Earnings) để đánh giá wage-price spiral.

---

## 4. Commodity & Inflation Pulse

- **DRAM, Baltic Dry Index:** đo health supply chain.
- **Copper/Gold ratio:** proxy growth vs safety.
- **Agri indices:** FAO Food Price, gạo/palm oil (quan trọng cho ASEAN).

---

## 5. Implementation Guide

1. **Data Pipeline:** Python script kéo dữ liệu (alpha vantage, fredapi), lưu CSV/Parquet.
2. **Transform:** tạo bảng normalized (z-score, % change 3m/6m).
3. **Dashboard:** Metabase/Looker Studio hiển thị heatmap.
4. **Alert:** Zapier/IFTTT bắn email khi chỉ báo chạm ngưỡng.

### Sample Heatmap

| Indicator | Latest | Trend | Signal |
| --- | --- | --- | --- |
| Global PMI | 49.2 | ↓ | Bearish |
| Fed Net Liquidity | -$200B | ↓ | Tight |
| HY Spread | 550bps | ↑ | Risk-off |

---

## 6. Use Cases

- **Asset allocators:** quyết định overweight/underweight risk assets.
- **Corporate FP&A:** dự báo cầu, giá input.
- **Product Builders:** design features theo liquidity regime (ví dụ BNPL tightening khi spreads tăng).

---

> Cross-link: [Economic Cycles](./economic-cycles.md) & [Interest Rate Impact](./interest-rate-impact.md)