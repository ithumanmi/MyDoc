# 🛡️ AI Security & Adversarial ML

> [← Advanced Topics](./README.md)

AI Security đảm bảo mô hình không bị tấn công (adversarial examples, model stealing, poisoning) và bảo vệ tài sản trí tuệ.

---

## 1. Threat Landscape

- **Adversarial Attacks:** perturb inputs để làm mô hình dự đoán sai.
- **Data Poisoning:** chèn dữ liệu độc vào pipeline training.
- **Model Stealing:** query API để học lại mô hình.
- **Prompt Injection / Jailbreak (LLM):** ép mô hình output trái policy.
- **Supply Chain:** dependency trojan, compromised weights.

---

## 2. Defensive Techniques

| Threat | Defense |
| --- | --- |
| Adversarial examples | Adversarial training, randomized smoothing, input sanitization |
| Poisoning | Data validation, differential privacy, robust aggregation |
| Model stealing | Rate limiting, watermark output, API response truncation |
| LLM prompt injection | Strict instruction hierarchy, tool sandbox, output guardrails |
| Supply chain | Signed artifacts, SBOM, reproducible builds |

---

## 3. Workflow hardening

1. **Threat modeling:** xác định assets (model weights, data), attack surface.
2. **Data pipeline guard:** schema validation, outlier detection trước training.
3. **Training defenses:** adversarial training, DP-SGD nếu cần.
4. **Serving protections:** auth, rate limit, anomaly detection trên input.
5. **Monitoring:** log drift + security events, alert nếu pattern bất thường.

---

## 4. Tooling

- **Adversarial testing:** CleverHans, Foolbox, IBM ART.
- **Poison detection:** CleanLab, data-centric AI.
- **LLM guardrails:** Guardrails AI, Rebuff, Llama Guard, OpenAI policy framework.
- **Model watermarking:** RAIN, DeepMind SynthID (image/audio text watermark).

---

## 5. Checklist vận hành

- Review third-party weights/codes → verify checksum.
- Bảo vệ secrets/API keys khi chia sẻ notebook.
- Thiết lập bug bounty hoặc red-team exercise.
- Có kế hoạch rollback + rotate secrets khi phát hiện compromise.
- **Cross-domain:** [Network Security](../../network-security/README.md) cung cấp playbook SecOps, incident response và red-team lab để phối hợp đội bảo mật.

> 🎯 Lab: dùng IBM ART tạo adversarial examples cho mô hình Vision → so sánh accuracy trước/sau adversarial training.
