# 🎨 Unity Render Pipelines: Built-in vs URP vs HDRP

> [← Back to Game Dev Roadmap](../README.md) | [Graphics Index](./shader-programming.md)
>
> **TL;DR:** Chọn pipeline phù hợp giúp bạn cân bằng giữa hiệu năng và chất lượng hình ảnh, tránh việc “port” dự án khi đã quá muộn.

---

## 1. Tổng quan nhanh

| Pipeline | Đối tượng | Ưu điểm | Hạn chế |
| --- | --- | --- | --- |
| **Built-in (BiRP)** | Project cũ, team nhỏ | Ổn định, asset store hỗ trợ rộng | Khó tùy biến, lighting cũ, thiếu Scriptable Render Features |
| **Universal Render Pipeline (URP)** | Mobile, Switch, game indie đa nền tảng | Hiệu năng tối ưu, hỗ trợ ScriptableRendererFeature, dễ custom | Thiếu một số hiệu ứng cao cấp (Ray Tracing, volumetric lighting) |
| **High Definition Render Pipeline (HDRP)** | PC/Console high-end, visual fidelity cao | Ray Tracing, Volumetric Fog, Physical Light Units, DLSS/FSR | Không hỗ trợ mobile, yêu cầu GPU mạnh, workflow phức tạp |

> Quy tắc vàng: **Mobile/Indie = URP**, **AAA PC/Console = HDRP**, **Legacy/Prototype = Built-in**.

---

## 2. Khi nào chọn URP?

### Use Case
- Game mobile 2D/3D, Nintendo Switch, VR standalone (Quest).
- Studio cần build một lần chạy trên nhiều nền tảng (PC mid-tier, Android, iOS).

### Tính năng nổi bật
- **Forward Renderer + ScriptableRendererFeature:** Chèn pass custom (Outline, Decals, SSAO) mà không phải viết pipeline từ đầu.
- **Shader Graph hỗ trợ URP Lit:** Tạo vật liệu PBR với vài cú kéo thả.
- **2D Renderer:** Pixel Perfect Camera, Light2D, Shadow2D cho game 2D ánh sáng động.
- **Renderer Feature:** Post-processing tích hợp (Bloom, Color Grading, Depth of Field) nhẹ và dễ tinh chỉnh.

### Best Practice URP
1. **Asset Store:** Chỉ dùng assets đã port sang URP. Nếu import asset BiRP, cần dùng `Render Pipeline Converter`.
2. **Light Mode:** Dùng Baked/Realtime mix. Tránh realtime shadow trên mobile > 2 light.
3. **SRP Batcher:** Bật `Project Settings > Graphics > SRP Batcher` để giảm CPU overhead (đặc biệt trên Android low-end).
4. **Render Scale:** Cho phép scale về 0.8 trên mobile để đổi lấy FPS cao.

---

## 3. Khi nào chọn HDRP?

### Use Case
- Game PC/Console đòi hỏi độ trung thực cao, cinematic, mô phỏng ánh sáng vật lý.
- Dự án cần Ray Tracing (mirror, reflection, GI) hoặc Visual Effects phức tạp (Volumetric Fog, Decal Projector chất lượng cao).

### Tính năng nổi bật
- **Physically Based Lighting:** Sử dụng lumen (lm), nits, lux như ngoài đời; giúp team art/lighting dễ làm việc với reference thực.
- **Ray Tracing / Path Tracing:** Reflection chính xác, GI thời gian thực, transparent shadow.
- **Decal Projector + Layered Lit:** Tạo bẩn/bóng cho môi trường AAA.
- **DLSS/FSR/XeSS integration:** Nâng FPS cho PC high-end.

### Best Practice HDRP
1. **Hardware Target:** Tối thiểu RTX 2060 / RX 5700 nếu bật Ray Tracing. Nếu target PC tầm trung, cân nhắc URP.
2. **Lighting workflow:** Sử dụng **Area Light, Spot Light** với Physical Light Units, bật **Volumetric Fog** có chừng mực (tốn performance).
3. **Custom Pass:** HDRP cho phép tạo full-screen/custom pass để làm hiệu ứng outline, stylized – tận dụng tính linh hoạt nhưng quản lý cẩn thận để tránh render pass dư.
4. **HDR Output:** Nếu game hỗ trợ HDR10, HDRP đã tích hợp pipeline sẵn.

---

## 4. Built-in Pipeline – Khi nào nên giữ?
- Dự án cũ đã có hàng trăm shader tùy biến dựa trên Surface Shader / CGPROGRAM.
- Team không đủ thời gian migrate hoặc phụ thuộc asset legacy.
- Prototype nhanh (dự án nhỏ, game jam).

Tuy nhiên, nếu dự án mới, nên chọn URP/HDRP ngay từ đầu để tránh chi phí chuyển đổi.

---

## 5. Quy trình chuyển pipeline
1. **Backup project.**
2. **Install URP/HDRP:** `Window > Package Manager > Unity Registry > Universal RP or High Definition RP`.
3. **Create Pipeline Asset:** `Assets > Create > Rendering > URP/HDRP Pipeline Asset`.
4. **Assign in Graphics Settings:** `Project Settings > Graphics` và `Quality`.
5. **Convert Materials:** Dùng `Render Pipeline Converter` (URP) hoặc `HDRP Wizard` → Convert Folders.
6. **Fix Lighting:** Re-bake lightmaps, kiểm tra reflection probe, post-processing.

> Note: Shader tùy biến phải viết lại (Shader Graph hoặc HLSL). Asset store cũ cần check compatibility.

---

## 6. Performance Checklist
- **Batching:** SRP Batcher (URP/HDRP) giảm CPU so với Built-in batching.
- **Render Features:** Tắt pass không dùng. Mỗi RendererFeature thêm draw call.
- **Shadows:** Giới hạn shadow cascades (URP max 4). Trên mobile, dùng 1 cascade + 1024 resolution.
- **Post-processing:** Bloom/Depth of Field đắt đỏ trên mobile. Trong HDRP, Motion Blur và SSAO nặng – nên expose toggle cho user.
- **Light Layers (HDRP):** Dùng để giới hạn light ảnh hưởng đối tượng cụ thể, giảm overdraw.

---

## 7. Quyết định pipeline theo sản phẩm
| Loại game | Target | Pipeline khuyến nghị |
| --- | --- | --- |
| Casual mobile 2D/3D | Android/iOS low-mid | URP (2D Renderer nếu cần Pixel Perfect) |
| Indie PC, stylized | PC mid-tier + mobile high-end | URP |
| VR PC high-end | PC VR (Index, Rift) | URP hoặc HDRP (nếu chấp nhận chi phí) |
| AAA realistic | PC/Console (RTX/PS5) | HDRP |
| Simulation/ArchViz | PC high-end | HDRP |

---

## 8. Kết hợp với Shader Graph & VFX Graph
- URP + Shader Graph: Tạo shader lightweight, hỗ trợ Lit/Unlit, Sprite Lit, Custom Function.
- HDRP + Shader Graph: Có cả Master Stack HDRP Lit, Eye, Hair. Tích hợp trực tiếp với VFX Graph để tạo hiệu ứng Volumetric, Raymarching.
- Built-in: Dùng Surface Shader hoặc Amplify Shader Editor (3rd party) nếu cần workflow node-based.

---

## 9. Tài nguyên học tập
- **Unity Learn:** “Introduction to URP/HDRP” courses.
- **Docs chính thức:** [URP Manual](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest), [HDRP Manual](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest).
- **YouTube:** Brackeys (URP basics), Unity Official (HDRP lighting), MinionsArt (stylized URP shaders).

---

> 💡 **Pro Tip:** Quyết định pipeline là quyết định kiến trúc. Hãy xác định nền tảng mục tiêu, yêu cầu nghệ thuật và năng lực team ngay từ Sprint 0 để tránh “port hell”.