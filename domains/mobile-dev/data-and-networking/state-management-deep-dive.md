# State Management Deep Dive

## Khi nào chọn gì
- **Flutter:** Provider (đơn giản), BLoC (flow rõ, testable), Riverpod (declarative, DI nhẹ).
- **React Native:** Redux Toolkit (chuẩn hoá, devtools), Zustand/Jotai (nhẹ), Context cho scope nhỏ.

## Nguyên tắc
- Unidirectional data flow, tránh shared mutable state không kiểm soát.
- Phân tách UI state vs server/cache state; dùng query libs (React Query/SWR) khi phù hợp RN.
- Co-locate state theo feature/module; tránh global không cần thiết.

## Patterns thực dụng
- Loading/Error/Empty states chuẩn hóa; retry/backoff.
- Optimistic update + rollback cho mutation.
- Selector/memoization giảm re-render (BLoC selectors, RTK selectors, Zustand `subscribeWithSelector`).

## Testing
- Flutter: `bloc_test`, `riverpod_test`; fake repository.
- RN: Redux Toolkit slices test; component test với mocked store.

## Liên quan
- Kiến trúc: [mvvm-clean-architecture.md](mvvm-clean-architecture.md)
- Offline & sync: [../advanced-features/offline-first-and-sync.md](../advanced-features/offline-first-and-sync.md)