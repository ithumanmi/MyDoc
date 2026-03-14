# Challenge: SPA Performance & Core Web Vitals

- **Loại:** project (web-ui only)
- **Mảng:** web-ui
- **Mức:** Intermediate
- **Ước lượng thời gian:** 1-2 ngày
- **Prerequisites (tùy chọn):** Kiến thức bundler (Vite/Webpack), React/Vue/Svelte tùy chọn, Lighthouse/Web Vitals cơ bản.

## Mục tiêu học tập
- Tối ưu bundle (split, lazy load), tối ưu ảnh và critical path.
- Cải thiện Core Web Vitals (LCP, FID/INP, CLS) trên môi trường dev.

## Đề bài
Chọn một SPA (có thể là demo e-commerce/blog) và tối ưu:
- **Bundle:** code splitting, lazy load route/component nặng.
- **Assets:** image optimization, preload/preconnect hợp lý.
- **Perf budget:** thiết lập budget cơ bản (bundle size, LCP target) và đo bằng Lighthouse/Web Vitals.

## Đầu vào (Input)
- Mã nguồn SPA mẫu (có thể scaffold từ template hoặc repo sẵn).

## Đầu ra (Output)
- Code tối ưu + README mô tả thay đổi, số liệu trước/sau (Lighthouse hoặc web-vitals).
- Bảng so sánh: bundle size trước/sau, LCP/FID/CLS trước/sau.

## Tiêu chí chấm (Acceptance)
- **Đúng trọng tâm:** Có áp dụng split/lazy load, tối ưu ảnh, preconnect/preload hợp lý.
- **Đo lường:** Cung cấp kết quả trước/sau (screenshot hoặc số liệu) cho LCP/FID/CLS (hoặc INP).
- **Code quality:** Giải thích ngắn gọn các thay đổi; không phá vỡ chức năng.

## Gợi ý / Hint
- Dùng dynamic import cho route nặng; tách vendor bundle nếu hợp lý.
- Ảnh: dùng định dạng tối ưu, width/height cố định để tránh CLS.
- Dùng Lighthouse (desktop/mobile) hoặc web-vitals trong devtools.

## Reference solution (tùy chọn)
- (Tuỳ chọn) Đính kèm repo và số đo trước/sau.