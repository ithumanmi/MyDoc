# Memory & Leaks

## Nguyên tắc
- Cleanup listener/subscription trong dispose/unmount.
- Tránh giữ context/references lâu không cần thiết.
- Cache có hạn, tránh global singleton giữ nhiều ảnh/data.

## Flutter
- Dispose controllers (TextEditingController, AnimationController).
- Theo dõi allocations bằng DevTools; tìm zombie listeners.

## React Native
- Cleanup `useEffect` return; remove event listeners.
- Theo dõi JS heap, Hermes/JSI; Flipper memory plugin.

## Best practices
- Giải phóng resources khi rời screen.
- Tránh leak từ closures giữ biến cũ; dùng weak refs khi cần (Native).