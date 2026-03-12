# 📦 Packaging & Distribution

## 1. Python Toolchain
- **PyInstaller:** bundle script → standalone exe.
  - Pros: nhanh, hỗ trợ Windows/Linux.
  - Cons: dễ bị reverse.
- **Nuitka:** compile sang C, tối ưu tốc độ, khó reverse hơn.
- **Briefcase/PyOxidizer:** khi cần GUI hoặc embedding interpreter đặc biệt.

## 2. Build Matrix
- Target OS: Win10, Ubuntu 22.04.
- `pyenv` để pin version (3.10/3.11).
- Docker image chứa dependency (Chrome, adb, libusb...).

## 3. Obfuscation & Hardening
- **Code Obfuscation:**
  - Use Nuitka + `--lto` + plugin anti-decompile.
  - For PyInstaller: add tools như PyArmor để encrypt bytecode.
- **Secrets:** load từ config encrypted (sops/Vault), không bake vào binary.
- **Integrity:** ký checksum (SHA256) + optional code signing cert.

## 4. Distribution Channels
- Private S3/MinIO bucket với presigned URL.
- Self-hosted update server (nginx) + auth token.
- For Windows ops: package MSI via WiX hoặc Inno Setup.

## 5. Release Flow
1. `make build-win` / `make build-linux` chạy test + bundle.
2. Upload artifact + checksum.
3. Update changelog + release note.
4. Notify ops team qua bot.

## 6. Checklist
- [ ] CI build qua container reproducible.
- [ ] Binary obfuscation & signing hoàn tất.
- [ ] Upload + checksum verified.