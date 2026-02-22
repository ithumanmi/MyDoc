# 🔥🌊 Mastering Shaders with Trigonometry: Water & Fire

> [← Back to Game Dev Roadmap](../README.md) | [← Back to Advanced Trigonometry](../../guides/01-mental-models/mathematics/advanced-trigonometry.md)
>
> *"Trong thế giới đồ họa, Lượng giác là 'bút vẽ' để tạo ra sự chuyển động vô hình. Mọi ngọn lửa bập bùng hay làn sóng lăn tăn đều bắt nguồn từ những hàm số tuần hoàn."*

Để viết được các Shader (HLSL/GLSL) tạo hiệu ứng nước hoặc lửa, bạn không cần dùng vật lý thực tế. Thay vào đó, bạn dùng lượng giác để **đánh lừa thị giác** bằng sự biến dạng không gian và thời gian.

---

## 1. Nền tảng: Hàm Sóng thời gian (Time-based Waves)

Hầu hết các hiệu ứng động trong Shader đều bắt đầu bằng biến `_Time` kết hợp với `sin` hoặc `cos`.

*   **Công thức cơ bản:** `y = amplitude * sin(time * speed + phase)`
*   **Ứng dụng:** Tạo sự nhấp nhô tuần hoàn cho các đỉnh (Vertex) hoặc thay đổi màu sắc theo thời gian.

---

## 🌊 2. Hiệu ứng Nước (Water Displacement)

Để tạo mặt nước, chúng ta kết hợp nhiều lớp sóng lượng giác để tạo ra sự ngẫu nhiên giả (Pseudo-randomness).

### A. Vertex Displacement (Biến dạng hình học)
Chúng ta thay đổi tọa độ $y$ của các đỉnh trên một mặt phẳng để tạo sóng:
```hlsl
// Một hàm sóng đơn giản trong HLSL
float wave = sin(v.vertex.x * _WaveFrequency + _Time.y * _WaveSpeed) * _WaveAmplitude;
v.vertex.y += wave;
```

### B. UV Distortion (Biến dạng bề mặt)
Thay vì thay đổi hình dạng, ta thay đổi cách "nhìn" vào bức ảnh (Texture) bằng cách bẻ cong tọa độ UV:
```hlsl
float2 uv = i.uv;
uv.x += sin(uv.y * _DistortionFreq + _Time.y) * _DistortionStrength;
float4 col = tex2D(_MainTex, uv);
```
**Kết quả:** Hình ảnh phản chiếu dưới nước trông như đang lung linh.

---

## 🔥 3. Hiệu ứng Lửa (Fire & Plasma)

Lửa phức tạp hơn vì nó không chỉ nhấp nhô mà còn bốc lên và biến dạng theo kiểu "hỗn loạn".

### A. Kết hợp hàm Sin đa hướng
Để tạo ra hình dạng ngọn lửa, chúng ta chồng nhiều hàm $\sin, \cos$ ở các tần số khác nhau:
```hlsl
float fireShape = sin(uv.x * 10.0 + _Time.y * 5.0) * cos(uv.y * 5.0 - _Time.y * 2.0);
```

### B. Noise + Trigonometry (Sự hỗn loạn có trật tự)
Lượng giác tạo ra sự tuần hoàn, nhưng lửa cần sự ngẫu nhiên. Chúng ta dùng **Perlin Noise** làm đầu vào cho các hàm lượng giác:
1.  Lấy giá trị Noise tại tọa độ $(uv.x, uv.y - _Time.y)$.
2.  Dùng giá trị đó làm `phase` cho hàm `sin`.
3.  Kết quả: Một làn khói hoặc lửa bốc lên trông rất tự nhiên.

---

## 🎨 4. Kỹ thuật nâng cao: Fresnel Effect

Hiệu ứng Fresnel xác định độ phản chiếu của mặt nước dựa trên góc nhìn.
*   **Công thức:** $1.0 - \max(0, \vec{v} \cdot \vec{n})$ (Tích vô hướng - liên quan đến $\cos \theta$).
*   **Ứng dụng:** Nhìn thẳng xuống nước thì thấy đáy, nhìn xa thì thấy mặt nước phản chiếu bầu trời.

---

## 🛠️ Code Snippet: Làn sóng nước 2D đơn giản (HLSL)

```hlsl
fixed4 frag (v2f i) : SV_Target
{
    float2 uv = i.uv;
    // Tạo sóng sin kép để mặt nước trông tự nhiên hơn
    float wave = sin(uv.x * 10 + _Time.y * 2) * 0.05;
    wave += cos(uv.x * 15 - _Time.y * 3) * 0.02;
    
    // Nếu tọa độ y nằm dưới đường sóng, tô màu xanh nước biển
    if (uv.y < 0.5 + wave) {
        return fixed4(0, 0.5, 1, 1);
    }
    return fixed4(0, 0, 0, 0); // Trong suốt phía trên
}
```

---

## 🧠 Mental Model: Biến dạng không gian (Space Warping)

Đừng nghĩ về việc "vẽ" nước hay lửa. Hãy nghĩ về việc **"bẻ cong"** không gian bằng lượng giác:
*   **$\sin, \cos$** là những chiếc thước dẻo.
*   **Frequency (Tần số)** quyết định độ nhọn của sóng.
*   **Amplitude (Biên độ)** quyết định độ cao của sóng.
*   **Time** là thứ làm cho không gian "trôi" đi.

---

## 🚀 Thử thách cho bạn

1.  **Level 1:** Viết một shader làm cho một tấm Sprite "vẫy" như một lá cờ bằng hàm `sin`.
2.  **Level 2:** Kết hợp 3 hàm `sin` khác nhau để tạo ra một mặt biển trông bớt "máy móc" hơn.
3.  **Level 3:** Thử dùng hàm `atan2` để tạo ra hiệu ứng xoáy nước (Vortex).

---

## 🔗 Liên kết mở rộng
*   **[Advanced Trigonometry Guide](../../guides/01-mental-models/mathematics/advanced-trigonometry.md):** Hiểu sâu về chuỗi Fourier để kết hợp sóng.
*   **[Shader Programming Concepts](./shader-programming.md):** Nền tảng về Vertex và Fragment Shaders.
