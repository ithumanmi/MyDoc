# 🏭 Warehouse & Inventory Management

> [← Back to Logistics](../../../README.md)

Quản lý kho (Warehouse Management) không chỉ là xếp hàng vào chỗ trống. Đó là nghệ thuật **tối ưu không gian** và **luân chuyển hàng hóa** để giảm chi phí và tăng tốc độ giao hàng.

---

## 1. Inventory Strategy (Chiến lược tồn kho)

### Just-in-Time (JIT)
*   **Nguyên tắc:** Nhập hàng "vừa kịp lúc" để sản xuất hoặc bán. Tồn kho = 0 (Lý thuyết).
*   **Ưu điểm:** Giảm chi phí lưu kho, giảm vốn đọng (Working Capital).
*   **Rủi ro:** Cực kỳ dễ vỡ khi chuỗi cung ứng bị gián đoạn (Vụ chip ô tô).
*   **Ví dụ:** Toyota, các hãng lắp ráp linh kiện điện tử.

### Safety Stock (Tồn kho an toàn)
*   **Nguyên tắc:** Luôn giữ một lượng hàng dự trữ để phòng ngừa rủi ro (Nhu cầu tăng đột biến, nhà cung cấp giao trễ).
*   **Công thức:** `(Max Usage x Max Lead Time) - (Avg Usage x Avg Lead Time)`
*   **Mục tiêu:** Cân bằng giữa chi phí giữ hàng (Holding Cost) và chi phí mất khách (Stock-out Cost).

### EOQ (Economic Order Quantity)
*   **Nguyên tắc:** Tính toán lượng đặt hàng tối ưu để tổng chi phí (Đặt hàng + Lưu kho) là thấp nhất.
*   **Ứng dụng:** Dùng cho các mặt hàng có nhu cầu ổn định (Gạo, Muối, Ốc vít).

---

## 2. Warehouse Operations (Vận hành kho)

### Inbound (Nhập kho)
1.  **Receiving:** Nhận hàng, kiểm đếm số lượng/chất lượng.
2.  **Put-away:** Xác định vị trí lưu trữ (Bin Location) và cất hàng. Dùng quy tắc ABC (Hàng bán chạy để gần cửa).

### Outbound (Xuất kho)
1.  **Picking:** Lấy hàng theo đơn (Order Picking). Có nhiều phương pháp:
    *   *Zone Picking:* Mỗi người phụ trách một khu vực.
    *   *Wave Picking:* Gom nhiều đơn lại pick một lần.
    *   *Batch Picking:* Pick nhiều mặt hàng giống nhau cho nhiều đơn.
2.  **Packing:** Đóng gói, dán nhãn vận chuyển (Shipping Label).
3.  **Shipping:** Phân loại theo tuyến và bàn giao cho đơn vị vận chuyển (3PL).

### Cross-docking
*   **Kỹ thuật cao cấp:** Hàng nhập về kho -> Không lưu trữ -> Chuyển thẳng sang khu vực xuất hàng đi luôn.
*   **Lợi ích:** Loại bỏ chi phí lưu kho và bốc xếp (Handling).
*   **Yêu cầu:** Đồng bộ hóa cực cao giữa xe tải đến và đi. (Walmart là bậc thầy về cái này).

---

## 3. Technology (Công nghệ kho)

*   **WMS (Warehouse Management System):** Phần mềm "bộ não" của kho. Quản lý vị trí, tồn kho real-time.
*   **Barcode / RFID:** Quét mã vạch để nhập/xuất nhanh và chính xác. RFID đắt hơn nhưng quét được nhiều hàng cùng lúc mà không cần nhìn thấy (Line of sight).
*   **AS/RS (Automated Storage and Retrieval System):** Hệ thống robot tự động cất và lấy hàng ở độ cao lớn.
*   **AGV (Automated Guided Vehicle):** Xe tự hành di chuyển Pallet trong kho.

---

## 4. Key Metrics (KPI Kho)

*   **Order Picking Accuracy:** Độ chính xác khi lấy hàng (Cực kỳ quan trọng với E-commerce).
*   **Inventory Accuracy:** Độ chính xác tồn kho (Thực tế vs Hệ thống). Phải kiểm kê (Cycle Count) thường xuyên.
*   **Space Utilization:** Hiệu suất sử dụng không gian kho (M3).
