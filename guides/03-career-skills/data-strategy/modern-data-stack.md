# 🧱 Modern Data Stack 2026 Roadmap

> Lộ trình chọn công nghệ ingest → storage → transform → semantic → activation phù hợp quy mô SMB/scale-up.

## 1. Reference Architecture

```
Data Sources → Ingest (ELT) → Storage/Lakehouse → Transform/Semantic Layer → Serving (BI/API) → Activation (Reverse ETL/ML)
```

| Layer | Mục tiêu | Công cụ gợi ý |
| --- | --- | --- |
| Ingest | Đồng bộ dữ liệu từ SaaS/DB | Fivetran, Airbyte, Meltano, Kafka Connect |
| Storage | Lưu trữ chuẩn hóa, tách compute/storage | Snowflake, BigQuery, Databricks Lakehouse, DuckDB (team nhỏ) |
| Transform | Chuẩn hóa, kiểm thử, lineage | dbt Core/Cloud, Dataform, SQLMesh |
| Semantic Layer | Định nghĩa metric, caching | LookML, MetricFlow, Cube.dev |
| Serving (BI) | Dashboard & self-service | Tableau, Power BI, Looker, Lightdash, Hex |
| Activation | Đẩy insight vào tool vận hành | Hightouch, Census, RudderStack Reverse ETL |
| Observability | Monitoring dữ liệu, SLA | Monte Carlo, Metaplane, open-source (Great Expectations) |

## 2. Maturity Stages

| Stage | Đặc điểm | Hành động |
| --- | --- | --- |
| **Starter** | Data silo, Excel nặng, chưa có warehouse | Bắt đầu với cloud warehouse + ELT nhẹ (Fivetran/Airbyte) |
| **Growth** | Có warehouse, cần chuẩn hóa transform | Đầu tư dbt, thiết lập CI/CD, data quality tests |
| **Scale** | Nhiều domain dữ liệu, nhu cầu real-time | Lakehouse + streaming ingest, semantic layer, observability |

## 3. Tool Evaluation Checklist (F.I.T)

- **Functionality:** đáp ứng use case nào? (batch vs streaming, governance)
- **Integration:** kết nối sẵn với stack hiện tại? API/SDK?
- **Total Cost:** license + compute + nhân sự vận hành?

## 4. Sample Stack Combinations

- **Lean Analytics Team (<10 người):** Airbyte + BigQuery + dbt Core + Looker Studio + Hightouch Lite.
- **Product-led Scale-up:** Fivetran + Snowflake + dbt Cloud + MetricFlow + Hex/Looker + Census + Monte Carlo.
- **Hybrid On-prem:** Kafka Connect + Databricks + dbt + Power BI + Fabric OneLake.

## 5. Governance Hooks

- Tích hợp metadata và lineage từ dbt vào catalog (Atlan/Castor).
- Thiết lập data contract giữa engineering và analytics (ví dụ với SQLMesh / dbt tests).
- Observability alert → gửi tới Slack/Teams, liên kết với incident playbook.

## 6. Cost Optimization Tips

- Tận dụng storage tiering (Iceberg/Delta + object storage) cho dữ liệu lạnh.
- Tắt phiên bản warehouse rảnh (auto suspend) và giám sát query heavy users.
- Dùng DuckDB/Polars cho prototyping local để giảm chi phí cloud.

## 7. When to revisit stack

- Khi số lượng nguồn dữ liệu > 20, cân nhắc chuyển ELT managed.
- Khi đội business yêu cầu KPI thống nhất → bổ sung semantic layer.
- Khi ML/activation trở thành nhu cầu chính → đầu tư feature store / MLOps nhẹ.

> 🧭 *Guiding principle:* chọn stack “đủ dùng” theo maturity hiện tại, nhưng chuẩn hóa quy trình (version control, testing, monitoring) ngay từ giai đoạn sớm để tránh nợ kỹ thuật.