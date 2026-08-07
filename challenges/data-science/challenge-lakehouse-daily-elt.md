# Challenge: Daily Lakehouse ELT

- **Loại:** project
- **Mảng:** data-science
- **Mức:** Intermediate
- **Ước lượng:** 2–4 ngày
- **Prerequisites:** [lakehouse project](../../domains/data-science/projects/lakehouse-ecommerce-elt.md)

## Đề bài
Implement (subset) Bronze→Silver→Gold cho orders + payments. Chạy daily idempotent.

## Acceptance
- [ ] Re-run cùng ngày không nhân đôi gold facts
- [ ] ≥3 automated quality checks fail pipeline khi broken
- [ ] README: how to seed, run, query GMV 7d
- [ ] Diagram layers

Local stack OK (DuckDB/Polars thay Spark nếu cần).
