# 💰 Toán học của Sự giàu có (Financial Math)

## 1. Lãi suất kép (Compound Interest) & Số e
Lãi suất kép không chỉ là $A = P(1+r)^n$. Bản chất của nó liên quan đến hằng số $e$ (Số Euler).

### Công thức rời rạc vs Liên tục
*   **Rời rạc (Hàng năm):** $A = P(1 + r)^t$
*   **Liên tục (Continuous Compounding):** Khi kỳ hạn trả lãi chia nhỏ vô hạn (mỗi giây, mỗi tích tắc), công thức trở thành:
    $$A = P \cdot e^{rt}$$
*   **Ý nghĩa:** Sự tăng trưởng trong tự nhiên (vi khuẩn, dân số, lan truyền tin đồn) thường tuân theo hàm mũ liên tục $e^x$. Tiền bạc nếu được tái đầu tư liên tục cũng sẽ tăng trưởng theo cách này.

### Quy tắc 72 (Rule of 72)
Công thức nhẩm nhanh thời gian nhân đôi vốn:
$$t \approx \frac{72}{r}$$
*   Lãi 10%/năm -> $72/10 = 7.2$ năm nhân đôi.
*   Lãi 20%/năm (Warren Buffett) -> $72/20 = 3.6$ năm nhân đôi.

## 2. Giá trị thời gian của tiền (Time Value of Money - TVM)
Tiền có giá trị thay đổi theo thời gian do lạm phát và chi phí cơ hội.

### Hiện giá (Present Value - PV)
$$PV = \frac{FV}{(1 + r)^n}$$
*   **Bài học:** 1 tỷ đồng 10 năm sau chỉ có giá trị bằng khoảng 385 triệu hôm nay (nếu lạm phát/lãi suất là 10%). Đừng bị lừa bởi những hợp đồng bảo hiểm/tiết kiệm hứa hẹn con số lớn trong tương lai xa.

### Giá trị hiện tại ròng (Net Present Value - NPV)
Công thức để quyết định có nên đầu tư vào một dự án hay không. Nó là tổng của tất cả dòng tiền vào và ra, đã được chiết khấu về hiện tại.

$$NPV = \sum_{t=0}^{n} \frac{R_t}{(1 + i)^t}$$

*   $R_t$: Dòng tiền ròng tại thời điểm t.
*   $i$: Tỷ suất chiết khấu (Discount rate - thường là chi phí vốn hoặc lãi suất kỳ vọng).
*   **Quy tắc:**
    *   $NPV > 0$: Đầu tư (Dự án sinh lời cao hơn chi phí vốn).
    *   $NPV < 0$: Bỏ qua (Dự án phá hủy giá trị).

### Tỷ suất hoàn vốn nội bộ (Internal Rate of Return - IRR)
Là mức lãi suất $i$ làm cho $NPV = 0$. Nó cho biết hiệu quả thực tế của dự án.

## 3. Chi phí cơ hội (Opportunity Cost)
Mọi quyết định đều có giá. Giá của việc chọn A là mất đi lợi ích của phương án tốt nhất tiếp theo (B).
*   **Toán học:** Lợi nhuận kinh tế = Lợi nhuận kế toán - Chi phí cơ hội.
*   **Ví dụ:** Bạn tự mở quán cà phê, lãi 20tr/tháng. Nhưng nếu bạn đi làm thuê lương 25tr/tháng -> Bạn đang lỗ 5tr/tháng (Lợi nhuận kinh tế âm), dù sổ sách ghi lãi 20tr.

## 4. Nguyên lý Pareto (80/20) & Phân phối Power Law
Trong tài chính, kết quả không tuân theo phân phối chuẩn (Normal Distribution) mà tuân theo Luật Lũy thừa (Power Law).
*   $$f(x) = ax^{-k}$$
*   **Ý nghĩa:** Sự bất bình đẳng là đặc tính tự nhiên của hệ thống tài chính. Top 1% người giàu sở hữu tài sản lớn hơn 50% người nghèo gộp lại.
*   **Chiến lược:** Đừng cố đánh bại trung bình ở mọi nơi. Hãy tìm kiếm những cơ hội có tính chất Power Law (Rủi ro giới hạn, Lợi nhuận vô hạn - Asymmetric Upside) như đầu tư Startup, viết sách, tạo phần mềm.

## 5. Hệ số Kelly (Kelly Criterion)
Công thức quản lý vốn tối ưu để tối đa hóa tốc độ tăng trưởng hình học của tài sản mà không bị cháy túi.

$$f^* = \frac{bp - q}{b}$$

*   $f^*$: Tỷ lệ vốn nên cược.
*   $b$: Tỷ lệ trả thưởng (Odds) (Ví dụ: Thắng được 1 ăn 2 -> b=2).
*   $p$: Xác suất thắng.
*   $q$: Xác suất thua ($1-p$).
*   **Ví dụ:** Cược tung xu sấp ngửa. Thắng ăn 2, Thua mất 1. Xác suất thắng 50%.
    *   $b=2, p=0.5, q=0.5$.
    *   $f^* = (2*0.5 - 0.5) / 2 = 0.25$. -> Bạn nên cược 25% số vốn mỗi lần.
*   **Bài học:** Ngay cả khi bạn có lợi thế (Edge), nếu bạn cược tất tay (All-in), bạn chắc chắn sẽ phá sản trong dài hạn vì biến động. Quản lý vốn (Risk Management) quan trọng ngang bằng khả năng dự đoán.

---

## 🛠️ Ứng dụng Thực chiến (Life Applications)

### 1. Mua nhà vs. Thuê nhà (Bài toán NPV)
Nhiều người nghĩ: "Thuê nhà là ném tiền qua cửa sổ, mua nhà là giữ được tài sản".
*   **Thực tế:** Mua nhà có "chi phí ẩn" (lãi vay, thuế, bảo trì, phí môi giới) và "chi phí cơ hội" (tiền trả trước down-payment không được mang đi đầu tư sinh lời).
*   **Cách tính:** So sánh NPV của dòng tiền (Mua) vs NPV của dòng tiền (Thuê + Đầu tư phần tiền dư).
*   **Kết luận:** Nếu tỷ lệ Giá nhà / Giá thuê năm > 25 -> Nên thuê. Nếu < 15 -> Nên mua.

### 2. Latte Factor vs. Big Wins (Pareto)
*   **Lời khuyên phổ biến:** "Bớt uống Starbucks để giàu."
*   **Toán học 80/20:** Tiết kiệm 50k/ngày (Latte) không giúp bạn giàu nhanh bằng việc đàm phán tăng lương 5tr/tháng hoặc tối ưu lãi suất vay mua nhà (Big Wins).
*   **Chiến lược:** Tập trung tối ưu 3 khoản mục lớn nhất (Nhà, Xe, Thuế). Đừng để ý tiểu tiết (Sweat the small stuff).

### 3. Đánh đổi thời gian (Time-Money Trade-off)
Lương bạn là 200k/giờ.
*   Bạn thấy món đồ rẻ hơn 50k ở cửa hàng cách xa 30 phút đi đường (Tổng 1 tiếng đi về).
*   Lợi ích: 50k. Chi phí: 200k (thời gian). -> **Lỗ 150k.**
*   **Bài học:** Hãy thuê người làm những việc có giá trị thấp hơn mức lương theo giờ của bạn (Dọn nhà, Giặt ủi) để giải phóng thời gian làm việc giá trị cao hoặc nghỉ ngơi tái tạo sức lao động.
