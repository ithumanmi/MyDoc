## 🧮 Model Selection & Hyperparameter Tuning

> [← Back to Classic ML](./README.md)

Model tốt không chỉ đến từ thuật toán mà còn từ quy trình chọn mô hình, cross-validation và tối ưu hyperparameter.

---

## 1. Cross-validation (CV)

| Kiểu CV | Khi nào dùng | Notes |
| --- | --- | --- |
| K-Fold (K=5/10) | Dataset vừa phải, IID | Trade-off bias/variance |
| Stratified K-Fold | Classification mất cân bằng | Bảo toàn tỷ lệ class |
| TimeSeriesSplit | Dữ liệu thời gian | Giữ tính thời gian, không shuffle |
| Group K-Fold | Khi có nhóm (user/session) | Tránh leakage giữa nhóm |

**Nested CV:** outer loop đánh giá generalization, inner loop tuning hyperparameters → tránh overfitting vào validation.

> 🛠️ Snippet sklearn:
```python
from sklearn.model_selection import StratifiedKFold, cross_validate

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_validate(model, X, y, cv=cv, scoring=['accuracy', 'f1'])
```

---

## 2. Hyperparameter Optimization (HPO)

### 2.1 Grid Search
* Thử toàn bộ tổ hợp hyperparameters.
* Dễ hiểu nhưng tốn thời gian nếu grid lớn.

### 2.2 Random Search
* Chọn ngẫu nhiên từ distribution → khám phá nhanh.
* `RandomizedSearchCV` thường hiệu quả hơn grid.

### 2.3 Bayesian Optimization
* Sử dụng surrogate model (Gaussian Process, TPE) để dự đoán vùng tốt.
* Công cụ: Optuna, Hyperopt, scikit-optimize.

### 2.4 Hyperparameter via Gradient/Population
* **Hyperband/ASHA:** early stop các trial kém.
* **Population Based Training (PBT):** tiến hoá hyperparameters online.

> ⚙️ Optuna ví dụ:
```python
import optuna

def objective(trial):
    c = trial.suggest_float('C', 1e-3, 10.0, log=True)
    gamma = trial.suggest_float('gamma', 1e-4, 1.0, log=True)
    model = SVC(C=c, gamma=gamma)
    scores = cross_val_score(model, X, y, cv=5, scoring='f1')
    return scores.mean()

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)
```

---

## 3. Model Comparison & Selection Criteria

1. **Metrics phù hợp domain:** Accuracy, ROC-AUC, PR-AUC, RMSE, MAE...
2. **Complexity vs Interpretability:** Logistic vs Tree vs Boosting.
3. **Latency & Resource:** Model nhỏ hơn cho inference realtime.
4. **Robustness:** Kiểm tra cross-validation std, stress test với adversarial/noisy samples.
5. **Cost:** Training/inference cost, licensing.

Tạo bảng so sánh (score, inference time, footprint) để trình lên stakeholders.

---

## 4. Workflow Recommended

1. Xây pipeline `Pipeline( preprocessing → model )` để tránh leakage.
2. Dùng `cross_validate`/`GridSearchCV` với scoring đa chỉ tiêu.
3. Lưu lại model + params + scores trong MLflow/W&B.
4. Chọn best model theo metric chính, nhưng giữ candidate runner-up.
5. Chạy thêm holdout test set hoặc backtest (time-series) trước khi deploy.

---

## 5. Tools

* **sklearn:** `GridSearchCV`, `RandomizedSearchCV`, `HalvingGridSearchCV`.
* **Optuna/Hyperopt:** Bayesian/TPE tuning, pruning.
* **Ray Tune:** scale tuning trên cluster.
* **MLflow:** log hyperparameters, metrics, artifacts.


> 📈 Tip: Khi dataset lớn, dùng **early stopping + warm start** để tiết kiệm chi phí tuning. Luôn ghi lại seed, data split để reproducible.

> 🧪 Notebook: [Optuna Tuning Lab](./notebooks/optuna-tuning-lab.ipynb)
