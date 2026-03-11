---
title: "Shader Graph Capture"
description: "Bắt output Shader Graph thành texture/material reference."
tags:
  - graphics
  - shader-graph
  - tooling
updated: 2026-03-11
---

# 📸 Shader Graph Capture

## 1) Custom Render Texture (CRT)
- Tạo Shader Graph (HDRP/URP) sử dụng target `Custom Render Texture`.
- CRT update mode: OnLoad/Realtime/OnDemand.
- Dùng để bake gradient ramp, LUT, flowmap.

## 2) Capture Script Example

**ShaderGraphCapture.cs**

```csharp
public class ShaderGraphCapture : MonoBehaviour
{
    [SerializeField] CustomRenderTexture customRT;
    [SerializeField] int size = 512;

    [ContextMenu("Capture")]
    public void Capture()
    {
        if (customRT == null)
        {
            Debug.LogError("Assign Custom Render Texture first");
            return;
        }

        customRT.Initialize();
        customRT.Update();

        Texture2D tex = new Texture2D(size, size, TextureFormat.RGBAHalf, false);
        RenderTexture.active = customRT;
        tex.ReadPixels(new Rect(0, 0, size, size), 0, 0);
        tex.Apply();

        string path = Path.Combine(Application.dataPath, "ShaderGraphCapture.png");
        File.WriteAllBytes(path, tex.EncodeToPNG());
        Debug.Log($"Saved capture to {path}");
    }
}
```

- Attach script vào GameObject, assign CRT (driven by Shader Graph material).
- Run `Capture` từ context menu để lưu PNG.

## 3) Camera Capture Variant

```csharp
[ExecuteAlways]
public class MaterialPreviewCapture : MonoBehaviour
{
    [SerializeField] Material targetMaterial;
    [SerializeField] int size = 1024;
    [SerializeField] string fileName = "MaterialPreview.png";

    RenderTexture rt;

    void OnEnable()
    {
        rt = new RenderTexture(size, size, 0, RenderTextureFormat.ARGBHalf);
    }

    [ContextMenu("CaptureMaterial")]
    public void Capture()
    {
        if (targetMaterial == null)
        {
            Debug.LogError("Assign material");
            return;
        }

        Graphics.Blit(null, rt, targetMaterial);
        Texture2D tex = new Texture2D(size, size, TextureFormat.RGBAHalf, false);
        RenderTexture.active = rt;
        tex.ReadPixels(new Rect(0, 0, size, size), 0, 0);
        tex.Apply();

        string path = Path.Combine(Application.dataPath, fileName);
        File.WriteAllBytes(path, tex.EncodeToPNG());
        Debug.Log($"Saved {fileName}");
    }

    void OnDisable()
    {
        rt?.Release();
    }
}
```

- Sử dụng material tạo từ Shader Graph (unlit preview) → capture ra texture.
- Có thể chạy trong editor (ExecuteAlways) để bake atlas.

## 4) Tips
- Bật `sRGB (Color Texture)` đúng theo pipeline để tránh gamma sai.
- Lưu file vào `Assets/Art/Baked` và commit.
- Dùng `AssetPostprocessor` tự động import settings (no compression, clamp wrap).

## ✅ Apply it
- [ ] Thiết lập CRT + Shader Graph để preview effect.
- [ ] Dùng script capture để bake LUT/ramp/flowmap.
- [ ] Lưu asset + versioning (naming `SG_<effect>_capture.png`).
- [ ] Tự động import setting qua AssetPostprocessor.
- [ ] Share capture trong style guide để align art team.