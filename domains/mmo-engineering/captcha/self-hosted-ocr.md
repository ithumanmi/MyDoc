# 🏭 Self-hosted OCR for Text Captcha

## 1. Use Cases
- Legacy text captchas (distorted characters) trên forum, CMS cũ.
- Muốn tránh lệ thuộc dịch vụ bên ngoài, chủ động scale.

## 2. Data Pipeline
- Crawl captcha samples (screenshot, base64) + label thủ công (Label Studio).
- Augment: rotation, blur, background noise để tăng robustness.
- Store trong dataset versioned (DVC, Weights & Biases).

## 3. Model Choices
- **CRNN (Convolutional Recurrent Neural Network)**: phổ biến cho OCR sequence.
- **Transformer-based (TRBA/ViT):** accuracy cao hơn khi có data lớn.
- **Lightweight (Tesseract custom training):** nhanh, dễ deploy nhưng cần tuning nặng.

## 4. Training Setup
- Framework: PyTorch + `torchvision`, hoặc TensorFlow/Keras.
- Loss: CTC (Connectionist Temporal Classification).
- Hyperparams: batch 64, image resize 100x32, Adam optimizer.
- Track metrics: character accuracy, sequence accuracy.

## 5. Deployment
- Export model (TorchScript/ONNX) → serve bằng FastAPI + GPU/CPU server.
- REST endpoint `/solve` nhận base64 → trả text.
- Optimize: batch requests, quantization (int8) để chạy CPU.

## 6. Ops & Monitoring
- Log confidence score, auto route low-confidence (<0.6) sang manual solver.
- Retrain định kỳ khi site đổi font.
- Protect API bằng auth token, rate limit.

## 7. Checklist
- [ ] Dataset >= 50k samples đa dạng noise.
- [ ] Mô hình có fallback manual.
- [ ] Monitor accuracy và retrain schedule.