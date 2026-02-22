# 📊 SaaS Metrics Bible: Các chỉ số sống còn của Startup

> [← Back to Tech Startup](./README.md)

Làm SaaS (Software as a Service) giống như cho thuê nhà. Bạn tốn tiền xây nhà 1 lần (Acquisition), và thu tiền thuê hàng tháng (Subscription).
Để thành công, bạn phải hiểu rõ các chỉ số sau.

---

## 1. Doanh thu (Revenue)

### **MRR (Monthly Recurring Revenue)**
*   Tổng doanh thu định kỳ hàng tháng.
*   Chỉ tính phí thuê bao, không tính phí cài đặt 1 lần (Setup fee).
*   *Ý nghĩa:* Đây là "nhịp tim" của SaaS. MRR tăng = Sức khỏe tốt.

### **ARR (Annual Recurring Revenue)**
*   `ARR = MRR x 12`.
*   Dùng để định giá công ty khi gọi vốn (Valuation thường = 10x - 20x ARR).

---

## 2. Retention & Churn (Giữ chân & Rời bỏ)

### **Churn Rate (Tỷ lệ rời bỏ)**
*   `Churn Rate = (Số khách hàng hủy trong tháng / Tổng khách hàng đầu tháng) x 100%`.
*   *Ví dụ:* Đầu tháng có 100 khách, cuối tháng 5 khách hủy -> Churn Rate = 5%.
*   **The Leaky Bucket:** Nếu Churn cao, bạn cứ đổ thêm nước (khách mới) vào cái xô thủng -> Không bao giờ đầy.
*   *Mục tiêu:* Churn < 5% (B2C) và < 1% (B2B Enterprise).

### **LTV (Lifetime Value)**
*   Giá trị trọn đời của một khách hàng.
*   `LTV = (ARPU / Churn Rate)`.
    *   *ARPU:* Doanh thu trung bình trên một người dùng (Average Revenue Per User).
*   *Ví dụ:* Khách trả $50/tháng, Churn Rate là 5% -> LTV = $50 / 0.05 = $1000.

---

## 3. Hiệu quả kinh doanh (Unit Economics)

### **CAC (Customer Acquisition Cost)**
*   Chi phí để có 1 khách hàng trả phí (Paid Customer).
*   `CAC = Tổng tiền Sales & Marketing / Số khách hàng mới`.

### **LTV / CAC Ratio**
*   Tỷ lệ vàng quyết định sự sống chết.
*   **< 1:** Lỗ vốn (Chi 1 đồng quảng cáo, thu về < 1 đồng). -> Chết chắc.
*   **= 3:** Khỏe mạnh (Chi 1 đồng, thu về 3 đồng). -> Chuẩn mực ngành.
*   **> 5:** Quá tốt (Hoặc bạn đang chi quá ít cho Marketing, bỏ lỡ cơ hội tăng trưởng).

---

## 4. Payback Period (Thời gian thu hồi vốn)

*   `Payback Period = CAC / (ARPU - Cost to Serve)`.
*   Mất bao lâu để bạn lấy lại số tiền đã chi ra để mua khách hàng đó?
*   *Mục tiêu:* < 12 tháng. (Tốt nhất là < 6 tháng).

---

## 5. The Rule of 40 (Quy tắc 40)

Dành cho các Startup đã trưởng thành (Growth Stage).
> **Growth Rate (%) + Profit Margin (%) >= 40%**

*   *Ví dụ A:* Tăng trưởng 100% nhưng Lỗ 50% -> 100 - 50 = 50% (> 40%). -> **ĐẦU TƯ ĐƯỢC**. (Ưu tiên Growth).
*   *Ví dụ B:* Tăng trưởng 20% và Lãi 30% -> 20 + 30 = 50% (> 40%). -> **ĐẦU TƯ ĐƯỢC**. (Ưu tiên Profit).
*   *Ví dụ C:* Tăng trưởng 20% và Lỗ 10% -> 20 - 10 = 10% (< 40%). -> **BỎ QUA**.
