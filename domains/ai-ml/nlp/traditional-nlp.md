## 📘 Traditional NLP Playbook

> [← Back to NLP](./README.md)

Khung kiến thức tiền-Transformer: từ POS tagging, NER đến sentiment analysis với mô hình thống kê/ML cổ điển.

---

## 1. Pipeline cổ điển

1. **Preprocessing:** tokenization, stopwords, stemming/lemmatization.
2. **Feature engineering:** Bag-of-Words, TF-IDF, n-gram, char n-gram.
3. **Model:** Logistic Regression, SVM, CRF, HMM, Naive Bayes.
4. **Evaluation:** Precision/Recall/F1, confusion matrix.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(texts)
clf = LogisticRegression(max_iter=200)
clf.fit(X, labels)
```

---

## 2. POS Tagging

| Approach | Mô tả |
| --- | --- |
| **Rule-based** | Dùng luật ngữ pháp, ít linh hoạt |
| **HMM/CRF** | Sequence labeling dựa trên xác suất | 
| **BiLSTM + CRF** | Neural trước Transformer |

**Tools:** `NLTK`, `spaCy`, `VnCoreNLP`.

---

## 3. Named Entity Recognition (NER)

* **Feature-based:** CRF với từ + POS + gazetteer.
* **Neural BiLSTM-CRF:** embedding + char-level CNN.
* **Metrics:** F1 per entity.

> Datasets: CoNLL-2003, VLSP (tiếng Việt).

---

## 4. Sentiment Analysis

1. **Rule-based:** VADER, lexicon.
2. **ML:** Logistic/SVM với TF-IDF.
3. **Deep learning:** CNN/LSTM trước khi có Transformer.

**Tip:** xử lý negation và sarcasm, cân nhắc multi-class (positive/neutral/negative).

---

## 5. Topic Modeling

* **LDA:** generative model, cần chọn số topic.
* **NMF:** matrix factorization, interpretability tốt.
* **Evaluation:** coherence score, manual inspection.

---

## 6. Deployment considerations

- [ ] Lưu vectorizer + model bằng pickle/joblib.
- [ ] Theo dõi drift: vocab thay đổi, slang mới.
- [ ] Kết hợp rule + ML để xử lý edge cases.

> 🎯 Tip: Các mô hình cổ điển vẫn hữu ích cho pipeline lightweight, explainable hoặc làm baseline nhanh trước khi chuyển sang Transformer.
