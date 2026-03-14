# List & Scroll Performance

## Nguyên tắc
- Dùng list ảo hóa/recycling: `ListView.builder` (Flutter), `FlatList`/`FlashList` (RN).
- Tránh inline heavy work trong render; tách memoized components.
- Batch updates; debounce scroll handlers.

## Hình ảnh & network
- Lazy load + cache; limit kích thước ảnh; dùng placeholders.
- Prefetch hợp lý; tránh block UI thread.

## Debug
- Measure FPS/jank (Perf overlay, Flipper/React DevTools).
- Profile slow frames, JS thread (RN) vs UI thread.

## Liên quan
- State mgmt selectors để giảm re-render.