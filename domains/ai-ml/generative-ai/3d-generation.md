# 🧱 Text-to-3D & Gaussian Splatting

> [← Back to Generative AI](./README.md)

Generative 3D bùng nổ với các phương pháp Text-to-3D (DreamFusion, Magic3D), Gaussian Splatting và NeRF, mở đường cho game, AR/VR, product design.

---

## 1. Landscape

| Công cụ | Loại | Mô tả |
| --- | --- | --- |
| **DreamFusion / Magic3D** | Text-to-3D | Optimize latent NeRF từ text prompt, tạo mesh + texture. |
| **Shap-E / Point-E** | Text-to-PointCloud/Mesh | Fast sampling, phù hợp prototype đơn giản. |
| **Gaussian Splatting** | Novel View Synthesis | Reconstruct cảnh từ ảnh/video, render realtime. |
| **3D Gaussian Splatting in ComfyUI** | OSS workflow | Pipeline kết hợp COLMAP + training + viewer. |

---

## 2. Text-to-3D Workflow

1. **Prompt:** mô tả object + style + camera.
2. **Optimize:** chạy pipeline (DreamFusion, Magic3D, Shap-E) → tạo NeRF/mesh.
3. **Cleanup:** dùng Blender/ZBrush để retopo, UV unwrap.
4. **Texture & Rig:** bake texture map, rig skeleton nếu cần animation.
5. **Export:** glTF/FBX/OBJ vào game engine (Unity/Unreal).

---

## 3. Gaussian Splatting Pipeline

1. **Capture:** quay video quanh object (đảm bảo overlap cao) hoặc chụp 100+ ảnh.
2. **COLMAP:** reconstruct camera poses + sparse point cloud.
3. **Train:** chạy Gaussian Splatting trainer (~minutes trên GPU) để tối ưu blob.
4. **Viewer:** render realtime qua web viewer (three.js) hoặc integrate vào AR.

```bash
# ví dụ chạy gaussian-splatting repo
python train.py -s data/captured_scene -m outputs/scene --iterations 30_000
python render.py -m outputs/scene --video
```

---

## 4. Stack Gợi ý

- **Text-to-3D:** Fantasia3D, TripoSR, Luma Dream Machine.
- **Reconstruction:** COLMAP, Nerfstudio, Gaussian Splatting repo (Inria).
- **Editing:** Blender, Substance Painter, MeshLab.
- **Deployment:** WebGL (Babylon.js), USDZ/GLB cho AR Quick Look.

---

## 5. Tips & Use Cases

- **Game assets:** tạo NPC/props nhanh, sau đó retopo để tối ưu polygon.
- **Product visualization:** convert 2D concept thành prototyping 3D.
- **AR Commerce:** scan sản phẩm thực tế bằng Gaussian Splatting, publish lên web.
- Đảm bảo bản quyền (scan vật thể thật → có permission?).

> 🎯 Lab: capture món đồ tại nhà → Gaussian Splatting → publish viewer web (three.js) để xoay 360°.
