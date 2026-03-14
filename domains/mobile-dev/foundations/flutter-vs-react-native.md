# Flutter vs React Native

## Khi nào chọn Flutter
- Team mới, cần tốc độ UI cao, widget nhất quán.
- Single codebase, ít phụ thuộc native libs đặc thù.
- UI tuỳ chỉnh mạnh, animation mượt (Skia).

## Khi nào chọn React Native
- Team web (JS/TS) muốn tận dụng kỹ năng hiện có.
- Ecosystem JS phong phú, cần dùng nhiều SDK JS có sẵn.
- Chấp nhận cấu hình native và tối ưu thêm bằng module.

## Tiêu chí chọn
- **Talent pool:** JS/TS sẵn có → RN; thích Dart/Flutter → Flutter.
- **UI/Animation:** Flutter mượt hơn mặc định; RN cần tối ưu thêm (Reanimated/Skia).
- **SDK phụ thuộc native:** Cả hai cần module native; RN có nhiều lib JS hơn.
- **Performance:** Flutter ổn định out-of-box; RN cần chú ý bridge, batching, profiling.
- **Time-to-market:** Flutter (widgets đầy đủ) vs RN (tận dụng lib JS sẵn có).