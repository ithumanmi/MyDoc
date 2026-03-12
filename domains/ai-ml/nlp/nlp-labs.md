## 🧪 NLP Labs — Classical Tasks

> [← Back to NLP Roadmap](./README.md)

Các bài lab giúp luyện pipeline truyền thống trước khi fine-tune LLM.

---

## Lab 1 — Tokenization & Preprocessing Toolkit

| Item | Nội dung |
| --- | --- |
| Dataset | [Vietnamese News Titles](https://www.kaggle.com/datasets/duongnguyen269/vietnamese-news-classification) |
| Goal | Xây dựng module `text_cleaner.py` hỗ trợ normalization đa ngữ |
| Steps | 1) Benchmark regex vs spaCy vs underthesea 2) Unit test edge cases (emoji, acronym) 3) Export pip package |
| Deliverables | CLI `python tools/clean_text.py --input news.csv --lang vi` |

Checklist:
- [ ] Viết docstring mô tả các rule clean
- [ ] Benchmark tốc độ (docs/sec)
- [ ] Publish ghép với Hugging Face tokenizer

---

## Lab 2 — NER with CRF

| Item | Nội dung |
| --- | --- |
| Dataset | [VLSP 2018 NER](https://vlsp.org.vn/) |
| Goal | Train CRF & BiLSTM-CRF, so sánh F1 |
| Steps | 1) Feature template `.template` 2) Train CRF++ 3) Train Flair BiLSTM-CRF 4) Error analysis |
| Deliverables | Notebook + model checkpoint + report F1 per entity |

Checklist:
- [ ] Gazetteer cho địa danh Việt Nam
- [ ] Visualization bằng spaCy displaCy
- [ ] Script convert dữ liệu sang CoNLL format

---

## Lab 3 — Sentiment Classification (LogReg vs BERT)

| Item | Nội dung |
| --- | --- |
| Dataset | [UIT-VSFC](https://www.kaggle.com/datasets/uitnlp/vietnamese-sentiment) |
| Goal | So sánh pipeline TF-IDF + Logistic Regression vs PhoBERT fine-tuning |
| Steps | 1) Feature extraction 2) Train logistic regression 3) Fine-tune PhoBERT 4) Viết bảng trade-off latency/accuracy |
| Deliverables | Markdown report + inference script `predict.py`

Checklist:
- [ ] Dùng SHAP để giải thích model cổ điển
- [ ] Stress test trên emoji/slang
- [ ] Đóng gói logistic model bằng ONNX

---

## Lab 4 — Topic Modeling Dashboard

| Item | Nội dung |
| --- | --- |
| Dataset | Reddit/Forum dump (Elasticsearch export) |
| Goal | Triển khai LDA + BERTopic, visualize trong Streamlit |
| Steps | 1) Preprocess + bigram 2) Train LDA và BERTopic 3) Build Streamlit dashboard hiển thị top words, document search |
| Deliverables | `app.py`, Dockerfile, hướng dẫn deploy |

Checklist:
- [ ] Metric coherence (c_v) log vào MLflow
- [ ] Cho phép user feedback topic label
- [ ] Schedule cập nhật bằng Airflow DAG

> 📌 Tip: Kết hợp Labs này với [CV Repo Template](../computer-vision/cv-repo-template.md) style để chuẩn hóa cấu trúc dự án NLP.
