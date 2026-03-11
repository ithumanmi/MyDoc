---
title: "Audio Middleware (Unity)"
description: "FMOD vs Wwise vs Unity built-in: tiêu chí chọn, tích hợp, build pipeline."
tags:
  - audio
  - middleware
  - unity
updated: 2026-03-11
---

# 🧩 Audio Middleware (Unity)

## 1) Khi nào dùng middleware?
- Cần authoring tool mạnh (RTPC, snapshot, mixer nâng cao, timeline music) và workflow cho sound designer không phụ thuộc lập trình.
- Yêu cầu platform đặc thù (switching bank, memory tuning sâu) hoặc profiling audio chi tiết.
- Cần live-update (connect) để chỉnh âm trong runtime mà không rebuild.

## 2) So sánh nhanh
- **Unity built-in:** miễn phí, đơn giản; hạn chế RTPC phức tạp và bank streaming; profiling vừa phải.
- **FMOD:** workflow thân thiện, RTPC/event mạnh, Live Update; license theo doanh thu, plugin Unity dễ; bank nhẹ.
- **Wwise:** mạnh về profiling/memory, HDR audio, authoring lớn; license tiered; tích hợp cần setup chi tiết.

## 3) Tích hợp Unity
- Version: khóa phiên bản plugin theo Unity version; kiểm tra IL2CPP hỗ trợ.
- Platform: bật platform bank (Android/iOS/Windows/PS/Xbox/Switch); add to Addressables/StreamingAssets.
- Events: map gameplay event → audio event (C#) qua wrapper; tránh gọi event mỗi frame, chỉ khi state đổi.
- RTPC/Parameters: expose gameplay state (intensity/health/speed) sang middleware RTPC; clamp và debounce.

### Ví dụ C# (RTPC wrapper tối giản)
```csharp
using UnityEngine;
using UnityEngine.Audio;

[CreateAssetMenu(menuName = "Audio/RTPCParam")]
public class RtpcParam : ScriptableObject
{
    public string exposedParam; // tên Exposed Parameter trong AudioMixer
    [Range(-80f, 20f)] public float minDb = -30f;
    [Range(-80f, 20f)] public float maxDb = 0f;

    public void Set(AudioMixer mixer, float t01)
    {
        float v = Mathf.Lerp(minDb, maxDb, Mathf.Clamp01(t01));
        mixer.SetFloat(exposedParam, v);
    }
}

public class RtpcDriver : MonoBehaviour
{
    public AudioMixer mixer;
    public RtpcParam intensityParam;
    public Transform player;
    public Transform boss;
    public float maxDistance = 30f;

    void Update()
    {
        float d = Mathf.Clamp01(Vector3.Distance(player.position, boss.position) / maxDistance);
        // intensity tăng khi gần boss → tăng volume bus combat
        intensityParam.Set(mixer, 1f - d);
    }
}
```

## 4) Build & Deployment
- Bank/Assets: đặt trong StreamingAssets hoặc Addressables; bật Load on Demand; strip unused platforms.
- CI: step build bank trước build player; validate bank version và GUID sync với project.
- Size: nén Vorbis/ADPCM per platform; split SFX/VO/Music bank.

## 5) Profiling & Debug
- Dùng Profiler của middleware (Live Update/Profiler) trên device thật; log voice count, CPU, memory.
- Kiểm tra voice stealing rules; cap voice per bus.
- Log event fail/stop reason để debug (invalid path, bank chưa load).

### Ví dụ C# (Addressables load bank/clip rồi play)
```csharp
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;

public class AudioBankLoader : MonoBehaviour
{
    public AssetReferenceT<AudioClip> musicClipRef;   // Addressables entry (Music/MainTheme)
    public AssetReference bankRef;                    // Nếu dùng middleware bank đặt trong Addressables
    public AudioSource musicSource;

    AsyncOperationHandle<AudioClip> _clipHandle;
    AsyncOperationHandle _bankHandle;

    async void Start()
    {
        // Load bank nếu có (FMOD/Wwise bank được pack vào Addressables/StreamingAssets)
        if (bankRef.RuntimeKeyIsValid())
        {
            _bankHandle = bankRef.LoadAssetAsync<object>();
            await _bankHandle.Task;
        }

        // Load clip bằng Addressables
        _clipHandle = musicClipRef.LoadAssetAsync<AudioClip>();
        var clip = await _clipHandle.Task;

        musicSource.clip = clip;
        musicSource.loop = true;
        musicSource.Play();
    }

    void OnDestroy()
    {
        if (_clipHandle.IsValid()) Addressables.Release(_clipHandle);
        if (_bankHandle.IsValid()) Addressables.Release(_bankHandle);
    }
}
```

### Ví dụ C# (Addressables VO/SFX theo locale + preload theo scene)
```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;

public class LocaleAudioPreloader : MonoBehaviour
{
    public string localeCode = "en";   // ví dụ lấy từ LocalizationSettings.SelectedLocale.Identifier.Code
    public string sceneKey = "level1"; // đặt label cho scene

    readonly List<AsyncOperationHandle> _handles = new();

    async void Start()
    {
        // Preload VO theo locale: label ví dụ "vo_en"
        string voLabel = $"vo_{localeCode}";
        var voHandle = Addressables.LoadAssetsAsync<AudioClip>(voLabel, null);
        _handles.Add(voHandle);
        await voHandle.Task;

        // Preload SFX theo scene: label ví dụ "sfx_level1"
        string sfxLabel = $"sfx_{sceneKey}";
        var sfxHandle = Addressables.LoadAssetsAsync<AudioClip>(sfxLabel, null);
        _handles.Add(sfxHandle);
        await sfxHandle.Task;

        // (Tùy chọn) preload bank per locale nếu dùng middleware
        // var bankHandle = Addressables.LoadAssetAsync<object>($"bank_{localeCode}");
        // _handles.Add(bankHandle);
        // await bankHandle.Task;
    }

    void OnDestroy()
    {
        foreach (var h in _handles)
        {
            if (h.IsValid()) Addressables.Release(h);
        }
    }
}
```

## 6) TRC/TCR & Compliance
- Tôn trọng mute system, party chat ducking nếu platform yêu cầu.
- Save/resume: đảm bảo re-init audio system khi suspend/resume.
- Rating: lọc tiếng chửi/UGC nếu có; route qua VO/Chat bus để mute theo parental control.

## ✅ Apply it
- [ ] Quyết định pipeline: built-in vs FMOD vs Wwise dựa trên scope/nhu cầu.
- [ ] Thiết lập bank build step trong CI và Addressables/StreamingAssets.
- [ ] Map gameplay event → audio event, và RTPC từ state/intensity.
- [ ] Voice cap/stealing rule, bank load/unload chiến lược.
- [ ] Test Live Update/Profiler trên device thật, và suspend/resume.