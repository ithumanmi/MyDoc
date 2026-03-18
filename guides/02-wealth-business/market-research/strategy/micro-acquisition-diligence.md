# 💼 Micro-Acquisition Due Diligence: Rà Soát Trước Khi Mua Lại SaaS

> [← Back to Strategy & Advanced](./README.md) | [Home](../../../README.md)

Thị trường đang chứng kiến sự bùng nổ của nền tảng như **Acquire.com** hay **Flippa**, nơi bạn có thể mua một SaaS nhỏ (Micro-SaaS) đang có sẵn doanh thu $2,000/tháng với giá $60,000. Thay vì tự code từ đầu mất 1 năm chưa chắc có khách, thà bỏ tiền mua luôn!

Nhưng, **Trong M&A (Mua bán sáp nhập), Người Bán luôn tô vẽ Cô Dâu đẹp nhất có thể**. Đây là framework Lọc Lừa (Due Diligence) dành riêng cho dân kỹ thuật để không mua phải "Cục Nợ".

---

## 1. Xác Nhận Traffic Nội Lực (Tránh Backlink Bơm Hơi)

App có 50k visitors/tháng. MRR (Doanh thu hàng tháng) $5k. Nghe rất hấp dẫn.

### 🔴 Red Flag (Cờ đỏ): Traffic bạo tàn từ PBN (Private Blog Network).
*   Thủ đoạn của người bán: Họ thuê một đội SEO bơm hàng ngàn link "rác" (Spam Backlinks) từ các trang web đánh bạc, sex, hoặc web vệ tinh trỏ về Domain của SaaS để thao túng Google Ranking lên Top 1 trong 3 tháng. 
*   **Hậu quả:** Bạn vừa chuyển tiền mua xong. Lượt Update Thuật Toán cốt lõi (Core Update) của Google quét qua. Domain bị Phạt (Penalty), văng khỏi bảng xếp hạng. Traffic rơi về 0. Doanh thu rơi về 0. 

### 🟢 Cách Khám Hiện Trường (Dùng `Ahrefs` hoặc `Semrush`):
1.  **Check Lịch Sử Link Profile:** Gõ tên miền SaaS vào Ahrefs -> Quét phần "Referring Domains". Nếu biểu đồ đường link cắm thẳng lên trời một cách đột biến trong 2-3 tháng gần nhất -> Mùi lừa đảo 100%. Mua Traffic Bơm.
2.  **Check Độ Phân Bổ Anchor Text:** Nếu > 30% Link có chung 1 cụm từ khóa y chang nhau (Ví dụ: "best ai pdf reader") thay vì tên thương hiệu (Ví dụ: "chatpdf"). Chắc chắn đây là thủ thuật SEO mũ đen.
3.  **Cross-check SimilarWeb:** Kiểm tra nguồn Traffic thật sự đến từ Tìm Kiếm (Organic Search) hay là Direct (Gõ trực tiếp). Rất nhiều ca, người bán dùng Bot Traffic (Botnet chạy giả lập) ấn Direct vào web để lừa mắt bạn.

---

## 2. Thẩm Định Sự Mục Nát Của Tech Stack (Tech Debt Decay)

Bạn xem doanh thu thấy Ngon, nhưng Codebase (Mã nguồn) bên trong là một "Nồi lẩu thập cẩm" bốc mùi (Spaghetti Code).

### 🔴 Red Flag: Framework hóa thạch / One-Man Show (Code dị hợm).
*   Người bán tự code App này cách đây 7 năm bằng PHP 5.x hoặc AngularJS (Bản cũ đã ngừng hỗ trợ bảo mật). 
*   Không có Unit Test, không có Comments, hàm (Function) dài 3000 dòng.

### 🟢 Giao Thức Khám Bệnh Code (Tech Audit Checklist):
1.  **Xin quyền View-only kho Github:**
    *   **Check Commit Frequency:** Bức tranh đóng băng. Lần cuối cùng có người commit sửa lỗi là 8 tháng trước? Nghĩa là App này đang chạy kiểu "Sống thoi thóp" (Zombie App).
    *   **Packages / Dependencies:** Mở file `package.json` hoặc `requirements.txt`. Quết lệnh check version. Có bao nhiêu thư viện (Libraries) lõi đã bị Deprecated (Ngưng phát triển) hoặc có hổng bảo mật rủi ro cực nguy hiểm mức Critical? Mua về, bạn sẽ phải tốn 3 tháng chỉ để nâng cấp thư viện. Khấu trừ thẳng tiền chi phí Refactor vào Giá Mua!
2.  **Hỏi Founder cũ 3 câu sinh tử:**
    *   "Quá trình Deploy lên Production diễn ra như thế nào?" (Nếu họ bảo: Kéo file thủ công qua FTP -> Chạy ngay! Hệ thống CI/CD bằng 0).
    *   "Phần tốn nhiều tính toán (Bottleneck) lớn nhất của hệ thống nằm ở đâu khi có lượng user tải PDF cùng lúc?"
    *   "API Keys của bên thứ 3 (Stripe, OpenAI) đang lồng (hardcoded) trong Code, hay để biến Môi Trường (Env Variables)?"

---

## 3. Hệ Số Định Giá Tiêu Chuẩn (Valuation Multiples) Của Micro-SaaS

Chào bán giá nào là hợp lý? Đừng định giá bằng Cảm xúc. Định giá ở thị trường Micro-SaaS ($10k - $500k Annual Revenue) dùng một chỉ số cực kỳ lạnh lùng: **SDE Multiple (Mức nhân của Doanh thu Lợi nhuận Chủ sở hữu).**

*   **SDE (Seller Discretionary Earnings):** Là tổng Lợi nhuận Gộp + Lương giám đốc (của họ tự nhận) + Các chi phí cá nhân (Nhà, xe lồng vào hóa đơn công ty). 
*   Là số Tiền Ròng Thật Sự bạn sẽ Đút Cất Túi sau 1 năm nếu bạn vào thay.

### Công thức Giá Mua Thường Thấy (Năm 2026):
*   **Giá Chốt Mua Tốt** = SDE x `3.0` đến `4.0` (Tức bạn làm 3-4 năm mới Dòng Tiền Hòa Vốn Nếu Chỉ Duy Trì - Chưa Tính Lãi Nếu Đạt Tăng Trưởng Khắc Phục Tốt Hơn)
*   **Ví Dụ Rõ Ràng:** Doanh Thấp Lợi Tốt SDE $50.000 / Năm.
    *   App có SDE rớt 10%/tháng: Bạn trả Multiple = `2x -> 2.5x` ($100k-$125k). Tiềm tàng rủi ro "Con Dao Rơi" - Rơi Đỏ Máu Không Gượng Dậy.
    *   App Có Tốc Độ Churn Rate < 5%, Organic Lên Đều: Multiple = `4.0x` ($200.000). Giá Siêu Tốt.

> **Tâm Pháp:** "Trong Micro-Acquisition, bạn không mua một App. Bạn mua Sự Suy Giảm Churn Rate (Thoát của Khách Cũ) và Hệ Số Lợi Nhuận Thật." Thà mua một App Thiết Kế Xấu Doanh Thu Ổn Định SDE Thực mà Code Chuẩn, Còn Hơn Mua App Giao Diện Đẹp Như Tranh Nhưng Traffic Bơm Bằng Bot Và Chạy Bằng Nền Tảng Hết Date. Mọi Phép Thử, Hãy Lấy Thời Gian Dev Chữa Lỗi Làm Đồng Hồ Đếm Ngược Định Giá Lỗ Hổng Giá Chào Bắt Cú Lặp Lại.
