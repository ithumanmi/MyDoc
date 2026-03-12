## 🎥 Video Understanding Guide

> [← Back to Computer Vision](./README.md)

Action recognition, temporal modeling và video representation cho các use case surveillance, sports analytics, short-form content.

---

## 1. Kiến trúc action recognition

| Model | Ý tưởng | Ghi chú |
| --- | --- | --- |
| **2D CNN + Temporal Pooling** | Áp CNN từng frame + average | Baseline nhanh nhưng không nắm động tác |
| **Two-Stream (RGB + Optical Flow)** | Xử lý spatial và motion riêng | Cần tính optical flow, tốn compute |
| **3D CNN (C3D, I3D)** | Conv 3D trên (T, H, W) | Học chuyển động trực tiếp, chi phí cao |
| **SlowFast** | Hai nhánh tốc độ khác nhau (slow global, fast motion) | SOTA cho hành động, trade-off tốt |
| **Video Transformer (TimeSformer, ViViT)** | Self-attention theo trục không gian + thời gian | Scalable, cần nhiều dữ liệu |

---

## 2. Temporal Modeling Techniques

1. **Temporal Shift Module (TSM):** dịch một phần feature giữa frames để mô phỏng 3D conv.
2. **Temporal Convolution / Dilated Conv:** 1D conv theo trục thời gian (TCN).
3. **Recurrent Layers (LSTM/GRU):** lấy feature từ CNN → đưa vào RNN.
4. **Attention-based pooling:** chiếu trọng số theo thời gian.

---

## 3. Dataset & Evaluation

| Dataset | Domain |
| --- | --- |
| **Kinetics-700** | Tổng hợp hành động YouTube |
| **Something-Something** | Motion-centric (phụ thuộc thứ tự) |
| **AVA** | Action detection spatio-temporal |
| **Sports-1M** | Sports multi-label |

**Metrics:** Top-1/Top-5 accuracy, mAP (detection), F1 theo hành động.

---

## 4. Deployment Considerations

- [ ] Sampling frames: uniform vs clip sampling theo motion.
- [ ] Preprocess: resize/crop + optical flow (nếu dùng two-stream).
- [ ] Edge deployment: dùng 2D CNN + temporal shift (TSM) để tiết kiệm compute.
- [ ] Streaming: batching theo clip (t=16/32 frames) → phục vụ realtime inference.
- [ ] Monitoring: log latency, drop frame, accuracy theo từng hoạt động.

> ⚡ Tip: Fine-tune từ pretrained Kinetics giúp tăng accuracy đáng kể so với train from scratch.

---

## 5. Tooling

* [PySlowFast](https://github.com/facebookresearch/SlowFast)
* [MMAction2](https://github.com/open-mmlab/mmaction2)
* [TorchVision Video Models](https://pytorch.org/vision/stable/models.html#video-classification)
