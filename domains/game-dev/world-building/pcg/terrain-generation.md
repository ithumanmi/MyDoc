---
title: "Terrain Generation"
description: "Heightmap, erosion, biome layering cho thế giới mở."
tags:
  - pcg
  - terrain
  - unity
updated: 2026-03-11
---

# 🏞️ Terrain Generation

## 1) Heightmap Basics
- Heightmap = texture grayscale (0–1). Dùng noise (Perlin, Simplex) + ridge noise.
- Multi-octave + domain warp cho chi tiết.
- Mask biomes theo noise (heat + moisture) → blend height profile.
- Lưu heightmap raw (float array) để feed vào mesh/terrain system.

## 2) Erosion Models
- **Thermal erosion:** slope vượt angle → vật liệu chảy xuống. Thực hiện iteration update height.
- **Hydraulic erosion:** mô phỏng nước chảy mang sediment.
  - Raindrop: thả giọt nước, update velocity, sediment capacity, deposit khi chậm.
  - River: trace flow map theo gradient, accumulate water, carve channel.
- Erosion giúp terrain tự nhiên (river/valley). Tốn CPU → nên precompute hoặc GPU compute.

### GPU Hydraulic Erosion Example

**HydraulicErosion.compute**

```hlsl
#pragma kernel Simulate

RWTexture2D<float> HeightMap;
RWTexture2D<float> SedimentMap;
int Size;
float DeltaTime;
float Evaporation = 0.02;
float SedimentCapacity = 1.5;

float SampleHeight(int2 coord)
{
    coord = clamp(coord, 0, Size - 1);
    return HeightMap[coord];
}

[numthreads(8,8,1)]
void Simulate(uint3 id : SV_DispatchThreadID)
{
    if (id.x >= Size || id.y >= Size) return;
    int2 coord = int2(id.xy);
    float height = HeightMap[coord];

    float2 gradient = float2(
        SampleHeight(coord + int2(1,0)) - SampleHeight(coord - int2(1,0)),
        SampleHeight(coord + int2(0,1)) - SampleHeight(coord - int2(0,1))
    );

    float flow = length(gradient);
    float capacity = flow * SedimentCapacity;
    float currentSediment = SedimentMap[coord];

    if (currentSediment > capacity)
    {
        float deposit = (currentSediment - capacity) * DeltaTime;
        HeightMap[coord] += deposit;
        SedimentMap[coord] -= deposit;
    }
    else
    {
        float erode = min((capacity - currentSediment) * DeltaTime, 0.01);
        HeightMap[coord] -= erode;
        SedimentMap[coord] += erode;
    }

    SedimentMap[coord] *= (1.0 - Evaporation * DeltaTime);
}
```

**HydraulicErosionDispatcher.cs**

```csharp
public class HydraulicErosionDispatcher : MonoBehaviour
{
    [SerializeField] ComputeShader erosionCompute;
    [SerializeField] int size = 512;
    [SerializeField] int iterations = 200;
    [SerializeField] float deltaTime = 0.02f;

    RenderTexture heightRT;
    RenderTexture sedimentRT;

    void Start()
    {
        heightRT = CreateRT();
        sedimentRT = CreateRT();

        int kernel = erosionCompute.FindKernel("Simulate");
        erosionCompute.SetTexture(kernel, "HeightMap", heightRT);
        erosionCompute.SetTexture(kernel, "SedimentMap", sedimentRT);
        erosionCompute.SetInt("Size", size);
        erosionCompute.SetFloat("DeltaTime", deltaTime);

        int groups = Mathf.CeilToInt(size / 8f);
        for (int i = 0; i < iterations; i++)
        {
            erosionCompute.Dispatch(kernel, groups, groups, 1);
        }

        // Copy result về CPU hoặc feed trực tiếp cho terrain shader
        Texture2D heightTex = CopyToTexture(heightRT);
        File.WriteAllBytes("Assets/height_erosion.png", heightTex.EncodeToPNG());
    }

    RenderTexture CreateRT()
    {
        var rt = new RenderTexture(size, size, 0, RenderTextureFormat.RFloat)
        {
            enableRandomWrite = true
        };
        rt.Create();
        return rt;
    }

    Texture2D CopyToTexture(RenderTexture rt)
    {
        var tex = new Texture2D(size, size, TextureFormat.RFloat, false);
        RenderTexture.active = rt;
        tex.ReadPixels(new Rect(0, 0, size, size), 0, 0);
        tex.Apply();
        return tex;
    }
}
```

- Compute shader chạy nhiều iteration để mô phỏng deposit/erosion theo gradient.
- Có thể mở rộng thêm velocity map, water map (height + water) để mô phỏng droplet.
- Dispatch chunk-based, apply erosion offline hoặc runtime tùy yêu cầu.

## 3) Biome Layering
- Input maps: height, temperature, moisture.
- Phân zone (snow, desert, forest) dựa threshold.
- Blend terrain splat/texture per biome (Unity Terrain: SplatMap). Sử dụng noise để soften border.
- Spawn vegetation/lake/props theo biome rules.

## 4) Chunking & Streaming
- Chia thế giới thành chunk (256x256) -> generate lazily khi camera gần.
- Sử dụng seed + chunk coordinate (x,z) để deterministic.
- Cache heightmap + mesh; unload khi xa.
- Burst/Jobs hoặc compute shader để generate chunk parallel.

## 5) Unity Implementation Tips
- Unity Terrain API: `TerrainData.SetHeights`, `SetAlphamaps` cho texture.
- Custom mesh: build grid mesh, sample heightmap array.
- GPU-based: compute shader cho noise + erosion, copy result vào RenderTexture → Texture2D.
- Editor tool: create ScriptableObject profile (seed, octave, erosion iterations) để share giữa designer.

## ✅ Apply it
- [ ] Generate heightmap base (noise + domain warp) theo seed.
- [ ] Áp erosion (thermal/hydraulic) nếu cần realism.
- [ ] Map biome (height/temp/moisture) và blend texture/props tương ứng.
- [ ] Chunk-based streaming; deterministic theo chunk coordinate.
- [ ] Tối ưu bằng Jobs/compute shader, expose profile cho designer.