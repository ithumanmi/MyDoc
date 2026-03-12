# 🗂️ Model Registry & Lifecycle Management

> [← Back to MLOps](./README.md)

Model Registry là "nguồn sự thật" cho tất cả phiên bản mô hình, trạng thái (staging, production) và metadata triển khai.

---

## 1. Lý do cần Model Registry

- Tracking phiên bản mô hình giống như tracking phiên bản code.
- Quản lý luồng promote: **Development → Staging → Production**.
- Phân quyền rõ ràng: ai được approve, ai được rollback.
- Tích hợp monitoring để biết model nào đang phục vụ production.

---

## 2. Thành phần chính

- **Model Version:** hash, artifact path, metrics snapshot.
- **Stages:** `None`, `Staging`, `Production`, `Archived`.
- **Metadata:** owner, tags (use case, dataset version), created date.
- **Events:** promotion history, comments, rollback log.

---

## 3. Công cụ

| Tool | Tính năng | Lưu ý |
| --- | --- | --- |
| **MLflow Model Registry** | OSS, REST API, integrate với MLflow Tracking. | Dễ self-host, linh hoạt. |
| **SageMaker Model Registry** | Integrated với SageMaker Pipelines & Studio. | AWS-first. |
| **Vertex AI Model Registry** | Managed, audit logging, Vertex Pipelines. | GCP-first. |
| **Databricks Unity Catalog** | Governance mạnh, lineage, access control. | Cho stack Databricks. |

---

## 4. Workflow mẫu (MLflow)

1. Log model từ training run.
2. Register model:

```python
result = mlflow.register_model(
    model_uri="runs:/123abc/model",
    name="fraud-detector"
)
```

3. Transition stage:

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()
client.transition_model_version_stage(
    name="fraud-detector",
    version=result.version,
    stage="Staging",
    archive_existing_versions=False
)
```

4. Kết nối CI/CD: khi stage chuyển sang Production → trigger deploy pipeline.

---

## 5. Governance & Best Practices

- [ ] Mỗi model link với dataset version + experiment run ID.
- [ ] Tự động chạy validation suite trước khi promote.
- [ ] Lưu ý backward compatibility (schema, feature availability).
- [ ] Log canary/batch inference kết quả khi model mới deploy.
- [ ] Có quy trình rollback nhanh (CLI/script `promote previous version`).

> 🎯 Bonus: tạo dashboard hiển thị model đang chạy Production + metric health (latency, drift) từ monitoring.
