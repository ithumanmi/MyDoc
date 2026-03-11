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

### GPU Compute Shader Example

**NoiseGenerator.compute**

```hlsl
#pragma kernel CSMain

RWTexture2D<float> Result;
int Size;
float Scale;
float2 Offset;

float Noise(float2 uv)
{
    return frac(sin(dot(uv, float2(12.9898, 78.233))) * 43758.5453);
}

[numthreads(8,8,1)]
void CSMain(uint3 id : SV_DispatchThreadID)
{
    if (id.x >= Size || id.y >= Size) return;
    float2 uv = (float2(id.xy) + Offset) / Scale;
    float value = 0;
    float amp = 0.5;
    float freq = 1;
    for (int i = 0; i < 5; i++)
    {
        value += amp * Noise(uv * freq);
        freq *= 2;
        amp *= 0.5;
    }
    Result[id.xy] = value;
}
```

**NoiseComputeDispatcher.cs**

```csharp
public class NoiseComputeDispatcher : MonoBehaviour
{
    [SerializeField] ComputeShader noiseCompute;
    [SerializeField] int size = 512;
    [SerializeField] float scale = 128f;
    [SerializeField] Vector2 offset;

    RenderTexture rt;

    void Start()
    {
        rt = new RenderTexture(size, size, 0, RenderTextureFormat.RFloat)
        {
            enableRandomWrite = true
        };
        rt.Create();

        int kernel = noiseCompute.FindKernel("CSMain");
        noiseCompute.SetTexture(kernel, "Result", rt);
        noiseCompute.SetInt("Size", size);
        noiseCompute.SetFloat("Scale", scale);
        noiseCompute.SetVector("Offset", offset);

        int groups = Mathf.CeilToInt(size / 8f);
        noiseCompute.Dispatch(kernel, groups, groups, 1);

        Texture2D tex = new Texture2D(size, size, TextureFormat.RFloat, false);
        RenderTexture.active = rt;
        tex.ReadPixels(new Rect(0, 0, size, size), 0, 0);
        tex.Apply();

        // Debug: save PNG hoặc assign vào material
        File.WriteAllBytes("Assets/noise.png", tex.EncodeToPNG());
    }
}
```

- Compute shader chạy song song 8×8 threads để tạo heightmap.
- `Noise` function có thể thay bằng Perlin/Simplex HLSL hoặc domain warp GPU.
- Dispatch theo chunk, stream kết quả vào terrain system mà không block main thread.

### GPU Worley Noise Example

**WorleyNoise.compute**

```hlsl
#pragma kernel CSMain

RWTexture2D<float> Result;
StructuredBuffer<float2> FeaturePoints; // precomputed points per chunk
int Size;
int PointCount;

float Distance(float2 a, float2 b)
{
    return length(a - b);
}

[numthreads(8,8,1)]
void CSMain(uint3 id : SV_DispatchThreadID)
{
    if (id.x >= Size || id.y >= Size) return;
    float2 uv = float2(id.xy) / Size;
    float minDist = 9999;
    for (int i = 0; i < PointCount; i++)
    {
        float2 p = FeaturePoints[i];
        float d = Distance(uv, p);
        minDist = min(minDist, d);
    }
    Result[id.xy] = minDist;
}
```

**WorleyComputeDispatcher.cs**

```csharp
public class WorleyComputeDispatcher : MonoBehaviour
{
    [SerializeField] ComputeShader worleyCompute;
    [SerializeField] int size = 256;
    [SerializeField] int pointCount = 32;

    ComputeBuffer featureBuffer;
    RenderTexture rt;

    void Start()
    {
        Vector2[] featurePoints = GeneratePoissonPoints(pointCount);
        featureBuffer = new ComputeBuffer(pointCount, sizeof(float) * 2);
        featureBuffer.SetData(featurePoints);

        rt = new RenderTexture(size, size, 0, RenderTextureFormat.RFloat)
        {
            enableRandomWrite = true
        };
        rt.Create();

        int kernel = worleyCompute.FindKernel("CSMain");
        worleyCompute.SetTexture(kernel, "Result", rt);
        worleyCompute.SetBuffer(kernel, "FeaturePoints", featureBuffer);
        worleyCompute.SetInt("Size", size);
        worleyCompute.SetInt("PointCount", pointCount);

        int groups = Mathf.CeilToInt(size / 8f);
        worleyCompute.Dispatch(kernel, groups, groups, 1);
    }

    Vector2[] GeneratePoissonPoints(int count)
    {
        Vector2[] pts = new Vector2[count];
        for (int i = 0; i < count; i++)
            pts[i] = new Vector2(UnityEngine.Random.value, UnityEngine.Random.value);
        return pts;
    }

    void OnDestroy()
    {
        featureBuffer?.Dispose();
        rt?.Release();
    }
}
```

- Feature points có thể dùng Poisson disk để phân bố đều; truyền vào compute buffer.
- Có thể lưu `Result` thành `RenderTexture` để dùng mask biome hoặc blend texture.
- Kết hợp Perlin + Worley bằng shader graph hoặc compute pass tiếp theo.

## ✅ Apply it
- [ ] Chọn loại noise phù hợp: Perlin (terrain), Simplex (volumetric), Worley (biome/cell).
- [ ] Combine octaves (fBM), ridged, domain warp để tăng chi tiết.
- [ ] Threshold + curve remap để ra mask/heightmap mong muốn.
- [ ] Tối ưu: Jobs/Burst/compute shader khi generate lớn; cache seed.
- [ ] Test visual bằng debug preview (texture) để tune tham số.