## ✂️ Text Preprocessing Playbook

> [← Back to NLP](./README.md)

Chuẩn hóa dữ liệu văn bản để pipeline NLP ổn định trước khi vào model truyền thống hay Transformer.

---

## 1. Tokenization Strategies

| Chiến lược | Mô tả | Khi dùng |
| --- | --- | --- |
| **Whitespace/Simple** | Tách bằng dấu cách | Rule-based, log nhanh |
| **Word-level** | Tách từ, xử lý punctuation | Trước Transformer, utilized cho Vietnamese tokenizer |
| **Subword (BPE, WordPiece, SentencePiece)** | Ghép byte để giảm OOV | Hầu hết LLM/NLP hiện đại |
| **Character-level** | Token từng ký tự | Ngôn ngữ nhiều từ mới, lỗi chính tả |

> Tools: `underthesea`, `pyvi`, `SentencePiece`, `tokenizers` (HF).

---

## 2. Normalization

1. **Lowercase / Case folding** (nếu model không case-sensitive).
2. **Unicode normalization (NFC/NFD)** để xử lý dấu tiếng Việt.
3. **Strip punctuation, HTML, emojis** tùy use case.
4. **Noise removal:** URL, mention, số điện thoại → replace token `[URL]`.

```python
import unicodedata, re

def normalize(text):
    text = unicodedata.normalize('NFC', text)
    text = text.lower()
    text = re.sub(r"https?://\S+", "<URL>", text)
    return text
```

---

## 3. Stemming vs Lemmatization

| Kỹ thuật | Đặc điểm | Pros/Cons |
| --- | --- | --- |
| **Stemming** | Cắt hậu tố (Porter, Snowball) | Nhanh nhưng không ngữ nghĩa |
| **Lemmatization** | Dùng từ điển + POS để về dạng gốc | Chính xác hơn, chậm |

> Với tiếng Việt, ưu tiên lemmatization/tokenization chuyên biệt thay vì stem đơn giản.

---

## 4. Stopwords & Filtering

1. Tạo custom stopword list theo domain (logistics, finance).
2. Giữ lại từ quan trọng (negation như "không", "chưa").
3. Lọc ký tự lặp, spam ("aaaa", "!!!!").

---

## 5. Handling Special Text

- **Emojis/emoticons:** map sang sentiment tokens :)
- **Code/Formula:** wrap bằng tag `<code>...</code>`.
- **Mixed languages:** detect language, áp dụng pipeline riêng.

---

## 6. Pipeline Template

```python
def preprocess(text):
    text = normalize(text)
    tokens = tokenizer(text)
    tokens = [lemmatize(tok) for tok in tokens if tok not in stopwords]
    return tokens
```

- [ ] Log distribution độ dài câu để tune max sequence length.
- [ ] Lưu tokenizer + vocab version để reproducible.

> 🎯 Tip: Đối với LLM, chuẩn hóa input (strip spaces, chuẩn hóa dấu) giúp giảm hallucination vì tokenization nhất quán.
