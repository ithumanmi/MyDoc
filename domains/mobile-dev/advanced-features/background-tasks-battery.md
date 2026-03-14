# Background Tasks & Battery

## Task types
- Periodic fetch, push handling, location updates, uploads.
- Long-running vs short-lived; iOS hạn chế hơn Android.

## Android
- WorkManager cho deferrable tasks; Foreground Service cho tác vụ cần hiển thị notif.
- Location: priority/batching; tránh wake CPU quá thường xuyên.

## iOS
- BGTaskScheduler, Push Notification triggers; background modes giới hạn.
- Location: significant-change vs high-accuracy; tiết kiệm pin.

## Best practices
- Throttle sync; batch requests.
- Respect OS constraints; fail gracefully khi bị kill.
- Đo battery impact; tắt khi người dùng opt-out.