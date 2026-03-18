# Lab 1: Chạy và Tinh Chỉnh Small Language Models (SLMs) Cục Bộ

> [← Back to Labs AI/ML Focus](./README.md) | [Home](../../../README.md)

Lý thuyết về SLM đã rõ ràng ở bài [Small Language Models](../nlp/small-language-models.md). Trong Lab này, chúng ta sẽ bắt tay vào thực hành:

1.  Dùng Ollama chạy Llama 3 8B trên máy cá nhân (Terminal/API).
2.  Dùng thư viện `unsloth` trên Colab để fine-tune (QLoRA) mô hình Llama 3 nhận diện cảm xúc.

---

## 🛠️ Phần 1: Chạy SLM Cục Bộ với Ollama

Ollama là trợ thủ đắc lực giúp bạn chạy SLM nhẹ nhàng như chạy Docker.

### Bước 1: Cài đặt Ollama
*   Truy cập [ollama.com](https://ollama.com/) và tải file cài đặt tương ứng với HĐH (Windows, Mac, Linux).
*   Cài đặt xong, mở Terminal (cmd/Powershell/BASH).

### Bước 2: Tải và Chạy Llama 3 8B
Chỉ cần gõ 1 dòng lệnh:
```bash
ollama run llama3
```
*   Nó sẽ tải file weights (khoảng 4.7GB cho phiên bản Quantized Q4) về máy. Lần chạy sau sẽ vào thẳng mô hình.
*   Bạn có thể chat trực tiếp với Llama 3 ngay trên Terminal!

### Bước 3: Gọi qua API (Python)
Để tích hợp SLM vừa tải vào ứng dụng, Ollama mở sẵn port `11434`. Cài thư viện `ollama` trên Python:
```bash
pip install ollama
```

Tạo file `app.py`:
```python
import ollama

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Tại sao SLM lại quan trọng đối với Edge AI? Trả lời ngắn gọn bằng tiếng Việt.',
  },
])
print(response['message']['content'])
```
*   Lợi ích là bạn không tốn một đồng cắt mạng nào, dữ liệu không rời khỏi máy tính bạn.

---

## 🚀 Phần 2: Tinh chỉnh (Fine-tune) SLM với `unsloth` (Colab Miễn phí)

Llama 3 mặc định trả lời rất dông dài (General Chat). Ta sẽ "nắn" nó thành một cỗ máy gán nhãn JSON ngắn gọn bằng kỹ thuật QLoRA.
*Thư viện `unsloth` giúp tăng tốc độ train gấp 2 lần và giảm 70% VRAM so với cách cũ của HuggingFace.*

### Bước 1: Setup Môi Trường
1.  Truy cập Google Colab, tạo một Notebook mới.
2.  Vào `Runtime -> Change runtime type`, chọn hardware là **Tesla T4 GPU**.

Cài đặt thư viện:
```python
!pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
!pip install --no-deps xformers "trl<0.9.0" peft accelerate bitsandbytes
```

### Bước 2: Load Model (Bản Quantized 4-bit)
```python
from unsloth import FastLanguageModel
import torch

max_seq_length = 2048 # Độ dài token tối đa
dtype = None
load_in_4bit = True   # Chỉ tốn ~6-7GB VRAM thay vì 16GB

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/llama-3-8b-bnb-4bit",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# Kích hoạt LoRA adapters
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Ma trận nhỏ (Rank 16) - bạn chỉ train <1% tham số
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 3407,
    use_rslora = False,
    loftq_config = None,
)
```

### Bước 3: Chuẩn bị Dataset (Ví dụ: Sentiment format prompt)
Sử dụng bộ dataset nhỏ từ HuggingFace (ví dụ `dair-ai/emotion`). Hàm dưới đây format input.

```python
alpaca_prompt = """Dưới đây là một nhận định. Hãy phân loại cảm xúc thành [Tích cực, Tiêu cực, Trung lập]. Chỉ trả về tên cảm xúc, không giải thích.

### Nhận định:
{}

### Cảm xúc:
{}"""

def formatting_prompts_func(examples):
    inputs       = examples["text"]
    outputs      = examples["label_text"]
    texts = []
    for i, o in zip(inputs, outputs):
        # Nối câu hỏi và đáp án vào chuẩn template
        text = alpaca_prompt.format(i, o) + tokenizer.eos_token
        texts.append(text)
    return { "text" : texts, }

# (Đoạn load dataset từ dataset_dict tùy ý, tham khảo doc của SFTTrainer)
```

### Bước 4: Train (Học Sinh Đi Vào Lớp)
Chúng ta dùng `SFTTrainer` (Supervised Fine-Tuning).
```python
from trl import SFTTrainer
from transformers import TrainingArguments

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset, # Thay bằng biến dataset của bạn
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    dataset_num_proc = 2,
    packing = False, # Tập dữ liệu ngắn nên False
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60, # Train thử nghiệm nhanh, nếu train thật có thể là 1 epoch
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    ),
)

trainer_stats = trainer.train()
```
*Tốc độ train cực nhanh, bạn chỉ mắt tầm 5 phút cho 60 steps.*

### Bước 5: Thử Nghiệm Model Vừa Train & Đóng Gói (GGUF)
Hãy đặt câu hỏi: "Tôi cảm thấy sản phẩm này vô dụng".
Nếu trước khi train model có thể trả lời "Xin lỗi vì bạn có trải nghiệm không tốt, sản phẩm...", thì sau khi train nó CÓ THỂ CHỈ NHẢ RA một chữ: "Tiêu cực". (Đúng cấu trúc ta ép nó học).

```python
# Inference tại chỗ để test
FastLanguageModel.for_inference(model)

inputs = tokenizer(
[
    alpaca_prompt.format(
        "Giao hàng nhanh, đóng gói cẩn thận, sản phẩm đúng mô tả.", 
        "" # Để trống phần output cho model tự điền
    )
], return_tensors = "pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens = 64, use_cache = True)
print(tokenizer.batch_decode(outputs))
```

**Export sang `.gguf` để chép vào USB mang về chạy nội bộ (Ollama) nhé!**
```python
# Tốn khoảng vài chục giây để convert weight về gguf
model.save_pretrained_gguf("model_gguf", tokenizer, quantization_method = "q4_k_m")
```

---
> Chúc mừng! Bạn vừa trải qua "Lễ trưởng thành" của AI Engineer: Từ việc down mô hình mã nguồn mở, cho đến custom hóa logic của nó hoàn toàn thuộc về doanh nghiệp/ứng dụng cá nhân của mình.
