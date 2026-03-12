# 🕵️ Browser Fingerprinting & Anti-Detect

> [← Back to Network Security](../README.md)

Trong thế giới MMO (Make Money Online), kẻ thù lớn nhất không phải là Hacker, mà là **AI của Google/Facebook/Amazon**. Nó biết bạn là ai, kể cả khi bạn đổi IP.

---

## 1. Browser Fingerprinting là gì?

Web server thu thập hàng trăm thông số nhỏ từ trình duyệt của bạn. Khi gộp lại, chúng tạo thành một "Dấu vân tay" (Fingerprint) duy nhất.
**Độ chính xác:** 99.5%.

### **Các thông số bị thu thập:**
1.  **Canvas Fingerprint:** Vẽ một hình ẩn. Mỗi Card màn hình (GPU) + Driver sẽ vẽ ra pixel hơi khác nhau một chút -> Lộ diện thiết bị.
2.  **AudioContext:** Cách card âm thanh xử lý tín hiệu.
3.  **WebGL:** Thông số chi tiết về GPU (Vendor, Renderer).
4.  **Fonts:** Danh sách font chữ đã cài trên máy (Máy Design nhiều font lạ -> Dễ bị phát hiện).
5.  **Screen Resolution:** Độ phân giải màn hình + Kích thước cửa sổ trình duyệt.
6.  **WebRTC:** Có thể làm lộ IP thật dù đang dùng VPN.

---

## 2. Anti-Detect Browser (Trình duyệt ẩn danh)

Trình duyệt thường (Chrome/Firefox) không cho phép đổi các thông số phần cứng này. Bạn cần trình duyệt chuyên dụng.

### **Cơ chế hoạt động:**
*   Tạo ra các **Profile** ảo độc lập.
*   Mỗi Profile giả lập một thiết bị khác nhau (Fake User-Agent, Fake Canvas, Fake WebGL...).
*   Cách ly Cookie/Cache hoàn toàn.

### **Các công cụ phổ biến (MMO Tools):**
1.  **Gologin / Multilogin / AdsPower:** (Trả phí). Mạnh, database vân tay chuẩn, ít bị phát hiện. Dùng để nuôi tài khoản Facebook Ads, Ebay, Amazon.
2.  **GenLogin:** (Việt Nam). Có tích hợp Automation (kéo thả).
3.  **HydraHeaders:** (Free/Open Source). Cơ bản, dùng để test.

---

## 3. Chiến lược "Nuôi" (Farming Strategy)

### **A. Consistency (Sự nhất quán)**
*   Đừng bao giờ đổi Fingerprint giữa chừng.
*   Profile A phải luôn dùng đúng bộ thông số A và Proxy A.
*   Nếu hôm nay bạn dùng iPhone 14 ở Mỹ, mai bạn dùng Samsung S23 ở Việt Nam -> **Checkpoint ngay lập tức.**

### **B. Cookies Aging (Làm già tài khoản)**
*   Tài khoản mới tạo (Fresh) rất yếu.
*   Phải cho đi "tương tác dạo" (lướt web, xem youtube, scroll facebook) trong 1-2 tuần để tạo lịch sử (Cookies History) trước khi làm việc chính (Reg acc, Chạy quảng cáo).

### **C. Tránh "WebRTC Leak"**
*   Luôn tắt WebRTC hoặc dùng extension chặn WebRTC để không bị lộ IP thật khi dùng VPN/Proxy.

---

## 4. Tự xây fingerprint (DIY Anti-detect)

Khi không muốn phụ thuộc tool thương mại, bạn có thể tự patch Chromium/Playwright với fingerprint riêng.

### 4.1 Navigator override
```javascript
// preload.js - inject vào mỗi tab
Object.defineProperty(navigator, "platform", { get: () => "Win32" });
Object.defineProperty(navigator, "hardwareConcurrency", { get: () => 8 });
Object.defineProperty(navigator, "languages", { get: () => ["en-US", "vi-VN"] });
navigator.permissions.query = (orig => (params) => {
  if (params.name === "notifications") {
    return Promise.resolve({ state: "denied" });
  }
  return orig(params);
})(navigator.permissions.query);
```

### 4.2 Canvas/WebGL spoof
```javascript
const toDataURL = HTMLCanvasElement.prototype.toDataURL;
HTMLCanvasElement.prototype.toDataURL = function() {
  const ctx = this.getContext("2d");
  ctx.globalAlpha = 0.99; // thêm noise nhỏ
  return toDataURL.apply(this, arguments);
};

const getParameter = WebGLRenderingContext.prototype.getParameter;
WebGLRenderingContext.prototype.getParameter = function(parameter) {
  if (parameter === this.RENDERER) {
    return "ANGLE (NVIDIA GeForce GTX 1660)";
  }
  if (parameter === this.VENDOR) {
    return "Google Inc.";
  }
  return getParameter.apply(this, arguments);
};
```

### 4.3 Playwright config mẫu
```ts
import { chromium } from "playwright";

const context = await chromium.launchPersistentContext("./profiles/userA", {
  headless: false,
  viewport: { width: 1280, height: 720 },
  userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
  proxy: { server: "http://res-proxy:8000" },
  args: [
    "--disable-web-security",
    "--disable-webrtc",
    "--use-angle=gl",
    "--lang=en-US"
  ],
  bypassCSP: true,
});

await context.addInitScript({ path: "preload.js" });
const page = await context.newPage();
```

### 4.4 Fingerprint dataset
- Tạo file JSON mô tả fingerprint (GPU, font list, screen size). Script đọc profile → inject vào init script.
- Random hóa theo phân phối thực tế (thu thập từ [fingerprintjs.com](https://fingerprintjs.com/), [amiunique.org](https://amiunique.org/)).
- Tham khảo [anti-detect/fingerprint-database.md](./anti-detect/fingerprint-database.md) để quản lý data chuẩn hóa.

### 4.5 Testing
- Sử dụng trang `https://audiofingerprint.openwpm.com/`, `https://browserleaks.com/` để đo uniqueness.
- Log kết quả từng profile để tránh fingerprint trùng nhau.

### 4.6 Deep Dive Resources
- [fingerprint-components.md](./anti-detect/fingerprint-components.md)
- [noise-injection-techniques.md](./anti-detect/noise-injection-techniques.md)
- [chromium-patching-guide.md](./anti-detect/chromium-patching-guide.md)
- [detection-bypass-research.md](./anti-detect/detection-bypass-research.md)

---

## 5. Checklist
- [ ] Mỗi profile gắn cố định proxy + fingerprint.
- [ ] Có script kiểm tra WebRTC leak.
- [ ] Kiểm tra uniqueness score trước khi dùng cho tài khoản thật.
- 🔗 **Cross-domain:** Đối chiếu với [Anonymity & OpSec](../network-security/anonymity-opsec.md) để xây mô hình compartmentalization + metadata hygiene song song với fingerprint randomization.
