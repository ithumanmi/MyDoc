---
title: LLM Fine-tuning Playbook
description: Lựa chọn kỹ thuật, dữ liệu, và quy trình đánh giá cho fine-tuning LLM.
---

# 🧠 LLM Fine-tuning

## Khi nào fine-tune
- Cần kiến thức domain-specific hoặc phong cách phản hồi nhất quán.  
- RAG chưa đủ vì cần reasoning chuỗi dài hoặc tuân thủ quy tắc chặt.  
- Muốn nén prompt (instruction) và giảm chi phí token.

## Các kỹ thuật
- **Full fine-tune:** nhiều tham số, tốn compute; cần cẩn trọng catastrohpic forgetting.  
- **PEFT:** LoRA, QLoRA, Prefix/Prompt Tuning, AdaLoRA — tiết kiệm VRAM, phù hợp mô hình lớn.  
- **Adapters:** thêm module nhỏ vào từng layer; cân bằng giữa hiệu năng và compute.  
- **DPO/IPO/KTO:** alignment qua preference data thay vì chỉ SFT.  
- **RLHF/RLAIF:** cho phép tối ưu preference phức tạp, nhưng tốn kém.

## Quy trình chuẩn (SFT + Eval)
1) **Xác định mục tiêu & policy:** style, domain, guardrails.  
2) **Dữ liệu:** deduplicate, lọc độc hại, chuẩn hóa format (instruction/input/output).  
3) **Split:** train/val; tránh leak giữa phiên bản dữ liệu.  
4) **Huấn luyện:** chọn PEFT (LoRA/QLoRA) nếu VRAM hạn chế; chọn seq length phù hợp.  
5) **Đánh giá:**
   - **Tự động:** Rouge/BLEU (nếu tóm tắt/dịch), exact match, pass@k, gsm8k/mmlu subset.  
   - **LLM-as-a-judge** có kiểm soát prompt, hoặc **rule-based** cho format/guardrails.  
6) **Safety/guardrail:** kiểm tra jailbreak, prompt injection; red-team một số mẫu.  
7) **Quantize & deploy:** Q4/Q8; kiểm tra độ lệch chất lượng sau quant.  
8) **Monitoring:** drift, toxicity, refusal rate; vòng phản hồi dữ liệu.

## Cấu hình tham khảo (QLoRA, HuggingFace TRL)
```python
peft_config = LoraConfig(
    r=64, lora_alpha=128, target_modules=["q_proj","k_proj","v_proj","o_proj"],
    lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
)

trainer = SFTTrainer(
    model=model,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    peft_config=peft_config,
    max_seq_length=2048,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,
    logging_steps=50,
    eval_steps=500,
    save_steps=500,
    bf16=True,
)
```

## Dữ liệu & kiểm soát chất lượng
- Loại bỏ prompt rời rạc, câu trả lời không liên quan.  
- Dùng **rubric chấm điểm** (fluency, relevance, safety) để lọc.  
- Tận dụng synthetic data nhưng phải de-dup và đa dạng hóa cấu trúc.

## Pitfalls
- **Catastrophic forgetting:** thêm mix dữ liệu gốc (regularization) hoặc dùng adapters để hạn chế drift.  
- **Overfit guardrails:** mô hình có thể quá từ chối (over-refusal); cần cân bằng.  
- **Leakage license:** chắc chắn dữ liệu tuân thủ giấy phép, tránh PII.

## Liên quan
- [LLM Inference Optimization](./llm-inference-optimization.md)
- [Transformers & LLM](./transformers-llm.md)
- [PEFT & LoRA Guide](./peft-lora-guide.md)