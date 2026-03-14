# 🕵️ Market Research & Analysis Guide

> [← Back to Guides](../../../README.md) | [Home](../../../README.md)

Tài liệu hướng dẫn toàn diện về Nghiên cứu Thị trường & Phân tích Đối thủ cạnh tranh cho Game Dev, App Dev và Indie Hackers.

---

## 🚪 Start Here (theo vai)

- **Game Dev:** xem nhanh [Game Market Research](./games/game-market-research.md), [Game Market Sizing Practice](./games/game-market-sizing-practice.md), và nếu MMO/tools thì [MMO Tools Research](./games/mmo-tools-market-research.md). Cross-link: roadmaps MMO/game trong `domains/game-dev/`, `domains/mmo-engineering/`.
- **App / SaaS Builder:** bắt đầu từ [Mobile App Market Research](./apps-saas/mobile-app-market-research.md) hoặc [SaaS Market Research](./apps-saas/saas-market-research.md); xem thêm [B2B Sales Intelligence](./apps-saas/b2b-sales-intelligence.md), [PLG Research](./apps-saas/plg-research-framework.md). Cross-link: `domains/web-dev/`, `domains/backend-dev/`, `domains/ai-ml/` (LLM-based app), `domains/data-analytics/` (dashboard/BI), `domains/mmo-engineering/` nếu build automation.
- **Indie hacker / Side-hustle:** đi theo [Validation Strategy](./strategy/validation-strategy.md) + [Trend Spotting](./strategy/trend-spotting-alpha.md); tham khảo `guides/03-career-skills/` (productivity) và `domains/ai-ml/agents/` nếu muốn build agentic tool.

### 🧭 Bắt đầu theo vai (bảng điều hướng nhanh)

| Vai | Đọc trước (Intro/Competitor) | Ưu tiên theo vertical | Nâng cao (sizing/pricing/trend) |
| --- | --- | --- | --- |
| **Game Dev (PC/Console/Mobile)** | [Introduction](./core/introduction-to-market-research.md), [Competitor Analysis](./core/competitor-analysis-framework.md) | [Game Market Research](./games/game-market-research.md), [MMO Tools](./games/mmo-tools-market-research.md) nếu MMO/tools | [Market Sizing Practice](./games/game-market-sizing-practice.md), [Advanced Pricing](./strategy/advanced-pricing-strategy.md), [Trend Spotting](./strategy/trend-spotting-alpha.md) |
| **Mobile App Builder** | [Introduction](./core/introduction-to-market-research.md), [Competitor Analysis](./core/competitor-analysis-framework.md) | [Mobile App Research](./apps-saas/mobile-app-market-research.md), ASO | [Advanced Monetization](./apps-saas/mobile-app-monetization-advanced.md), [Market Sizing & Forecasting](./strategy/market-sizing-forecasting.md) |
| **SaaS / B2B** | [Introduction](./core/introduction-to-market-research.md), [Competitor Analysis](./core/competitor-analysis-framework.md) | [SaaS Market Research](./apps-saas/saas-market-research.md), [B2B Sales Intelligence](./apps-saas/b2b-sales-intelligence.md), [PLG Research](./apps-saas/plg-research-framework.md) | [Advanced Pricing](./strategy/advanced-pricing-strategy.md), [Market Sizing & Forecasting](./strategy/market-sizing-forecasting.md), [Trend Spotting](./strategy/trend-spotting-alpha.md) |
| **MMO / Automation** | [Introduction](./core/introduction-to-market-research.md), [Competitor Analysis](./core/competitor-analysis-framework.md) | [MMO Tools Research](./games/mmo-tools-market-research.md) | [Market Sizing & Forecasting](./strategy/market-sizing-forecasting.md), [Advanced Pricing](./strategy/advanced-pricing-strategy.md) |
| **Founder chung / Validation** | [Introduction](./core/introduction-to-market-research.md) | [Validation Strategy](./strategy/validation-strategy.md), [Primary Research 101](./core/primary-research-101.md) | [Market Sizing & Forecasting](./strategy/market-sizing-forecasting.md), [Trend Spotting](./strategy/trend-spotting-alpha.md), [Advanced Pricing](./strategy/advanced-pricing-strategy.md) |

### 🗺️ Start Here (INDEX theo tình huống)

| Tình huống | Bước nhanh | Trang/Tool chính | Output mong muốn |
| --- | --- | --- | --- |
| **Launch mobile game (global)** | 1) [Game Market Research](./games/game-market-research.md) (Steam/mobile); 2) [Game Market Sizing Practice](./games/game-market-sizing-practice.md); 3) Ads creative check; 4) Pricing/PPP tham chiếu [Geo & Localization](./core/geo-localization-guide.md) | SteamDB, Data.ai/Sensor Tower, Gamalytic, TikTok/Meta Ads Library | One-pager thị trường + ước tính ARPDAU/retention mục tiêu |
| **B2B SaaS (US/EU)** | 1) [SaaS Market Research](./apps-saas/saas-market-research.md); 2) [B2B Sales Intelligence](./apps-saas/b2b-sales-intelligence.md); 3) [PLG Research](./apps-saas/plg-research-framework.md); 4) Phỏng vấn: [Primary Research 101](./core/primary-research-101.md) | Similarweb, BuiltWith, LinkedIn Sales Navigator, Crunchbase/Pitchbook, G2/Capterra review mining | Slide 5-10 trang: ICP, pain, willingness-to-pay, top 3 đối thủ, kênh vào cửa |
| **VN-only app/game/tool** | 1) [Mobile App Market Research](./apps-saas/mobile-app-market-research.md) (nếu app); 2) [Geo & Localization](./core/geo-localization-guide.md) (payment, PPP, kênh VN); 3) Survey/interview nội địa: [Primary Research 101](./core/primary-research-101.md); 4) Pricing local/PPP | Similarweb country split, Google Trends (VN), local store charts, Adsota/Q&Me reports, Momo/ZaloPay data points | Dashboard nhẹ + quyết định pilot: kênh UA VN, pricing VND, backlog localization |
| **Console/PC premium launch** | 1) [Game Market Research](./games/game-market-research.md) (PC/console focus); 2) Check wishlist/CCU/price band đối thủ; 3) Press/creator plan; 4) Regional pricing theo PPP [Geo & Localization](./core/geo-localization-guide.md) | SteamDB, VGInsights/Gamalytic, creator coverage (Twitch/YouTube), platform cut/fee | One-pager giá/định vị + lịch PR/creator + benchmark review score |
| **Marketplace 2-sided** | 1) Xác định bên cung/cầu và chicken-egg; 2) Nghiên cứu pricing/fee cấu trúc; 3) Phỏng vấn đôi bên [Primary Research 101](./core/primary-research-101.md); 4) Theo dõi liquidity metrics | Similarweb, BuiltWith (stack), search volume, job posts của đối thủ, G2/Capterra (nếu B2B) | Slide ngắn: ICP đôi bên, take rate, kênh acquire mỗi bên, rủi ro churn/liquidity |
| **B2B APAC (SEA/India/JP/KR)** | 1) [SaaS Market Research](./apps-saas/saas-market-research.md); 2) Geo đặc thù: [Geo & Localization](./core/geo-localization-guide.md) (payment, PPP, kênh local); 3) Local proof/partners; 4) Pricing local vs USD | Similarweb by country, AppMagic/Data.ai (nếu app), LinkedIn Sales Navigator theo country, local payment/UPI, compliance note | Plan 1-2 country pilot, pricing đề xuất theo PPP, danh sách partner/kênh local |
| **Marketplace B2C (EU)** | 1) Xác định category & fee/cancellation policy của đối thủ; 2) Demand-side research (survey/traffic); 3) Supply acquisition plan; 4) Privacy/GDPR check | Similarweb (EU split), search trends, AppMagic/Data.ai nếu mobile, Trustpilot reviews, GDPR basics | One-pager: fee/commission benchmark, top channels (paid/SEO/affiliate), rủi ro CAC/return, GDPR notes |
| **Fintech (compliance-first)** | 1) Kiểm tra khung pháp lý (KYC/AML, PSD2/Open Banking, license); 2) Đối thủ & pricing; 3) Primary research user trust & willingness-to-switch; 4) Security/infra note | Regulator docs, licensing list, Similarweb, app store reviews (trust), bank API/provider (Plaid/Tink), legal counsel checklist | Slide: compliance requirements, cạnh tranh, giá/fee, rủi ro pháp lý, kế hoạch sandbox/pilot |
| **Edtech K12** | 1) Segment (phụ huynh vs học sinh vs trường); 2) Giá/ARPU và lịch năm học; 3) Content localization & curriculum fit; 4) Kênh phân phối (school, phụ huynh online, teacher community) | Similarweb/AppMagic/Data.ai, search volume theo môn/lớp, local curriculum requirements, parent forums/groups | One-pager: segment/needs, seasonality, pricing gói, kênh acquire, rủi ro churn/compliance |

### 🔗 Cross-links hữu ích
- **Side-hustle & freelancing:** [Freelancer Framework](../../03-career-skills/productivity/side-hustle/freelancer-framework.md), [Freelancer Roadmap](../../03-career-skills/productivity/side-hustle/freelancer-roadmap.md), [Content Creation Blueprint](../../03-career-skills/productivity/side-hustle/content-creation-blueprint.md).
- **Investing / validation mindset:** xem `domains/data-analytics/` (phân tích dữ liệu), `guides/03-career-skills/career/indie-hacker-roadmap.md`, và nếu cần góc đầu tư thị trường rộng hơn: `domains/blockchain/` và `guides/03-career-skills/productivity/side-hustle/monetization-models.md`.
- **Related guides:** [MMO Roadmap](../mmo-roadmap/README.md), macro/industry góc đầu tư (xem `domains/blockchain/`, `resources/vietnam-it-landscape.md`), và productivity/side-hustle cho validation ý tưởng (`guides/03-career-skills/productivity/README.md`).

## 🧰 Tools & Data Sources (tập trung)
- **App/SaaS:** Similarweb, BuiltWith, Wappalyzer, G2/Capterra review mining, LinkedIn Sales Navigator, Crunchbase/Pitchbook (paid), Product Hunt/Betalist.
- **Mobile:** Data.ai / Sensor Tower (paid), AppMagic (mid), ASO tools (AppTweak, MobileAction), Mobbin/UXArchive (UX patterns), Google Play Console (own app data).
- **Game:** SteamDB, Gamalytic, VGInsights, Noicecharts, Itch analytics; mobile game cũng dùng Data.ai/Sensor Tower.
- **Ads/Creatives:** Meta Ads Library, TikTok Creative Center, Pinterest Ads, Spy tools (BigSpy, Pipiads), YouTube Ads Transparency.
- **Geo/localization:** Google Trends, Similarweb by country, local app stores, local payment/PPP data.
- **Primary research tools:** Typeform/Google Forms, Lookback/Zoom for interviews, UserTesting/PlaytestCloud (paid), Airtable/Sheets cho mã hóa dữ liệu.
- (Mỗi trang con vẫn có tools cụ thể; đây là bản tập trung để tra nhanh.)

👉 **Bảng tra nhanh theo use case:** [Tools & Data Sources](./core/tools-and-data-sources.md)
👉 **Cách báo cáo & kể chuyện:** [Research Reporting Playbook](./strategy/research-reporting-playbook.md)
👉 **Chọn thị trường & localize:** [Geo & Localization Research](./strategy/geo-and-localization-research.md)

---

## 📚 Mục lục

1.  **[Introduction to Market Research](./core/introduction-to-market-research.md)**
    *   Tại sao Market Research quan trọng?
    *   Các phương pháp nghiên cứu cơ bản (Qualitative vs Quantitative).
    *   Công cụ cần thiết (Tools).

2.  **[Competitor Analysis Framework](./core/competitor-analysis-framework.md)**
    *   Cách xác định đối thủ (Direct vs Indirect).
    *   SWOT Analysis (Điểm mạnh, yếu, cơ hội, thách thức).
    *   Phân tích Pricing & Business Model.

3.  **[Game Market Research (Deep Dive)](./games/game-market-research.md)**
    *   Phân tích thị trường trên Steam (SteamDB, Gamalytic).
    *   Phân tích thị trường Mobile (Sensor Tower, Data.ai).
    *   Cách tìm "Blue Ocean" (Đại dương xanh) trong ngành Game.

4.  **[Mobile App Market Research](./apps-saas/mobile-app-market-research.md)**
    *   ASO Intelligence (Nghiên cứu từ khóa).
    *   **[Advanced Monetization](./apps-saas/mobile-app-monetization-advanced.md):** Hybrid Strategy, Subscription Optimization.
    *   UI/UX Research (Mobbin).

5.  **[SaaS Market Research](./apps-saas/saas-market-research.md)**
    *   **[B2B Sales Intelligence](./apps-saas/b2b-sales-intelligence.md):** ICP, Decision Maker Mapping.
    *   **[PLG Research](./apps-saas/plg-research-framework.md):** Viral Loop, Time-to-Value.
    *   Review Mining & Tech Stack Analysis.

6.  **[MMO & Automation Tools Research](./games/mmo-tools-market-research.md)**
    *   Nghiên cứu thị trường ngách (Underground).
    *   Social Media Automation & E-commerce Tools.
    *   Chiến lược Pre-sale trong cộng đồng kín.

7.  **[User Research & Persona](./core/user-research-persona.md)**
    *   Xây dựng chân dung khách hàng (User Persona).
    *   Phỏng vấn người dùng (User Interviews).
    *   Khảo sát (Surveys) hiệu quả.
    *   **[Primary Research 101](./core/primary-research-101.md)**: khi nào dùng interview/survey, cỡ mẫu, bias, checklist.

8.  **[Validation Strategy](./strategy/validation-strategy.md)**
    *   MVP (Minimum Viable Product) vs SLC (Simple Lovable Complete).
    *   Landing Page Test.
    *   Fake Door Testing.

---

## 🚀 Advanced Strategy (Nâng cao)

Dành cho Startup Founders và những người muốn đi sâu vào chiến lược kinh doanh:

9.  **[Market Sizing & Forecasting](./strategy/market-sizing-forecasting.md)**
    *   TAM / SAM / SOM Framework.
    *   Mô hình dự báo doanh thu (Revenue Modeling).
    *   Fermi Estimation (Ước lượng nhanh).

10. **[Advanced Pricing Strategy](./strategy/advanced-pricing-strategy.md)**
    *   Định giá tâm lý (Psychological Pricing).
    *   Van Westendorp Model (Tìm giá tối ưu).
    *   Chiến lược giá theo vùng (Localized Pricing - PPP).

11. **[Ad Monetization & eCPM Optimization](./strategy/ad-monetization-ecpm.md)**
    *   Tối ưu hóa eCPM & Fill Rate.
    *   Waterfall vs Bidding (Chiến lược đấu giá).
    *   Các định dạng quảng cáo hiệu quả nhất (Rewarded Video).

12. **[Trend Spotting & Alpha Hunting](./strategy/trend-spotting-alpha.md)**
    *   Phân biệt Trend (Xu hướng) vs Fad (Nhất thời).
    *   Công cụ săn tìm Alpha (GitHub Trending, Product Hunt).
    *   Chiến lược Fast Follow.

---

## 💡 Quick Tips

*   **Bắt đầu sớm:** Đừng đợi đến khi build xong sản phẩm mới nghiên cứu.
*   **Dữ liệu không nói dối:** Hãy tin vào số liệu hơn là cảm tính.
*   **Đối thủ là thầy:** Học từ thành công và thất bại của họ.
