# 📉 Interest Rate Impact Playbook

> "When the tide goes out, you discover who's been swimming naked." – Warren Buffett

Tài liệu này phân tích tác động của chu kỳ tăng/giảm lãi suất lên các lớp tài sản, ngân hàng và doanh nghiệp.

---

## 1. Rate Cycle Overview

- **Hike phase:** Fed/central banks tăng lãi để hạ nhiệt lạm phát → credit tightening.
- **Pause:** dữ liệu đủ nguội để giữ nguyên.
- **Cut:** tăng trưởng suy yếu/sự cố tài chính → cắt để hỗ trợ.

### 1.1 Key Indicators
- Policy rate vs neutral rate (r*).
- Yield curve slope (2y-10y, 3m-10y).
- Financial Conditions Index (FCI).
- Bank lending standards (Senior Loan Officer Survey).

---

## 2. Asset Class Sensitivity

| Asset | Rate Hikes | Rate Cuts |
| --- | --- | --- |
| Growth equities | P/E compression, funding khó | Multiple expansion, easier capital |
| Value/Financials | Short-term hưởng lợi NIM, nhưng rủi ro credit | Nếu cut do suy thoái, nợ xấu tăng |
| Bonds | Price giảm (duration risk) | Price tăng, nhất là long duration |
| Real Estate | Cap rate tăng, giá tài sản giảm | Refi rẻ hơn, kích cầu |
| USD | Thường mạnh khi hike | Yếu đi khi cut (carry giảm) |

> Rule: Duration asset (tech, long bonds) nhạy với kỳ vọng lãi suất dài hạn; Financials nhạy với lãi suất ngắn hạn + credit quality.

---

## 3. Banking Lens

### 3.1 Net Interest Margin (NIM)
- Hike nhanh → funding cost tăng nhanh hơn asset yield → squeeze NIM.
- Depositors chuyển sang money market khi lãi suất cao → funding outflow.

### 3.2 Liquidity Stress
- Treasuries/MBS bị mark-to-market lỗ → unrealized loss (SVB case).
- Theo dõi LCR, NSFR, collateral haircuts.

### 3.3 Playbook
- ALM hedging (swap fixed-floating).
- Offer tiered deposit rates để giữ khách.
- Diversify funding (covered bonds, wholesale).

---

## 4. Corporate Finance Impact

| Function | Hike Response | Cut Response |
| --- | --- | --- |
| Treasury | Lock fixed rate nếu còn thấp, xếp hàng vay trước | Refi debt dài hơn, optimize capital structure |
| Capex | Delay project IRR thấp, ưu tiên ROI nhanh | Restart dự án dài hạn, M&A nhiều hơn |
| Startup runway | Runway ngắn nếu burn rate cao → cần profitability push | Fundraising cải thiện, valuations lên |
| FX hedging | USD mạnh → hedge nhập khẩu | USD yếu → tận dụng xuất khẩu |

---

## 5. Rate Shock Scenarios

### Scenario A: 200-300bps hike trong 12 tháng
- Equity: tránh long-duration growth, ưu tiên cash flow.
- Bond: shorten duration, dùng floating rate.
- CRE: stress test DSCR khi lãi vay > 10%.
- Ops: renegotiate supplier terms, lock price.

### Scenario B: Emergency cuts (≥100bps) vì khủng hoảng
- Tín hiệu recession → tăng vị thế phòng thủ (long UST 10y+, gold).
- Credit event nguy cơ: junk bonds, leveraged loans.
- Doanh nghiệp: chuẩn bị covenant waiver, reduce capex.

---

## 6. Tools & Automation

- Rate dashboard: Fed Funds futures (CME), SOFR curve, OIS curve.
- Alert: khi market pricing ≥50bps change sau FOMC.
- Scenario engine: Python/Excel sensitivity DSCR, interest expense, WACC.

---

## 7. Vietnam Context Notes

- SBV kiểm soát room tăng trưởng tín dụng; lãi suất điều hành tác động chậm nhưng mạnh đến bất động sản.
- Lợi suất TPCP VN 10y dao động 2.5-4.5%; spreads với USD debt ảnh hưởng capital flow.
- Banking: chú ý trần lãi huy động và margin bancassurance.

---

> Cross-link: [Inflation-Deflation Playbook](./inflation-deflation-playbook.md) & [Economic Cycles](./economic-cycles.md).