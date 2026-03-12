# 🔊 Audio & Music Generation

> [← Back to Generative AI](./README.md)

Audio Gen bao gồm Text-to-Speech (TTS), voice cloning và music generation. Hệ sinh thái đang chạy đua về natural prosody, multilingual, và control theo sheet/chord.

---

## 1. Use Cases

- **Voiceover tự động:** video explainers, podcast, training.
- **Voice cloning:** tạo bản sao voice talent cho localization.
- **Music Loops:** background music, trailer, TikTok trend.
- **Interactive Agents:** assistants, NPC game, IVR.

---

## 2. Key Tools

| Tool | Type | Điểm mạnh |
| --- | --- | --- |
| **ElevenLabs** | TTS/Cloning | Natural tone, voice design, API dễ tích hợp. |
| **PlayHT v3** | TTS/Realtime | Latency thấp, hỗ trợ streaming. |
| **Suno** | Music | Text → full song (verse + chorus), style đa dạng. |
| **Udio** | Music | Chất lượng vocal tốt, edit lyric từng đoạn. |
| **VALL-E / XTTS** | OSS | Fine-tune voice clone on-premise. |

---

## 3. Workflow

1. **Script/Prompt:** Viết lời thoại/lyric.
2. **Voice Selection:** Chọn voice hoặc ghi 1 phút mẫu (voice clone).
3. **Generate:** call API hoặc chạy pipeline local.
4. **Post-processing:** chỉnh EQ, noise reduction, timing.
5. **Mix & Master:** ghép với video hoặc music bed.

```python
import elevenlabs

client = elevenlabs.ElevenLabs(api_key="...")
audio = client.text_to_speech.generate(
    voice_id="adam",
    text="Xin chào, đây là voiceover AI!",
    model_id="eleven_multilingual_v2"
)
with open("voice.mp3", "wb") as f:
    f.write(audio)
```

---

## 4. Voice Cloning Tips

- Thu mẫu 1-3 phút, chất lượng 16-bit/44kHz, môi trường yên tĩnh.
- Cover data diversity: nhiều emotion, tốc độ, ngữ cảnh.
- Kiểm tra legal consent & usage policy.
- Với OSS (VALL-E, XTTS): cần GPU, dataset tối thiểu vài phút.

---

## 5. Music Generation Playbook

- Prompt template: `genre + tempo + instrumentation + mood + reference artist`.
- Generate nhiều phiên bản → chọn track tốt nhất.
- Dùng stems export (nếu có) để mix thủ công.
- Thêm layer thủ công (guitar, vocal) để tăng bản sắc.

> 🎯 Lab gợi ý: tạo podcast intro 30s (script → voiceover ElevenLabs → background Suno → mix trong Audition).
