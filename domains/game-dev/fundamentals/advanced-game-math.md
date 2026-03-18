# Advanced Game Math: Giải Ngố Toán Học Trong Game

> [← Back to Fundamentals](../README.md) | [Home](../../../README.md)

Lập trình viên Game có một "Biên giới Vô Hình". Phía bên này là những Junior Dev chỉ biết gọi hàm `transform.Translate()` và Google lệnh xoay hướng. Phía bên kia là Technical/Senior Dev tự code shader nước, tính điểm rơi đường đạn đạn và bắt ma sát lốp xe đua. Biên giới đó gọi là **Toán Học Không Gian (Vector & Trigonometry)**.

Bài viết này "bình dân hóa" những khái niệm toán học khô khan nhất thành vũ khí thực chiến.

---

## 📐 1. Vector: Dot Product & Cross Product (Vũ khí tối thượng)

Bạn nghĩ Vector chỉ là hướng `(X, Y, Z)`? Nó là cốt lõi của mọi Combat system.

### Dot Product (Tích vô hướng)
Hàm huyền thoại: `Vector3.Dot(A, B)` trả về một Tỉ lệ Vô Hướng (Một con số đơn thuần từ -1 đến 1).
*   **Ý Nghĩa:** Nó độ xem 2 vector đang "cùng hướng" nhau tới mức nào.
    *   Cắt nhau tạo góc nhọn (cùng nhìn 1 phía): Số Dương (> 0)
    *   Vuông góc 90 độ: Bằng 0.
    *   Quay đít vào nhau (góc tù): Số Âm (< 0)

*   **⚡ Ứng Dụng Thực Chiến (Tính Tầm Nhìn Chiến Thuật):**
    Làm sao AI biết Player đang rình ở SAU LƯNG hay TRƯỚC MẶT nó? Đỉnh cao là không cần tính Góc độ phức tạp. 
    Lấy Vector Hướng Mặt Của AI (`transform.forward`) Dot với Vector Chỉ Từ AI tới Player (`Player.position - AI.position`). 
    **Nếu Dot < 0 --> Tức là Player đứng khuất sau lưng. Đừng báo động!**

### Cross Product (Tích có hướng)
Hàm: `Vector3.Cross(A, B)` trả về 1 VECTOR THỨ 3, vuông góc chặt đứt cả A lẫn B.
*   **⚡ Ứng Dụng Thực Chiến (Đụng Độ & Lái Tàu):**
    Chiếc bè đang chạy thẳng (Vector A). Gió thổi từ bên hông phải (Vector B).
    Muốn bánh lái quay về hướng nào để con tàu chống lại gió lật? Dùng Cross(A, B) sẽ ra luôn cái Đòn Bẩy mô-men xoắn của bánh lái 3D. 
    Trong Mario Kart, khi xe đụng tường, Cross Product quyết định mũi xe sẽ tượt nảy sang góc chéo nào.

---

## 🔄 2. Quaternions: Nỗi Sợ Hãi Cấm Kỵ (Xoay 3D)

Ở Inspector Unity, Rotate là `(X=90, Y=0, Z=0)`. Đó là **Euler Angles** (Gắn liền con người hiểu).
Vào trong Code cùa Unity hay Unreal, xoay được lưu trong `Quaternion(X, Y, Z, W)`. Đứa nào can thiệp thay x,y,z,w trực tiếp bằng tay thì Game crash/vặn vẹo quái thai lập tức.

### Tại sao CÓ Quaternions Sinh Ra?
Bởi vì Gimbal Lock. Nếu bạn xoay Euler, hãy thử tưởng tượng trục X xoay lên lồng 90 độ vào trục Z. Hai trục dính lại làm 1. Game mất hẳn một chiều không gian xoay (Trục Z và Y giờ xoay như nhau). Camera quay hất lên Trời bị Kẹt cứng.
Quaternions (4 chiều) né Gimbal Lock hoàn hảo bằng số Yêu Tinh.

### ⚡ Khẩu Quyết Xài Quaternions Không Cần Hiểu Cơ Chế Toán:
Đừng bao giờ `transform.rotation.z += 10`.
1.  **Nhìn về hướng ai đó ngay lập tức:** (Thích hợp cho Trụ bắn súng, Tên lửa dò đường)
    `transform.rotation = Quaternion.LookRotation(Dich.transform.position - KyNu.transform.position)`
2.  **Xoay một góc tương đối (Quay chong chóng rỉ rỉ):** Đem Quaternion nhân (Tích) Quaternion. Dấu nhân `*` ở Quaternion trong Unity nghĩa là "Cộng thêm lực xoay".
    `transform.rotation *= Quaternion.Euler(0, 50 * Time.deltaTime, 0)` -> Xoay trơn trục Y 50 độ/giây.
3.  **Xoay lia mượt mà (Dành cho Camera xoay lướt ngắm):** Dùng `Quaternion.Slerp(HienTai, MucTieu, TocDo)`. Nó sẽ cong góc quay thay vì lia cái giật thót.

---

## 🌊 3. Lượng Giác Học (Trigonometry): Nhịp Đập Sự Sống

Sin và Cos. Nếu bạn từng chê Toán cấp 3, giờ là lúc ân hận. Sin(Thời gian) sinh ra đồ thị hình Cơn Sóng uốn lượn liên tục từ -1 tới 1 và ngược lại theo mãi mãi.

### ⚡ Cày Đi Cày Lại Mọi Hiệu Ứng Bằng Sin()
*   **Vật Phẩm Lơ Lửng Rơi Chậm (Floating Idle):** Thay vì dùng Physics/Rigidbody làm nặng máy, chỉ cần đặt ở `Update()`: 
    ```csharp
    transform.position = new Vector3(X_Goc, Y_Goc + Mathf.Sin(Time.time * TocDo) * BienDo, Z_Goc);
    ```
    Quả bóng bay sẽ lắc nhẹ bay lên rớt xuống mượt như lụa vĩnh viễn. Không tốn % CPU vật lý nào.
*   **Shader Nước và Gió:** Sóng biển uốn vòm đập vào bờ, lá cây đung đưa trên cành? Đem Sin() ném vào Shader Graph tác động vào Y Position (Height Map).
*   **Làm Screen Shake Chuyên Nghiệp:** Nhân 2 sóng Sin biên độ khác nhau lồng ghép -> Tạo ra đường đi zíc zắc hỗn loạn làm camera rung rẩy như động đất.

> 🛠️ **Tầm Niệm Vững Nhất của Kỹ Sư Gameplay**: Mọi chuyển động trong game nên được giải bằng "Công thức Toán Cố Định (Math/Vector/Sin)" trước. Khi nào Bí Đường mới kéo cục Vật Lý Nặng Nề của Engine (`Rigidbody, BoxCollider`) vào xài để giữ Performance cho con game 60FPS.
