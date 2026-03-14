# Challenge: List + Detail với Networking, Cache, Pull-to-Refresh

- **Loại:** project
- **Mảng:** mobile
- **Mức:** Beginner
- **Ước lượng thời gian:** 1-2 ngày
- **Prerequisites (tùy chọn):** Kinh nghiệm mobile cơ bản (UIKit/SwiftUI hoặc Android Compose/XML), HTTP client.

## Mục tiêu học tập
- Xây dựng màn hình list + detail với gọi API, trạng thái loading/error.
- Thêm caching nhẹ và pull-to-refresh.

## Đề bài
Xây app đơn giản hiển thị danh sách (ví dụ: articles/products/users) từ một public API:
- Màn **List**: hiển thị ảnh/thumb, title, subtitle; trạng thái loading/error; pull-to-refresh.
- Màn **Detail**: hiển thị thông tin đầy đủ; xử lý loading/error.
- **Cache**: lưu response lần đầu và đọc lại khi mở app (in-memory hoặc local file/DB tuỳ stack).

## Đầu vào (Input)
- Public API (REST) hoặc mock JSON.

## Đầu ra (Output)
- App chạy được 2 màn hình, có loading/error state, pull-to-refresh, cache cơ bản.
- README hướng dẫn build/run, nêu rõ API dùng và cách mock (nếu mock).

## Tiêu chí chấm (Acceptance)
- **Đúng chức năng:** List và detail hoạt động; pull-to-refresh; lỗi hiển thị được.
- **Cache:** Dữ liệu cũ hiển thị khi offline/mở lại (tối thiểu 1 lần).
- **UI/UX:** Hiển thị rõ trạng thái (loading/error/empty), không crash.

## Gợi ý / Hint
- Tách layer: data (API + cache) / viewmodel / view.
- Với iOS: URLSession + Codable; với Android: Retrofit/OkHttp + Room/Cache.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Link repo mẫu nếu public.