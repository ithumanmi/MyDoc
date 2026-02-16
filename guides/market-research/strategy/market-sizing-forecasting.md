# 📈 Market Sizing & Forecasting

> [← Back to Market Research](./README.md)

Khi bạn pitching với nhà đầu tư hoặc tự mình quyết định có nên "all-in" vào dự án hay không, câu hỏi quan trọng nhất là: **"Thị trường này lớn đến mức nào?"**.

---

## 1. TAM / SAM / SOM Framework

Đừng nói chung chung "Thị trường game trị giá 200 tỷ đô". Hãy chia nhỏ nó ra để thực tế hơn.

### **TAM (Total Addressable Market)**
*   **Định nghĩa:** Tổng nhu cầu thị trường toàn cầu nếu bạn độc quyền 100% (Điều không thể).
*   *Ví dụ:* Tổng doanh thu của tất cả các game thể loại Roguelike trên Steam ($500M/năm).

### **SAM (Serviceable Addressable Market)**
*   **Định nghĩa:** Phần thị trường bạn thực sự có thể phục vụ với sản phẩm của mình (dựa trên ngôn ngữ, nền tảng, địa lý).
*   *Ví dụ:* Game của bạn chỉ có tiếng Anh + tiếng Việt, chạy trên PC (Windows). SAM = Doanh thu Roguelike PC (EN + VI) ($100M/năm).

### **SOM (Serviceable Obtainable Market)**
*   **Định nghĩa:** Phần thị phần bạn thực tế có thể chiếm được trong 1-3 năm đầu (dựa trên ngân sách marketing và đối thủ).
*   *Ví dụ:* Với ngân sách $10k marketing, bạn kỳ vọng chiếm 0.5% thị phần SAM. SOM = $100M * 0.5% = **$500k/năm**. -> Đây là con số mục tiêu của bạn.

> 👉 **Xem thực hành:** [Ví dụ tính toán TAM/SAM/SOM chi tiết cho Game](./game-market-sizing-practice.md)

---

## 2. Fermi Estimation (Phép tính ước lượng)

Khi không có số liệu chính xác, hãy dùng tư duy Fermi để phỏng đoán có cơ sở.

**Bài toán:** Có bao nhiêu người Việt sẵn sàng mua tool nuôi nick Facebook giá 200k/tháng?

**Cách tính:**
1.  **Dân số:** 100 triệu người.
2.  **Số người kinh doanh online:** Giả sử 5% (5 triệu người).
3.  **Số người cần nuôi nick (Seeding):** Giả sử 10% trong số đó (500k người).
4.  **Số người sẵn sàng trả tiền (Conversion Rate):** Thường là 1-2% (5k - 10k người).
5.  **Doanh thu tiềm năng:** 5,000 * 200,000đ = **1 tỷ VNĐ/tháng**.

-> Con số này đủ hấp dẫn để làm không? Có.

---

## 3. Revenue Modeling (Mô hình Doanh thu)

Tạo một bảng Excel đơn giản để dự báo dòng tiền.

| Chỉ số (Metric) | Kịch bản Xấu (Worst) | Kịch bản Trung bình (Base) | Kịch bản Tốt (Best) |
| :--- | :--- | :--- | :--- |
| **Traffic (Visitors/mo)** | 1,000 | 5,000 | 20,000 |
| **Conversion Rate (%)** | 1% | 2% | 3% |
| **Số khách hàng (Buyers)** | 10 | 100 | 600 |
| **Giá bán (ARPPU)** | $10 | $15 | $20 |
| **Doanh thu tháng (MRR)** | **$100** | **$1,500** | **$12,000** |

*   **Lời khuyên:** Luôn chuẩn bị tâm lý cho **Kịch bản Xấu nhất**. Nếu Kịch bản Xấu nhất vẫn giúp bạn đủ sống (ramen profitability) -> Hãy làm.
