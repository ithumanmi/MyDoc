## 🏁 Kaggle Starter Repo Template

> [← Back to Hands-on Labs](./hands-on-labs.md)

Sử dụng cấu trúc repo dưới đây để bắt đầu một competition Kaggle và cộng tác với team.

```
kaggle-project/
├── README.md
├── data/
│   ├── raw/ (kaggle competitions download ...)
│   └── processed/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── data.py
│   ├── features.py
│   └── models.py
├── configs/
│   └── lgbm.yml
├── scripts/
│   ├── run_train.sh
│   └── submit.sh
├── experiments/
│   └── 2026-03-12_lgbm.json
├── requirements.txt
└── kaggle.json (API token - đừng commit)
```

---

## 1. README.md template

```
# Kaggle Competition Name

## Setup
- `pip install -r requirements.txt`
- `kaggle competitions download -c <competition-name>`

## Workflow
1. Chạy `notebooks/01_eda.ipynb`
2. Chạy `python src/features.py` để tạo features
3. `python src/models.py --config configs/lgbm.yml`
4. `python scripts/submit.py --input submissions/latest.csv`

## Experiments
- Lưu JSON/YAML trong `experiments/`
```

---

## 2. Config sample (configs/lgbm.yml)

```yaml
dataset:
  train: data/processed/train.parquet
  test: data/processed/test.parquet
model:
  type: lightgbm
  params:
    num_leaves: 64
    learning_rate: 0.05
    n_estimators: 1000
training:
  cv_folds: 5
  seed: 42
  early_stopping_rounds: 100
output:
  submission: submissions/lgbm_20260312.csv
```

---

## 3. Training script snippet (src/models.py)

```python
import yaml
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold

with open("configs/lgbm.yml") as f:
    cfg = yaml.safe_load(f)

train = pd.read_parquet(cfg["dataset"]["train"])
X = train.drop("target", axis=1)
y = train["target"]

skf = StratifiedKFold(n_splits=cfg["training"]["cv_folds"], shuffle=True, random_state=cfg["training"]["seed"])
oof = np.zeros(len(X))
models = []

for fold, (tr_idx, val_idx) in enumerate(skf.split(X, y)):
    X_tr, X_val = X.iloc[tr_idx], X.iloc[val_idx]
    y_tr, y_val = y.iloc[tr_idx], y.iloc[val_idx]
    train_set = lgb.Dataset(X_tr, y_tr)
    val_set = lgb.Dataset(X_val, y_val)
    model = lgb.train(
        cfg["model"]["params"],
        train_set,
        valid_sets=[val_set],
        num_boost_round=cfg["model"]["params"]["n_estimators"],
        early_stopping_rounds=cfg["training"]["early_stopping_rounds"]
    )
    models.append(model)
    oof[val_idx] = model.predict(X_val)

np.save("experiments/oof_lgbm.npy", oof)
```

---

## 4. Submission helper (scripts/submit.py)

```python
import argparse
import pandas as pd
from kaggle import api

parser = argparse.ArgumentParser()
parser.add_argument("--input", default="submissions/latest.csv")
parser.add_argument("--message", default="baseline")
args = parser.parse_args()

api.competition_submit(file_name=args.input, competition="<competition-name>", message=args.message)
```

---

## 5. Tips

*   `kaggle datasets list -s <keyword>` để tìm dataset phụ trợ.
*   Dùng `Makefile` để gói lệnh (make data, make train, make submit).
*   Sync notebook/output lên DVC để theo dõi version.

> 🎯 Tip: Clone template này cho mỗi competition, chỉ cần cập nhật config và dataset path là có thể chạy pipeline end-to-end.
