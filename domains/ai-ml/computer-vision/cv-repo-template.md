## 🗂️ Computer Vision Project Repo Template

> [← Back to Computer Vision](./README.md)

Clone cấu trúc này để triển khai dự án CV từ training đến deployment.

```
cv-project/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_explore.ipynb
│   ├── 02_training.ipynb
│   └── 03_evaluation.ipynb
├── src/
│   ├── datasets/
│   │   └── transforms.py
│   ├── models/
│   │   ├── unet.py
│   │   └── yolov8.py
│   ├── training/
│   │   └── trainer.py
│   └── inference/
│       └── serve.py
├── configs/
│   ├── seg_unet.yaml
│   └── detect_yolo.yaml
├── deployments/
│   ├── docker/
│   │   └── Dockerfile.triton
│   └── scripts/
│       └── deploy_triton.sh
├── experiments/
│   └── 2026-03-13_seg.json
├── Makefile
├── requirements.txt
└── mlruns/ (MLflow)
```

---

## 1. README checklist

- Use cases & metric (mAP, Dice).
- Data pipeline mô tả folder `data/`.
- How to run:
  ```bash
  make data
  make train SEG_CONFIG=configs/seg_unet.yaml
  make deploy
  ```
- Link tới demo/inference endpoint.

---

## 2. Makefile sample

```makefile
DATA_CONFIG ?= configs/data.yaml

data:
	python scripts/download_data.py --config $(DATA_CONFIG)

train:
	python src/training/trainer.py --config $(SEG_CONFIG)

deploy:
	sh deployments/scripts/deploy_triton.sh
```

---

## 3. Config snippet (seg_unet.yaml)

```yaml
dataset:
  train: data/processed/train
  valid: data/processed/valid
model:
  encoder: resnet34
  decoder: unet
training:
  epochs: 40
  lr: 1e-4
  mixed_precision: true
logging:
  mlflow_uri: ./mlruns
  experiment: cv-segmentation
deployment:
  export_path: deployments/models/unet.onnx
```

---

## 4. Inference server (serve.py)

```python
import torch
from fastapi import FastAPI, UploadFile

app = FastAPI()
model = torch.jit.load("deployments/models/unet.pt")

@app.post("/segment")
async def segment(file: UploadFile):
    # preprocess -> model -> postprocess
    return {"mask": "base64..."}
```

---

## 5. Deployment script skeleton

```bash
#!/bin/bash
MODEL_NAME=unet
TRITON_REPO=deployments/models

tritonserver --model-repository=$TRITON_REPO \
    --model-control-mode=poll --repository-poll-secs=60
```

---

> ⚙️ Tip: Repo nên kèm `.devcontainer` hoặc `docker-compose` để chuẩn hóa môi trường dev và inference.
