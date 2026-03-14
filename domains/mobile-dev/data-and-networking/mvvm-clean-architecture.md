# MVVM & Clean Architecture (Mobile)

## Layering
- **Presentation:** UI + ViewModel/Controller (state, intent).
- **Domain:** Use cases, business rules; pure, không phụ thuộc platform.
- **Data:** Repository implementations, API/DB mappers.

## Nguyên tắc
- Dependency inversion: UI -> Domain (use case) -> abstract repo; infra inject.
- DTO ↔ Domain model mapping; tránh leak DTO vào UI.
- Module hóa theo feature để tách scope state & dependency.

## Testing
- Domain: test use case thuần; fake repo.
- Presentation: test ViewModel/BLoC với fake use case.
- Data: integration test API/DB khi cần.

## Liên quan
- State mgmt: [state-management-deep-dive.md](state-management-deep-dive.md)
- Offline/sync: [../advanced-features/offline-first-and-sync.md](../advanced-features/offline-first-and-sync.md)