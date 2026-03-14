# ☁️ SaaS Market Research (B2B & Web App Focus)

> [← Back to Market Research](./README.md)

Hướng dẫn nghiên cứu thị trường cho Software as a Service (SaaS), tập trung vào B2B và Web Applications.

---

### 1. Intent Research (Nghiên cứu Ý định Tìm kiếm)
*   **[B2B Sales Intelligence](./b2b-sales-intelligence.md):** Cách tìm kiếm khách hàng doanh nghiệp, vẽ chân dung ICP và bản đồ ra quyết định.
*   **[PLG Research Framework](./plg-research-framework.md):** Nghiên cứu cơ chế "Product-Led Growth" (Viral Loop, Time-to-Value) của đối thủ.

### 2. SEO Tools & Review Mining
Khách hàng SaaS thường có ý định rõ ràng khi tìm kiếm giải pháp.
*   **SEO Tools (Ahrefs / Semrush):**
    *   **"Alternative to X":** Tìm những người đang chán ghét đối thủ lớn.
    *   **"How to [Problem]":** Tìm vấn đề mà khách hàng đang gặp phải.
*   **Review Platforms (G2 / Capterra):**
    *   Tìm "Dislikes" của đối thủ để làm tính năng cạnh tranh.

---

## 3. Pricing & Tech Stack Analysis

Bạn cần biết đối thủ (hoặc khách hàng tiềm năng) đang dùng công nghệ gì.

### Công cụ
*   **BuiltWith / Wappalyzer:** Xem website đối thủ dùng công nghệ gì (React, Vue, AWS, Stripe...).
*   **Lợi ích:**
    *   Biết họ dùng dịch vụ gì để... chào hàng dịch vụ thay thế (nếu bạn làm tool cho dev).
    *   Biết họ tích hợp với ai (Integrations) -> Bạn cũng nên tích hợp với những tool đó (VD: Slack, Zapier).

---

## 4. Pricing Strategy (Chiến lược Giá)

SaaS Pricing là một nghệ thuật tâm lý.

### Các mô hình phổ biến
*   **Per User (Theo đầu người):** $10/user/tháng. (Phổ biến nhất B2B).
*   **Tiered (Theo gói):** Basic ($0) - Pro ($29) - Enterprise (Contact us).
*   **Usage-based (Theo dung lượng):** Trả theo số lượng email gửi đi, số GB lưu trữ. (AWS, Mailgun).

### Phân tích đối thủ
*   Họ có **Free Plan** hay chỉ có **Free Trial**?
    *   *Free Plan:* Thu hút nhiều user rác, tốn resource nhưng viral tốt (Product-Led Growth).
    *   *Free Trial:* Lọc được user chất lượng, conversion cao hơn.
*   Giá trị cốt lõi (Core Value) nằm ở gói nào?
    *   Thường họ sẽ giấu tính năng hay nhất ở gói giữa (Pro) để hướng user mua gói đó (Decoy Effect).

---

## 5. Cold Outreach Test (Kiểm chứng B2B)

Khác với B2C (chạy ads), B2B có thể kiểm chứng bằng cách... đi bán hàng trực tiếp.

*   Tìm 10 khách hàng tiềm năng trên LinkedIn.
*   Gửi tin nhắn: *"Chào [Tên], mình thấy công ty bạn đang dùng [Đối thủ]. Mình đang xây dựng một tool giúp giải quyết [Vấn đề X] mà [Đối thủ] đang gặp phải (dựa trên research G2). Bạn có muốn dùng thử bản Beta miễn phí không?"*
*   Nếu 3/10 người trả lời -> Tín hiệu tốt.

---

## 6. Competitive Win/Loss (Học từ thắng/thua)

**Mục tiêu:** Hiểu vì sao bạn thắng/thua deal để ưu tiên roadmap và messaging.

### Cách thu thập
- **Sales feedback ngay sau deal:** note lý do win/loss (price, feature, security, timing, incumbent lock-in).
- **Post-churn survey / exit interview:** ngắn gọn (2-4 câu hỏi), ưu tiên open-ended.
- **CS/support signals:** ticket lặp lại về thiếu tính năng, performance, UX.
- **Third-party reviews (G2/Capterra) của bạn và đối thủ:** lọc "dislikes", "reasons for switching".

### Template câu hỏi (rút gọn)
1) Điều gì khiến bạn chọn / không chọn chúng tôi? (top 1-2 lý do)
2) Nếu chọn đối thủ khác: họ hơn ở điểm nào? (tính năng, giá, bảo mật, tích hợp...)
3) Có tính năng/bảo mật/tích hợp nào thiếu khiến bạn không yên tâm?
4) Điều gì cần có để bạn cân nhắc chúng tôi trong 3-6 tháng nữa?

### Map feature gap / hành động
- Gom lý do loss theo nhóm: **Price**, **Feature Gap**, **Security/Compliance**, **Integration**, **Performance/UX**, **Timing/Budget freeze**.
- Với **Feature Gap**: map sang backlog (P0/P1) và ghi rõ "loss count" để ưu tiên.
- Với **Price**: xem lại packaging (đưa tính năng đắt vào add-on/tier cao), cạnh tranh theo ROI thay vì hạ giá chung.
- Với **Security/Compliance**: chuẩn bị một-pager (SOC2/GDPR, SSO/SCIM, DPA, data residency) để giảm loss vì rủi ro.
