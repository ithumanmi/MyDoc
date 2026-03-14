# Challenge: Accessibility Core (ARIA, Keyboard, Contrast)

- **Loại:** project (web-ui only)
- **Mảng:** web-ui
- **Mức:** Beginner
- **Ước lượng thời gian:** 0.5-1 ngày
- **Prerequisites (tùy chọn):** HTML/ARIA cơ bản, DevTools/Lighthouse a11y.

## Mục tiêu học tập
- Đảm bảo navigable bằng bàn phím, role/aria-label đúng, tương phản màu đạt chuẩn.
- Chạy check a11y cơ bản và sửa lỗi phổ biến.

## Đề bài
Chọn một trang web đơn giản (landing hoặc form) và:
- Bổ sung ARIA/role/label đúng cho form, button, nav.
- Đảm bảo keyboard navigation: tab order hợp lý, focus ring rõ, skip link (tuỳ chọn).
- Kiểm tra contrast (WCAG AA) và sửa màu nếu cần.
- Chạy Lighthouse/axe và giảm lỗi a11y.

## Đầu vào (Input)
- Trang HTML/CSS/JS (có thể từ template hiện có hoặc tự tạo).

## Đầu ra (Output)
- Code đã sửa a11y.
- Báo cáo ngắn: các lỗi ban đầu, hành động fix, kết quả check (screenshot hoặc log Lighthouse/axe).

## Tiêu chí chấm (Acceptance)
- **Keyboard:** Tab qua được các thành phần chính, focus visible, không trap.
- **ARIA:** Role/aria-label hợp lý cho input, button, nav, landmark.
- **Contrast:** Đạt WCAG AA cho text chính.
- **Báo cáo:** Nêu lỗi → fix → kết quả sau fix.

## Gợi ý / Hint
- Dùng `aria-label`/`aria-labelledby` cho input không có label.
- Landmarks: `header`, `main`, `nav`, `footer`.
- Check contrast bằng DevTools hoặc công cụ online.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Đính kèm trang trước/sau và kết quả Lighthouse/axe.