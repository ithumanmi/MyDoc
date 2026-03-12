# 🔬 Fingerprint Components Deep Dive

## 1. Canvas Fingerprint
- **Mechanism:** web app vẽ hình 2D/3D → đọc pixel data (`toDataURL`).
- **Entropy Sources:** GPU vendor, driver version, font rendering.
- **Attack Surface:** subtle difference (sub-pixel) giúp platform match device.
- **Defense:**
  - *Deterministic spoof:* thay toàn bộ pixel bằng pattern chuẩn → giống thiết bị thật.
  - *Noise injection:* thêm jitter nhỏ (±1% gamma) nhưng phải consistent trên profile.
  - Hook API: override `HTMLCanvasElement.toDataURL`, `getImageData`.

## 2. WebGL
- Provides `RENDERER`, `VENDOR`, supported extensions.
- **Detection:** Cloudflare/Akamai lấy cả `UNMASKED_RENDERER_WEBGL`.
- **Defense:**
  - Patch ANGLE (Chromium) để trả về string mong muốn.
  - Hook `WEBGL_debug_renderer_info` extension.
  - Align extension list với GPU thật (ví dụ GTX 1650 có `OES_element_index_uint`).

## 3. AudioContext
- Fingerprint qua `DynamicsCompressorNode`, `AnalyserNode` output.
- **Entropic factors:** CPU, audio driver, OS latency.
- **Defense:**
  - Add noise vào buffer trước khi read.
  - Precompute signature dựa trên “real device” database → playback.

## 4. Fonts & Font Enumeration
- `document.fonts`, canvas text measurement.
- **Technique:** load hidden iframe, detect fallback width.
- **Defense:**
  - Ship curated font pack (tương ứng user persona).
  - Disable access bằng CSP khó (vì nhiều site cần fonts) → thay bằng virtualization (Fake font list).

## 5. Screen/Window Metrics
- `window.screen`, `devicePixelRatio`, `innerWidth/Height`.
- **Detection:** mismatch giữa viewport, available width, taskbar height.
- **Defense:** set viewport consistent (e.g., 1920x1080, DPR 1.25) và sync DWM values trong Chromium.

## 6. WebRTC & IP Leak
- `RTCPeerConnection` gather candidates.
- **Defense:**
  - `--disable-webrtc` hoặc set `iceServers: []`.
  - Override `createDataChannel` để block candidate.
  - For anti-detect browsers → expose virtual network stack.

## 7. Sensor APIs
- Gyroscope, device motion (mobile farm).
- **Defense:** emulate realistic noise pattern (Perlin noise) thay vì constant value.

## 8. Checklist
- [ ] Profile gắn fingerprint dataset theo persona (desktop vs mobile).
- [ ] Canvas/WebGL hook đã test uniqueness.
- [ ] Font pack đồng nhất với locale.
- [ ] WebRTC leak test pass.