# 📱 Mobile Dev Domain: Nhận xét & Đề xuất mở rộng, đào sâu

> Tài liệu nội bộ: đánh giá domain `domains/mobile-dev` và kế hoạch mở rộng nội dung, đào sâu kỹ thuật.

---

## 📋 1. Nhận xét hiện trạng

### Điểm mạnh
- **README.md rõ ràng, có định hướng:** Bảng so sánh App Dev vs Web/Game/AI, Mermaid roadmap 4 level (Foundations → Data & Networking → Advanced Features → Engineering Excellence).
- **Cross-platform first:** Giải thích rõ "90% Startup/Outsourcing chọn Flutter hoặc React Native", phù hợp thị trường VN.
- **Hai stack song song:** Flutter (Dart) và React Native (JS/TS) được nêu trong từng level, giúp người học chọn theo nền tảng (mới vs đã biết Web).
- **Ba path Level 4 rõ ràng:** Cross-Platform Architect, Native Specialist (iOS/Android), Indie Hacker (Product/Monetization).
- **Liên kết đầy đủ:** Knowledge Audit (EcoRide SuperApp), `resources/collected_links/mobile-dev.md`, DIFFICULTY-GUIDE, GLOSSARY.
- **Career/Monetization tách riêng:** `guides/03-career-skills/mobile-dev/` lo phần kiếm tiền & sự nghiệp; domain tập trung kỹ thuật.
- **Knowledge Audit chất lượng:** 5 thử thách (State Management, UX/Design System, Offline-first, Monetization/ASO, CI/CD) + Answer Key, bám sát thực tế SuperApp.

### Hạn chế
| Vấn đề | Chi tiết |
|--------|----------|
| **Cấu trúc phẳng** | Chỉ có 1 file `README.md`. Không có thư mục con, không có INDEX/sitemap như `backend-dev`. |
| **Thiếu tài liệu đào sâu** | State management (BLoC vs Riverpod vs Redux), Offline-first & sync, List performance, Platform channels, Native modules chưa có doc riêng. |
| **Native (iOS/Android) chưa có đường dẫn** | Path B "Native Specialist" chỉ là keywords (Swift/SwiftUI, Kotlin/Jetpack Compose); không có roadmap hoặc doc dẫn vào. |
| **Testing chưa xuất hiện trong roadmap** | Unit test, Widget/Component test, E2E (Detox, Maestro, Integration test) chưa được nêu trong Level 2–3. |
| **Performance & battery chưa tách** | Jank, 60fps, memory leak, battery (GPS/Background) nằm rải rác trong README và Knowledge Audit, chưa có doc tổng hợp. |
| **CI/CD chỉ nhắc qua** | Fastlane, GitHub Actions, Bitrise chưa có hướng dẫn hoặc checklist trong domain. |
| **Challenges chưa gắn** | `challenges/mobile/` tồn tại (Networking, offline sync, UI performance, battery, a11y) nhưng README domain không link tới. |
| **Guides career có link nhưng nhiều file chưa tồn tại** | `guides/03-career-skills/mobile-dev/` tham chiếu mobile-career-ladder, remote-mobile-guide, monetization/*, indie-hacker-guide… một số file có thể chưa được tạo. |

### So sánh nhanh với domain khác
- **backend-dev:** INDEX.md + nhiều thư mục (architecture/, system-design/, database/, security/, devops-sre/, templates/) → dễ tìm và đào sâu từng chủ đề.
- **mobile-dev:** Một README toàn diện, nội dung kỹ thuật "đào sâu" chưa tách thành doc riêng → khó tra cứu và mở rộng.

---

## 🚀 2. Đề xuất mở rộng cấu trúc

### 2.1 Cấu trúc thư mục đề xuất

```
domains/mobile-dev/
├── README.md                    # Giữ, rút gọn: overview + link ra các doc con
├── INDEX.md                     # [MỚI] Sitemap toàn bộ mobile-dev (theo level + chủ đề)
├── EXPANSION-PROPOSAL.md        # File này
│
├── foundations/                  # [MỚI] Level 1
│   ├── README.md                # Language (Dart/JS), UI system (Widgets/Components), Layouts
│   ├── flutter-vs-react-native.md  # Khi nào chọn Flutter vs RN, so sánh ngắn
│   └── app-lifecycle.md         # Init, Build, Dispose; tránh leak
│
├── data-and-networking/          # [MỚI] Level 2
│   ├── README.md                # HTTP, JSON, API integration
│   ├── state-management-deep-dive.md  # [ĐÀO SÂU] Provider, BLoC, Riverpod (Flutter); Redux, Zustand (RN); khi nào dùng gì
│   ├── local-storage.md         # SharedPreferences, SQLite, Hive, Realm; chọn stack
│   └── mvvm-clean-architecture.md   # Sơ đồ folder, tách Data/Domain/Presentation
│
├── advanced-features/            # [MỚI] Level 3
│   ├── README.md                # Camera, GPS, Bluetooth, Biometric, Push, Firebase
│   ├── offline-first-and-sync.md    # [ĐÀO SÂU] Local-first, conflict resolution, Idempotency Key, sync strategies
│   ├── native-features-and-channels.md  # [ĐÀO SÂU] Platform Channels (Flutter), Native Modules (RN); khi nào cần
│   ├── background-tasks-battery.md     # Background Fetch, Location updates, tiết kiệm pin
│   └── deep-linking.md          # Universal Links, App Links, deferred deep links
│
├── performance/                  # [MỚI] Đào sâu hiệu năng
│   ├── README.md                # 60fps, jank, startup time
│   ├── list-and-scroll-performance.md # View recycling, ListView.builder, FlatList, lazy loading
│   ├── memory-and-leaks.md      # Detach listeners, dispose, profiling
│   └── app-size-and-bundle.md   # Dynamic delivery, on-demand resources, split APK/App Bundle
│
├── design-and-ux/                # [MỚI] Theming, responsive, a11y
│   ├── README.md                # Design tokens, Dark mode, Localization
│   ├── responsive-and-adaptive.md     # Breakpoints, Foldables, Notch, tablet
│   └── accessibility.md         # Screen reader, contrast, touch targets
│
├── senior-paths/                  # [MỚI] Level 4
│   ├── README.md                # 3 path A/B/C
│   ├── cross-platform-architect.md     # Platform Channels, Super App structure, module federation
│   ├── native-ios-android/      # [ĐÀO SÂU] Path Native
│   │   ├── README.md            # Khi nào đi Native, so sánh với cross-platform
│   │   ├── ios-swift-swiftui.md # Roadmap Swift/SwiftUI, Xcode, App Store
│   │   └── android-kotlin-compose.md  # Roadmap Kotlin/Jetpack Compose, Android Studio
│   └── indie-hacker-product.md  # Tóm tắt + link guides (monetization, ASO, IAP)
│
├── testing/                      # [MỚI] Bổ sung vào roadmap
│   ├── README.md                # Unit, Widget/Component, Integration, E2E
│   └── e2e-and-automation.md    # Detox, Maestro, Appium; CI test
│
├── cicd-and-ops/                 # [MỚI]
│   ├── README.md                # Fastlane, GitHub Actions, Bitrise
│   ├── fastlane-playbook.md     # Lanes, screenshots, certs, submit Store
│   └── feature-flags-remote-config.md # Firebase Remote Config, A/B, Canary
│
├── portfolio-career/             # [MỚI] Tóm tắt + link guides
│   └── README.md                # Checklist portfolio, interview prep, link guides/03-career-skills/mobile-dev
│
└── resources/                    # [MỚI] Tùy chọn
    └── README.md                # YouTube, courses, books (dời từ README gốc)
```

---

## 🔬 3. Đề xuất đào sâu (Deep-dive topics)

Các chủ đề nên có ít nhất một doc riêng để người học và người đi làm tra cứu nhanh.

### 3.1 State Management (ưu tiên cao)
- **File đề xuất:** `data-and-networking/state-management-deep-dive.md`
- **Nội dung:** So sánh Provider / BLoC / Riverpod (Flutter); Redux Toolkit / Zustand / Jotai (RN). Khi nào dùng global state vs local, unidirectional flow, multi-module state (SuperApp). Link Knowledge Audit Thử thách 1.

### 3.2 Offline-first & Sync (ưu tiên cao)
- **File đề xuất:** `advanced-features/offline-first-and-sync.md`
- **Nội dung:** Local-first là gì, chọn SQLite/Room/Hive/Realm. Conflict resolution (last-write-wins, CRDT, operational transform). Idempotency key, sync queue, retry. Optimistic UI. Link Knowledge Audit Thử thách 3.

### 3.3 List & Scroll Performance (ưu tiên cao)
- **File đề xuất:** `performance/list-and-scroll-performance.md`
- **Nội dung:** View recycling, ListView.builder / FlatList / FlashList. Tránh tác vụ nặng trên UI thread, lazy load ảnh. 60/120 FPS, jank debugging. Link Knowledge Audit Thử thách 1.

### 3.4 Platform Channels & Native Modules (ưu tiên trung bình)
- **File đề xuất:** `advanced-features/native-features-and-channels.md`
- **Nội dung:** Khi nào cần viết Native (Swift/Kotlin). Flutter: Method Channel, Event Channel. RN: Native Modules, Turbo Modules. Ví dụ: Bluetooth, custom camera, SDK bên thứ 3 chỉ có Native.

### 3.5 Background Tasks & Battery (ưu tiên trung bình)
- **File đề xuất:** `advanced-features/background-tasks-battery.md`
- **Nội dung:** Background Fetch, WorkManager (Android), BGTaskScheduler (iOS). Location updates (accuracy vs battery). Best practices tránh bị OS kill, tiết kiệm pin. Link Knowledge Audit Thử thách 3.

### 3.6 CI/CD & Fastlane (ưu tiên trung bình)
- **File đề xuất:** `cicd-and-ops/fastlane-playbook.md`
- **Nội dung:** Lanes (build, test, screenshot, submit). Certificates & provisioning. GitHub Actions / Bitrise integration. Auto-increment build number, upload to TestFlight/Play Internal. Link Knowledge Audit Thử thách 5.

### 3.7 Native iOS & Android roadmaps (ưu tiên trung bình – đào sâu Path B)
- **File đề xuất:** `senior-paths/native-ios-android/ios-swift-swiftui.md`, `android-kotlin-compose.md`
- **Nội dung:** Roadmap ngắn: Swift/SwiftUI (iOS), Kotlin/Jetpack Compose (Android). Toolchain, Store submission, khi nào công ty cần Native thuần. Cross-link với cross-platform khi cần hybrid.

### 3.8 Design System & Theming (ưu tiên trung bình)
- **File đề xuất:** `design-and-ux/README.md` + `responsive-and-adaptive.md`
- **Nội dung:** Design tokens, ThemeData (Flutter) / Theme (RN). Dark mode, localization. Responsive: breakpoints, Foldables, Notch, tablet layout. Link Knowledge Audit Thử thách 2.

### 3.9 Testing (Unit, Widget, E2E) (ưu tiên trung bình)
- **File đề xuất:** `testing/README.md`, `e2e-and-automation.md`
- **Nội dung:** Unit test (bloc_test, Jest). Widget/Component test (Flutter widget test, RN component test). E2E: Detox, Maestro, Appium. Chạy trong CI.

### 3.10 App Size & Store (ASO kỹ thuật) (ưu tiên thấp – business nhiều ở guides)
- **File đề xuất:** `performance/app-size-and-bundle.md`
- **Nội dung:** Split APK, App Bundle, on-demand resources. Giảm size ảnh/font/native libs. Link ASO (keywords, screenshots) sang `guides/03-career-skills/mobile-dev/monetization/`.

---

## 📌 4. Rút gọn README.md hiện tại

- **Giữ:** Reality Check, Mermaid roadmap, bảng tóm tắt 4 level, Portfolio checklist (rút gọn), Interview prep (rút gọn), Core Skills/CV keywords.
- **Chuyển:** Chi tiết từng level (Core Concepts, Actions, Completion Criteria) → link tới `foundations/`, `data-and-networking/`, `advanced-features/`, `senior-paths/`.
- **Chuyển:** Resources (YouTube, courses, books) → `resources/README.md` hoặc giữ 1 đoạn + link `collected_links/mobile-dev.md`.
- **Thêm:** Mục "Challenges" link tới `challenges/mobile/`. Mục "Sitemap" link tới `INDEX.md`.

---

## 🔗 5. Cross-domain & liên kết

- **backend-dev:** API design, Auth (JWT, OAuth), sync protocol design → link khi nói Offline-first, IAP server-side validation.
- **guides/03-career-skills/mobile-dev:** Monetization (AdMob, IAP, ASO), Career ladder, Remote, Indie Hacker → domain chỉ tóm tắt + link.
- **challenges/mobile:** Thêm link từ README và INDEX; có thể thêm 1–2 challenge "state management" hoặc "offline sync" nếu chưa có.
- **case-studies/knowledge-audits/mobile-dev-knowledge-audit.md:** Mỗi doc đào sâu nên có đoạn "Liên quan Knowledge Audit: Thử thách X".

---

## ✅ 6. Checklist triển khai (gợi ý)

### Phase 1 – Nền tảng
- [ ] Tạo `INDEX.md` (sitemap theo level + chủ đề).
- [ ] Cập nhật README: thêm link INDEX, link Challenges (`challenges/mobile/`), rút gọn chi tiết level → link.

### Phase 2 – Đào sâu ưu tiên cao
- [ ] `data-and-networking/state-management-deep-dive.md`
- [ ] `advanced-features/offline-first-and-sync.md`
- [ ] `performance/list-and-scroll-performance.md`

### Phase 3 – Đào sâu ưu tiên trung bình
- [ ] `advanced-features/native-features-and-channels.md`
- [ ] `advanced-features/background-tasks-battery.md`
- [ ] `cicd-and-ops/fastlane-playbook.md`
- [ ] `design-and-ux/README.md` + `responsive-and-adaptive.md`
- [ ] `testing/README.md` + `e2e-and-automation.md`

### Phase 4 – Cấu trúc và path
- [ ] Tạo README cho từng thư mục: `foundations/`, `data-and-networking/`, `advanced-features/`, `performance/`, `senior-paths/`.
- [ ] `senior-paths/native-ios-android/` (README + ios + android roadmap ngắn).
- [ ] `portfolio-career/README.md` (tóm tắt + link guides).

### Phase 5 – Tùy chọn
- [ ] `performance/app-size-and-bundle.md`
- [ ] `foundations/flutter-vs-react-native.md`, `app-lifecycle.md`
- [ ] `resources/README.md` (dời Resources từ README gốc)

---

*Tài liệu này có thể cập nhật khi triển khai từng bước.*
