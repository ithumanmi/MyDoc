# Challenge: SQL Window/CTE + Dashboard KPI Spec

- **Loại:** project
- **Mảng:** data-analytics
- **Mức:** Beginner
- **Ước lượng thời gian:** 1-2 ngày
- **Prerequisites (tùy chọn):** [`domains/data-analytics/README.md`](../../domains/data-analytics/README.md)

## Mục tiêu học tập
- Viết truy vấn SQL dùng **window functions** và **CTE**.
- Thiết kế dashboard spec với KPI rõ ràng.

## Đề bài
Cho một dataset bán hàng/transactions (có bảng orders, order_items, customers, products). Nhiệm vụ:
1) Viết 5-10 truy vấn SQL bao phủ: window function (rank/row_number/lag), CTE, join, filter thời gian.
2) Định nghĩa KPI và draft spec cho 1 dashboard (ví dụ: Doanh thu theo ngày, Top sản phẩm, LTV đơn giản, churn proxy).

## Đầu vào (Input)
- Schema mẫu: `orders(id, customer_id, order_date, amount)`, `order_items(order_id, product_id, qty, price)`, `customers(id, segment)`, `products(id, category)` (có thể tùy biến).

## Đầu ra (Output)
- File SQL hoặc notebook chứa truy vấn.
- 1 file markdown mô tả dashboard: KPI, biểu đồ, filter, tần suất cập nhật.

## Tiêu chí chấm (Acceptance)
- **Đúng:** Truy vấn chạy được, syntax hợp lệ.
- **Đa dạng:** Có dùng window (lag/lead/rank), CTE, join nhiều bảng.
- **Dashboard spec:** Nêu rõ KPI, công thức, biểu đồ, segment/filter.

## Gợi ý / Hint
- Viết truy vấn daily revenue, top N products, moving average.
- Dùng CTE để tách bước: filter thời gian, aggregate, rank.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Kèm file .sql hoặc notebook mẫu nếu public.