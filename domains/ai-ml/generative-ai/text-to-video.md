# 🎬 Text-to-Video Frontier

> [← Back to Generative AI](./README.md)

Text-to-video đang bước vào giai đoạn "cú nhảy" với Sora, Runway Gen-2, Pika 1.0. Khả năng dựng cảnh dài, camera chuyển động phức tạp và vật lý thuyết phục dần trở thành chuẩn mới.

---

## 1. Landscape & Key Players

| Vendor | Điểm nổi bật | Dùng khi nào |
| --- | --- | --- |
| **Sora (OpenAI)** | Video 1 phút, shot phức tạp, consistency cao. | Quảng cáo, cinematic storytelling (hiện chỉ beta). |
| **Runway Gen-2** | Text/image → video, có motion brush, control frames. | Studio nhỏ, cần UI thân thiện, kết hợp video editing. |
| **Pika 1.0** | Nổi bật về anime/cartoon, hỗ trợ mobile app. | Creator cá nhân, social content nhanh. |
| **Stable Video Diffusion** | OSS từ Stability, 25 fps, extend frame. | Muốn self-host, kết hợp pipeline tùy chỉnh. |

---

## 2. Workflow Text-to-Video

1. **Ideation:** storyboard + prompt mô tả shot, camera, mood.
2. **Prompt Template:**
   ```
   [Subject] [Action], camera [movement], in [style], lighting [type], shot [framing], mood [tone]
   ```
3. **Control:** upload image/frame reference, depth/pose map để cố định nhân vật.
4. **Edit & Upscale:** dùng Runway/Pika editor hoặc After Effects để polish.
5. **Sound:** ghép audio từ ElevenLabs, Suno hoặc stock library.

---

## 3. Best Practices

- **Prompt + Seed library** để tái sử dụng phong cách.
- Viết prompt chú trọng camera motion: "dolly zoom", "steady cam fly-through".
- Dùng ControlNet / AnimateDiff để giữ nhất quán nhân vật.
- Render nhiều clip ngắn (5-10s) rồi ghép lại để kiểm soát chất lượng.
- Track licensing & output policy (OpenAI policy, Runway commercial terms).

---

## 4. Stack tự host (OSS)

- **Stable Video Diffusion** + AnimateDiff cho chuyển động.
- **Kohya/ComfyUI** để điều phối pipeline.
- **LoRA/ControlNet** custom phong cách nhân vật.
- **FFmpeg** + **DaVinci Resolve** để hậu kỳ.

> 🎯 Gợi ý dự án: dựng đoạn TVC 15s giới thiệu sản phẩm (storyboard 3 cảnh → gen video → voiceover → caption).
