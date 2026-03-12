## 🧱 NLP Foundations — Tokenization & Classical Pipeline

> [← Back to NLP Roadmap](./README.md)

Nắm vững pipeline truyền thống trước khi bước vào Transformers.

---

## 1. Workflow 6 bước

1. **Text Acquisition** — thu thập, crawl, OCR.
2. **Cleaning & Normalization** — lowercase, remove HTML, punctuation, unicode normalize.
3. **Tokenization** — word, subword (BPE), sentence.
4. **Linguistic Features** — POS tagging, stemming, lemmatization.
5. **Vectorization** — Bag-of-Words, TF-IDF, word embeddings (Word2Vec/GloVe).
6. **Modeling** — Naive Bayes, SVM, CRF.

---

## 2. Tokenization Techniques

| Technique | Use case | Pros/Cons |
| --- | --- | --- |
| Regex/Simple | Rule-based tasks | Dễ nhưng thiếu context |
| Word-level | Classic models | Vỡ với OOV |
| Subword (BPE) | Pretrain language models | Trade-off vocab size |
| SentencePiece | Multilingual | Learn vocab trực tiếp từ corpus |

Python snippet (spaCy + Hugging Face):

```python
import spacy
from transformers import AutoTokenizer

nlp = spacy.load("en_core_web_sm")
doc = nlp("Vietnam AI ecosystem is booming")
tokens = [token.lemma_.lower() for token in doc]

hf_tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
input_ids = hf_tokenizer("Xin chao Viet Nam", return_tensors="pt")
```

---

## 3. Feature Engineering for Text

*   **Statistical**: n-grams, character grams, TF-IDF.
*   **Syntactic**: POS tags, dependency relations.
*   **Semantic**: Word embeddings, doc2vec, topic distributions (LDA).
*   **Domain-specific**: Sentiment lexicon, custom dictionaries.

Feature unions (scikit-learn):

```python
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer

pipeline = FeatureUnion([
    ("tfidf", TfidfVectorizer(ngram_range=(1,2))),
    ("len", FunctionTransformer(lambda X: [[len(x)] for x in X]))
])
```

---

## 4. Classical Models

| Task | Model | Notes |
| --- | --- | --- |
| Sentiment | Logistic Regression, SVM | Sử dụng TF-IDF, n-gram |
| Topic | LDA, NMF | Cần tune số topic |
| NER/POS | CRF, HMM | Đòi hỏi feature handcrafted |
| Text Classification | Naive Bayes | Nhanh, baseline tốt |

---

## 5. Evaluation & Error Analysis

*   Metrics: precision, recall, F1, confusion matrix.
*   Cross-validation theo nguồn dữ liệu (time-based split cho social).
*   Error bucket: slang, sarcasm, spelling.
*   Tooling: Weights & Biases tables, spaCy displaCy, ConfusionMatrixDisplay.

---

## 6. Resources

*   [Speech & Language Processing (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/)
*   [NLTK Book](https://www.nltk.org/book/)
*   [FastText](https://fasttext.cc/)

> 🧠 Tip: Khi áp dụng LLM, vẫn giữ các bước cleaning/tokenization đúng chuẩn để giảm hallucination và latency.
