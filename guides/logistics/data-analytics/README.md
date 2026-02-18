# 📊 Logistics Data & Analytics (Dữ liệu Logistics)

> [← Back to Logistics](../README.md)

Bạn không thể quản lý những gì bạn không đo lường được. Trong kỷ nguyên số, dữ liệu chính là tài sản quý giá nhất của Logistics.

---

## 1. Nguồn dữ liệu công khai (Public Datasets)

Để thực hành phân tích, bạn có thể lấy dữ liệu từ các nguồn uy tín sau:

### Kaggle (Kho dữ liệu Data Science)
*   **[Supply Chain Logistics Problem Dataset](https://www.kaggle.com/):** Dữ liệu thực tế về đơn hàng, kho bãi, trọng lượng, phương thức vận chuyển. Rất tốt để thực hành tối ưu hóa mạng lưới.
*   **[Global Superstore](https://www.kaggle.com/):** Bộ dữ liệu kinh điển về bán hàng và vận chuyển toàn cầu. Phù hợp cho bài toán phân tích chi phí và lợi nhuận theo khu vực.
*   **[Brazilian E-Commerce Public Dataset (Olist)](https://www.kaggle.com/):** 100k đơn hàng thực tế tại Brazil. Phân tích Last-mile delivery, Customer sentiment, Payment methods.

### Tổ chức Quốc tế
*   **[World Bank LPI (Logistics Performance Index)](https://lpi.worldbank.org/):** Chỉ số hiệu quả Logistics của các quốc gia. Dùng để so sánh năng lực vĩ mô.
*   **[UN Comtrade](https://comtrade.un.org/):** Dữ liệu xuất nhập khẩu chi tiết (HS Code) giữa các quốc gia. Phù hợp phân tích dòng chảy thương mại toàn cầu.

### Dữ liệu Vận tải biển (Maritime Data)
*   **[MarineTraffic / VesselFinder](https://www.marinetraffic.com/):** Theo dõi vị trí tàu bè thời gian thực (AIS Data). Bản miễn phí cho phép xem mật độ tàu tại các cảng lớn.
*   **[Freightos Baltic Index (FBX)](https://fbx.freightos.com/):** Chỉ số giá cước container hàng ngày (Spot rates) cho các tuyến chính (China - US, China - EU).

---

## 2. Dữ liệu Nội bộ Doanh nghiệp (Internal Data)

Trong môi trường thực tế, dữ liệu thường nằm rải rác ở các hệ thống:

*   **ERP (Enterprise Resource Planning):** SAP, Oracle. Chứa dữ liệu Đơn hàng (Sales Order), Mua hàng (Purchase Order), Tài chính.
*   **WMS (Warehouse Management System):** Dữ liệu Tồn kho (Inventory level), Vị trí hàng (Bin location), Năng suất nhân viên (Picking productivity).
*   **TMS (Transportation Management System):** Dữ liệu Vận chuyển, Cước phí, Lộ trình, Trạng thái giao hàng (POD - Proof of Delivery).
*   **IoT Sensors:** Dữ liệu nhiệt độ, độ ẩm (Cold chain), GPS hành trình xe tải.

---

## 3. Cách tạo dữ liệu giả lập (Mock Data)

Nếu không có dữ liệu thật, hãy tự tạo (Mock) để luyện tập kỹ năng SQL/Python/Excel:

*   **Công cụ:** `Mockaroo` (Web), thư viện `Faker` (Python), `Pandas`.
*   **Các trường cần thiết:**
    *   `Order ID` (Unique)
    *   `Product SKU`, `Quantity`
    *   `Origin Address`, `Destination Address` (Lat/Long để tính khoảng cách)
    *   `Shipping Date`, `Delivery Date` (Để tính Lead Time)
    *   `Shipping Cost`, `Carrier Name`

---

## 4. Công cụ phân tích (Analytics Stack)

*   **Excel / Google Sheets:** Vẫn là vua cho các phân tích nhanh, Ad-hoc. (Pivot Table, Solver).
*   **Power BI / Tableau:** Trực quan hóa dữ liệu (Dashboarding). Theo dõi KPI real-time.
*   **Python / R:** Xử lý dữ liệu lớn (Big Data), chạy mô hình dự báo (Forecasting), tối ưu hóa tuyến đường (Optimization).
*   **SQL:** Truy vấn dữ liệu từ Database. Kỹ năng bắt buộc phải có.
