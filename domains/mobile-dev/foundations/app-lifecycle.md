# App Lifecycle & Cleanup

## Flutter
- Stateless vs Stateful; `initState`/`dispose` dùng để đăng ký/hủy listener.
- Tránh leak: huỷ StreamSubscription, controller (TextEditingController, AnimationController).
- Navigator: pop/dispose đúng; tránh giữ context sau dispose.

## React Native
- Component lifecycle: mount → update → unmount; cleanup trong `useEffect` return.
- Tránh leak: huỷ event listener, subscriptions (AppState, Dimensions, NetInfo).
- Navigation (React Navigation): cleanup focus listeners.

## Best practices
- Giảm side-effects trong render; tách side-effect vào effect/hook chuyên biệt.
- Đặt cleanup mặc định cho mọi subscription/listener.
- Profile memory khi nghi ngờ (DevTools/Flipper), kiểm tra zombie listeners.