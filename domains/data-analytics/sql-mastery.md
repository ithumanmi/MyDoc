# 👑 SQL Mastery: Window Functions & CTEs

> [← Back to Data Analytics Roadmap](./README.md)

Khi bạn đã biết `SELECT`, `FROM`, `WHERE` và `GROUP BY`, bạn mới chỉ là **Junior Data Analyst**.
Để xử lý các bài toán phức tạp (như xếp hạng, tính doanh thu tích lũy, so sánh tháng trước), bạn cần **Window Functions** và **CTEs**. Đây là "vũ khí hạng nặng" giúp bạn viết SQL ngắn gọn và mạnh mẽ hơn.

---

## 1. Common Table Expressions (CTEs) 🏗️
CTE (biểu thức bảng chung) giống như việc tạo một "biến tạm" chứa kết quả của câu truy vấn.

### Tại sao dùng CTE?
*   **Dễ đọc:** Thay vì viết lồng nhau `(SELECT (SELECT ...))`, bạn tách thành từng bước rõ ràng.
*   **Tái sử dụng:** Bạn có thể gọi lại bảng tạm này nhiều lần trong cùng 1 câu lệnh.

### Cú pháp
```sql
WITH MonthlySales AS (
    SELECT 
        FORMAT(OrderDate, 'yyyy-MM') AS Month,
        SUM(TotalAmount) AS Revenue
    FROM Orders
    GROUP BY FORMAT(OrderDate, 'yyyy-MM')
)
SELECT * 
FROM MonthlySales
WHERE Revenue > 10000;
```

---

## 2. Window Functions (Hàm Cửa Sổ) 🪟
Khác với `GROUP BY` (gộp nhiều dòng thành 1), **Window Functions** giữ nguyên số dòng nhưng tính toán dựa trên một "cửa sổ" trượt qua các dòng đó.

**Cú pháp:**
```sql
Function_Name() OVER (
    PARTITION BY [cột chia nhóm] 
    ORDER BY [cột sắp xếp]
)
```

### 2.1. Ranking Functions (Xếp hạng) 🏆
*   `ROW_NUMBER()`: Đánh số thứ tự liên tục (1, 2, 3, 4).
*   `RANK()`: Xếp hạng có nhảy số khi trùng (1, 2, 2, 4).
*   `DENSE_RANK()`: Xếp hạng không nhảy số (1, 2, 2, 3).

**Ví dụ:** Tìm top 3 nhân viên bán hàng xuất sắc nhất mỗi tháng.
```sql
SELECT * FROM (
    SELECT 
        EmployeeName, 
        Month, 
        Revenue,
        RANK() OVER (PARTITION BY Month ORDER BY Revenue DESC) as Rank
    FROM EmployeeSales
) t
WHERE Rank <= 3;
```

### 2.2. Aggregate Window Functions (Tính tổng tích lũy) 📈
Dùng `SUM()`, `AVG()`, `COUNT()` kết hợp với `OVER` để tính **Running Total** (Doanh thu cộng dồn).

**Ví dụ:** Tính doanh thu tích lũy từ đầu năm đến nay.
```sql
SELECT 
    Date,
    DailyRevenue,
    SUM(DailyRevenue) OVER (ORDER BY Date) as RunningTotal
FROM DailySales;
```

### 2.3. Value Window Functions (So sánh quá khứ/tương lai) 🕰️
*   `LAG(col, n)`: Lấy giá trị của dòng trước đó n dòng.
*   `LEAD(col, n)`: Lấy giá trị của dòng sau đó n dòng.

**Ví dụ:** Tính tỷ lệ tăng trưởng so với tháng trước (MoM Growth).
```sql
SELECT 
    Month,
    Revenue,
    LAG(Revenue, 1) OVER (ORDER BY Month) as LastMonthRevenue,
    (Revenue - LAG(Revenue, 1) OVER (ORDER BY Month)) / LAG(Revenue, 1) OVER (ORDER BY Month) * 100 as GrowthRate
FROM MonthlySales;
```

---

## 3. Thứ Tự Thực Thi SQL (Order of Execution) ⚙️
Hiểu máy tính chạy code của bạn như thế nào để tối ưu hiệu năng.

1.  **FROM / JOIN:** Lấy dữ liệu từ bảng nào?
2.  **WHERE:** Lọc dữ liệu thô.
3.  **GROUP BY:** Gom nhóm.
4.  **HAVING:** Lọc sau khi gom nhóm.
5.  **SELECT:** Chọn cột hiển thị.
6.  **DISTINCT:** Loại bỏ trùng lặp.
7.  **ORDER BY:** Sắp xếp.
8.  **LIMIT / TOP:** Lấy số lượng dòng giới hạn.

> **Mẹo:** Đừng bao giờ `SELECT *` trong dự án thực tế. Chỉ lấy cột bạn cần để tiết kiệm I/O.

---

## 4. Thử Thách (Challenge) 💪
Dùng bảng `Orders` trong [E-commerce Case Study](./projects/ecommerce-analysis-case-study.md), hãy viết câu lệnh SQL để:
1.  Tính doanh thu của từng Khách hàng.
2.  Xếp hạng Khách hàng dựa trên doanh thu đó (`DENSE_RANK`).
3.  Chỉ lấy ra những Khách hàng thuộc **Top 10**.

👉 *Gợi ý: Dùng CTE để tính doanh thu trước, sau đó dùng Window Function để xếp hạng.*
