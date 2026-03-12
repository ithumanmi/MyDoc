## 🧊 3D Vision & Neural Rendering

> [← Back to Computer Vision](./README.md)

Các kỹ thuật ước lượng chiều sâu, tái dựng cảnh 3D và Neural Radiance Fields (NeRF) đang mở ra ứng dụng AR/VR, robotics, digital twin.

---

## 1. Depth Estimation

| Phương pháp | Mô tả | Ứng dụng |
| --- | --- | --- |
| **Stereo Matching** | So khớp hai ảnh trái-phải để tính disparity | Robotics, autonomous driving |
| **Monocular Depth (DenseDepth, MiDaS)** | Dự đoán depth từ ảnh đơn nhờ learning | AR, hậu kỳ phim |
| **LiDAR Fusion** | Kết hợp camera + point cloud | Ứng dụng cần độ chính xác cao |

**Loss:** Scale-invariant loss, ordinal regression (DORN).

---

## 2. Point Cloud & Mesh

1. **PointNet/PointNet++:** trực tiếp học trên point cloud.
2. **Graph neural network:** model neighbor relationships.
3. **Poisson Reconstruction / Marching Cubes:** Từ point cloud → mesh.

> Tools: Open3D, PyTorch3D cho xử lý point cloud/mesh.

---

## 3. Neural Radiance Fields (NeRF)

* **Ý tưởng:** Dùng MLP học hàm ánh sáng f(x, d) → density + color.
* **Training:** Lấy nhiều ảnh cùng cảnh, optimize via volume rendering.
* **Extensions:** Instant-NGP (hash encoding, train <1 phút), NeRF in the Wild, Gaussian Splatting.

### Gaussian Splatting
* Thay NeRF bằng tập Gaussian 3D + rasterization nhanh.
* Tốc độ render realtime, phù hợp XR/Metaverse.

---

## 4. Ứng dụng thực tế

1. **AR/VR Content:** Quét cảnh thành assets 3D.
2. **Robotics/Autonomous:** Perception 3D cho navigation.
3. **Digital Twin:** Tái dựng nhà máy, công trình kiến trúc.
4. **Medical Imaging:** 3D reconstruction từ CT/MRI.

---

## 5. Workflow gợi ý

- [ ] Capture multi-view với calibration tốt.
- [ ] Chọn pipeline: COLMAP → NeRF/Gaussian Splatting.
- [ ] Optimize + kiểm tra PSNR/SSIM.
- [ ] Export mesh/point cloud cho Unity/Unreal.
- [ ] Deploy viewer WebGL/WebGPU cho client.

> 🎯 Tip: Instant-NGP + Gaussian Splatting cho tốc độ cao; kết hợp NeRF với depth supervision giúp hội tụ nhanh và chính xác hơn.
