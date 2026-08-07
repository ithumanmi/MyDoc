# Data Quality & Testing

> [← Data Science](../README.md)

## Tầng kiểm tra
1. **Schema tests:** cột bắt buộc, type, PK uniqueness
2. **Content tests:** ranges, null %, referential integrity
3. **Business tests:** revenue ≥ 0, sessions ≥ pageviews (soft)

## Tooling mindset
dbt tests / Great Expectations / custom asserts trong Airflow — chọn một stack và giữ nghiêm.

## Quarantine
Fail pipeline ồn ào hơn silent garbage. Có bảng bad_rows + alert.

## Checklist trước production DAG
- [ ] Freshness check
- [ ] Volume anomaly (drop 50% ngày thường)
- [ ] Null spike trên cột critical

> **Last Updated:** August 2026
