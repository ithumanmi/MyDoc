## 🔊 Speech Processing — ASR & TTS Essentials

> [← Back to NLP Roadmap](./README.md)

Nắm workflow xây dựng hệ thống nhận dạng tiếng nói (ASR) và tổng hợp tiếng nói (TTS).

---

## 1. Pipeline Tổng Quan

```
Audio Input -> Preprocessing -> Feature Extraction -> Model -> Post-processing -> Application
```

*   **Preprocessing:** resample (16k), VAD, normalization.
*   **Feature Extraction:** MFCC, log-mel spectrogram.
*   **Model:** CTC, seq2seq, Transformer/Conformer.
*   **Post-processing:** language model rescoring, punctuation, diarization.

---

## 2. Automatic Speech Recognition (ASR)

### Architectures
| Model | Đặc điểm | Framework |
| --- | --- | --- |
| CTC (DeepSpeech) | Simpler alignment | Mozilla DeepSpeech |
| Seq2Seq (Listen, Attend and Spell) | Attention-based | ESPnet |
| Transformer/Conformer | SOTA accuracy | Wav2Vec 2.0, Whisper |

### Workflow
1. Chuẩn hóa dataset (Common Voice, FPT Open Speech).
2. Feature extraction (torchaudio, librosa).
3. Fine-tune pre-trained (Wav2Vec2, Whisper) hoặc train scratch.
4. Punctuation + normalization.
5. Deploy via REST/gRPC.

Example fine-tune Wav2Vec2 (Hugging Face):

```python
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-xlsr-53")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-xlsr-53", ctc_loss_reduction="mean")
```

---

## 3. Text-to-Speech (TTS)

### Components
1. **Acoustic model:** Tacotron 2, FastSpeech.
2. **Vocoder:** WaveGlow, HiFi-GAN.
3. **Prosody control:** Duration, pitch, energy.

### Deployment
* Precompute mel-spectrogram → run vocoder.
* Optimize: quantize vocoder, use TensorRT.

---

## 4. Tools & Frameworks

*   **SpeechBrain** — end-to-end ASR/TTS toolkit.
*   **ESPnet** — ASR, TTS, Speech Translation.
*   **Coqui TTS** — OSS TTS, multi-speaker cloning.
*   **NVIDIA NeMo** — large-scale speech training.

---

## 5. Evaluation & Monitoring

| Task | Metric |
| --- | --- |
| ASR | WER (Word Error Rate), CER |
| TTS | MOS (Mean Opinion Score), STOI |
| VAD | Precision/Recall |

Tips:
* Sử dụng domain-specific lexicon để giảm WER.
* Monitor latency (audio chunking) và memory footprint.
* Tạo feedback loop: lưu audio mẫu khó để retrain.

> 🎙️ Tip: Trong sản phẩm đa ngữ, dùng config YAML để map language → model → tokenizer → phoneme set.
