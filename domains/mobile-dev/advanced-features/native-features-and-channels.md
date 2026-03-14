# Native Features & Channels

## Khi nào cần native
- SDK chỉ có Swift/Kotlin/ObjC/Java.
- Yêu cầu low-latency (Bluetooth, camera pipeline, audio DSP).
- Cần quyền/feature đặc thù OS.

## Flutter: Platform Channels
- MethodChannel, EventChannel; isolate main vs background.
- Viết plugin: iOS (Swift), Android (Kotlin). Tách interface + impl.

## React Native: Native Modules
- Turbo Modules / JSI cho hiệu năng; bridging ít overhead hơn classic bridge.
- Native UI Components khi cần view tùy chỉnh.

## Best practices
- Đóng gói SDK vào module/plugin; API surface nhỏ, testable.
- Quản lý permission rõ: camera/location/bluetooth.
- Bench và fallback: nếu feature không critical, degrade gracefully.