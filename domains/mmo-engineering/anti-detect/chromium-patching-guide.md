# 🧩 Chromium Patching Guide (Custom Anti-Detect Build)

## 1. Mục tiêu
- Build Chromium fork với fingerprint spoofing native (Canvas/WebGL/Audio/Sensor) và automation-friendly.

## 2. Prerequisites
- Host Linux (Ubuntu 22.04).
- Depot Tools, 200GB disk, 16GB RAM.

## 3. Setup Steps
```bash
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=$PATH:$PWD/depot_tools
fetch chromium
cd src
git checkout branch-heads/120
gclient sync
```

## 4. Patch Points
- **`content/renderer/`**: inject preload script system.
- **Canvas/WebGL:** `third_party/blink/renderer/modules/canvas/canvas2d_*` và `gpu/command_buffer/service`. Patch `Skia` pipeline để add noise.
- **Navigator overrides:** `content/renderer/renderer_blink_platform_impl.cc`.
- **WebRTC:** disable ICE candidate via `modules/peerconnection`.
- **AudioContext:** modify `third_party/blink/renderer/modules/webaudio`.

## 5. Build Config
`gn args out/Release`:
```
is_component_build = false
is_debug = false
symbol_level = 0
blink_symbol_level = 0
enable_nacl = false
use_thin_lto = true
is_official_build = true
```

## 6. Patching Workflow
1. Apply patch files (`.patch`) giữ riêng trong repo.
2. Run `gn gen out/Release` → `ninja -C out/Release chrome`.
3. Copy binary + `swiftshader` libs vào bundle.
4. Wrap bằng launcher script để pass `--proxy-server`, `--lang` per profile.

## 7. Testing
- Use `chrome://gpu` để xác nhận spoof.
- Run `https://browserleaks.com/webrtc`.
- Automate test suite (Playwright hooking custom engine):
```ts
const browser = await playwright.chromium.connectOverCDP({ endpointURL: "ws://localhost:9222" });
```

## 8. Maintenance
- Rebase mỗi khi Chrome release security fix.
- CI job build container để share artifact.
- Keep patch list minimal để dễ merge.

## 9. Checklist
- [ ] Patch áp dụng sạch trên branch-head.
- [ ] Build artifact signed + checksum.
- [ ] Test suite pass (fingerprint, automation scripts).