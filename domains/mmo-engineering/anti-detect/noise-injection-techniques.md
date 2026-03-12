# 🌫️ Noise Injection Techniques

> Cách thêm nhiễu có kiểm soát vào fingerprint để uniqueness cao nhưng vẫn giống thiết bị thật.

## 1. Canvas Noise
- **Technique:** thêm offset nhỏ vào pixel khi đọc.
```js
const orig = HTMLCanvasElement.prototype.toDataURL;
HTMLCanvasElement.prototype.toDataURL = function() {
  const ctx = this.getContext("2d");
  const { width, height } = this;
  const imgData = ctx.getImageData(0, 0, width, height);
  const data = imgData.data;
  for (let i = 0; i < data.length; i += 4) {
    data[i] = (data[i] + 1) % 256; // R channel offset 1
  }
  ctx.putImageData(imgData, 0, 0);
  return orig.apply(this, arguments);
};
```
- **Control:**
  - Seed noise theo profile ID để deterministic.
  - Giới hạn ±1 để tránh artifact.

## 2. WebGL Randomization
- Override `vertexAttribPointer`, `getParameter`.
- Add jitter vào `ANGLE_instanced_arrays.drawArraysInstancedANGLE`.
- Use PRNG (e.g., xorshift) seeded by profile.

## 3. Audio Fingerprint Noise
- Hook `OfflineAudioContext.prototype.startRendering`.
- Add white noise amplitude 0.0001 trước khi resolve buffer.

## 4. Timing & Performance API
- `performance.now()` có thể leak CPU speed.
- Scale timestamp: `performance.now = () => orig() * 1.002 + bias;`
- Keep monotonic để không phá logic app.

## 5. Device Sensors
- Gyro noise: `value + perlinNoise(time)`.
- Touch events: randomize `radiusX`, `radiusY` trong khoảng 0.1-0.3.

## 6. Threats
- **Over-noise:** làm fingerprint quá khác lạ → bị flag.
- **Inconsistency:** noise thay đổi mỗi lần → fingerprint unstable.

## 7. Checklist
- [ ] Seed noise per profile.
- [ ] Noise amplitude matching real hardware variance.
- [ ] Unit test noise hooks vs site detection (Cloudflare Radar, BotD).