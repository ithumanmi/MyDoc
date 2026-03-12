## 🛡️ Regularization trong Deep Learning

> [← Back to Deep Learning](../README.md)

Regularization giúp mô hình tổng quát tốt hơn, tránh thuộc lòng dữ liệu train. Bảng cheat-sheet dưới đây tổng hợp các kỹ thuật hay dùng.

---

## 1. Dropout & Biến thể

* **Dropout:** Ngẫu nhiên “tắt” một tỷ lệ neuron trong training → ép mạng học các representation bền hơn. Tỷ lệ phổ biến 0.1–0.5.
* **SpatialDropout:** Drop toàn bộ channel (CNN) → giảm co-adaptation features.
* **DropConnect:** Drop các weight thay vì activation, dùng trong một số kiến trúc (e.g., RNN).

> PyTorch: `nn.Dropout(p=0.3)` đặt sau tầng fully connected; với CNN dùng `nn.Dropout2d`.

---

## 2. Early Stopping & Checkpointing

1. Chia train/validation rõ ràng.
2. Theo dõi metric (loss, accuracy) trên validation.
3. Nếu metric không cải thiện sau `patience` epochs → dừng training, load lại checkpoint tốt nhất.

```python
if val_loss < best_loss:
    best_loss = val_loss
    torch.save(model.state_dict(), 'best.pt')
    patience_counter = 0
else:
    patience_counter += 1
    if patience_counter > patience:
        break
```

**Ưu điểm:** Tiết kiệm tài nguyên, tránh overfit muộn. Cẩn thận với dữ liệu nhiều noise – nên kết hợp smoothing/EMA metric.

---

## 3. Data Augmentation

### 3.1 Computer Vision
* **Geometric:** flip, rotation, crop, Cutout, MixUp, CutMix.
* **Color:** brightness/contrast jitter, HSV shift.
* **AutoAugment/RandAugment:** search policy augmentation tự động.

### 3.2 NLP
* **Back-translation:** dịch sang ngôn ngữ khác rồi dịch lại.
* **EDA (Easy Data Augmentation):** synonym replacement, random insertion/deletion.
* **Mixing embedding:** Interpolate latent space.

### 3.3 Audio / Time-series
* **Time Masking / Frequency Masking (SpecAugment).**
* **Jittering, scaling, permutation.**

> ⚠️ Ví dụ CV: dùng Albumentations hoặc torchvision.transforms; NLP dùng NLPAug.

---

## 4. Weight Regularization

| Kỹ thuật | Tác dụng |
| --- | --- |
| L2 / Weight Decay | Phạt weight lớn → mạng đơn giản hơn |
| L1 | Sparse weight → useful khi muốn feature selection |
| Max-Norm Constraint | Giới hạn norm của weight vector |
| Label Smoothing | Phân phối nhãn “mềm” → giảm overconfidence |

**Label Smoothing:** với softmax, thay `y_onehot` bằng `(1-ε)` cho class đúng, `ε/(K-1)` cho phần còn lại.

---

## 5. Noise-based Regularization

1. **Gaussian Noise Layer:** thêm noise vào input hoặc feature intermediate → robust hơn.
2. **Stochastic Depth / DropPath:** random bỏ bớt layer (ResNet/Transformer) trong training.
3. **ShakeDrop / Shake-Shake:** dùng trong kiến trúc ResNeXt.

---

## 6. Checklist triển khai

- [ ] Thử dropout 0.2–0.5 ở fully connected; 0.1 ở CNN.
- [ ] Thiết lập early stopping + checkpoint theo metric business.
- [ ] Áp dụng augmentation phù hợp domain (Albumentations, SpecAugment, NLPAug…).
- [ ] Dùng weight decay chuẩn (AdamW với `weight_decay=0.01`).
- [ ] Thử label smoothing (`epsilon=0.1`) với classification nhiều lớp.
- [ ] Log rõ config regularization để reproducible.

> 🎯 Tip: Chỉ thêm regularization khi model đã đủ capacity. Nếu model underfit, ưu tiên tăng model size/epoch trước rồi mới bật regularization mạnh.
