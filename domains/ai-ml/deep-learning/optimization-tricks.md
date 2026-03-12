## ⚙️ Optimization Tricks cho Deep Learning

> [← Back to Deep Learning](../README.md)

Training mạng sâu không chỉ là chọn optimizer “auto”. Dưới đây là các kỹ thuật tối ưu hoá được áp dụng thực chiến để tăng tốc hội tụ và giảm overfitting.

---

## 1. Optimizer Landscape

| Optimizer | Khi nào dùng | Ưu / Nhược |
| --- | --- | --- |
| SGD + Momentum | Vision, khi cần generalization tốt | Đơn giản, ổn định nhưng cần tuning LR kỹ |
| Nesterov Momentum | Giảm overshoot | Bias thấp hơn momentum truyền thống |
| Adam / AdamW | NLP, Transformer, mô hình lớn | Tự động điều chỉnh LR từng tham số; AdamW tách weight decay chuẩn |
| RMSProp | RNN, sequence | Điều chỉnh LR theo EMA gradient |
| Adagrad | Sparse feature (NLP cổ điển) | LR giảm dần – cẩn trọng vì có thể “chết” LR sau vài nghìn step |

### Adam vs AdamW
* **Adam**: weight decay được áp dụng như L2 trong loss → thực chất là L2 regularization → gây bias.
* **AdamW**: tách hẳn weight decay và gradient update → giữ chuẩn hoá bước update, là mặc định trong hầu hết Transformer.

> 🔧 PyTorch: `torch.optim.AdamW(model.parameters(), lr=3e-4, betas=(0.9, 0.95), weight_decay=0.01)`

---

## 2. Learning Rate Scheduling

| Scheduler | Ý tưởng | Use case |
| --- | --- | --- |
| Step / MultiStep | Giảm LR tại epoch cố định | Vision ResNet training |
| Exponential | LR = lr0 * γ^epoch | Khi muốn decay mượt |
| Cosine Annealing | LR giảm theo cos → có thể warm restarts | Transformers, diffusion |
| OneCycle | LR tăng rồi giảm | Fast convergence (FastAI) |
| Cyclical LR | Dao động giữa min-max | Khám phá landscape tốt hơn |

**Warmup:** vài trăm đến vài nghìn step đầu tăng LR từ nhỏ → mục tiêu để optimizer ổn định (đặc biệt với batch norm/AdamW + Transformers).

```python
from torch.optim.lr_scheduler import CosineAnnealingLR
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-4)
scheduler = CosineAnnealingLR(optimizer, T_max=100)
for epoch in range(100):
    train_one_epoch(...)
    scheduler.step()
```

---

## 3. Gradient Tricks

1. **Gradient Clipping:** hạn chế giá trị gradient để tránh exploding (`torch.nn.utils.clip_grad_norm_`).
2. **Mixed Precision Training (AMP):** dùng float16/bfloat16 với scaler → tăng tốc 2-3x và giảm memory.
3. **Gradient Accumulation:** mô phỏng batch lớn khi GPU nhỏ (`loss / accumulation_steps`).
4. **Lookahead / SAM:** (Sharpness-Aware Minimization) giúp model tìm minima “phẳng” hơn → generalization tốt.

---

## 4. Batch Normalization & Biến thể

| Layer | Mục đích | Lưu ý |
| --- | --- | --- |
| BatchNorm | Chuẩn hoá mean/std trên batch | Phù hợp CNN, batch size ≥ 16 |
| LayerNorm | Normalize theo feature | Transformers, batch size 1 vẫn ổn |
| GroupNorm | Chia channels thành group nhỏ | Vision với batch bé |
| RMSNorm | Normalize theo RMS, bỏ mean | Một số Transformer hiện đại |

**Benefits:** ổn định gradient, cho phép LR lớn hơn, đóng vai trò regularizer nhẹ.

> ⚠️ Khi inference nhớ bật `model.eval()` để sử dụng running mean/var.

---

## 5. Checklist tối ưu hoá training loop

- [ ] Dùng optimizer phù hợp domain (SGD+mom cho vision, AdamW cho Transformer).
- [ ] Thiết lập warmup + scheduler rõ ràng, log LR trong training dashboard.
- [ ] Theo dõi gradient norm (TensorBoard) để phát hiện exploding/vanishing.
- [ ] Sử dụng AMP + gradient clipping để ổn định và tiết kiệm tài nguyên.
- [ ] Khi huấn luyện dài, bật EMA weights (Exponential Moving Average) để tăng stability.

> 📌 Tip: Khi tuning, bắt đầu với LR lớn (1e-3) + cosine scheduler, quan sát loss; nếu loss “nổ” → giảm LR hoặc tăng warmup steps.
