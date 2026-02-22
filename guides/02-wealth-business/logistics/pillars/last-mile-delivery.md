# 🚚 Last-Mile Delivery (Giao hàng Chặng cuối)

> [← Back to Logistics](../../../README.md)

Last-mile (chặng cuối cùng đến tay khách hàng) là phần **đắt đỏ nhất** (chiếm tới 53% tổng chi phí vận chuyển) và **khó nhằn nhất** trong chuỗi cung ứng E-commerce.

---

## 1. Thách thức của Last-Mile

### Chi phí (Cost)
*   **Failed Delivery Attempts:** Khách không nghe máy, sai địa chỉ -> Phải giao lại (Re-delivery) -> Tốn gấp đôi chi phí.
*   **Stop Density:** Mật độ điểm dừng thấp ở vùng ngoại ô (Mỗi đơn cách nhau xa) -> Tốn xăng và thời gian.

### Tốc độ (Speed)
*   Khách hàng ngày càng đòi hỏi giao nhanh (Same-day, Instant Delivery).
*   Áp lực từ các sàn TMĐT (Shopee, Lazada, TikTok Shop).

### Trải nghiệm khách hàng (CX)
*   Shipper thái độ kém -> Khách ghét Shop.
*   Hàng móp méo, vỡ -> Hoàn hàng (Return Rate tăng).

---

## 2. Mô hình vận hành (Operations Models)

### Hub & Spoke (Truyền thống)
*   **Hub:** Kho tổng phân loại (Sorting Center).
*   **Spoke:** Các bưu cục vệ tinh (Post Office).
*   **Quy trình:** Seller -> Hub (Sort) -> Spoke (Gần khách) -> Shipper -> Customer.
*   **Ưu điểm:** Tối ưu hóa tuyến đường dài.
*   **Nhược điểm:** Chậm ở khâu trung chuyển.

### Point-to-Point (Giao hàng tức thời)
*   **Quy trình:** Shipper lấy hàng từ Shop -> Giao thẳng cho Khách (GrabExpress, AhaMove).
*   **Ưu điểm:** Siêu tốc (30p - 1h).
*   **Nhược điểm:** Chi phí cao, chỉ phù hợp nội thành.

### Crowdsourcing (Kinh tế chia sẻ)
*   Tận dụng tài xế tự do (Freelance Drivers) hoặc người đi đường tiện chuyến.
*   **Ưu điểm:** Linh hoạt năng lực giao hàng (Elastic capacity) vào mùa cao điểm (Sale 11.11, Tết).

---

## 3. Công nghệ tối ưu (Optimization Tech)

### Route Optimization (Tối ưu lộ trình)
*   Dùng thuật toán (VRP - Vehicle Routing Problem) để sắp xếp lộ trình đi giao nhiều điểm nhất với quãng đường ngắn nhất.
*   Tính toán cả kẹt xe (Traffic jam) và thời gian dừng đỗ.

### Smart Lockers (Tủ khóa thông minh)
*   Đặt tủ locker ở chung cư, tòa nhà văn phòng.
*   Shipper bỏ hàng vào tủ -> Khách nhận mã Code -> Tự lấy khi rảnh (24/7).
*   **Lợi ích:** Loại bỏ Failed Delivery, Shipper giao được nhiều đơn 1 điểm.

### PUDO (Pick-up Drop-off Points)
*   Hợp tác với cửa hàng tiện lợi (Circle K, FamilyMart) làm điểm gửi/nhận hàng.

---

## 4. Key Metrics (Chỉ số quan trọng)

*   **Cost per Order (CPO):** Chi phí trung bình cho mỗi đơn giao thành công.
*   **First Attempt Delivery Rate:** Tỷ lệ giao thành công ngay lần đầu (Càng cao càng tốt).
*   **Delivery Time:** Thời gian trung bình từ lúc lấy hàng đến lúc giao xong.
