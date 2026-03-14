# 🧩 Insurance Product Deep Dive: Life, Health, P&C & Embedded Models

> "Insurance products are financial software: they encode risk, capital, and behavior." – Adapted from Josh Wolfe

Tài liệu này bóc tách kiến trúc sản phẩm bảo hiểm theo từng dòng (Life, Health, P&C, Embedded), giúp đội sản phẩm/dev hiểu rõ pricing, cashflow, và yếu tố vận hành.

---

## 1. Product Stack Overview

| Layer | Mô tả | Ví dụ câu hỏi |
| --- | --- | --- |
| **Coverage Design** | Benefit, exclusion, waiting period | Có loại trừ bệnh có sẵn không? |
| **Pricing & Reserve** | Premium table, actuarial assumption | Mortality table nào? Expense loading bao nhiêu? |
| **Cashflow Mechanics** | Premium frequency, surrender value | Khi nào khách rút được tiền? Penalty thế nào? |
| **Distribution Package** | Rider, bundling, commission | Bán qua bancassurance hay digital? |
| **Embedded Finance Hooks** | API, triggers, data sharing | Merchant/fintech lấy dữ liệu gì để quote?

---

## 2. Life Insurance Lines

### 2.1 Term Life
- **Feature:** Pure protection, kỳ hạn 5-30 năm, không có giá trị hoàn lại.
- **Premium Mechanics:** Level/step premium, có thể gắn rider critical illness.
- **Risk Driver:** Mortality, lapse rate, selection risk.
- **Tech Stack:** Underwriting rule engine + eKYC + medical data API.

### 2.2 Whole Life / Endowment
- **Feature:** Lifetime coverage, có cash value, dividend participation.
- **Cashflow:** Premium định kỳ, lãi tích lũy → surrender value.
- **Consideration:** IFRS17 measurement (contract boundary dài), asset-liability matching.

### 2.3 Unit-linked / Investment-linked
- **Feature:** Premium tách thành insurance charge + investment fund.
- **Ops:** Yêu cầu integration với fund admin, NAV update hàng ngày, switch fund workflow.
- **Key Metrics:** Persistency (13th month), fund performance relative benchmark.

### 2.4 Annuities / Retirement Income
- **Feature:** chuyển lump-sum sang dòng thu nhập định kỳ.
- **Risks:** Longevity risk, interest rate hedge.
- **Digital Hooks:** Retirement calculator, payout simulation API.

---

## 3. Health & Group Benefits

| Product | Cấu trúc | Điểm cần lưu ý |
| --- | --- | --- |
| Individual Health | Sum insured theo plan, mạng lưới bệnh viện | Pre-authorization API, fraud detection |
| Critical Illness | Lump-sum khi chẩn đoán bệnh trọng yếu | Waiting period, multiple claim structure |
| Group Health | Enrollment theo nhân viên, capitation/premium per head | Integration với HRIS, mid-term endorsement |
| Income Protection | Trả % lương khi mất khả năng lao động | Link với payroll, evidence of insurability |

**Pricing Inputs:** Medical inflation, utilization rate, demographic mix, employer contribution.

**Digital Experience:** eCard, provider search, claim submission app, telemedicine add-on.

---

## 4. Property & Casualty (P&C)

### 4.1 Motor Insurance
- **Coverage:** TPL (bắt buộc), comprehensive (own damage, theft, natural disaster).
- **Rating Factors:** Vehicle type, age, location, telematics score.
- **Tech Hooks:** Telematics SDK, OBD devices, integration với DMV để verify giấy tờ.

### 4.2 Home/Property
- **Coverage:** Building, contents, liability.
- **Cat Risk:** Flood, earthquake modeling → cần dữ liệu GIS, hazard map.
- **Underwriting:** Sum insured vs rebuilding cost, occupancy.

### 4.3 Travel / Specialty
- Short-term, high automation, embedded trong flows (airline, OTA).
- Claim fast-track: lost baggage, trip delay.

### 4.4 Commercial Lines
- **SME Package:** Property + liability + cyber basic.
- **Mid/Large:** Tailored, cần broker portal, exposure schedule.

---

## 5. Embedded & On-demand Insurance

| Model | Use case | Integration |
| --- | --- | --- |
| Checkout Add-on | Mua điện thoại thêm bảo hành mở rộng | API pricing real-time, SKU mapping |
| Ride-hailing Protection | Bảo hiểm chuyến đi theo phút | Usage-based billing, webhook event trip start/end |
| SaaS Workforce Benefit | Gói bảo hiểm nhân viên cho SMEs | HRIS sync, payroll deduction |
| Credit Protection | Bệnh/lost job bảo vệ khoản vay | Core banking event, premium baked vào EMI |

Key requirements: instant underwriting, simplified disclosure, claims API để merchant theo dõi trạng thái.

---

## 6. Pricing & Actuarial Inputs (Snapshot)

| Line | Data nguồn | Biến động chính |
| --- | --- | --- |
| Life | Mortality table (V15), interest rate, expense loading | longevity improvements |
| Health | Claims triangle, medical inflation index | thuốc mới, trend telemedicine |
| Motor | Loss ratio by segment, telematics, repair cost index | giá phụ tùng, hành vi lái xe |
| Property | Cat models (AIR, RMS), construction cost | climate risk, urban density |

**IFRS17 Angle:** Measurement approach khác nhau (GMM vs PAA). Single product có thể split thành cohorts.

### 6.1 Actuarial Modeling Toolkit

1. **Assumption Set Library**
    * Mortality/Morbidity tables (local vs reinsurance).
    * Expense assumptions (acquisition, maintenance, overhead).
    * Lapse/persistency curves theo channel.
    * Investment yield curves (risk-free + spread scenario).

2. **Model Types**
    * **Deterministic projection** (best estimate) – Excel/AXIS/Prophet.
    * **Stochastic scenario** – economic scenario generator (ESG) cho unit-linked/annuity.
    * **Dynamic Lapse model** – lapse rate phụ thuộc chênh lệch lãi suất thị trường.

3. **Reserving & Capital**
    * IFRS17: phân loại GMM/PAA, thiết lập Contract Service Margin (CSM) và Loss Component.
    * RBC/Solvency: risk charge cho underwriting, market, counterparty.
    * Stress test: mortality ±15%, lapse ±25%, interest shock ±100bps.

4. **Sensitivity & What-if Dashboard**
    * Break-even premium khi chi phí tăng 10%.
    * Loss ratio impact khi telematics score bias.
    * Cashflow waterfall: premium → acquisition cost → claims → reserve release.

> Tooling gợi ý: Moody’s AXIS, Prophet, in-house Python model (NumPy, pandas) cho scenario nhanh.

---

## 7. Product Launch Checklist

- [ ] Xác định customer job + coverage gap cụ thể.
- [ ] Thiết kế benefit table, exclusion rõ ràng.
- [ ] Dựng premium model + sensitivity (lãi suất, mortality, utilization).
- [ ] Chuẩn hóa rider/bundle library để tái sử dụng.
- [ ] Thiết lập rule underwriting + evidence yêu cầu.
- [ ] Config PAS + rating engine, mapping với billing/claims.
- [ ] Chuẩn bị distribution kit: illustration, API spec, commission plan.
- [ ] Run pilot với cohort nhỏ, monitor claim ratio & lapse.

---

## 8. Product Analytics & Feedback Loop

1. **Persistency dashboards:** theo channel, product, age.
2. **Loss ratio heatmap:** theo coverage, geography, driver (motor).
3. **Underwriting exceptions log:** theo lý do override.
4. **Embedded partner performance:** conversion, claim severity, fraud flags.

> KPI tối thiểu: Loss ratio target ±5%, Combined ratio < 100% (P&C), Persistency 13 tháng > 85% (life).

---

## 9. Case Study: Unit-linked x Digital Bank

**Bối cảnh:** Digital bank muốn bán sản phẩm unit-linked cho tệp khách hàng giàu có, tích hợp trực tiếp trong app.

| Thành phần | Thiết kế |
| --- | --- |
| Coverage | Life cover = 10x annual premium, rider critical illness |
| Premium | Min 1,000 USD/lần, cho phép top-up | 
| Investment Funds | 4 lựa chọn (Global Equity, ESG, Fixed Income, Balanced) |
| Fee Structure | Policy charge, fund management fee, surrender penalty năm 1-3 |
| Distribution | Bank app với journey: risk profiling → illustration → eKYC → e-sign |
| Data flow | Core banking gửi profile & risk score → insurer rating engine trả premium | 

**Actuarial lưu ý:**
1. Persistency 13 tháng dự kiến 90% nhờ auto-debit từ tài khoản bank.
2. Investment return assumptions dựa trên portfolio benchmark (MSCI World, Bloomberg Agg).
3. Stress scenario: equity drawdown 30% + lapse tăng 20% → đánh giá CSM impact.

**Tech/ops:**
- Event streaming để cập nhật NAV và hiển thị giá trị hợp đồng real-time.
- API cho redemption/switch fund, xử lý trong 2 ngày làm việc.
- Compliance: integrate suitability questionnaire để đáp ứng Luật Kinh doanh bảo hiểm VN.

**Kết quả pilot (3 tháng):**
- 5,000 policy phát hành, ANP 12 triệu USD.
- Loss ratio (insurance charge) thấp < 25% nhờ underwriting đơn giản + tệp khách hàng tốt.
- CSAT 4.7/5 vì journey hoàn toàn digital, payout claim rider xử lý < 48h.

---

## 9. Reference Materials

- Swiss Re, Munich Re product innovation reports.
- NAIC Product Filing requirements.
- AXA Embedded Insurance whitepaper.
- VN Decree 67/2023 về bảo hiểm vi mô và bancassurance.

---

📌 Gợi ý tiếp theo: kết nối file này với [Insurance Policy Administration Playbook](./insurance-policy-admin-playbook.md) để triển khai hệ thống tương ứng.