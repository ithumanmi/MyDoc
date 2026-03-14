# Offline-first & Sync

## Nguyên tắc
- Local-first: thao tác ngay trên cache/DB; sync nền.
- Idempotency key cho mutation; retry/backoff có giới hạn.
- Conflict resolution: last-write-wins, CRDT, server merge; chọn chiến lược theo business.

## Kiến trúc
- Queue sync: hàng đợi mutation, trạng thái pending/sent/failed.
- Versioning/timestamp để resolve; optimistic UI + rollback khi fail.
- Detect connectivity: chuyển chế độ offline/online; debounce sync.

## Dữ liệu & storage
- Chọn storage phù hợp (SQLite/Room, Hive/Realm, WatermelonDB).
- Mã hóa dữ liệu nhạy cảm; migration có version.

## Testing
- Giả lập mất mạng, xung đột ghi, trùng lặp request.
- Kiểm tra idempotent và rollback UI.

## Liên quan
- State mgmt: [../data-and-networking/state-management-deep-dive.md](../data-and-networking/state-management-deep-dive.md)
- Local storage: [../data-and-networking/local-storage.md](../data-and-networking/local-storage.md)