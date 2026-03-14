---
title: Ensemble Methods Cheatsheet
description: Bagging, boosting, stacking — khi dùng, cách tối ưu, và cảnh báo.
---

# 🧱 Ensemble Methods

## Khi nào dùng
- Cần tăng độ chính xác so với mô hình đơn lẻ.
- Dữ liệu tabular/phức tạp, nhiều feature hỗn hợp.
- Muốn giảm variance (bagging) hoặc bias (boosting).

## Các họ chính
- **Bagging:** Random Forest, Extra Trees — giảm variance, song song tốt.
- **Boosting:** XGBoost, LightGBM, CatBoost — giảm bias, mạnh trên tabular, xử lý missing tốt (CatBoost/LightGBM).
- **Stacking/Blending:** Kết hợp nhiều base learners, meta-learner ở tầng trên.

## Lựa chọn nhanh
- **Baseline mạnh tabular:** LightGBM/CatBoost/XGBoost.
- **Nhiều feature category:** CatBoost (native categorical), LightGBM với categorical.
- **Cần ít tuning, robust:** Random Forest/Extra Trees.
- **Ít dữ liệu, tránh overfit:** Extra Trees hoặc CatBoost với regularization.

## Công thức tuning (gợi ý)
- **Random Forest/Extra Trees:**
  - `n_estimators`: 200–500 (tăng đến khi OOB ổn định).
  - `max_depth`: giới hạn để tránh overfit; thử None, rồi 8–20.
  - `max_features`: sqrt/auto cho classification, log2 cho speed.

- **XGBoost/LightGBM/CatBoost:**
  - Giảm overfit: tăng `min_child_samples`/`min_child_weight`, tăng `lambda_l1/l2`, giảm `max_depth`/`num_leaves`, dùng `subsample` & `colsample_bytree` < 1.
  - Tăng tốc: dùng `hist`/`gpu_hist` (XGB), `device=gpu` (LGBM/CatBoost), giảm `n_estimators` kết hợp `learning_rate` hợp lý.
  - Early stopping: split validation, `early_stopping_rounds=100`.

## Mẫu code ngắn (LightGBM)
```python
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
train_set = lgb.Dataset(X_train, y_train)
val_set = lgb.Dataset(X_val, y_val, reference=train_set)

params = {
    "objective": "binary",
    "metric": "auc",
    "learning_rate": 0.05,
    "num_leaves": 64,
    "feature_fraction": 0.8,
    "bagging_fraction": 0.8,
    "bagging_freq": 1,
}

gbm = lgb.train(
    params,
    train_set,
    num_boost_round=2000,
    valid_sets=[val_set],
    early_stopping_rounds=100,
)

pred = gbm.predict(X_val)
print("AUC", roc_auc_score(y_val, pred))
```

## Stacking đơn giản (sklearn)
```python
from sklearn.ensemble import StackingClassifier, RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression

estimators = [
    ("rf", RandomForestClassifier(n_estimators=300, random_state=42)),
    ("xgb", XGBClassifier(tree_method="hist", eval_metric="logloss", random_state=42)),
]

stack = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(max_iter=500),
    passthrough=False,
)
stack.fit(X_train, y_train)
```

## Pitfalls & lưu ý
- Boosting dễ overfit nếu learning rate cao, max_depth sâu, không có early stopping.
- Feature leakage khi stacking/blending: cần k-fold out-of-fold predictions cho meta-learner.
- Ensemble nặng chi phí inference; xem xét distillation hoặc giảm số cây.
- Với dữ liệu cực mất cân bằng: điều chỉnh `scale_pos_weight` (XGB) hoặc `is_unbalance/scale_pos_weight` (LGBM), dùng AUC/PR thay vì accuracy.

## Đánh giá
- Dùng cross-validation; ưu tiên stratified cho phân loại.
- Theo dõi cả **variance** giữa các fold; ensemble nên giảm variance.
- So sánh với baseline đơn giản để chắc chắn ensemble thực sự mang lại lợi ích.

## Liên quan
- [Feature Engineering](./feature-engineering.md)
- [Model Selection](./model-selection.md)
- [Semi-supervised Learning](./semi-supervised-learning.md)