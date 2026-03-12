## 🧾 Experiment Tracking Templates

> [← Back to AI/ML Roadmap](../README.md)

Giữ lịch sử thí nghiệm rõ ràng giúp tái lập kết quả, so sánh mô hình, và bàn giao cho team dễ dàng.

---

## 1. Pillars của Tracking

1. **Metadata:** Thông tin dataset, commit hash, hyperparameters.
2. **Metrics:** Train/validation/test, custom business KPI.
3. **Artifacts:** Model binary, scaler, feature importance, plots.
4. **Reproducibility:** Script/pipeline để chạy lại.

---

## 2. Template Notebook / README

```
## Experiment ID: 2026-03-ML-001

### Objective
- Predict customer churn with new feature set (lag features).

### Data
- Dataset: Telco Churn v2 (2026-02 snapshot)
- Split: 70/15/15 (stratified)

### Features / Engineering
- Added rolling call_count_7d
- Encoded plan_type via target encoding

### Model & Hyperparameters
- LightGBM v3.3.5
- max_depth=6, learning_rate=0.05, num_leaves=32

### Metrics
| Metric | Value |
| --- | --- |
| ROC-AUC | 0.864 |
| PR-AUC | 0.445 |
| F1 | 0.61 |

### Notes
- Feature importance shows call_count_7d ranks #2
- Needs calibration check

### Next Steps
- Try SHAP for interpretability
- Evaluate cost-based threshold
```

---

## 3. Tooling & Config Snippets

### MLflow Quickstart

```python
import mlflow
mlflow.set_experiment("churn-classic-ml")

with mlflow.start_run(run_name="lgbm-lag-features"):
    mlflow.log_params({"max_depth": 6, "learning_rate": 0.05})
    mlflow.log_metric("roc_auc", 0.864)
    mlflow.sklearn.log_model(model, "model")
```

### Weights & Biases Config

```yaml
project: classic-ml
entity: your-team
config:
  dataset_version: 2026-02
  model_type: lightgbm
  max_depth: 6
  learning_rate: 0.05
```

---

## 4. Checklist

- [ ] Ghi lại dataset version và hashing pipeline.
- [ ] Lưu hyperparameters & random seed.
- [ ] Log metric chuẩn + custom KPI.
- [ ] Lưu artifacts (model, scaler, feature list).
- [ ] Link tới dashboard giám sát trong production.

---

## 5. Collaboration Tips

*   Dùng template chung (Notion, Confluence) để mô tả experiment.
*   Đặt naming convention cho run (YYYYMMDD-usecase-model).
*   Tự động sync run summary vào Slack/Teams channel.

> 🧠 Tip: Khi bàn giao, cung cấp bundle gồm notebook, config YAML, và link đến run dashboard để người khác có thể tái chạy ngay.
