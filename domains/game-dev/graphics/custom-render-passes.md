---
title: "Custom Render Passes"
description: "Tùy biến SRP (URP/HDRP), ScriptableRenderPass/RendererFeature."
tags:
  - graphics
  - render-pipeline
  - unity
updated: 2026-03-11
---

# 🧱 Custom Render Passes

## 1) URP ScriptableRendererFeature
- Tạo class kế thừa `ScriptableRendererFeature` + `ScriptableRenderPass`.
- Override `AddRenderPasses` để enqueue pass đúng injection point (BeforeRendering, AfterRenderingTransparents, etc.).
- Pass cấu hình render target, shader tag, filter settings.

### Sample (Fullscreen Effect)

```csharp
public class OutlineFeature : ScriptableRendererFeature
{
    class OutlinePass : ScriptableRenderPass
    {
        Material mat;
        RenderTargetIdentifier source;
        RenderTargetHandle temp;

        public OutlinePass(Material material)
        {
            mat = material;
            temp.Init("_OutlineTemp");
        }

        public override void Execute(ScriptableRenderContext context, ref RenderingData data)
        {
            CommandBuffer cmd = CommandBufferPool.Get("OutlinePass");
            RenderTextureDescriptor desc = data.cameraData.cameraTargetDescriptor;
            cmd.GetTemporaryRT(temp.id, desc);
            Blit(cmd, source, temp.Identifier());
            Blit(cmd, temp.Identifier(), source, mat);
            context.ExecuteCommandBuffer(cmd);
            CommandBufferPool.Release(cmd);
        }

        public void Setup(RenderTargetIdentifier src) => source = src;
    }

    OutlinePass pass;

    public override void Create()
    {
        pass = new OutlinePass(Resources.Load<Material>("Outline"))
        {
            renderPassEvent = RenderPassEvent.AfterRenderingTransparents
        };
    }

    public override void AddRenderPasses(ScriptableRenderer renderer, ref RenderingData data)
    {
        pass.Setup(renderer.cameraColorTarget);
        renderer.EnqueuePass(pass);
    }
}
```

- Attach Feature vào URP Renderer Asset để kích hoạt.
- Dùng cho fullscreen effect, mask, decal, custom depth copy.

## 2) HDRP Custom Pass
- Sử dụng `CustomPassVolume` → add pass (Fullscreen/DrawRenderers/Custom Buffer).
- CustomPass script override `Execute(CustomPassContext ctx)`.
- Có thể access camera depth, normal, custom buffers.

### Sample (Depth Preprocess)

```csharp
[CustomPassInjectionPoint(CustomPassInjectionPoint.BeforeOpaque)]
public class DepthCopyPass : CustomPass
{
    protected override void Execute(CustomPassContext ctx)
    {
        var cmd = ctx.cmd;
        cmd.CopyTexture(ctx.cameraDepthBuffer, Shader.PropertyToID("_SceneDepth"));
    }
}
```

- Attach vào Custom Pass Volume (Global/Local). Dùng cho custom DOF, SSR replacement.

## 3) Debug & Profiling
- `RenderDoc`/`Frame Debugger` để xem pass order.
- Gắn `ProfilingScope` cho mỗi pass.
- Theo dõi render target lifetime, tránh allocate RT mỗi frame.

## 4) Use Cases
- Outline, toon shading post-process.
- Decal projector custom, selective blur.
- Render minimap camera, planar reflection, portal view.
- Copy depth/normal cho effect (fog, stylized).

## ✅ Apply it
- [ ] Chọn injection point phù hợp (Before/After Rendering).
- [ ] Tái sử dụng render texture để tránh leak.
- [ ] Gắn profiling scope + frame debugger validation.
- [ ] Đóng gói feature thành asset (RendererFeature/CustomPassVolume) để share team.
- [ ] Document parameter (material, layer masks) trong repo.