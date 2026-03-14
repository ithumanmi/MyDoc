---
title: Deep Learning Optimization Tricks
description: Hướng dẫn thực dụng tối ưu training/inference cho mô hình deep learning.
---

# ⚡ Deep Learning Optimization Tricks

## Setup & reproducibility
- **Seed everything:** `torch.manual_seed`, `numpy`, `random`, `deterministic` flags nếu cần tái lập.
- **Mixed Precision (AMP):** `torch.cuda.amp.autocast` + `GradScaler` để tăng tốc, giảm VRAM.
- **cuDNN:** bật `benchmark=True` cho input size cố định; tắt nếu input biến thiên để tránh overhead.

## Optimizer & scheduler
- **Optimizers phổ biến:** Adam/AdamW (ổn định), SGD + momentum (tổng quát tốt), Lion/Adafactor cho mô hình lớn.
- **Weight decay:** dùng AdamW thay vì Adam + L2. Chú ý loại trừ bias/LayerNorm khỏi decay.
- **Learning rate schedules:** Cosine decay + warmup; One-cycle policy cho vision; Step decay cho đơn giản.
- **Gradient clipping:** `clip_grad_norm_` để tránh exploding gradients.

## Regularization
- **Dropout:** hợp lý cho fully-connected; với CNN/ViT xem xét Stochastic Depth.
- **Data Augmentation:** RandAugment/AutoAugment, Mixup/CutMix (vision), SpecAugment (audio), label smoothing.
- **Early stopping:** theo dõi val metric, patience.

## Batch size & accumulation
- Tăng batch size nếu có VRAM; nếu không đủ, dùng **gradient accumulation** để giả lập batch lớn hơn.
- Chú ý hiệu chỉnh learning rate khi batch size thay đổi (linear scaling rule).

## Initialization & normalization
- **Init:** Kaiming/He cho ReLU, Xavier/Glorot cho tanh/sigmoid, `trunc_normal_` cho ViT.
- **Normalization:** BatchNorm (phổ biến), LayerNorm (transformer), GroupNorm (nhỏ batch). Với micro-batch, ưu tiên LayerNorm/GroupNorm.

## Training stability
- Kiểm tra **loss nan/inf:** learning rate quá cao, AMP loss scale sai, input contains NaN.
- Kiểm tra **label/target**: one-hot vs class index; đảm bảo không sai dtype/device.
- **Gradient check:** log norm; nếu 0 → dead path, nếu quá lớn → exploding.

## Inference tối ưu
- **ONNX/TensorRT/torch.compile:** chuyển mô hình để tối ưu graph.  
- **Quantization:** PTQ (int8) hoặc QAT khi cần độ chính xác cao hơn.  
- **Batching & caching:** ghép batch inference, cache encoder/kv-cache cho decoder.

## Checklists nhanh
- [ ] Đặt seed & log mọi config.  
- [ ] Dùng AMP + grad scaler.  
- [ ] Có scheduler (warmup + decay).  
- [ ] Clipping gradient khi cần.  
- [ ] Augmentation hợp lý, label smoothing nếu classification.  
- [ ] Monitor gradient norm, learning rate, GPU util, throughput.  
- [ ] Val metric theo epoch/steps với early stop.

## Liên quan
- [Regularization](./regularization.md)
- [Architectures Zoo](./architectures-zoo.md)
- [Transformers Fundamentals](./transformers-fundamentals.md)