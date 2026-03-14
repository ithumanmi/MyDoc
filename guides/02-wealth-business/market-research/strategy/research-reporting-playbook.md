# Research Reporting & Storytelling Playbook

> Mục tiêu: Research phải dẫn tới **quyết định** (so what) chứ không chỉ dừng ở thông tin.

## 1) Output nhanh: One-pager

**Cấu trúc 1 trang:**
- **Problem / Goal:** Câu hỏi kinh doanh cần trả lời (decision question).
- **Method:** Bạn đã làm gì? (Secondary, interview, survey, scrape, benchmark).
- **Findings:** 3-5 phát hiện chính (bullet, có số liệu nếu có).
- **Implications (So what):** Ý nghĩa đối với sản phẩm/kênh/định vị.
- **Next steps / Decision:** Chọn A/B, thử nghiệm gì, ai chịu trách nhiệm, deadline.

Mẫu gợi ý (copy/paste):
```
Problem: Giảm churn gói Pro 20% trong 90 ngày.
Method: 12 interview power users + 150 survey; benchmark 5 đối thủ chính.
Findings:
- 48% rời đi vì thiếu integration X; 32% vì giá.
- Đối thủ Y khóa tính năng integration ở gói cao hơn, giá +25%.
Implications:
- Ưu tiên build integration X, giảm giá không phải đòn chính.
Next steps:
- Sprint build integration X (owner: Eng), ship trong 3 tuần.
- AB test messaging “integration X” trên landing (owner: Growth).
```

## 2) Slide deck (pitch-ready)
- **TAM/SAM/SOM**: 1 slide (con số + cách tính ngắn gọn, nguồn).
- **Competitor matrix**: 1 slide (tính năng/giá/kênh). Link chi tiết: [Competitor Analysis](../core/competitor-analysis-framework.md).
- **So what**: 1 slide tổng hợp quyết định/ưu tiên.
- **Back pocket** (appendix): dữ liệu chi tiết, survey chart, quote.

## 3) Dashboard theo dõi đối thủ (lean)
- **Mục tiêu:** nhìn nhanh biến động quan trọng, tránh quá tải.
- **Bảng tối thiểu:**
  - Metric | Đối thủ | Giá trị | Nguồn | Tần suất cập nhật | Ghi chú hành động
  - Ví dụ metric: giá gói, feature flag, traffic share, ad spend ước tính, ranking store, release mới.
- **Nguồn & tần suất:**
  - Pricing page (manual monthly), Ads Library (weekly), Similarweb (monthly), Data.ai/Sensor Tower (weekly), SteamDB/VGInsights (weekly), G2/Capterra reviews (monthly), BuiltWith/Wappalyzer (quarterly).
- **Cảnh báo (alert):** thiết lập watch (RSS/change monitor) cho pricing page, release note, store ranking.

## 4) Storytelling tips
- Bắt đầu bằng câu hỏi quyết định (decision question), không phải phương pháp.
- Dùng 3-5 bullet insight; mỗi bullet có số liệu hoặc quote.
- Trả lời "So what?" và "What next?" ngay trên slide.
- Giới hạn 10-15 slide; đưa chi tiết vào appendix.
- Nêu rõ nguồn và ngày thu thập; tránh tranh luận "số liệu từ đâu".

## 5) Checklist
- [ ] Có decision question rõ ràng
- [ ] One-pager đủ 5 phần (Problem, Method, Findings, Implications, Next steps)
- [ ] Slide deck có 3 slide chính (TAM/SAM/SOM, Competitor matrix, So what)
- [ ] Dashboard lean với metric, nguồn, tần suất
- [ ] Link nguồn & ngày thu thập

## 6) Liên kết nhanh
- Phân tích đối thủ chi tiết: [Competitor Analysis](../core/competitor-analysis-framework.md)
- Market sizing & TAM/SAM/SOM: [Market Sizing & Forecasting](./market-sizing-forecasting.md)
- Primary research (interview/survey): [Primary Research 101](../core/primary-research-101.md)