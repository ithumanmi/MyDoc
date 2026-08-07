# Dimensional Modeling Primer

> [← Data Science](../README.md)

## Star schema nhanh
- **Fact:** sự kiện đo được (orders, pageviews) — nhiều FK, ít text
- **Dimension:** ngữ cảnh (user, product, date) — descriptive

## Grain
Viết một câu: “1 row = 1 order line mỗi ngày” — nếu không nói được grain, model sẽ nát.

## SCD type thường gặp
| Type | Ý nghĩa | Dùng khi |
| --- | --- | --- |
| Type 1 | Overwrite | Sửa lỗi chính tả |
| Type 2 | Version + effective dates | Cần lịch sử (“user ở city nào lúc mua?”) |

## Liên hệ
Warehouse vs Lakehouse sâu hơn: [data-warehouse-lakehouse.md](../architecture/data-warehouse-lakehouse.md)

> **Last Updated:** August 2026
