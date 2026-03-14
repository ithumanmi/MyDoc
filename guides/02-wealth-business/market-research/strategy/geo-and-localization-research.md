# Geo & Localization Research

> Mục tiêu: biết khi nào ưu tiên VN-first vs global-first, chọn market tier, và localize đúng (keyword, kênh, payment, văn hóa).

## 1) Nguồn dữ liệu theo thị trường
- **Store intelligence theo country:** Data.ai / Sensor Tower (downloads, revenue, ranking theo country). Nếu budget thấp: AppMagic mid-tier.
- **Search & trend:** Google Trends (region), Similarweb by country, YouTube Trends, TikTok Creative Center (country filter).
- **Pricing & PPP:** World Bank PPP, local store pricing tiers (Steam regional, App Store/Play regional), FX volatility.
- **Ads cost & monetization:** Meta/TikTok Ads Library (creative benchmark), ad network eCPM reports (by geo), CPI dashboards (Sensor Tower/Data.ai) theo Tier 1 vs 2/3.
- **Local payment & compliance:** VN: Momo/ZaloPay, COD, telco billing; global: PayPal/Stripe, local wallets (GCash/GrabPay/Paytm). Kiểm tra thuế/VAT in-app.
- **Cultural signals:** App reviews theo ngôn ngữ/region; social/community local (Facebook group VN, Discord/Reddit EN, JP/KR boards).

## 2) Tier 1 vs Tier 2/3 (CPI, LTV, Ad revenue)
- **Tier 1 (US/CA/UK/EU5/AU/NZ/JP/KR):** CPI cao, LTV cao, ad eCPM cao; yêu cầu local chất lượng cao (ngôn ngữ, support, privacy/compliance).
- **Tier 2/3 (SEA/LatAm/India/MENA/EE):** CPI thấp, LTV trung bình/thấp, eCPM thấp hơn; cần tối ưu retention và local payment; ad-first/hybrid dễ hợp hơn subscription đắt.
- **Heuristic chọn thị trường:**
  - Nếu **ARPU/monetization phụ thuộc ads** → ưu tiên Tier 1 để tận dụng eCPM cao; hoặc volume lớn Tier 2/3 nếu sản phẩm nhẹ, wide appeal.
  - Nếu **subscription/B2B** → ưu tiên Tier 1; Tier 2/3 khi có local sales/support.
  - **Game premium PC/console** → thường Tier 1 + regional pricing PPP để mở rộng.

## 3) Localization checklist
- **Keyword & ASO per language:** nghiên cứu keyword bản địa (Data.ai/AppTweak), dịch tiêu đề/mô tả/subtitle; giữ brand không dịch.
- **Cultural fit:** hình ảnh, nhân vật, màu sắc, ngày lễ (Tết/VN, Golden Week/JP, Ramadan/MENA, Diwali/IN); tránh biểu tượng nhạy cảm.
- **Payment & pricing:** hiển thị đơn vị tiền tệ địa phương; gói giá PPP-friendly; hỗ trợ ví địa phương (VN: Momo/ZaloPay), telco billing nếu cần.
- **UX & support:** timezone support, FAQ ngôn ngữ địa phương; kênh cộng đồng local.
- **Compliance:** nội dung nhạy cảm (rating, pháp lý), thuế số (VAT/GST), dữ liệu (PDPA/GPDR).

## 4) Khi nào VN-first vs Global-first?
- **Chọn VN-first nếu:**
  - Bạn có kênh phân phối sẵn tại VN (community, KOL, partnership), chi phí thử nghiệm thấp.
  - Sản phẩm cần hiểu văn hóa nội địa sâu (giáo dục K12, fintech địa phương, MMO tool liên quan nền tảng VN).
  - Mục tiêu chứng minh traction nhanh với budget hạn chế.
- **Chọn Global-first nếu:**
  - Sản phẩm ngách quốc tế (dev tools, AI/LLM, SaaS B2B), hoặc game premium muốn review/creator quốc tế.
  - Monetization phụ thuộc eCPM/ARPU cao (ads/subscription cao cấp) mà VN khó đạt.
  - Bạn sẵn có năng lực tiếng Anh, kênh creator/ads global.
- **Lộ trình hybrid:** Pilot VN (cost thấp, tốc độ cao) để chốt core loop/retention, sau đó localize EN và Tier 1; hoặc ngược lại nếu bạn build cho US trước rồi bản địa hóa VN.

## 5) Output đề xuất
- **One-pager per geo:** TAM/SAM/SOM sơ bộ, CPI/LTV giả định, kênh chính, pricing PPP, payment, compliance note.
- **ASO/Keyword sheet:** 5-10 keyword chính mỗi ngôn ngữ; title/short description A/B.
- **Localization backlog:** copy, hình ảnh, payment method, support script, holiday calendar.
- **Dashboard geo:** ranking, CPI, eCPM, retention, top creative per geo; tần suất weekly.

## 6) Liên kết nhanh
- Hướng dẫn địa phương hóa chi tiết: [Geo & Localization Guide (tactical)](../core/geo-localization-guide.md)
- Sizing & forecast: [Market Sizing & Forecasting](./market-sizing-forecasting.md)
- Reporting & kể chuyện: [Research Reporting Playbook](./research-reporting-playbook.md)