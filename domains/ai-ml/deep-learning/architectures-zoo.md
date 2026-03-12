## 🧬 Architectures Zoo: RNN → LSTM → GRU

> [← Back to Deep Learning](../README.md)

Trước thời Transformers, các kiến trúc tuần tự cổ điển như RNN/LSTM/GRU vẫn rất hữu ích cho dữ liệu chuỗi ngắn, hoặc khi muốn mô hình nhẹ hơn.

---

## 1. Vanilla RNN

### Công thức
$$ h_t = \tanh(W_{xh}x_t + W_{hh}h_{t-1} + b_h) $$
$$ y_t = W_{hy}h_t + b_y $$

**Vấn đề:** Vanishing/Exploding gradient với chuỗi dài.

**Use cases:** language modeling cơ bản, tín hiệu thời gian ngắn.

---

## 2. LSTM (Long Short-Term Memory)

### Gates
1. **Forget Gate:** quyết định quên bao nhiêu trạng thái cũ.
2. **Input Gate:** chọn thông tin mới.
3. **Output Gate:** quyết định output từ cell state.

LSTM giữ một vector `c_t` (cell state) giúp gradient flow ổn định hơn.

| Gate | Công thức |
| --- | --- |
| Forget | $f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f)$ |
| Input | $i_t = \sigma(W_i x_t + U_i h_{t-1} + b_i)$ |
| Candidate | $\tilde{c}_t = \tanh(W_c x_t + U_c h_{t-1} + b_c)$ |
| Cell update | $c_t = f_t * c_{t-1} + i_t * \tilde{c}_t$ |
| Output | $h_t = o_t * \tanh(c_t)$ |

**Ưu điểm:** học được dependencies dài hạn, chống vanishing gradient tốt.

**Nhược:** nặng (nhiều tham số), chậm.

---

## 3. GRU (Gated Recurrent Unit)

### Gates
* **Reset gate** và **Update gate** thay cho 3 gate của LSTM.
* GRU gộp cell state & hidden state → ít tham số hơn.

| Gate | Công thức |
| --- | --- |
| Update | $z_t = \sigma(W_z x_t + U_z h_{t-1})$ |
| Reset | $r_t = \sigma(W_r x_t + U_r h_{t-1})$ |
| Candidate | $\tilde{h}_t = \tanh(W_h x_t + r_t * (U_h h_{t-1}))$ |
| Hidden | $h_t = (1 - z_t) * h_{t-1} + z_t * \tilde{h}_t$ |

**Ưu:** tốc độ nhanh hơn LSTM, đủ tốt cho nhiều task NLP/time-series.

---

## 4. Bidirectional & Stacked RNNs

* **Bidirectional:** chạy forward + backward → dùng được context hai chiều (e.g., POS tagging).
* **Stacked RNN:** nhiều layer, cần dropout giữa các layer.

> PyTorch snippet:
```python
import torch.nn as nn
model = nn.LSTM(input_size=300, hidden_size=256, num_layers=2,
                batch_first=True, bidirectional=True, dropout=0.3)
```

---

## 5. Khi nào dùng RNN/LSTM/GRU hiện nay?

1. **Hardware hạn chế:** không đủ GPU để chạy Transformer lớn.
2. **Chuỗi ngắn (≤ 200 tokens):** RNN đủ tốt, latency thấp.
3. **TinyML / Edge:** GRU nhẹ, deploy dễ.
4. **Legacy pipelines:** dễ integrate với hệ thống cũ.

> 📌 Tip: Có thể dùng LSTM encoder → trích feature → feed vào model khác (Gradient Boosting) cho time-series tabular.

---

## 6. Checklist triển khai

- [ ] Chuẩn hoá input (padding, masking, pack_padded_sequence cho chuỗi dài).
- [ ] Dùng dropout giữa các layer RNN để tránh overfit.
- [ ] Monitor gradient norm để tránh exploding (clip_grad_norm_).
- [ ] Batch size nhỏ, learning rate thấp (1e-3 với Adam) cho stability.
- [ ] Khi chuyển sang Transformer, có thể reuse embedding/preprocessing.

> 🧠 Insight: Dù Transformer chiếm ưu thế, hiểu RNN/LSTM giúp nắm các khái niệm gating, sequence modeling và so sánh hiệu năng khi triển khai thực tế.
