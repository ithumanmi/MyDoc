---
title: "Noise Algorithms"
description: "Perlin, Simplex, Worley noise deep dive cho PCG map, terrain, texture."
tags:
  - pcg
  - noise
  - unity
updated: 2026-03-11
---

# 🌫️ Noise Algorithms

## 1) Perlin Noise
- Gradient noise; smooth, periodic.
- 2D/3D dùng sum octave (fractal Brownian Motion – fBM): `sum(amplitude * noise(freq * pos))`.
- Parameters:
  - Frequency (scale): ảnh hưởng kích thước đặc trưng.
  - Octaves: số layer; mỗi octave freq ×2, amplitude ×0.5.
  - Lacunarity: tỷ lệ freq giữa octaves; Gain: giảm amplitude.
- Ridged noise: lấy `1 - abs(noise)` để tạo núi nhọn.
- Tiling: dùng Perlin tiled hoặc sample 4 điểm và blend.

## 2) Simplex Noise
- Nhiều chiều hơn, ít artifact, nhanh hơn Perlin 3D/4D.
- Dùng simplex grid (tetrahedron) → ít gradient cần tính.
- Họa tiết mềm, dùng cho cloud, volumetric, texture procedural.
- Unity không built-in; dùng lib (OpenSimplex). Chú ý license (public domain, MIT).

## 3) Worley (Voronoi) Noise
- Cellular noise: tính khoảng cách đến điểm đặc trưng (feature points).
- `F1`, `F2` = khoảng cách nhỏ nhất, lớn thứ hai; mix để tạo cell/biome/pattern.
- Use cases: cracked earth, biome partition (closest site), city block layout.
- Combine với Perlin để tạo “Perlin-Worley” (detail + cell).

## 4) Noise Compositing
- **Domain Warp:** dùng noise khác để offset UV (warp pos) → detail tự nhiên.
- **Thresholding:** áp dụng `noise > t` → binary mask (land/water). Có thể blur để tránh jagged.
- **Curve remap:** dùng AnimationCurve để điều khiển phân phối (ví dụ plateau vs valley).
- **Multi-channel:** noise cho height, moisture, heat → map biome.

## 5) Unity Implementation Tips
- `Mathf.PerlinNoise` 2D only → bọc function 3D bằng extension (vec3). Hoặc GPU noise (compute shader) cho chunk lớn.
- Burst/Jobs: schedule noise calc chunk-based để generate terrain runtime.
- Cache seed & offset; expose parameters cho designer.
- Deterministic: seed-based random cho feature point (Worley).

### Sample C# (fBM + Domain Warp)

```csharp
public static float FBM(Vector2 uv, int octaves, float lacunarity, float gain)
{
    float amplitude = 0.5f;
    float frequency = 1f;
    float sum = 0f;
    for (int i = 0; i < octaves; i++)
    {
        sum += amplitude * Mathf.PerlinNoise(uv.x * frequency, uv.y * frequency);
        frequency *= lacunarity;
        amplitude *= gain;
    }
    return sum;
}

public static float DomainWarped(Vector2 uv, float warpStrength)
{
    Vector2 warp = new Vector2(
        Mathf.PerlinNoise(uv.x + 37.2f, uv.y + 11.5f),
        Mathf.PerlinNoise(uv.x - 19.7f, uv.y - 8.3f));
    uv += (warp * 2f - Vector2.one) * warpStrength;
    return FBM(uv, 5, 2f, 0.5f);
}

public static Texture2D GenerateNoiseTexture(int size, float scale)
{
    Texture2D tex = new Texture2D(size, size, TextureFormat.RFloat, false);
    for (int y = 0; y < size; y++)
    {
        for (int x = 0; x < size; x++)
        {
            Vector2 uv = new Vector2(x, y) / scale;
            float value = DomainWarped(uv, 0.25f);
            tex.SetPixel(x, y, new Color(value, value, value));
        }
    }
    tex.Apply();
    return tex;
}
```

- `FBM` gộp nhiều octave Perlin.
- `DomainWarped` offset UV bằng noise khác để tạo detail hữu cơ.
- `GenerateNoiseTexture` dùng preview trong editor để tune tham số.
- Có thể convert sang Burst Job để generate chunk song song.

## ✅ Apply it
- [ ] Chọn loại noise phù hợp: Perlin (terrain), Simplex (volumetric), Worley (biome/cell).
- [ ] Combine octaves (fBM), ridged, domain warp để tăng chi tiết.
- [ ] Threshold + curve remap để ra mask/heightmap mong muốn.
- [ ] Tối ưu: Jobs/Burst/compute shader khi generate lớn; cache seed.
- [ ] Test visual bằng debug preview (texture) để tune tham số.