# 🔊 Audio Captcha Bypass

## 1. Flow Overview
- Nhiều captcha (Google v2, hCaptcha) có tùy chọn audio → đọc số hoặc chữ.
- Bot có thể chọn audio challenge, tải file `.mp3`/`.wav`, convert sang text.

## 2. Pipeline
1. Trigger audio mode bằng DOM automation (click icon headphone).
2. Download audio link (thường là POST token → trả về URL tạm thời).
3. Chạy speech-to-text (STT) model.
4. Submit answer qua input → verify.

## 3. STT Options
- **Cloud API:** Google Speech, Azure, AWS Transcribe (chính xác cao nhưng tốn phí & traceable).
- **Open-source:** Vosk, Coqui STT, Whisper (OpenAI) tự host.
- **Custom training:** fine-tune mô hình nhỏ (QuartzNet) với audio captcha dataset.

## 4. Pre-processing
- Convert mp3 → wav 16kHz mono.
- Noise reduction (spectral gating) để loại bỏ static.
- Speed normalization (audio captcha đôi khi tăng/giảm tốc độ).

## 5. Error Handling
- Nếu confidence < threshold → request audio mới.
- Rate limit: platform giới hạn số lần audio, random delay.
- Detect background voice decoy (cloudflare đôi khi mix nhiều tiếng) → segmentation.

## 6. Ops Tips
- Cache audio+transcript để huấn luyện lại.
- Monitor success rate theo proxy/profile.
- Kết hợp manual fallback khi gặp accent khó.

## 7. Checklist
- [ ] STT engine đã benchmark với dataset captcha.
- [ ] Pipeline retry tối đa 3 lần trước khi escalate.
- [ ] Audio download channel dùng HTTPS + token bảo mật.