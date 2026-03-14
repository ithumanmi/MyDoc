# Deep Linking

## Loại link
- Universal Links (iOS), App Links (Android): HTTPS, tránh prompt chọn app.
- Custom scheme: nhanh, nhưng dễ xung đột tên; cân nhắc fallback.
- Deferred deep link: cài app rồi vào đúng screen.

## Best practices
- Routing rõ ràng: map URL -> screen + params validation.
- Fallback: nếu app chưa cài, mở web/Store.
- Tracking: campaign params; cẩn trọng privacy.

## Testing
- Kiểm tra mở app từ web/QR/email.
- Cold start vs warm start; param persist đúng.