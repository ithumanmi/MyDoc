## 💬 Project: Sentiment Analysis with Deployment

> [← Back to Labs](./README.md)

Pipeline NLP end-to-end: data → model → API.

---

## 1. Use Case & Dataset

- Chọn domain: review sản phẩm, phản hồi khách hàng, social listening.
- Thu thập dữ liệu: Kaggle, Twitter API, customer feedback.
- Tiền xử lý: deduplicate, language detection, anonymize.

Checklist data:

- [ ] Train/val/test split stratified theo sentiment
- [ ] Clean pipeline (emoji, URL, HTML)
- [ ] Label schema rõ (positive/negative/neutral)

---

## 2. Modeling Strategy

- Baseline: TF-IDF + Logistic Regression/SVM.
- Advanced: fine-tune BERT/RoBERTa/PhoBERT.
- Dùng `transformers` + `datasets` cho pipeline.

Training snippet:

```python
trainer = Trainer(
    model=model,
    args=TrainingArguments(output_dir="outputs", evaluation_strategy="epoch", fp16=True),
    train_dataset=train_ds,
    eval_dataset=val_ds,
    compute_metrics=compute_metrics,
)
trainer.train()
```

Metrics: accuracy, macro F1, confusion matrix.

---

## 3. Deployment

- Export model + tokenizer.
- FastAPI server (`app.py`) endpoint `/predict`.
- Docker image, deploy Cloud Run/Render/Vercel serverless.

Infra checklist:

- [ ] Health check endpoint
- [ ] Logging (request ID, latency)
- [ ] Rate limiting / auth token

---

## 4. Monitoring & Feedback Loop

- Log prediction + confidence → dashboard (Grafana/Metabase).
- Thu thập feedback người dùng, gắn nhãn lại các câu edge-case.
- Batch re-training (ví dụ mỗi tháng) với data mới.

---

## 5. Deliverables

- Repo với `notebooks/`, `src/`, `deploy/`, `infra/`
- README + demo video (API hoặc chatbot UI)
- Postmortem/retrospective ghi lại bài học (latency, data drift)

> 🎯 Bonus: tích hợp webhook với Slack/Teams để thông báo sentiment mới.
