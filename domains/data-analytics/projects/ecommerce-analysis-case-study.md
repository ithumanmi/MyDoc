# 📊 Case Study: E-commerce Sales Analysis (Phân Tích Bán Hàng)

> [← Back to Data Analytics Roadmap](../README.md)

Đây là một bài tập mô phỏng (Simulation) giúp bạn áp dụng Quy trình Phân tích Dữ liệu vào thực tế.

---

## 1. Bối Cảnh (Scenario) 🎬
Bạn là Data Analyst tại **TechMart**, một sàn thương mại điện tử chuyên bán đồ công nghệ.
Giám đốc Kinh doanh (CSO) vừa gửi cho bạn một email:

> *"Chào [Tên bạn],*
> *Anh thấy doanh số Quý 4 vừa rồi có vẻ biến động. Em giúp anh trả lời 3 câu hỏi này trước cuộc họp thứ Hai nhé:*
> 1. *Doanh thu theo tháng đang tăng hay giảm?*
> 2. *Sản phẩm nào bán chạy nhất (Best-seller)?*
> 3. *Khách hàng đến từ đâu nhiều nhất (Hà Nội hay TP.HCM)?*
> *Thanks,"*

---

## 2. Dữ Liệu Giả Định (The Dataset) 💾
Bạn có quyền truy cập vào 3 bảng trong Database:

### Bảng 1: `Orders` (Đơn hàng)
| OrderID | Date       | CustomerID | ProductID | Quantity | TotalAmount |
| :---    | :---       | :---       | :---      | :---     | :---        |
| 1001    | 2025-10-01 | C001       | P001      | 2        | 40.00       |
| 1002    | 2025-10-02 | C002       | P003      | 1        | 150.00      |
| ...     | ...        | ...        | ...       | ...      | ...         |

### Bảng 2: `Products` (Sản phẩm)
| ProductID | ProductName   | Category    | Price  | Cost   |
| :---      | :---          | :---        | :---   | :---   |
| P001      | Chuột Logitech| Accessories | 20.00  | 10.00  |
| P002      | Bàn phím Cơ   | Accessories | 80.00  | 50.00  |
| P003      | Màn hình Dell | Monitor     | 150.00 | 110.00 |

### Bảng 3: `Customers` (Khách hàng)
| CustomerID | Name        | City    | JoinDate   |
| :---       | :---        | :---    | :---       |
| C001       | Nguyen Van A| Ha Noi  | 2024-01-15 |
| C002       | Tran Thi B  | TP.HCM  | 2024-05-20 |

---

## 3. Thực Hiện Phân Tích (Step-by-Step) 🛠️

### Bước 1: ASK - Xác định vấn đề
*   **Vấn đề:** Đánh giá hiệu quả kinh doanh Quý 4.
*   **Metric cần đo:** Revenue (Doanh thu), Quantity Sold (Số lượng bán), Customer Count (Số khách).

### Bước 2: PREPARE & PROCESS - Xử lý dữ liệu (SQL)
*Giả sử dữ liệu đã sạch. Chúng ta sẽ dùng SQL để tổng hợp.*

#### Câu 1: Doanh thu theo tháng (Revenue by Month)
```sql
SELECT 
    FORMAT(Date, 'yyyy-MM') AS Month, 
    SUM(TotalAmount) AS Revenue
FROM Orders
WHERE Date BETWEEN '2025-10-01' AND '2025-12-31'
GROUP BY FORMAT(Date, 'yyyy-MM')
ORDER BY Month;
```

#### Câu 2: Top 5 Sản phẩm bán chạy nhất (Best-sellers)
```sql
SELECT TOP 5
    p.ProductName,
    SUM(o.Quantity) AS TotalSold,
    SUM(o.TotalAmount) AS TotalRevenue
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalRevenue DESC;
```

#### Câu 3: Khách hàng theo Thành phố (Customers by City)
```sql
SELECT 
    c.City,
    COUNT(DISTINCT o.OrderID) AS TotalOrders,
    SUM(o.TotalAmount) AS Revenue
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.City
ORDER BY Revenue DESC;
```

---

## 4. ANALYZE & SHARE - Tìm Insight & Báo cáo 💡

Sau khi chạy SQL, bạn nhận được kết quả (giả định):
1.  **Tháng 11 doanh thu cao nhất** (có thể do Black Friday). Tháng 12 giảm nhẹ.
2.  **Màn hình Dell** mang lại doanh thu cao nhất, nhưng **Chuột Logitech** bán được số lượng nhiều nhất.
3.  **TP.HCM** đóng góp 60% doanh thu, Hà Nội 30%.

### Đề xuất hành động (Actionable Insights):
*   👉 **Marketing:** Tập trung chạy quảng cáo tại TP.HCM vì thị trường này đang "hot".
*   👉 **Sales:** Tạo combo "Màn hình + Chuột" để tăng giá trị đơn hàng (AOV).
*   👉 **Inventory:** Nhập thêm hàng cho tháng 11 năm sau để đón đầu Black Friday.

---

## 5. Bài Tập Về Nhà (Challenge) 🏠
Hãy thử trả lời câu hỏi khó hơn:
> *"Tỷ lệ khách hàng quay lại mua lần 2 (Retention Rate) là bao nhiêu?"*

*Gợi ý: Dùng SQL để đếm số khách hàng có `COUNT(OrderID) > 1`.*

👉 **[Tải mẫu báo cáo phân tích chuyên nghiệp](../templates/project-report-template.md)**
