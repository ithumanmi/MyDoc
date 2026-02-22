# 🎯 RAT: Riskiest Assumption Testing (Kiểm Thử Giả Định Rủi Ro Nhất)

> [← Back to Design Thinking](./design-thinking.md)

## Tại sao MVP (Minimum Viable Product) chưa đủ?
MVP thường vẫn tốn quá nhiều công sức để xây dựng (Build). Chúng ta thường mắc sai lầm là build *cả một sản phẩm* (dù là tối thiểu) chỉ để kiểm tra xem khách hàng có cần nó không.

**RAT (Riskiest Assumption Testing)** là một tư duy nâng cao hơn: Thay vì build sản phẩm, hãy **build một thử nghiệm** (Experiment) để kiểm chứng giả định rủi ro nhất.

> *"Đừng xây dựng sản phẩm, hãy xây dựng thử nghiệm."*

---

## 3 Loại Giả Định Chính (The 3 Lenses of Innovation) 🔍
Để một ý tưởng thành công, nó phải thỏa mãn 3 yếu tố:

1.  **Desirability (Mong muốn):** Khách hàng có muốn nó không?
    *   *Rủi ro:* Làm ra thứ không ai cần.
2.  **Viability (Khả thi kinh doanh):** Nó có sinh lời không?
    *   *Rủi ro:* Bán được hàng nhưng lỗ vốn.
3.  **Feasibility (Khả thi kỹ thuật):** Chúng ta có làm được không?
    *   *Rủi ro:* Ý tưởng hay nhưng công nghệ chưa cho phép hoặc quá tốn kém.

👉 **RAT tập trung vào việc tìm ra giả định nào trong 3 loại trên là RỦI RO NHẤT và kiểm tra nó đầu tiên.**

---

## Quy Trình RAT (The RAT Process) 🔄

### Bước 1: Liệt kê giả định (Identify Assumptions)
Viết ra tất cả những điều bạn *tin là đúng* để ý tưởng này thành công.
*   "Tôi tin là sinh viên sẵn sàng trả 50k/tháng cho app học tiếng Anh này." (Viability)
*   "Tôi tin là họ thích học qua video ngắn TikTok." (Desirability)
*   "Tôi tin là AI có thể chấm điểm phát âm chính xác." (Feasibility)

### Bước 2: Xác định rủi ro (Prioritize)
Sử dụng **[Assumption Mapping](./templates/assumption-mapping.md)** để tìm ra giả định nào quan trọng nhất nhưng chưa chắc chắn nhất.
*   Nếu giả định này SAI, toàn bộ dự án sẽ CHẾT. Đó chính là **Riskiest Assumption**.

### Bước 3: Thiết kế thử nghiệm (Experiment)
Đừng build app! Hãy làm cách rẻ nhất để test.
*   *Test Desirability:* Chạy quảng cáo Facebook (Fake Door) xem có ai click không.
*   *Test Viability:* Bán trước (Pre-order) trên giấy.
*   *Test Feasibility:* Làm một bản Demo kỹ thuật nhỏ (Spike).

---

## Ví Dụ: Zappos (Bán giày online) 👟
*   **Ý tưởng:** Bán giày qua mạng (năm 1999).
*   **Giả định rủi ro nhất (Desirability):** Mọi người có dám mua giày mà không được thử không?
*   **Cách làm MVP (Sai):** Xây dựng hệ thống kho vận, nhập 1000 đôi giày, thuê nhân viên, làm website xịn. -> *Tốn kém, rủi ro cao.*
*   **Cách làm RAT (Đúng):**
    *   Founder đến cửa hàng giày địa phương, xin chụp ảnh giày.
    *   Đăng lên một website đơn giản.
    *   Khi có ai đặt mua, ông ra cửa hàng mua đúng đôi đó và ship cho khách.
    *   *Kết quả:* Ông chứng minh được người ta CÓ mua giày online mà không cần tốn tiền nhập kho.

---

## So sánh MVP vs. RAT

| Đặc điểm | MVP (Minimum Viable Product) | RAT (Riskiest Assumption Testing) |
| :--- | :--- | :--- |
| **Tư duy** | Xây dựng sản phẩm (Product) | Kiểm tra giả định (Assumption) |
| **Mục tiêu** | Ra mắt sớm để học hỏi | Học hỏi sớm để quyết định có nên xây dựng không |
| **Độ phức tạp** | Trung bình (cần code/design) | Rất thấp (đôi khi chỉ là 1 Landing Page) |
| **Tốc độ** | Tuần/Tháng | Giờ/Ngày |

👉 **[Thực hành: Mẫu Assumption Mapping](./templates/assumption-mapping.md)**
