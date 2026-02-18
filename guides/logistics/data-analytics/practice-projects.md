# 🧪 Practice Projects (Dự án thực hành Logistics)

> [← Back to Analytics](./README.md)

Học phải đi đôi với hành. Dưới đây là 3 dự án mẫu giúp bạn áp dụng kỹ năng phân tích dữ liệu vào bài toán Logistics thực tế.

---

## 🏗️ Project 1: Inventory Optimization (Tối ưu hóa tồn kho)

### Mục tiêu
Xác định mức tồn kho an toàn (Safety Stock) và điểm đặt hàng lại (Reorder Point) cho từng mã hàng (SKU) để giảm chi phí lưu kho mà không bị cháy hàng (Stock-out).

### Dữ liệu cần thiết
*   Lịch sử bán hàng (Sales History) trong 12 tháng.
*   Thời gian giao hàng của nhà cung cấp (Lead Time) và độ biến động của nó.
*   Chi phí đặt hàng (Ordering Cost) và Chi phí giữ hàng (Holding Cost).

### Các bước thực hiện
1.  **Phân loại ABC:** Dùng quy tắc Pareto (80/20) để xác định nhóm A (quan trọng nhất), B và C.
2.  **Tính toán:** Áp dụng công thức Safety Stock và EOQ (Economic Order Quantity).
3.  **Mô phỏng (Simulation):** Chạy thử với dữ liệu quá khứ xem nếu áp dụng mức tồn kho mới thì tiết kiệm được bao nhiêu tiền?

---

## 🚚 Project 2: Route Optimization (Tối ưu hóa lộ trình giao hàng)

### Mục tiêu
Lập kế hoạch giao hàng cho 50 đơn hàng tại TP.HCM với 5 xe tải sao cho tổng quãng đường ngắn nhất và không xe nào chở quá tải.

### Dữ liệu cần thiết
*   Danh sách đơn hàng: Địa chỉ (Kinh độ/Vĩ độ), Khối lượng/Thể tích hàng.
*   Danh sách xe: Sức chứa (Capacity), Thời gian hoạt động.
*   Ma trận khoảng cách (Distance Matrix) giữa các điểm (Dùng Google Maps API hoặc OSRM).

### Công cụ
*   **Excel Solver:** Cho bài toán nhỏ (< 20 điểm).
*   **Python (Google OR-Tools):** Cho bài toán lớn phức tạp (VRP - Vehicle Routing Problem).

---

## 💰 Project 3: Freight Spend Analysis (Phân tích chi phí vận chuyển)

### Mục tiêu
Tìm ra nguyên nhân khiến chi phí vận chuyển tăng cao bất thường và đề xuất giải pháp cắt giảm.

### Dữ liệu cần thiết
*   Dữ liệu lịch sử vận chuyển 1 năm: Tuyến đường, Hãng vận chuyển (Carrier), Loại dịch vụ (Express/Economy), Trọng lượng, Cước phí.

### Các câu hỏi cần trả lời (Business Questions)
1.  Tuyến đường nào tốn kém nhất? Tại sao?
2.  Carrier nào có giá tốt nhất cho từng khu vực? (Benchmarking).
3.  Có bao nhiêu đơn hàng gửi Express (đắt tiền) mà thực ra có thể gửi Economy (rẻ tiền) vẫn kịp deadline? (Service Level downgrade).
4.  Tỷ lệ đơn hàng giao trễ (On-time Performance) của từng Carrier là bao nhiêu?
