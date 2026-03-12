## 🧱 Convolutional Tricks: Làm chủ CNN thực chiến

> [← Back to Deep Learning](../README.md)

Các kỹ thuật dưới đây giúp tăng hiệu quả khi huấn luyện và triển khai mạng tích chập (CNN) cho Computer Vision.

---

## 1. Kiến trúc CNN hiện đại

| Kiến trúc | Ý tưởng chính | Khi dùng |
| --- | --- | --- |
| **ResNet** | Skip connection để tránh vanishing gradient | Phân loại hình ảnh tổng quát, backbone phổ biến |
| **DenseNet** | Kết nối dày đặc để tái sử dụng feature | Dataset nhỏ, cần parameter efficiency |
| **MobileNet / EfficientNet** | Depthwise separable conv + compound scaling | Edge device, inference nhanh |
| **ConvNeXt** | Conv-based với phong cách Transformer | Bài toán cần accuracy cao nhưng muốn dùng conv |

---

## 2. Convolution Tricks

### 2.1 Depthwise & Pointwise Convolution
* Tách conv 3×3 thành depthwise (per channel) + pointwise 1×1 → giảm tham số 8–9 lần.
* Core của MobileNet, EfficientNet.

### 2.2 Dilated / Atrous Convolution
* Giãn receptive field mà không giảm resolution.
* Dùng trong segmentation (DeepLab) để giữ spatial detail.

### 2.3 Grouped Convolution
* Chia channels thành group; ResNeXt dùng grouped conv để mở rộng width.

### 2.4 Squeeze-and-Excitation (SE)
* Học attention trên channel, tăng accuracy 1–2% với chi phí nhỏ.

---

## 3. Training Tricks

1. **Data Augmentation mạnh:** MixUp, CutMix, RandAugment để tăng robust.
2. **Label Smoothing:** 0.1 giúp giảm overconfidence khi huấn luyện lâu.
3. **Stochastic Depth / DropPath:** áp dụng trong ViT/CNN hybrid.
4. **EMA Weights:** duy trì moving average của weights để inference ổn định.
5. **Large Batch + LARS/LayerScale:** cho training ở scale ImageNet.

```python
import timm
model = timm.create_model('efficientnetv2_s', pretrained=True, drop_path_rate=0.2)
```

---

## 4. Deployment Tips

- [ ] Fuse BatchNorm vào Conv khi export → giảm latency.
- [ ] Dùng TorchScript/ONNX/TensorRT cho inference.
- [ ] Quantization-aware training (QAT) để chạy trên edge.
- [ ] Kiểm tra receptive field đủ lớn với Grad-CAM/Feature visualization.
- [ ] Sử dụng mixed precision (FP16) cho camera streaming realtime.

> 🔍 Debug CNN: visualize feature map, kiểm tra distribution activation để phát hiện dead ReLU.
