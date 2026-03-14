# App Size & Bundle

## Giảm kích thước
- Split APK / App Bundle; ABI splits.
- Tối ưu assets: nén ảnh, vector khi có thể; loại bỏ font/locale thừa.
- Loại bỏ native libs không dùng; ProGuard/R8 (Android), bitcode (iOS cũ) không còn bắt buộc.

## Delivery
- On-demand resources (iOS), dynamic feature modules (Android).
- Cache/prefetch hợp lý; tránh tải gói lớn khi mở app lần đầu.