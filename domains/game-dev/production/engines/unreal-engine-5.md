# 🎮 Unreal Engine 5: Kỷ nguyên mới của đồ họa (Level 7)

> [← Back to Game Development Roadmap](../README.md)

Unity mạnh về Mobile/Indie. Unreal Engine (UE5) là vua của đồ họa High-end (PC/Console) và điện ảnh.

---

## 1. Nanite (Virtualized Geometry)

Quên đi khái niệm LOD (Level of Detail) và Low-poly.

*   **Vấn đề cũ:** Càng xa camera phải dùng model càng ít lưới (polygon) để đỡ lag.
*   **Nanite:** Bạn có thể ném một bức tượng 30 triệu polygon (nguyên bản từ ZBrush) vào game. UE5 sẽ tự động chia nhỏ và chỉ render những gì pixel hiển thị được.
*   **Kết quả:** Hình ảnh chi tiết điện ảnh với hiệu năng thời gian thực.

---

## 2. Lumen (Global Illumination)

Ánh sáng là linh hồn của đồ họa.

*   **Vấn đề cũ:** Phải "nướng" ánh sáng (Light Baking) vào texture. Rất đẹp nhưng tĩnh (không thay đổi được).
*   **Lumen:** Tính toán ánh sáng phản xạ (Indirect Lighting) thời gian thực.
*   **Ví dụ:** Bạn mở cửa sổ -> Ánh nắng tràn vào phòng, phản xạ lên sàn gỗ, hắt màu lên tường -> Tất cả thay đổi ngay lập tức. Không cần Bake lại.

---

## 3. Blueprints (Visual Scripting)

Bạn không cần biết C++ để làm game bằng Unreal.

*   **Node-based:** Kéo thả các node logic (If, For Loop, Spawn Actor) và nối dây.
*   **Mạnh mẽ:** Có thể làm trọn vẹn một game phức tạp chỉ bằng Blueprint.
*   **C++ & Blueprint:** Các studio lớn thường dùng C++ cho core system (hiệu năng cao) và Blueprint cho gameplay (để Designer dễ chỉnh sửa).

---

## 4. MetaHuman Creator

Tạo nhân vật con người siêu thực chỉ trong vài phút.
*   Chỉnh sửa khuôn mặt, da, tóc chi tiết như thật.
*   Tích hợp sẵn khung xương (Rig) để làm animation.
