# Pandas for Analysts

> [← Data Analytics](../README.md) | [SQL mastery](../sql-mastery.md)

## Khi nào dùng Pandas thay SQL
- Ad-hoc trên CSV/export khi chưa vào warehouse
- Feature nhẹ trước khi visualize
- Lặp lại cleaning steps cần version trong git

## Cheatsheet thao tác lõi
```python
import pandas as pd

df = pd.read_csv("orders.csv", parse_dates=["order_date"])
df["revenue"] = df["qty"] * df["price"]

# cohort-ish
df["cohort"] = df["order_date"].dt.to_period("M")
summary = (
    df.groupby(["cohort", "channel"], as_index=False)
      .agg(orders=("order_id", "nunique"), revenue=("revenue", "sum"))
)
```

## Quality checks nhanh
- `df.isna().mean().sort_values(ascending=False)`
- `df.duplicated(subset=["order_id"]).sum()`
- Outlier: `df["revenue"].describe(percentiles=[.5,.9,.99])`

## Mini exercise
1. Load ecommerce CSV mẫu (tự tạo 200 rows cũng được)
2. Tính revenue theo tuần + channel
3. Export bảng cho dashboard case [marketing](../projects/marketing-dashboard-performance.md)

## Acceptance tự chấm
- [ ] Notebook/script chạy again được
- [ ] Có assert ≥1 (không empty, không dup PK)
- [ ] Chart hoặc pivot table cuối cùng

> **Last Updated:** August 2026
