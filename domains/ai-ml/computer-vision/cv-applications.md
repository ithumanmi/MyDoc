## 🧪 Computer Vision Applications Cheat-sheet

> [← Back to Computer Vision](./README.md)

Tổng hợp các domain ứng dụng CV phổ biến, kỹ thuật chính và lưu ý triển khai.

---

## 1. OCR (Optical Character Recognition)

* **Pipeline:** Text detection (EAST/CRAFT/DBNet) → Text recognition (CRNN/Transformer-based).
* **Challenges:** tài liệu scan kém, tiếng Việt dấu, layout phức tạp.
* **Tools:** PaddleOCR, Tesseract, TrOCR.

> Tip: Sử dụng augmentation giả lập nhiễu, skew, blur để tăng robust.

---

## 2. Face Recognition & Biometrics

* **Face Detection:** MTCNN, RetinaFace.
* **Face Embedding:** FaceNet, ArcFace, CosFace.
* **Liveness Detection:** texture analysis, depth, challenge-response.

**Privacy:** tuân thủ quy định bảo mật, mã hoá embedding, quản lý consent.

---

## 3. Medical Imaging

* **Modalities:** X-ray, CT, MRI, Ultrasound.
* **Tasks:** classification (Covid detection), segmentation (tumor), detection (lesions).
* **Requirements:** explainability (Grad-CAM), validation bởi bác sĩ, tuân thủ HIPAA.

> Checklist: annotate với chuyên gia, sử dụng data balancing, evaluate sensitivity/specificity.

---

## 4. Retail & Supply Chain

* **Use case:** kiểm tra chất lượng sản phẩm, inventory counting, cashierless checkout.
* **Tech:** object detection (YOLO/Mask R-CNN), tracking (DeepSORT), anomaly detection.
* **Deployment:** Cameras edge devices, latency thấp, multi-camera fusion.

---

## 5. Smart City & Surveillance

* **Traffic monitoring:** vehicle counting, speed estimation.
* **Safety compliance:** PPE detection, intrusion alert.
* **Challenges:** ánh sáng phức tạp, privacy.

> Gợi ý: dùng multi-sensor (camera + radar) để giảm false positive.

---

## 6. Industrial & Manufacturing

* **Fault detection:** surface defect (steel, PCB).
* **Pose estimation:** robot grasping.
* **Predictive maintenance:** thermal imaging.

**Key:** build dataset chất lượng cao, logging event để trace lỗi.

---

## 7. Implementation Checklist

- [ ] Thu thập dữ liệu đại diện đủ các điều kiện thực tế.
- [ ] Label chất lượng (ít bias), versioning bằng DVC/Label Studio.
- [ ] Training pipeline reproducible (MLflow/W&B).
- [ ] Đánh giá theo metric business (precision/recall cost-weighted).
- [ ] Monitor drift, false positive/negative sau deploy.
- **Cross-domain:** [Game Dev AI](../../game-dev/ai/README.md) tổng hợp pattern AI thị giác cho gameplay, NPC perception, camera system — hữu ích khi build CV feature trong game/AR.

> 📌 Tip: Với project regulated (medical/finance), chuẩn bị SOP + audit trail cho toàn bộ pipeline để đáp ứng compliance.
