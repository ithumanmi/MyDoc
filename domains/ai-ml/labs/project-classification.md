## 🖼️ Project: Image Classification Pipeline

> [← Back to Labs](./README.md)

Xây dựng dự án phân loại ảnh end-to-end (data → training → deployment).

---

## 1. Scoping & Dataset

- Chọn domain (hoa, đồ ăn, sản phẩm retail...)
- Thu thập data: Kaggle, scraping, gắn nhãn thủ công.
- Tạo `data/` cấu trúc `train/val/test` theo class.
- Thiết lập `data-card.md` ghi rõ nguồn, license, distribution.

Checklist:

- [ ] Train/val split không bị leakage
- [ ] Augmentation plan
- [ ] Class imbalance handling

---

## 2. Baseline Model

- Fine-tune pretrained model (ResNet50/MobileNetV3) bằng PyTorch/TensorFlow.
- Sử dụng transfer learning (freeze backbone → unfreeze).
- Theo dõi metrics: accuracy, F1, confusion matrix.

Script core (`train.py`):

```python
model = timm.create_model("resnet50", pretrained=True, num_classes=num_classes)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
criterion = nn.CrossEntropyLoss(weight=class_weights)
```

---

## 3. Experiment Tracking & HPO

- Log hyperparams, lr schedule, augmentation config.
- Dùng Optuna hoặc W&B Sweeps tìm lr, weight decay, mixup/cutmix.
- Lưu checkpoint tốt nhất + metrics vào `experiments/`.

---

## 4. Deployment

- Export model → TorchScript/ONNX.
- Tạo REST API (FastAPI/Flask) + Dockerfile.
- Viết `deployment.md` (hardware, latency, monitoring plan).

Example inference API snippet:

```python
@app.post("/predict")
async def predict(file: UploadFile):
    img = preprocess(await file.read())
    probs = torch.softmax(model(img), dim=1)
    return {"label": labels[torch.argmax(probs)], "confidence": probs.max().item()}
```

---

## 5. Deliverables

- ✅ Repo structure: `src/`, `configs/`, `notebooks/`, `deploy/`
- ✅ README với pipeline diagram + demo GIF
- ✅ Metrics dashboard (W&B link hoặc screenshots)

> 🎯 Bonus: triển khai batch inference (cron) và front-end upload ảnh demo.
