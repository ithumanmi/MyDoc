# 🖼️ Multimodal Models (Vision + Language + Audio)

> [← Back to Generative AI](./README.md)

LLM giờ đã "nhìn, nghe, nói". GPT-4V, Gemini, Claude 3, LLaVA cho phép xử lý đồng thời văn bản, hình ảnh, audio và video.

---

## 1. Key Players

| Model | Modalities | Điểm nổi bật |
| --- | --- | --- |
| **GPT-4V / GPT-4o** | Text, Image, Audio | Vision QA, chart reading, real-time voice. |
| **Google Gemini 1.5** | Text, Image, Audio, Video | Context length cực lớn (1M tokens), code + video reasoning. |
| **Claude 3 Opus/Sonnet** | Text, Image | Tốt trong reasoning, comply policy chặt. |
| **LLaVA / MiniGPT-4** | Text + Image (OSS) | Finetune từ LLaMA, open-source, deploy on-prem. |
| **IDEFICS, Kosmos-2** | Multimodal OSS | Pretrained checkpoints public, cần fine-tune. |

---

## 2. Workflow xây assistant đa phương thức

1. **Input acquisition:** camera stream, upload file (PDF, hình, audio).
2. **Pre-processing:** OCR/ASR nếu cần, trích key frames.
3. **Prompt design:** hướng dẫn model cách phân tích từng modality.
4. **Tool integration:** nếu cần output structured (JSON, bounding box), kết hợp model với vision tools (GroundingDINO, Segment Anything).
5. **Feedback loop:** thu nhận user feedback để cải thiện prompt/model.

---

## 3. Architecture Pattern (RAG + Multimodal)

- **Vision RAG:** trích text từ ảnh (OCR) + embed image patch → search knowledge base.
- **Document QA:** convert PDF sang image tiles + text, chunk theo layout.
- **Video QA:** sample frames + audio transcript → feed vào model.

```python
from openai import OpenAI
client = OpenAI()

resp = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "user", "content": [
            {"type": "input_text", "text": "Mô tả biểu đồ này"},
            {"type": "input_image", "image_url": image_url}
        ]}
    ]
)
print(resp.output_text)
```

---

## 4. LLaVA Workflow (OSS)

1. **Base model:** LLaMA 3 hoặc Mistral.
2. **Vision encoder:** CLIP ViT-L/14.
3. **Finetune dataset:** instruction tuning với BLIP/COCO, VizWiz, TextCaps.
4. **Serve:** dùng vLLM hoặc FastChat để deploy.

---

## 5. Use Cases

- **Visual QA:** đọc chart, UI screenshot, invoice.
- **Creative Studio:** upload moodboard → gợi ý prompt cho designer.
- **Customer Support:** khách gửi ảnh lỗi sản phẩm → model hướng dẫn sửa.
- **Accessibility:** mô tả hình ảnh cho người khiếm thị.

> 🎯 Lab: xây chatbot đọc hóa đơn — OCR (PaddleOCR) + GPT-4V extract field + output JSON.
