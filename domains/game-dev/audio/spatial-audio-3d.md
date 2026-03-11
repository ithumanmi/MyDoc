---
title: "Spatial Audio 3D (Unity)"
description: "HRTF, occlusion/obstruction, reverb zones, downmix kiểm tra stereo/mono trong Unity."
tags:
  - audio
  - spatial
  - unity
updated: 2026-03-11
---

# 🧠 Spatial Audio 3D (Unity)

## 1) Mục tiêu
- Định vị âm thanh rõ, depth và front/back chính xác; tương thích headphone và loa.
- Kiểm soát occlusion/obstruction, reverb phù hợp môi trường.
- Giữ hiệu năng CPU hợp lý với voice limit.

## 2) HRTF / Panner
- Unity built-in: 3D panner + Spread; kiểm tra trên headphone và stereo speaker.
- HRTF: dùng plugin (Oculus/Steam Audio, Resonance Audio); bật binaural cho source cần chính xác (footstep, projectile).
- Downmix: kiểm tra stereo/mono; đừng rely vào binaural cho loa ngoài → fallback to stereo panning.

### Ví dụ setup HRTF plugin (Steam Audio hoặc Resonance Audio)
- Cài plugin: import package (Steam Audio/Resonance) cho Unity version tương thích.
- Project Settings → Audio: đặt Spatializer Plugin = Steam Audio (hoặc Resonance); Ambisonic Decoder nếu dùng Ambisonic.
- Trên AudioSource: bật Spatialize, Spatial Blend = 1 (3D), chọn HRTF quality trong plugin settings nếu có.
- Occlusion/Reflections: với Steam Audio, add Steam Audio Source component; bật Occlusion, chọn simulation type (raycast/partial/full); bake nếu dùng pathing. Với Resonance, bật Occlusion, set material.
- Kiểm thử headphone vs loa: đảm bảo fallback stereo hợp lý (disable binaural khi output device là loa nếu cần script detect).

## 3) Occlusion & Obstruction
- Raycast/Physics check để đặt LPF/volume reduction; update khi listener/source di chuyển.
- Per-material: map vật liệu → mức LPF/attenuation khác nhau.
- Đừng bật occlusion cho mọi source; chỉ critical (VO, threat, projectile) để tiết kiệm CPU.

## 4) Reverb & Zones
- Dùng Audio Reverb Zone (hoặc plugin) cho area; blend khi vào/ra zone, tránh pop.
- Indoor/outdoor switch: snapshot/RTPC để đổi reverb amount/LPF.
- Long tail: render sẵn tail cho SFX nếu không cần realtime convolution.

## 5) Performance & Voice Management
- Voice cap: thiết lập max voices; ưu tiên bus (VO > threat SFX > ambience > UI).
- Culling: khoảng cách và priority; tắt spatialization cho UI/2D.
- Streaming: âm dài (ambience, music) stream; SFX ngắn preload.
- Profiling: kiểm tra Audio thread time, voice count peak (combat), GC spike.

## 6) Implementation (Unity)
- AudioSource settings: Spatial Blend 3D cho world SFX; Spread để widen stereo. Custom rolloff curve.
- Reverb: Audio Reverb Zone hoặc plugin (Steam/Resonance); snapshot để blend nhanh theo khu vực.
- Occlusion: script raycast + set LPF/volume trên AudioMixer exposed params.
- Binaural: bật per-source nếu plugin hỗ trợ; disable cho UI/mono VO nếu không cần.

### Ví dụ C# (Occlusion raycast → LPF trên AudioMixer)
```csharp
using UnityEngine;
using UnityEngine.Audio;

public class SimpleOcclusion : MonoBehaviour
{
    public Transform listener;
    public LayerMask occluderMask;
    public float maxDistance = 40f;
    public AudioMixer mixer;
    public string lpfParam = "SFX_LPF"; // Exposed Parameter trên AudioMixer
    public float lpfOcc = 800f;  // Hz khi bị che
    public float lpfClear = 22000f; // Hz khi không che
    public float smoothTime = 0.08f;

    float _vel;
    float _current;

    void Start()
    {
        _current = lpfClear;
    }

    void Update()
    {
        Vector3 dir = listener.position - transform.position;
        float dist = dir.magnitude;
        bool blocked = false;

        if (dist < maxDistance)
        {
            if (Physics.Raycast(transform.position, dir.normalized, out var hit, dist, occluderMask))
            {
                blocked = true;
            }
        }

        float target = blocked ? lpfOcc : lpfClear;
        _current = Mathf.SmoothDamp(_current, target, ref _vel, smoothTime);
        mixer.SetFloat(lpfParam, Mathf.Log10(_current) * 20f); // convert Hz -> dB if param is dB, or set exposed as Hz float
    }
}
```

## ✅ Apply it
- [ ] Chọn panner/HRTF plugin và thiết lập fallback stereo.
- [ ] Thiết lập occlusion raycast + LPF/attenuation per material.
- [ ] Reverb zone + snapshot cho indoor/outdoor; kiểm tra blend không pop.
- [ ] Voice cap + priority + culling cho combat peak.
- [ ] QA headphone vs loa, downmix stereo, và perf Audio thread.