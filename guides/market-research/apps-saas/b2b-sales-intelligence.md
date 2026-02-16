# 💼 B2B Sales Intelligence & ICP Research

> [← Back to Apps & SaaS](./saas-market-research.md) | [Back to Main](../README.md)

Trong B2B, bạn không bán cho "doanh nghiệp", bạn bán cho **con người** trong doanh nghiệp đó.

---

## 1. Ideal Customer Profile (ICP) - Chân dung Khách hàng Lý tưởng

Đừng cố bán cho tất cả. Hãy vẽ ra chân dung công ty có khả năng mua cao nhất.

### 4 Yếu tố của ICP:
1.  **Firmographics (Đặc điểm công ty):**
    *   Ngành nghề (Industry): Thương mại điện tử, Bất động sản, SaaS?
    *   Quy mô (Size): 1-10 người (SMB), 50-200 (Mid-market), hay 1000+ (Enterprise)?
    *   Vị trí (Location): US, UK, hay Vietnam?
2.  **Technographics (Công nghệ sử dụng):**
    *   Họ đang dùng tool gì? (Nếu họ dùng Shopify, họ có thể cần Klaviyo. Nếu họ dùng AWS, họ cần tool tối ưu Cloud).
3.  **Revenue:** Doanh thu ước tính (để biết họ có ngân sách $500/tháng cho tool của bạn không).
4.  **Growth Signal:** Họ có đang tuyển dụng không? (Tuyển nhiều Sales -> Cần CRM. Tuyển nhiều Dev -> Cần tool quản lý dự án).

---

## 2. Technographics Tools (Công cụ soi công nghệ)

Làm sao biết khách hàng đang dùng tool gì?

*   **BuiltWith / Wappalyzer:**
    *   Nhập website khách hàng -> Biết họ dùng WordPress, Shopify, HubSpot, Google Analytics...
    *   *Chiến thuật:* Tìm tất cả website dùng "WooCommerce" nhưng chưa dùng "Email Marketing Tool" nào -> Chào hàng tool của bạn.
*   **LinkedIn Sales Navigator:**
    *   Tìm các công ty đang tuyển dụng "ReactJS Developer" -> Họ đang làm app React -> Chào hàng tool test React.

---

## 3. Decision Maker Mapping (Bản đồ ra quyết định)

Trong một công ty B2B, người dùng tool (User) và người ký séc (Buyer) thường là 2 người khác nhau.

| Vai trò | Đặc điểm | Pain Point | Chiến thuật tiếp cận |
| :--- | :--- | :--- | :--- |
| **User (End-user)** | Nhân viên, Dev, Marketer. | Mất thời gian làm việc tay chân, tool cũ khó dùng. | Cho dùng thử Free. Biến họ thành "Fan" để họ đề xuất lên sếp. |
| **Champion (Người ủng hộ)** | Trưởng nhóm, Manager. | Muốn team đạt KPI, muốn giảm lỗi. | Gửi Case Study, báo cáo hiệu quả (ROI). |
| **Buyer (Economic Buyer)** | CEO, CFO, VP. | Quan tâm giá, bảo mật, ROI. Không quan tâm tính năng. | Nhấn mạnh "Tiết kiệm chi phí", "Tăng doanh thu", "Bảo mật". |
| **Blocker (Kẻ cản trở)** | IT Manager, Legal. | Sợ rủi ro, sợ tool mới không tương thích. | Gửi tài liệu Compliance (SOC2, GDPR), Integration Docs. |

-> **Chiến lược:** Tiếp cận **User** trước (Bottom-up) để tạo nhu cầu, sau đó tiếp cận **Buyer** (Top-down) để chốt deal.

---

## 4. 📧 Cold Outreach Playbook (Kịch bản Tiếp cận)

Đừng gửi email spam hàng loạt ("Hi Sir, buy my tool"). Hãy dùng chiến thuật **Spear Fishing** (Săn cá bằng lao).

### Nguyên tắc 3C:
*   **Company:** Chứng minh bạn đã tìm hiểu về công ty họ.
*   **Context:** Tại sao bạn liên hệ NGAY LÚC NÀY? (Họ mới gọi vốn? Họ mới tuyển người?).
*   **Call to Action (CTA):** Đừng đòi meeting 30p. Hãy hỏi 1 câu Yes/No đơn giản.

### Mẫu Email 1: The "Observation" (Quan sát)
> **Subject:** Câu hỏi về quy trình [Tech Stack] của [Tên Công ty]
>
> Chào [Tên],
>
> Mình thấy trên BuiltWith là [Công ty] đang dùng Shopify nhưng chưa cài tool [Email Marketing] nào.
>
> Thông thường các shop size như bên bạn đang mất khoảng 20% doanh thu vì không có abandoned cart flow.
>
> Mình có build một tool nhỏ giúp auto hóa việc này trong 5 phút. Bạn có muốn xem thử demo không?

### Mẫu Email 2: The "Pain Point" (Nỗi đau)
> **Subject:** [Vấn đề X] tại [Tên Công ty]?
>
> Chào [Tên],
>
> Mình thấy bên bạn đang tuyển 5 Sales mới. Chắc hẳn việc quản lý lead thủ công đang khá rối (mình từng gặp y hệt ở công ty cũ).
>
> Tool bên mình giúp auto-assign lead cho Sales, giảm thời gian chết xuống 0.
>
> Mình gửi bạn case study bên [Đối thủ cạnh tranh] đã dùng để tăng 30% sales nhé?

---

## 5. 🛠️ Modern B2B Sales Stack (Bộ công cụ)

Đừng làm thủ công. Hãy dùng tool để scale.

### **Data Enrichment (Tìm thông tin liên hệ)**
*   **Apollo.io:** Database khổng lồ chứa email/SĐT doanh nghiệp. (Có gói Free tốt).
*   **ZoomInfo:** Đắt nhưng xịn nhất cho thị trường Mỹ.

### **Intent Data (Ai đang muốn mua?)**
*   **Bombora:** Cho biết công ty nào đang search từ khóa liên quan đến bạn.
*   **G2 Buyer Intent:** Cho biết ai đang xem profile của... đối thủ bạn. -> *Cướp khách ngay!*

### **CRM & Outreach Automation**
*   **Lemlist / Instantly:** Gửi cold email tự động, có tính năng "warm-up" để không vào spam.
*   **HubSpot:** CRM miễn phí tốt nhất để quản lý deal.

---

## 6. Qualification Framework (Lọc khách hàng)

Đừng tốn thời gian với những người không bao giờ mua.

### **BANT (Cổ điển - Phù hợp SMB)**
*   **Budget:** Họ có tiền không?
*   **Authority:** Người này có quyền ký không?
*   **Need:** Họ có đau thật không?
*   **Timing:** Họ cần ngay bây giờ hay năm sau?

### **MEDDIC (Hiện đại - Phù hợp Enterprise)**
*   **Metrics:** Chỉ số nào quyết định thành công? (VD: Tiết kiệm $10k/tháng).
*   **Economic Buyer:** Ai là người cầm quỹ?
*   **Decision Criteria:** Họ so sánh dựa trên tiêu chí gì? (Giá hay Tính năng?).
*   **Decision Process:** Quy trình duyệt chi ra sao? (Cần sếp ký? Cần IT review?).
*   **Identify Pain:** Nỗi đau cụ thể là gì?
*   **Champion:** Ai là người sẽ bán tool này cho sếp thay bạn?

