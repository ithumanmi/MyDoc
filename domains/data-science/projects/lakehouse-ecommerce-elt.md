# Project: Ecommerce Lakehouse ELT (Bronze → Silver → Gold)

> [← Data Science](../README.md) | [Lakehouse theory](../architecture/data-warehouse-lakehouse.md)

## Mục tiêu
Xây pipeline ELT mini cho đơn hàng e-commerce trên lakehouse pattern (local OK: MinIO/S3 + Spark/DuckDB/Polars + warehouse Postgres).

## Layers
| Layer | Nội dung | Format |
| --- | --- | --- |
| Bronze | Raw events JSON/CSV (orders, pages, payments) | as-landed + ingest_ts |
| Silver | Dedupe, typed columns, PK/FK checks | Parquet partitioned by date |
| Gold | Star schema: `fact_orders`, `dim_customer`, `dim_product` | Tables query được |

## Acceptance
- [ ] Document grain của `fact_orders`
- [ ] Idempotent daily job (chạy 2 lần không nhân đôi fact)
- [ ] ≥3 data quality tests (null PK, orphan FK, revenue ≥ 0)
- [ ] DAG/scheduler sketch (Airflow/cron) + SLA freshness
- [ ] 1 dashboard hoặc SQL trả lời: GMV 7 ngày, top products, payment fail rate

## Suggested layout
```
lakehouse/
  bronze/  silver/  gold/
  jobs/ingest.py  jobs/transform.py  jobs/publish.py
  tests/test_quality.py
  README.md
```

**Related labs:** [PySpark](../labs/lab-pyspark-big-data.md) · [Airflow](../labs/lab-airflow-etl-pipeline.md)  
**Challenge:** [challenges/data-science](../../../challenges/data-science/README.md)

> **Last Updated:** August 2026
