## 🔧 LLM Fine-tuning Playbook

> [← Back to NLP](./README.md)

Tổng hợp chiến lược fine-tune mô hình ngôn ngữ lớn: full fine-tune, PEFT (LoRA/QLoRA) và workflow hands-on.

---

## 1. Lựa chọn chiến lược

| Phương pháp | Khi dùng | Yêu cầu |
| --- | --- | --- |
| **Full Fine-tune** | Dataset lớn, cần cập nhật toàn bộ weights | GPU VRAM cao, dài thời gian |
| **Adapter/Prefix Tuning** | Task cụ thể, cần lightweight | Thêm module nhỏ |
| **LoRA** | Hầu hết use case: instruction, domain adaptation | Giảm VRAM, plug-and-play |
| **QLoRA** | Fine-tune 4-bit quantized model | Single GPU 24GB vẫn fine-tune được |

---

## 2. Full Fine-tune Workflow

1. Chuẩn hóa dataset (JSONL, SFT schema).
2. Sử dụng `transformers` + `accelerate`.
3. Mixed precision (bf16/fp16) + gradient accumulation.
4. Evaluate mỗi epoch (eval loss, Rouge/BLEU nếu cần).

```python
from transformers import AutoModelForCausalLM, TrainingArguments, Trainer

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
args = TrainingArguments(
    output_dir="./finetune",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-5,
    num_train_epochs=3,
    bf16=True
)
trainer = Trainer(model=model, args=args, train_dataset=train_ds, eval_dataset=val_ds)
trainer.train()
```

---

## 3. LoRA / QLoRA

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"], lora_dropout=0.05)
model = get_peft_model(model, lora_config)
```

**QLoRA stack:** 4-bit nf4 quantization + LoRA + paged optimizer → tối ưu VRAM.

> Tools: `peft`, `trl` (SFTTrainer), `unsloth`, `axolotl`.

---

## 4. Data & Evaluation

- **SFT:** prompt/response, format consistent.
- **Preference (RLHF/DPO):** pairwise ranking.
- **Eval:** perplexity, rouge, BLEU, custom eval (truthfulQA, MT-bench).

Checklist:

- [ ] Split train/val/test rõ ràng, tránh leakage.
- [ ] Log metrics bằng W&B/MLflow.
- [ ] Kiểm tra hallucination với eval set domain.

---

## 5. Deployment & Handoff

1. Merge LoRA weights (`peft` → `merge_and_unload`).
2. Convert sang GGUF/ONNX/TensorRT nếu cần edge inference.
3. Tạo `model-card.md` ghi rõ data, hyperparams, hạn chế.

> 🎯 Tip: Khi fine-tune trên dữ liệu riêng, luôn kiểm tra license & privacy, đặc biệt với dữ liệu khách hàng.
