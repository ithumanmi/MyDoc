# Local Storage

## Lựa chọn
- Key-value: SharedPreferences (Android), NSUserDefaults (iOS), tương đương packages Flutter/RN.
- DB: SQLite/Room (Android), CoreData/SQLite (iOS), Flutter (sqflite), RN (WatermelonDB/SQLite), Hive/Realm (NoSQL nhẹ).

## Khi nào dùng gì
- Config nhẹ, flags: key-value.
- Data có quan hệ, tìm kiếm: SQLite/Room/WatermelonDB.
- Offline-first nhiều record: Hive/Realm (NoSQL) hoặc SQLite + sync queue.

## Best practices
- Mã hóa sensitive data (SecureStorage/Keychain); không lưu secret dài hạn.
- Migration versioning; seed data có kiểm soát.
- Tách layer repo; tránh truy cập DB trực tiếp trong UI.