## 🧭 Transformers Fundamentals

> [← Back to Deep Learning](../README.md)

Transformers đã trở thành xương sống của NLP, Vision và Multi-modal. File này tóm tắt kiến trúc cơ bản để bạn hiểu rõ trước khi đi sâu vào LLM hoặc ViT.

---

## 1. Kiến trúc tổng quan

1. **Embedding Layer:** chuyển token/id thành vector.
2. **Positional Encoding:** thêm thông tin vị trí (sinusoidal hoặc learned).
3. **Stack encoder/decoder blocks:** mỗi block gồm Multi-Head Attention + Feed Forward + skip connections + LayerNorm.
4. **Output Layer:** linear + softmax (NLP) hoặc head task-specific.

### Encoder vs Decoder
* **Encoder-only (BERT):** dùng cho understanding tasks (classification, NER).
* **Decoder-only (GPT):** autoregressive generation.
* **Encoder-decoder (T5, Transformer gốc):** sequence-to-sequence (translation, summarization).

---

## 2. Multi-Head Self-Attention

| Thành phần | Mô tả |
| --- | --- |
| Query (Q) | vector đại diện token cần “hỏi” |
| Key (K) | vector đại diện token cung cấp thông tin |
| Value (V) | thông tin thực tế được trộn |

Tính attention score: `softmax(QK^T / sqrt(d_k)) * V`

**Multi-head:** chia d_model thành nhiều head để học quan hệ khác nhau (syntax, position, semantics).

> ⚠️ Cần mask (causal mask) cho decoder-only để tránh nhìn tương lai.

---

## 3. Positional Encoding

### Sinusoidal (Transformer gốc)

```
PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

### Learned
* Parameter hóa vị trí, linh hoạt hơn cho dữ liệu ngắn.

### Rotary (RoPE)
* Dùng trong GPT-NeoX, Llama: xoay embedding theo vị trí → hỗ trợ extrapolation tốt hơn.

---

## 4. Feed Forward Network (FFN)

* Hai lớp linear + activation (GELU/ReLU).
* Thường giãn ra 4× `d_model` rồi co lại.

> PyTorch snippet:
```python
import torch.nn as nn

class TransformerBlock(nn.Module):
    def __init__(self, d_model=512, nhead=8):
        super().__init__()
        self.attn = nn.MultiheadAttention(d_model, nhead, batch_first=True)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_model*4),
            nn.GELU(),
            nn.Linear(d_model*4, d_model)
        )
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
    def forward(self, x, attn_mask=None):
        attn_out, _ = self.attn(x, x, x, attn_mask=attn_mask)
        x = self.norm1(x + attn_out)
        ff_out = self.ffn(x)
        return self.norm2(x + ff_out)
```

---

## 5. Transformer Variants

| Loại | Ý tưởng |
| --- | --- |
| **GPT (Decoder)** | Unidirectional, causal mask |
| **BERT (Encoder)** | Masked Language Modeling, bi-directional |
| **T5 (Encoder-Decoder)** | Text-to-text, shared tokenizer |
| **ViT (Vision Transformer)** | Chia ảnh thành patch, add positional embedding |
| **Swin Transformer** | Window attention, hierarchical |
| **Longformer/Performer** | Sparse/linear attention cho chuỗi dài |

---

## 6. Training Tips

- [ ] Sử dụng LayerNorm trước attention (Pre-LN) để gradient ổn định.
- [ ] Warmup learning rate vài nghìn steps + AdamW.
- [ ] Gradient checkpointing + mixed precision → tiết kiệm VRAM.
- [ ] Causal mask đúng khi training autoregressive.
- [ ] Với ViT, nên dùng augmentation mạnh (RandAugment, MixUp) và knowledge distillation.

> 📌 Tip: Khi fine-tune LLM nhỏ, dùng LoRA/QLoRA để giảm chi phí.
