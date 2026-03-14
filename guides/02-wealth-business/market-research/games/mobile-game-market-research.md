# Mobile Game Market Research

> Mục tiêu: tách riêng mobile (Hyper/Hybrid/Mid-core) với các bước ASO, creative analysis, genre lifecycle, benchmark CPI/LTV và liên kết sizing/ad monetization.

## 1) ASO cho game (khác app)
- **Keyword research theo gameplay/genre:** ví dụ “merge garden”, “survivor io”, “idle tycoon”, “anime gacha”. Dùng AppTweak/AppMagic/Data.ai.
- **Title & subtitle:** giữ brand + 1-2 keyword mạnh; A/B subtitle theo USP (roguelike idle, offline, no ads).
- **Icon & screenshots:** ưu tiên gameplay frame (power fantasy, boss fight, merge result); test nhiều variant trên Google Play Experiments hoặc ASA Creative Sets.
- **Reviews & localization:** lọc review theo ngôn ngữ để phát hiện keyword tự nhiên; localize mô tả ngắn/long description cho Tier ưu tiên.

## 2) Creative analysis (TikTok/FB Ads Library)
- **TikTok Creative Center:** filter game category, country; xem hook 3s đầu, CTA, visual motif, trend sound.
- **Meta Ads Library:** tìm theo brand/keyword; note format (UGC vs gameplay raw), caption claim, offer (no-ads pack, starter pack).
- **Benchmark:** lưu bảng "Top creatives" (hook type, claim, view count, date). Phát hiện “why it works”: power fantasy, fail montage, ASMR, choice.

## 3) Genre lifecycle: Hyper vs Hybrid vs Mid-core
- **Hyper-casual:** CPI rất nhạy (target < $0.4 US); LTV thấp (~$0.2-0.4); sống nhờ ads, cần volume lớn; lifecycle ngắn, hit-and-run.
- **Hybrid-casual:** gameplay đơn giản + meta (upgrade/merge/collection); CPI cao hơn (0.7-2.0 US), LTV 1-5$ nếu retention ổn; cần creative liên tục.
- **Mid-core (RPG/4X/SLG):** CPI cao (5-20$+ Tier1), LTV cao nếu giữ được whales; đòi hỏi UA + liveops nặng.

## 4) Benchmark CPI/LTV theo genre (gợi ý khung)
- **Hyper-casual:** CPI US mục tiêu < $0.40; eCPM Tier1 ~ $10-25; LTV global ~ $0.2-0.5.
- **Hybrid-casual:** CPI US mục tiêu 0.7-2.0; LTV 1-5$ (tùy meta/retention); eCPM Tier1 ~ $15-30.
- **Puzzle/Match/Decor:** CPI US 1-3$; LTV 2-8$ nếu IAP mạnh; ad+IAP hybrid thường tốt.
- **RPG/4X/SLG:** CPI US 5-20$+; LTV 20-100$+; cần target whales, offer ladder, events.
- **Idle/Incremental:** CPI US 0.8-2.0; LTV 1-4$; ad-first hybrid phù hợp.
> Tham khảo thêm báo cáo public của Data.ai/Sensor Tower và ad network eCPM reports theo geo.

### Bảng benchmark CPI / LTV theo geo (tham khảo, cần cập nhật theo thời điểm)

| Genre              | CPI Tier1 (US/CA/UK/EU5/JP/KR) | CPI Tier2/3 (SEA/LatAm/India/MENA/EE) | LTV Tier1 (ước lượng) | LTV Tier2/3 (ước lượng) |
| ------------------ | ------------------------------- | -------------------------------------- | --------------------- | ------------------------ |
| Hyper-casual       | $0.25 - $0.40                  | $0.05 - $0.15                          | $0.2 - $0.5           | $0.05 - $0.15            |
| Hybrid-casual      | $0.70 - $2.00                  | $0.20 - $0.60                          | $1 - $5               | $0.3 - $1.5              |
| Puzzle/Match/Decor | $1.00 - $3.00                  | $0.30 - $0.90                          | $2 - $8               | $0.7 - $2.5              |
| Idle/Incremental   | $0.80 - $2.00                  | $0.20 - $0.80                          | $1 - $4               | $0.4 - $1.5              |
| RPG/4X/SLG         | $5.00 - $20.00+                | $1.00 - $6.00                          | $20 - $100+           | $5 - $25                 |

Ghi chú:
- Dữ liệu mang tính khung tham chiếu; luôn kiểm tra report mới nhất của Data.ai/Sensor Tower và network eCPM.
- CPI Tier1 cao hơn nhưng eCPM và ARPPU cao → phù hợp ad-first (hyper) lẫn IAP mạnh (puzzle/RPG).
- Tier2/3 rẻ để test ý tưởng/creative, nhưng LTV thấp; cân nhắc geo mix (US + PH/BR/ID) để vừa đo chất lượng vừa tối ưu chi phí.

## 5) Quy trình nhanh để test market
1) Chọn 1-2 geo: US (Tier1) và 1 geo giá rẻ (PH/ID/BR) để đo CPI baseline.
2) Soft launch với 3-5 creatives khác biệt (hook/angle khác nhau), 2-3 icon/screenshot variant.
3) Đo CPI, D1 retention, eCPM; kill nếu CPI quá cao so với khung genre.
4) Nếu pass: mở rộng creative variations, tối ưu onboarding, thêm meta (nếu hyper→hybrid).

## 6) Liên kết nhanh
- Sizing mobile (casual/hybrid): [Game Market Sizing Practice](./game-market-sizing-practice.md) (mục Casual Mobile)
- Tối ưu quảng cáo & eCPM: [Ad Monetization & eCPM](../strategy/ad-monetization-ecpm.md)
- Geo & localization: [Geo & Localization Research](../strategy/geo-and-localization-research.md)
- Reporting: [Research Reporting Playbook](../strategy/research-reporting-playbook.md)