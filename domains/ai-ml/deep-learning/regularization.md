---
title: Regularization for Deep Learning
description: Các kỹ thuật giảm overfit, cải thiện generalization cho mô hình sâu.
---

# 🛡️ Regularization

## Mục tiêu
- Giảm overfitting, cải thiện khả năng khái quát hóa.  
- Ổn định training, tránh mô hình học nhiễu.

## Các kỹ thuật chính
- **Weight Decay (L2):** giảm norm của weights; dùng AdamW thay cho Adam + L2 truyền thống.
- **Dropout:** vô hiệu hóa ngẫu nhiên neuron; tốt cho fully-connected, cẩn trọng với BatchNorm.
- **Label Smoothing:** làm mềm one-hot targets (e.g., 0.1/num_classes) để giảm confidence quá mức.
- **Data Augmentation:**
  - Vision: Flip/Crop/ColorJitter, Cutout, Mixup, CutMix, RandAugment.
  - NLP: Back-translation, synonym replacement, dropout embedding.
  - Audio: SpecAugment (mask time/freq).
- **Early Stopping:** dừng khi val metric không cải thiện.
- **Stochastic Depth / DropPath:** bỏ ngẫu nhiên các block trong ResNet/ViT để regularize sâu.
- **BatchNorm/LayerNorm:** gián tiếp regularize bằng chuẩn hóa kích hoạt.
- **Noise injection:** thêm nhiễu vào input/hidden, hoặc Gaussian noise vào weights.

## Công thức thực dụng
- **Label smoothing (PyTorch):** dùng `label_smoothing` trong `CrossEntropyLoss` hoặc tự triển khai.
- **Mixup/CutMix:** áp dụng khi dữ liệu ít, model lớn; thường cải thiện robustness.
- **Weight decay selective:** loại trừ bias/LayerNorm/Gain khỏi decay để tránh underfit.

## Kiểm tra & debug
- Theo dõi khoảng cách train/val: nếu chênh lớn → tăng regularization; nếu cả hai kém → xem lại underfitting/learning rate.
- Kiểm tra ảnh hưởng augmentation: tắt/bật Mixup/CutMix để xem metric val; quá mạnh có thể làm chậm hội tụ.
- Với BatchNorm: batch nhỏ gây noise cao → xem xét GroupNorm/LayerNorm.

## Checklist
- [ ] Dùng weight decay hợp lý (AdamW).  
- [ ] Label smoothing cho classification.  
- [ ] Augmentation phù hợp domain.  
- [ ] Early stopping/patience.  
- [ ] Kiểm tra gap train/val định kỳ.  
- [ ] Loại trừ tham số không nên decay.  
- [ ] Test ảnh hưởng Mixup/CutMix/Dropout.

## Liên quan
- [Optimization Tricks](./optimization-tricks.md)
- [Architectures Zoo](./architectures-zoo.md)
- [Transformers Fundamentals](./transformers-fundamentals.md)