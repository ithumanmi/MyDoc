# 📒 Experiment Tracking Deep Dive

> [← Back to MLOps](./README.md)

Tracking giúp tái lập thí nghiệm, so sánh mô hình và cộng tác giữa Data Scientist.

---

## 1. Thành phần chính

1. **Metadata:** learning rate, batch size, seed, git commit.
2. **Artifacts:** model checkpoint, confusion matrix, plots.
3. **Metrics:** accuracy, loss, latency.
4. **Lineage:** datasource, feature version, code version.

---

## 2. Công cụ phổ biến

| Tool | Ưu điểm | Use case |
| --- | --- | --- |
| **MLflow Tracking** | OSS, dễ self-host, API Python/REST. | Nhóm muốn kiểm soát hạ tầng. |
| **Weights & Biases (W&B)** | UI mạnh, integrations (sweeps, reports). | Team remote, cần collaboration nhanh. |
| **DVC** | Git-like cho dữ liệu/artifacts, version control pipelines. | Repo code-first, cần reproducibility mạnh. |

---

## 3. Workflow mẫu (MLflow)

```python
import mlflow

with mlflow.start_run(run_name="xgboost-v1"):
    mlflow.log_params({"lr": 0.05, "max_depth": 6})
    mlflow.log_metric("rmse", 0.42)
    mlflow.log_artifact("plots/feature_importance.png")
    mlflow.sklearn.log_model(model, "model")
```

- Host local (`mlflow ui`) hoặc remote server + backend (Postgres) + artifact store (S3, GCS).
- Tag run với git SHA để truy ngược.

---

## 4. W&B Playbook

- `wandb.init(project="fraud-detection", config=config)`.
- Log bảng, audio, video → thay đổi hyperparam real-time.
- Dùng **Sweeps** để auto-tune: define search space (Bayesian, random).
- Reports: tạo dashboard chia sẻ với stakeholders.

---

## 5. DVC Pipelines

- `dvc run -n train -d data/processed -d src/train.py -o models/model.pkl python src/train.py`
- `dvc metrics show` so sánh metric qua các version.
- `dvc exp run` để chạy thí nghiệm nhanh, kết hợp `dvc exp apply`.

---

## 6. Best Practices

- [ ] Chuẩn hoá naming convention (project/run name).
- [ ] Log seed + random state để reproducible.
- [ ] Mỗi run gắn với dataset version (DVC hash, Delta table version).
- [ ] Thiết lập retention policy (xoá artifact cũ sau n ngày).
- [ ] Tự động sync với model registry sau khi đạt chuẩn.

> 🎯 Bonus: xây bot Slack thông báo run tốt nhất và link trực tiếp đến dashboard.
