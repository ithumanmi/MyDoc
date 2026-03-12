## 🚀 Classic ML Deployment Templates

> [← Back to AI/ML Roadmap](../README.md)

Checklist và template giúp đưa mô hình Classic ML từ notebook ra production.

---

## 1. Deployment Options

| Scenario | Template | Stack |
| --- | --- | --- |
| **REST API (Batch/Online)** | FastAPI/Flask + Uvicorn | Python, scikit-learn, pydantic |
| **Batch Scoring Pipeline** | Airflow/Prefect DAG | Python, pandas, cloud storage |
| **Stream Scoring** | Kafka consumer + Model server | Python, Faust, Redis |
| **Embedded / Edge** | ONNX / CoreML export | scikit-learn → ONNXRuntime |

---

## 2. REST API Template (FastAPI)

```python
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

class CustomerFeatures(BaseModel):
    age: int
    tenure: int
    credit_score: float
    # ...

app = FastAPI()

@app.post("/predict")
def predict(payload: CustomerFeatures):
    X = scaler.transform([[payload.age, payload.tenure, payload.credit_score]])
    proba = model.predict_proba(X)[0, 1]
    return {"churn_probability": proba}
```

**Checklist:**

- [ ] Input validation (pydantic).
- [ ] Logging + tracing (structlog, OpenTelemetry).
- [ ] Version headers (`X-Model-Version`).
- [ ] Healthcheck endpoint.

---

## 3. Batch Pipeline Template (Prefect)

```python
from prefect import flow, task
import pandas as pd
import joblib

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

@task
def load_data(path):
    return pd.read_parquet(path)

@task
def preprocess(df):
    df[feature_cols] = scaler.transform(df[feature_cols])
    return df

@task
def score(df):
    df["score"] = model.predict_proba(df[feature_cols])[:, 1]
    return df

@task
def save(df, path):
    df.to_parquet(path)

@flow
def batch_scoring(input_path, output_path):
    df = load_data(input_path)
    df = preprocess(df)
    df = score(df)
    save(df, output_path)
```

**Checklist:** version data/model, notify on failure, schedule via Prefect/Airflow.

---

## 4. CI/CD + Model Registry

1. **Git + Tests:** Unit tests cho preprocessing, serialization.
2. **Model Registry:** MLflow, SageMaker Model Registry, Vertex Model Registry.
3. **Promotion Flow:** Staging → Canary → Production.
4. **Monitoring:** Drift detection, latency, error rate.

---

## 5. Deployment Playbook

- [ ] Đóng gói model + artifacts (`requirements.txt`, `model.joblib`, `scaler.joblib`).
- [ ] Container hóa với Docker + slim base image.
- [ ] Chạy load test bằng Locust/k6.
- [ ] Thiết lập alerting (Prometheus + Grafana, Datadog).
- [ ] Rollback plan: giữ lại model version trước.

> 💡 Tip: Dù là Classic ML, hãy đối xử như microservice. Logging chuẩn, feature parity giữa training & inference, và monitoring đầy đủ giúp model sống lâu trong production.
