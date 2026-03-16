# 📊 Unity Impact Metrics Playbook

> [← Back to Game Dev Roadmap](../README.md) | [Home](../../../README.md)
>
> **Difficulty:** 🟡 Intermediate (Performance) → 🔴 Advanced (Live Ops)
>
> **Prerequisites:** Hiểu Unity Profiler, Build Pipeline, có dự án Unity đã ship
>
> **Time to Master:** 4-6 tuần nghiên cứu + 1-2 sprint tối ưu thực tế

---

## 1. Vì sao cần Impact Metrics cho Unity?

Unity game không chỉ cần “fun” mà còn phải **ổn định** và **tối ưu** để giữ chân người chơi. Impact metrics giúp team trả lời:

| Câu hỏi | Metric chính | Ý nghĩa kinh doanh |
| --- | --- | --- |
| Game có crash nhiều không? | Crash-Free Sessions %, Bugs per 1k sessions | Crash giảm → Player retention tăng |
| FPS/Memory có ổn trên target hardware? | Average FPS, Frame Pacing, Memory Footprint | Trải nghiệm mượt → Rating store cao |
| WebGL tải quá lâu không? | Time to First Interaction, Total Load Time | Onboarding tốt → Reduce bounce rate |
| Multiplayer chịu được bao nhiêu người? | Concurrent Users/Room, Tick Rate, Latency | Scale vs chi phí server |

**KPI framework**: Impact metrics = (Technical metric) × (Business impact). Ví dụ: Crash rate giảm 1% → giữ lại 10k MAU → tăng revenue $5k/tháng.

---

## 2. Crash & Bug Metrics

### 2.1 Crash-Free Rate
- **Definition:** `% sessions không crash`.
- **Goal:** Mobile ≥ 99.5%, Console ≥ 99.8%.
- **Tools:** Unity Cloud Diagnostics, Backtrace, Bugsnag.

| Baseline | Target | Tactics |
| --- | --- | --- |
| 96% crash-free (nhiều lỗi OOM) | 99% | - Addressables để stream asset<br>- Texture compression<br>- Kiểm soát memory bằng Profiler API |

### 2.2 Bug Density / 1k Sessions
- Đo số bug report/1k session → gắn severity (Critical, Major, Minor).
- **Goal:** Critical bug < 0.5/1k sessions.
- **Process:** LiveOps board (Jira), SLA fix 24h.

### 2.3 Silent Failures
- Logging exception trong background (ví dụ shader compiling fail) → track qua Sentry.

**Case study:** Studio X giảm crash từ 94% → 99.2% trong 2 sprint bằng cách:
1. Bật IL2CPP exception stack trace (Development build) tìm nguồn gốc crash.
2. Migration sang Unity 2022 LTS fix GC spikes.
3. Viết automated regression test bằng Test Runner + CI để catch null ref.

---

## 3. Performance Metrics (FPS, Memory, CPU/GPU)

### 3.1 FPS & Frame Pacing
- **Average FPS target:** Mobile 60fps, PC 120fps, VR 90fps.
- **Frame pacing:** Delta <±5ms để tránh stutter.
- **Tools:** Unity Profiler, Frame Debugger, RenderDoc.

| Optimization | Impact |
| --- | --- |
| Batching + GPU Instancing | FPS +15-25% trên scene nhiều mesh |
| Adaptive Quality (URP) | Giữ FPS ổn định khi GPU overheat |
| Scriptable Render Pipeline tuning | Giảm overdraw, strip shader variant |

### 3.2 Memory Footprint
- **Target:** Mobile < 1.5GB, WebGL < 1GB, PC < 4GB tùy game.
- **Key metrics:** Total allocated, Mono heap, Gfx driver memory.
- **Techniques:** Addressables, Asset bundle variant, Texture atlas, Audio streaming.

### 3.3 CPU/GPU Profiling
- **CPU:** Job System, Burst compiler, DOTS để xử lý AI/Physics.
- **GPU:** Analyze fill rate, render passes, light baking (Mixed lighting).

### 3.4 WebGL-Specific
- **FPS target:** 45-60fps (tùy browser/hardware).
- **Memory:** ~512MB limit (Chrome). Sử dụng `-s INITIAL_MEMORY=...`.
- **Tối ưu:**
  - Strip unused engine code (`Player Settings > Stripping Level`)
  - Compressed texture (ASTC) + Gzip/Brotli build
  - Lazy load (defer heavy scenes)

---

## 4. Load Time Metrics (Mobile/WebGL/PC)

### 4.1 Key Metrics
- **TTFI (Time to First Interaction):** Thời gian từ launch → user control.
- **TTS (Time to Start Level):** Từ chọn level → gameplay bắt đầu.
- **Total Load Time:** Toàn bộ pipeline (splash → main menu → level).

| Platform | Baseline | Target | Techniques |
| --- | --- | --- | --- |
| WebGL | 20-30s | <15s | Gzip + CDN + Asset streaming |
| Mobile | 10-15s | <8s | Cold start optimization, reduce plugin/SDK init |
| PC/Console | 15-60s | <20s | Async loading, shader warmup |

### 4.2 Optimization Playbook
1. **Build stripping:** bật `Script Debugging OFF`, `Managed Stripping Level = Medium/High`.
2. **Addressables & Preload:** preload critical assets, lazy load cosmetic.
3. **Splash to Menu:** load minimal scenes, async background loading.
4. **Progressive Mesh Loading:** LOD swap sau khi player đứng yên.

**Impact:** Studio Y giảm WebGL load time từ 28s → 12s (−57%) nhờ CDN + WebAssembly streaming.

---

## 5. Multiplayer Metrics: Concurrency & Latency

| Metric | Definition | Target |
| --- | --- | --- |
| **CCU per room** | Số người / phòng | Casual party game: 8-16, FPS: 8-64 |
| **Tick rate** | Số lần server update/giây | 30-60 Hz (casual) ; 60-128 Hz (competitive) |
| **Latency** | Round trip client ↔ server | <100ms SEA region; <50ms eSports |
| **Packet loss** | % packets fail | <1% |

**Monitoring stack:**
- Game server logs → InfluxDB/Prometheus.
- Network debug panel (Unity Transport) → collect RTT, jitter.
- Synthetic tests (Gamedriver, custom bots) → stress concurrency.

**Scaling strategy:**
- **Room-based:** Matchmaker + Kubernetes (Agones) scale pods theo CCU.
- **Authoritative server:** DOTS NetCode cho prediction/reconciliation.
- **Edge servers:** dùng AWS Global Accelerator/CDN để giảm latency cross-region.

---

## 6. Live Ops & Business Metrics liên quan

| Technical Metric | Business Impact |
| --- | --- |
| Crash-free session % | Direct ảnh hưởng retention day 1/7/30 |
| FPS stability | Store rating & virality |
| Load time | Funnel onboarding (Install → first session) |
| Latency & concurrency | ARPDAU của game multiplayer |
| Memory footprint | Device compatibility (low-end market share) |
| Patch size | Update compliance, user adoption rate |

### 6.1 Monetization Correlation
- **Example:** Crash giảm 3% → retention day 7 tăng 2% → LTV +$0.05/player.
- **AB testing:** deploy optimized build cho 10% traffic, đo uplift.

### 6.2 Ops Dashboard
- Grafana board: Crash rate, FPS buckets (<30, 30-45, 60+), load time percentiles, CCU.
- Alerting: PagerDuty khi crash spike >1%, latency >150ms.

---

## 7. Implementation Checklist

1. **Instrument**
   - Enable Unity Analytics + Cloud Diagnostics.
   - Custom telemetry (Application.logMessageReceived, ProfilerRecorder).
2. **Baseline**
   - Ship instrumentation build → thu 7 ngày data.
   - Xác định top device (Android low-end, iOS mid-range, PC spec target).
3. **Optimize**
   - Tạo performance squad (Engineer + Tech Artist + QA).
   - Ưu tiên theo impact: Crash > FPS > Load time > Memory.
4. **Verify**
   - A/B test build, canary release 5% → 25% → 100%.
   - Đo real-user monitoring (RUM) qua SDK.
5. **Communicate**
   - Release note highlight: “Crash giảm 40%, FPS +20% trên device X”.

---

## 8. Sample Metric Targets by Platform

| Platform | Crash-Free % | Avg FPS | Load Time | Memory | Latency |
| --- | --- | --- | --- | --- | --- |
| Mobile Casual | 99.5% | 60fps | TTFI < 6s | <1.2GB | N/A |
| Mobile Mid-core | 99.2% | 45-60fps | <8s | <1.5GB | 80-100ms (multiplayer) |
| WebGL | 99% | 45fps | <12s | <512MB | N/A |
| PC/Console | 99.8% | 60-120fps | <15s | <4GB | 40-60ms |
| VR | 99.5% | 72-90fps | <10s | <3GB | 30-50ms |

---

## 9. Reporting Template

```
🎯 Sprint 11 Impact Report - Unity LiveOps

Crash-Free Sessions: 98.9% → 99.6% (+0.7%)
Root cause: Addressables memory leak fixed (ticket #123)

FPS (Android mid-tier): P50 48fps → 58fps (+21%)
Optimization: GPU instancing foliage, reduce dynamic lights

WebGL Load Time: 18s → 11s (-39%)
Actions: CDN + Brotli + Asset bundle splitting

Multiplayer latency (SEA): 120ms → 85ms (-29%)
Actions: Added Singapore edge servers, tuned send rate

Next focus: Reduce patch size < 500MB, improve cold start login flow
```

---

> **Last Updated:** March 2026