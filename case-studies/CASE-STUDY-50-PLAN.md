# 📋 Kế hoạch sưu tầm 50 Case Study

> [← README](../../README.md) | [💡 Case Studies trong README](../../README.md#-case-studies-bài-học-thực-tế)
>
> **Mục tiêu:** Xây bộ sưu tập **50 case study** chất lượng — bài học từ doanh nghiệp, cá nhân và sự kiện thực tế (Vietnam & Global), phân tích qua lăng kính mental models và domain chuyên môn.

---

## 1. Định nghĩa & Phạm vi

**Case study** trong repo này là bài viết **phân tích có cấu trúc** về:
*   **Công ty / Sản phẩm:** Thành công hay thất bại (Amazon, Uber, Nokia, startup Vietnam...).
*   **Cá nhân / Lãnh đạo:** Hành trình, quyết định, bài học (founder, kỹ sư, nhà đầu tư...).
*   **Sự kiện / Vụ việc:** Sự cố kỹ thuật, khủng hoảng, bước ngoặt thị trường.

**Không tính vào 50:** Knowledge Audits (dạng self-test), Templates, hoặc bài chỉ mô tả lý thuyết không gắn case cụ thể.

---

## 2. Phân loại & Mục tiêu từng nhóm

| Nhóm | Mô tả | Hiện có | Mục tiêu | Còn thiếu |
|:-----|:------|:--------|:---------|:----------|
| **A. Mental Models Analysis** | Phân tích case qua lăng kính một discipline (Toán, Lý, Hóa, Sinh, Lịch sử, Kỹ thuật, Kinh tế, Chiến lược...) | 12 | 20 | 8 |
| **B. Vietnam Stories** | Người / Công ty Việt Nam thành công hoặc thất bại có bài học rõ ràng | 1* | 10 | 9 |
| **C. Global Tech & Business** | Công ty / leader toàn cầu (Blitzscaling, Pivot, M&A, Crisis) | 3* | 12 | 9 |
| **D. Failure & Post-Mortem** | Thất bại dự án, sản phẩm, startup — rút kinh nghiệm có hệ thống | 2 | 5 | 3 |
| **E. Industry / Domain Deep Dive** | Một ngành hoặc một chủ đề (Delivery, Fintech, Game, AI...) qua 1–2 case điển hình | 0 | 3 | 3 |
| **Tổng** | | **~18** | **50** | **~32** |

\* Vietnam Success Stories và Global Tech Leaders là **tổng hợp nhiều người/công ty trong 1 file**; có thể tách thành từng case riêng sau để đếm đủ 50.

---

## 3. Hiện trạng (đã có)

### A. Mental Models Analysis (12)
| # | File | Lăng kính | Chủ đề |
|:--|:-----|:----------|:-------|
| 1 | startup-failure-ancient-models.md | Xã hội học / Cổ đại | Startup thất bại |
| 2 | mathematical-analysis-business-case.md | Toán (Kelly, Game theory) | Marketing thất bại |
| 3 | physics-analysis-corporate-stagnation.md | Vật lý (Entropy, Quán tính) | Trì trệ tập đoàn |
| 4 | biology-analysis-corporate-ecosystem.md | Sinh học (Chọn lọc, Nữ hoàng Đỏ) | Retail ecosystem |
| 5 | chemistry-analysis-product-launch.md | Hóa học (Xúc tác, Le Chatelier) | Viral growth |
| 6 | history-analysis-nokia-fall.md | Lịch sử (Path dependence, Lindy) | Nokia sụp đổ |
| 7 | engineering-analysis-deployment-failure.md | Kỹ thuật (Margin of safety) | Knight Capital 440M |
| 8 | economics-analysis-platform-failure.md | Kinh tế (Chi phí cơ hội, Elasticity) | Food delivery platform |
| 9 | amazon-blitzscaling-analysis.md | Chiến lược (Blitzscaling, Flywheel) | Amazon |
| 10 | blitzscaling-comparison-amazon-uber-airbnb.md | Chiến lược | So sánh Amazon / Uber / Airbnb |
| 11 | uber-legal-strategy-analysis.md | Pháp lý / Risk | Uber toàn cầu |
| 12 | *(có thể thêm 1 case FMS/Fast Correction)* | Tâm lý / Chiến lược | Công ty thoát sai nhanh |

### B. Vietnam (1 file tổng hợp)
| # | Nội dung trong file |
|:--|:--------------------|
| 1 | vietnam-success-stories.md — Nguyễn Thành Trung (Axie), Hiếu PC, ... (nhiều người trong 1 file) |

### C. Global (2–3 case đã có trong mental-models + 1 file tổng hợp)
| # | Case |
|:--|:-----|
| 1 | Amazon (blitzscaling) |
| 2 | Uber (legal), Airbnb (so sánh) |
| 3 | Nokia (history) |
| 4 | Knight Capital (engineering) |
| 5 | global-tech-leaders.md — Elon, Linus, ... (tổng hợp) |

### D. Failure & Post-Mortem
| # | File |
|:--|:-----|
| 1 | startup-failure-ancient-models.md |
| 2 | engineering-analysis-deployment-failure.md (Knight Capital) |

### E. Industry Deep Dive
| # | Ghi chú |
|:--|:--------|
| 0 | Chưa có bài dạng "một ngành qua 1–2 case" |

---

## 4. Đề xuất case cần bổ sung (để đạt ~50)

### A. Mental Models Analysis (+8)
*   [ ] **Psychology / Bias:** Một công ty hoặc sản phẩm thất bại vì cognitive bias (anchoring, overconfidence...).
*   [ ] **Systems Dynamics:** Công ty hoặc thị trường với feedback loop, delay, unintended consequences.
*   [ ] **Probability / Black Swan:** Sự kiện “đuôi béo” (Taleb-style) trong tech hoặc tài chính.
*   [ ] **Network Effects:** Case một nền tảng thắng/thua nhờ network effects.
*   [ ] **Incentive Design:** Công ty hoặc sản phẩm hỏng vì incentive sai lệch.
*   [ ] **Optionality / Antifragility:** Công ty hoặc cá nhân tận dụng optionality / antifragile.
*   [ ] **Second-Order Thinking:** Quyết định có hệ quả bậc 2 rõ ràng (positive hoặc negative).
*   [ ] **Inversion:** Phân tích “làm sao để thất bại” rồi tránh — áp vào một case thật.

### B. Vietnam Stories (+9)
*   [ ] Tiki / Sendo / Shopee Vietnam — thị trường e-commerce.
*   [ ] MoMo / ZaloPay / VNPay — fintech và payment.
*   [ ] VNG (Zing, Zalo) — từ game đến super app.
*   [ ] FPT Software / FPT Telecom — mô hình doanh nghiệp và mở rộng.
*   [ ] Lozi (Loship) — delivery và pivot.
*   [ ] Trusting Social / các startup AI Vietnam — positioning và scaling.
*   [ ] Một founder / kỹ sư Việt “ẩn” nhưng có bài học rõ (career, product, exit).
*   [ ] Một startup Việt thất bại có post-mortem công khai hoặc phân tích được.
*   [ ] Công ty gia đình / SME Việt chuyển đổi số hoặc vượt khủng hoảng.

### C. Global Tech & Business (+9)
*   [ ] Netflix — pivot DVD → streaming, content strategy.
*   [ ] Apple — design, ecosystem, pricing.
*   [ ] Google (Alphabet) — search, ads, moonshots.
*   [ ] Meta (Facebook) — network effects, crisis (Cambridge, teen mental health).
*   [ ] Tesla — vertical integration, EV, Elon.
*   [ ] Stripe — developer-first, global payments.
*   [ ] Spotify — music, podcast, B2B.
*   [ ] Một công ty đình đám sụp đổ hoặc khủng hoảng (FTX, WeWork, Theranos...).
*   [ ] Một unicorn châu Á (Grab, Gojek, Sea, Coupang...) — so sánh hoặc đối chiếu với case đã có.

### D. Failure & Post-Mortem (+3)
*   [ ] Post-mortem kỹ thuật nổi tiếng (GitLab, AWS, Azure...) — dùng template Post-Mortem.
*   [ ] Một startup đóng cửa có bài học (product-market fit, burn rate, team).
*   [ ] Một dự án nội bộ (in-house) thất bại — rút ra process/communication.

### E. Industry / Domain Deep Dive (+3)
*   [ ] Một case “EdTech Vietnam hoặc Global” — business model, scaling.
*   [ ] Một case “HealthTech / InsurTech” — regulation, unit economics.
*   [ ] Một case “AI Product (B2B hoặc B2C)” — từ research đến product và thất bại/thành công.

---

## 5. Cách sử dụng bản kế hoạch này

1. **Ưu tiên:** Chọn 1 nhóm (ví dụ B. Vietnam hoặc A. Mental Models) và làm lần lượt 2–3 case.
2. **Template:** Dùng cấu trúc có sẵn trong các file `mental-models-analysis/*.md` (Background → Phân tích qua lăng kính → Bài học).
3. **Độ dài:** Mỗi case 800–2000 từ, đủ nội dung, có link về guides/domains liên quan.
4. **Cập nhật:** Sau khi thêm case mới, cập nhật bảng trong section 3 và tick [ ] thành [x] trong section 4; cập nhật README mục Case Studies.
5. **Review 50:** Khi đạt ~50 case, review lại phân bố A–E và bổ sung chỗ còn mỏng.

---

## 6. Liên kết nhanh

*   **Thư mục Mental Models Analysis:** [case-studies/mental-models-analysis/](./mental-models-analysis/)
*   **Thư mục Stories:** [case-studies/stories/](./stories/)
*   **Template gợi ý:** [templates/project-post-mortem.md](../templates/project-post-mortem.md) cho failure; cấu trúc file trong `mental-models-analysis/` cho analysis.
*   **README — Case Studies:** [README.md#Case Studies](../../README.md#-case-studies-bài-học-thực-tế)
