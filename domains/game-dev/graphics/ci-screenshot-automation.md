---
title: "CI Screenshot Automation"
description: "Pipeline chụp screenshot trong CI (Unity + RenderDoc/Graphics Tests)."
tags:
  - graphics
  - ci
  - automation
updated: 2026-03-11
---

# 🤖 CI Screenshot Automation

## 1) Goal
- Chụp screenshot định kỳ từ build CI để so sánh visual regression.
- Kết hợp với RenderDoc hoặc Unity Graphics Test Framework.

## 2) Unity Test Runner + Graphics Tests
- Sử dụng package `com.unity.testframework.graphics`.
- Tạo `GraphicsTestCase` asset (scene reference).
- Test chạy `GraphicsTestCase` → ghi screenshot so sánh với reference.

```csharp
using UnityEngine.TestTools.Graphics;

public class GraphicsRegressionTests : GraphicsTests
{
    [UnityTest]
    public IEnumerator Scene_BossArena_MatchesReference()
    {
        yield return LoadScene("BossArena_GraphicsTest");
        yield return null; // wait one frame
        Assert.IsTrue(CheckSceneAgainstReferenceImage("BossArena"));
    }
}
```

- Reference screenshot lưu tại `Assets/GraphicsTests/ReferenceImages`.
- CI chạy `-runTests -testPlatform PlayMode -graphicsTests` để xuất report.

## 3) Custom Screenshot Command

**CaptureScreenshot.cs**

```csharp
public class CaptureScreenshot : MonoBehaviour
{
    [SerializeField] string output = "Screenshots/shot.png";

    IEnumerator Start()
    {
        yield return new WaitForEndOfFrame();
        ScreenCapture.CaptureScreenshot(output);
        Debug.Log($"Saved screenshot {output}");
#if UNITY_EDITOR
        EditorApplication.Exit(0);
#endif
    }
}
```

- Build dedicated scene (e.g., `SceneScreenshotRunner`) attach script.
- CI chạy headless: `Unity.exe -batchmode -projectPath ... -executeMethod ScreenshotCI.Run` (script load scene, instantiate capture prefab).

## 4) RenderDoc Automation

```bash
renderdoccmd capture --exe "Builds/MyGame.exe" \
  --capture-file "artifacts/renderdoc/frame_ci.rdc" \
  --trigger-delay 10 --controller-port 39999

renderdoccmd export artifacts/renderdoc/frame_ci.rdc \
  --texture 0 --output artifacts/screenshots/frame_ci.png
```

- CI step run build → run capture → export texture.
- Upload PNG vào artifacts (Azure/GitHub Actions pipeline).

## 5) Diff Tool
- Dùng `ImageMagick compare` hoặc `PerceptualDiff` để so sánh screenshot vs baseline.

```bash
magick compare -metric RMSE baseline.png current.png diff.png
```

- Nếu RMSE vượt threshold → fail pipeline.

## ✅ Apply it
- [ ] Thiết lập Graphics Test Framework + reference screenshot.
- [ ] Tạo scene capture script (ScreenCapture/RenderDoc) + batch command.
- [ ] CI pipeline: build → run tests → capture screenshot → upload artifact.
- [ ] Thiết lập diff automation (ImageMagick) để báo regression.
- [ ] Lưu baseline trong repo/remote storage và cập nhật khi art direction thay đổi.