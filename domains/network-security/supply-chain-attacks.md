# 🔗 Supply Chain Attacks & CI/CD Poisoning

> Nội dung: dependency confusion, typosquatting, malicious build scripts, secure artifact pipeline.

---

## 1. Threat Overview
- Attackers nhắm vào dependency (npm, PyPI) hoặc CI/CD runner.
- Trust boundary mờ giữa vendor, OSS và nội bộ.
- SBOM & attestation trở thành bắt buộc (NIST SSDF, Executive Order 14028).

---

## 2. Dependency Confusion / Typosquatting

### 2.1 Pattern
- Private package `@corp/utils` vô tình fetch từ public registry.
- Attackers publish package cùng tên version cao hơn.

### 2.2 Defense
- cấu hình `.npmrc`, `pip.conf` chỉ trỏ private registry.
- Use `--prefer-offline` + lockfile (package-lock, poetry.lock).
- Monitor package install log cho domain lạ.

### 2.3 Tooling
- Dependabot/PyUp + `npm audit`.
- Sigstore `npm sign` / `pip trust` (emerging).

---

## 3. CI/CD Poisoning

| Vector | Mô tả | Mitigation |
| --- | --- | --- |
| Compromised runner | Reuse shared runner → attacker truy cập workspace | Self-hosted runner isolation, ephemeral VM |
| Secret exposure | `env` log ra secret | Use secret manager, mask output |
| Artifact tampering | `npm publish` từ runner bị hijack | Artifact signing + attestation |

### Hardening pipeline
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: sigstore/fulcio-setup@v1
      - run: cosign sign --key env://COSIGN_KEY dist/*.tar
```

---

## 4. SBOM & Attestation
- Generate SBOM (CycloneDX, SPDX) → attach artifact.
- in-toto attest build steps.
- Policy engine (Kyverno, OPA) verify SBOM + signature trước deploy.

---

## 5. Monitoring & Detection
- Log package registry access, alert khi domain mới.
- Checksum mismtach alert → pipeline dừng.
- Git hook `pre-push` scan secret, check for new build script.

---

## 6. Checklist
- [ ] Tất cả dependency lockfile commit vào repo.
- [ ] Private registry precedence cấu hình rõ.
- [ ] CI runner ephemeral, không reuse container có state.
- [ ] Artifact signing + attestation with in-toto/Cosign.
- [ ] SBOM được lưu trữ và so sánh mỗi lần phát hành.
- [ ] Playbook phản ứng khi dependency bị gỡ (yank) hoặc bị takeover.