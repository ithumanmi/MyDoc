# 🔄 Auto-Update System

## 1. Requirements
- Tool tự kiểm tra phiên bản mới, download an toàn, hỗ trợ rollback.

## 2. Version Manifest
- Host JSON manifest:
```json
{
  "version": "1.4.2",
  "url": "https://updates.mmo.internal/tool-v1.4.2.exe",
  "sha256": "...",
  "min_license_version": "2026-03",
  "notes": "Fix proxy rotation bug"
}
```

## 3. Update Flow
1. Tool gửi request (kèm current version, license token).
2. Nếu `manifest.version > current`, hiển thị changelog.
3. Download file → verify checksum → backup binary cũ → replace.
4. Restart tool, gửi telemetry `update_success`.

## 4. Delivery Channels
- Private CDN/S3 + signed URL.
- Torrent/LAN sync cho farm lớn (sử dụng BitTorrent sync hoặc rsync).

## 5. Rollback Strategy
- Giữ bản N-1 trong thư mục `.backup`.
- Nếu launch failure → auto rollback & alert server.

## 6. Security
- TLS pinning tới update server.
- Manifest ký bằng Ed25519, tool verify trước khi áp dụng.
- Rate limit + auth để tránh abuse.

## 7. Checklist
- [ ] Manifest versioning rõ ràng.
- [ ] Checksum/Signature verify trong CI.
- [ ] Rollback test trước khi release.