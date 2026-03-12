## 🔧 PEFT & LoRA Fine-tuning Guide (Hands-on)

> [← Back to NLP & LLMs](./transformers-llm.md)

Tập trung vào fine-tuning LLM hiệu quả trên GPU phổ thông: PEFT, LoRA, QLoRA và quy trình deploy.

---

## 1. Khi nào nên dùng PEFT?

| Tình huống | Vì sao chọn PEFT |
| --- | --- |
| Muốn fine-tune Llama-3 hoặc PhoGPT nhưng chỉ có 24GB VRAM | Giảm số tham số train được xuống vài triệu |
| Cần nhiều phiên bản chuyên biệt (legal, finance) | Fine-tune nhanh, lưu LoRA adapter nhỏ (100MB) |
| Triển khai on-premise | Dễ merge/unmerge adapter tùy môi trường |

---

## 2. Các kỹ thuật phổ biến

| Kỹ thuật | Mô tả | Notes |
| --- | --- | --- |
| LoRA | Chèn ma trận low-rank \(W = W_0 + A B^T\) vào layer attention | Rank (r=8/16), α scaling |
| QLoRA | Quantize mô hình gốc xuống 4-bit + LoRA | Tiết kiệm VRAM cực mạnh |
| Prefix/Prompt Tuning | Học thêm vector “prompt” cố định | Tốt cho task có format cố định |
| Adapter | Thêm feed-forward nhỏ sau mỗi block | Dễ triển khai, nhưng nặng hơn LoRA |

---

## 3. Hands-on: LoRA với Hugging Face PEFT

### 3.1 Chuẩn bị môi trường

```bash
pip install transformers datasets peft accelerate bitsandbytes trl
```

### 3.2 Cấu hình LoRA

```python
from peft import LoraConfig

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
```

### 3.3 Training Script (QLoRA ví dụ)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import get_peft_model
from datasets import load_dataset

model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    device_map="auto",
    bnb_4bit_compute_dtype="bfloat16",
)

model = get_peft_model(model, lora_config)
dataset = load_dataset("tatsu-lab/alpaca")

training_args = TrainingArguments(
    output_dir="outputs/lora-llama3",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    fp16=False,
    bf16=True,
    logging_steps=20,
    save_steps=200,
)

trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"].select(range(5000)),
    dataset_text_field="text",
)

trainer.train()
model.save_pretrained("outputs/lora-llama3")
```

### 3.4 Merge adapter (nếu cần export single checkpoint)

```python
from peft import AutoPeftModelForCausalLM

model = AutoPeftModelForCausalLM.from_pretrained("outputs/lora-llama3")
model = model.merge_and_unload()
model.save_pretrained("outputs/merged")
```

---

## 4. Dataset Template (Instruction format)

```json
{
  "instruction": "Viết email xin nghỉ phép",
  "input": "Tôi bị sốt cao",
  "output": "..."
}
```

* Sử dụng `datasets` để tokenize thành chuỗi `[INST] instruction [/INST] output`.
* Tạo script chuẩn hóa (remap fields, remove HTML, limit length).

---

## 5. Evaluation Checklist

| Hạng mục | Cách đo |
| --- | --- |
| Perplexity/LOSS | Evaluate trên validation set |
| Task-specific | BLEU/ROUGE/F1 tùy bài toán |
| Safety | Prompt adversarial, toxicity filters |
| Latency | Benchmark với `text-generation-inference` |

> Tip: Dùng `lm-eval-harness` hoặc `evals` để benchmark chuẩn.

---

## 6. Deployment & Serving

1. **Adapters runtime:**
   * Sử dụng `text-generation-inference` hoặc `llama.cpp` hỗ trợ LoRA trực tiếp.
   * Khi cần scale, load base model 1 lần và hot-swap adapter theo tenant.
2. **Merged checkpoint:** deploy trên vLLM/Inferentia nếu muốn đơn giản.
3. **Edge cases:** kiểm tra memory fragmentation khi chạy 4-bit.

Example FastAPI snippet:

```python
from fastapi import FastAPI
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")
adapter = PeftModel.from_pretrained(base_model, "outputs/lora-llama3")

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt").to(base_model.device)
    outputs = adapter.generate(**inputs, max_new_tokens=256)
    return {"text": tokenizer.decode(outputs[0], skip_special_tokens=True)}
```

---

## 7. Troubleshooting

* Gradient checkpointing để giảm VRAM.
* Nếu bị OOM: giảm rank r, tăng gradient_accumulation.
* Monitor loss spike khi resume training → reset optimizer states.

---

## 8. Benchmark với `lm-eval-harness`

### 8.1 Cài đặt

```bash
pip install lm-eval==0.4.1
```

### 8.2 Cấu hình model loader

- **Nếu dùng adapter runtime:** sử dụng script custom load LoRA rồi truyền vào `lm_eval.models.huggingface`. Ví dụ `eval_lora.py`:

```python
from lm_eval.models.huggingface import HFLM
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

class LoraHFLM(HFLM):
    def __init__(self, base_model, adapter_path, **kwargs):
        tokenizer = AutoTokenizer.from_pretrained(base_model)
        model = AutoModelForCausalLM.from_pretrained(base_model, device_map="auto")
        model = PeftModel.from_pretrained(model, adapter_path)
        super().__init__(pretrained=base_model, tokenizer=tokenizer, model=model, **kwargs)
```

- **Nếu đã merge adapter:** dùng `--model hf-causal-experimental` bình thường:

```bash
lm_eval --model hf-causal-experimental \
    --model_args pretrained=outputs/merged \
    --tasks hellaswag,truthfulqa,winogrande \
    --batch_size 8 \
    --output_path reports/lora_eval.json
```

### 8.3 Gợi ý bộ task

| Vùng bài toán | Task gợi ý |
| --- | --- |
| Reasoning | gsm8k, mathqa |
| Commonsense | hellaswag, winogrande |
| Instruction | truthfulqa, openbookqa |
| Tiếng Việt | vie_capability, vie_viquad (cần custom plugin) |

### 8.4 Đọc kết quả

`reports/lora_eval.json` chứa accuracy/perplexity từng task. Tạo bảng so sánh Base vs LoRA để đo improvement. Ví dụ snippet phân tích:

```python
import json, pandas as pd

with open("reports/lora_eval.json") as f:
    data = json.load(f)

rows = []
for task, metrics in data["results"].items():
    rows.append({
        "task": task,
        "metric": list(metrics.keys())[0],
        "score": list(metrics.values())[0]
    })

df = pd.DataFrame(rows)
print(df)
```

> 📊 Tip: chạy lm-eval trước và sau fine-tuning để chứng minh hiệu quả; log kết quả vào MLflow/W&B kèm hyperparameters LoRA.

---

## 9. Resources

* [PEFT Docs](https://huggingface.co/docs/peft/index)
* [QLoRA Paper](https://arxiv.org/abs/2305.14314)
* [TRL (Transformers Reinforcement Learning)](https://github.com/huggingface/trl)
* [LoRA explained](https://huggingface.co/blog/lora)

> 🛠️ Gợi ý: Tạo folder `generative-ai/fine-tuning/` để lưu notebook, config và checkpoints LoRA. Dùng DVC theo dõi dataset + adapter weights.
