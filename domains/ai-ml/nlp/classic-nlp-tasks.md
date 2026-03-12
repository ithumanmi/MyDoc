## 🧰 Classic NLP Tasks — NER, Sentiment, Topic Modeling

> [← Back to NLP Roadmap](./README.md)

Ba nhóm bài toán cốt lõi trước kỷ nguyên LLM.

---

## 1. Named Entity Recognition (NER)

### Pipeline
1. Tokenize + POS tag.
2. Feature extraction (word shape, suffix, gazetteer).
3. Sequence labeling model (CRF, BiLSTM-CRF).

### Feature template (CRF)
```
U00:%x[0,0]
U01:%x[0,0]/%x[-1,0]
U02=is_capitalized
U03=word_shape
```

### Tools & Libraries
* spaCy custom NER
* Flair (BiLSTM-CRF)
* Stanford NER

---

## 2. Sentiment Analysis

| Approach | Description | When to use |
| --- | --- | --- |
| Lexicon-based | VADER, SentiWordNet | Social media, không nhiều data |
| ML-based | Logistic Regression, SVM | Khi có dataset đã gán nhãn |
| Hybrid | Rule + ML | Đa ngôn ngữ, domain-specific |

Example (scikit-learn):

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

sentiment_clf = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
    ("clf", LogisticRegression(max_iter=200))
])
sentiment_clf.fit(texts, labels)
```

Tips:
* Balance class bằng class_weight hoặc resampling.
* Thêm feature domain (emoji, punctuation).
* Evaluate theo customer segment.

---

## 3. Topic Modeling

### LDA Flow
1. Preprocess (stopwords, lemmatize).
2. Vectorize (bag-of-words).
3. Fit LDA, tune num_topics.
4. Interpret topics, label.

```python
from gensim import corpora, models

dictionary = corpora.Dictionary(tokenized_docs)
corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]
lda = models.LdaModel(corpus, id2word=dictionary, num_topics=10, passes=20)
```

### Alternatives
* NMF + TF-IDF.
* BERTopic (embedding + clustering).
* Guided LDA (seed words).

---

## 4. Evaluation

| Task | Metrics |
| --- | --- |
| NER | Precision/Recall/F1 per entity, entity-level confusion |
| Sentiment | Accuracy, macro F1, ROC-AUC |
| Topic | Coherence (c_v), PMI, human evaluation |

Error analysis checklist:
* Mis-tokenization → update tokenizer.
* Domain shift → collect new lexicon.
* Class imbalance → adjust thresholds.

---

## 5. Deployment & Maintenance

* Package models bằng spaCy pipeline hoặc ONNX.
* Theo dõi drift bằng keyword distribution, sentiment trend.
* Retrain schedule dựa trên data drift metric (PSI).

> 🧭 Tip: Dù dùng LLM, vẫn giữ baseline classic models làm fallback khi thiếu GPU hoặc yêu cầu latency thấp.
