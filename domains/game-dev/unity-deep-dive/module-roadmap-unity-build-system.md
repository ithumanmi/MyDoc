# 🧱 Unity Module Roadmap – Build để tái sử dụng cho Product & Freelancer

> Mục tiêu: xây thư viện module Unity (code & asset) có thể reuse cho sản phẩm cá nhân hoặc gói dịch vụ freelance.

## 1. Khung chiến lược 3 lớp

| Lớp | Mục tiêu | Ví dụ module |
| --- | --- | --- |
| **Core Engine Extensions** | Nền tảng code tái sử dụng mọi dự án | Input system wrapper, scene loader async, save/load pipelines |
| **Feature Packs** | Chức năng cụ thể cho game/app | Inventory, Dialogue, Mission system, In-app purchase toolkit |
| **Production Toolbox** | Đẩy nhanh workflow build & handoff | Editor tools, CI/CD pipeline, asset validation, localization helper |

## 2. Roadmap 4 pha (12-16 tuần)

1. **Pha 1 – Foundation & Standards (2-3 tuần)**
   - Chọn kiến trúc chuẩn (MVC/MVVM + ScriptableObject).
   - Thiết lập coding standard, folder structure, naming.
   - Tạo base package: core utility (event bus, pooled objects, data persistence).
2. **Pha 2 – Core Engine Modules (3-4 tuần)**
   - Input & Interaction module (new Input System wrapper).
   - Scene management + async loader + loading UI.
   - Save/Load + cloud-sync hooks.
3. **Pha 3 – Feature Packs (4-5 tuần)**
   - Chọn 2-3 module high demand: ví dụ Inventory + Dialogue + LiveOps.
   - Viết document + sample scene.
   - Chuẩn bị packaging (Unity Package Manager / Git submodule).
4. **Pha 4 – Production Toolbox (3-4 tuần)**
   - Editor tooling (batch placement, level builder, animation retarget).
   - Build automation (Cloud Build pipeline, test suite).
   - Marketing asset generator (record template, screenshot pipeline).

## 3. Bảng module đề xuất

| Module | Use-case chính | Output | Monetization/Freelance angle |
| --- | --- | --- | --- |
| **Input & Action Mapping** | Mobile + PC cùng lúc | Prefab + script cho đa nền tảng | Bán như package hoặc dùng để giảm thời gian dev | 
| **Economy + In-app Purchase** | Casual/F2P | ScriptableObject config + UI template | Gói setup IAP cho khách hàng/đối tác |
| **Mission/Quest System** | Story, RPG nhẹ | Graph Editor + runtime API | Cung cấp như service update content |
| **Analytics & LiveOps Hooks** | SaaS game analytics, Remote config | SDK wrapper + event schema | Bán productized service (Dashboard + integration) |
| **Localization & Asset Pipeline** | Xây product global | CSV/Google Sheet adapter + auto import tool | Service dịch/localize nhanh |
| **Ads Monetization Kit** | Hyper-casual, hybrid casual | Script quản lý waterfall, mediation, A/B placement | Bán package + dịch vụ tối ưu eCPM |
| **Stylized Color & Material Library** | Multi-game studio muốn thống nhất look | Shader graph + color palette manager | Thu phí license hoặc bán theme pack |
| **Config & Remote Tuning** | LiveOps/seasonal event | ScriptableObject + Google Sheet sync + runtime override | Bán như “balance tuning service” |
| **Coroutine/Task Framework** | Game cần xử lý async phức tạp | Wrapper quản lý lifecycle, cancel token | Gói nâng hiệu suất + bảo trì |
| **FX/Particles Toolkit** | UI feedback, combat game | Prefab VFX + controller script | Bán asset pack + bundle dịch vụ tùy chỉnh |
| **Advanced Inventory + Crafting** | Survival, RPG lite | Modular inventory core + crafting recipe builder | Productized service cập nhật nội dung |
| **Loading & Streaming Suite** | Open world, mobile nặng | Addressables profile + streaming profiler | Gói tư vấn tối ưu memory |
| **Math & Utilities Pack** | Studio nhỏ cần chuẩn hóa | Vector extension, noise generators, curve tools | Bán license + training nội bộ |
| **In-game Shop + Offer Engine** | LiveOps monetization | UI prefab + promo scheduler + receipt validator | Triển khai cho khách hàng + doanh thu chia sẻ |
| **Sprite/UI System** | 2D toolkit | UI kit responsive + localization-ready | Bán template + workshop hướng dẫn |

## 4. Checklist reuse-ready

- [ ] Module đóng gói dạng Unity package hoặc UPM repo riêng.
- [ ] Có sample scene + README hướng dẫn tích hợp.
- [ ] Có test đơn giản (PlayMode/Editor) đảm bảo không vỡ khi nâng phiên bản.
- [ ] Có license rõ ràng (MIT/Commercial) khi dùng cho khách hàng.
- [ ] Tài liệu ghi rõ dependency và phiên bản Unity hỗ trợ.

> Khi checklist đạt 100%, thêm module vào catalog cá nhân (Notion/Website) để khách hàng thấy ngay năng lực.

## 5. Stack công cụ gợi ý

- **Versioning**: Git submodule + UPM.
- **CI/CD**: Unity Cloud Build / GitHub Actions.
- **Documentation**: Docusaurus/Notion + video demo ngắn.
- **Asset mgmt**: Addressables + automated import rules.

## 6. Liên kết trong repo

- [`architecture-patterns.md`](./architecture-patterns.md) – chọn kiến trúc tái sử dụng.
- [`editor-scripting.md`](./editor-scripting.md) – xây production toolbox.
- [`optimization-techniques.md`](./optimization-techniques.md) – đảm bảo module nhẹ, ít leak.
- [`vfx-lighting-mastery.md`](./vfx-lighting-mastery.md) – bổ sung visual module nếu cần bán asset.

> Đầu tư module một lần, sau đó có thể dùng để ship sản phẩm riêng hoặc bán gói freelancer. Hãy coi mỗi module như “asset sinh lời” – mài càng kỹ, biên lợi nhuận càng cao.