# Accessibility

## Nguyên tắc
- Touch targets tối thiểu 44x44pt; spacing đủ.
- Contrast đủ; hỗ trợ dark mode.
- Screen reader labels rõ (semantics/aria equivalents).

## Flutter
- Sử dụng Semantics; label cho icons/buttons.
- Kiểm tra focus order; hỗ trợ font scaling.

## React Native
- `accessibilityLabel`, `accessible`; roles.
- Kiểm tra bằng screen reader (TalkBack/VoiceOver).