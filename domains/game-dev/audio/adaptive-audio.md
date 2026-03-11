---
title: "Adaptive Audio (Unity)"
description: "Dynamic music, state-driven SFX, RTPC/parameters, snapshot/RTPC blending cho Unity."
tags:
  - audio
  - adaptive
  - unity
  - middleware
updated: 2026-03-11
---

# 🎼 Adaptive Audio (Unity)

## 1) Goals
- Nhạc/SFX phản ứng với state game (combat/stealth/menu), intensity, health, time-of-day.
- Chuyển cảnh mượt (crossfade/transition region), không pop/click.
- Đồng bộ tempo/bpm cho stem khi chuyển layer.

## 2) Music Systems
- Stem-based layering: rhythm/harmony/melody/percussion; crossfade hoặc additive khi combat/alert tăng.
- Section-based: Intro/Loop/Outro; đặt marker để cắt đúng bar/beat.
- Transition rules: on-bar/on-beat; fade time ngắn (100-500ms) hoặc synchronous swap.
- Tempo map: thống nhất BPM; loop length theo nhịp để tránh drift.

## 3) SFX Systems
- State-driven: dùng parameter/RTPC (intensity, speed, health) để blend volume/pitch/LPF.
- Footstep/locomotion: tốc độ chạy → pitch/volume; surface type → switch clip set.
- Weapons: charge level → layer thêm hum/whine; critical → add transient layer.

## 4) Implementation (Unity built-in)
- Music: dùng AudioMixer Snapshot để crossfade layer; hoặc điều khiển volume group bằng script (Lerp). Marker bằng Timeline/PlayableDirector nếu cần sync cutscene.
- Parameters: expose AudioMixer parameters (volume, LPF/HPF) và điều khiển qua script; tránh Update polling nặng, dùng event/state change.
- Scheduling: dùng AudioSource.PlayScheduled để sync on-beat; đặt DSP time trước vài beat.

## 5) Middleware Style (FMOD/Wwise-like patterns in Unity)
- RTPC-equivalent: ScriptableObject giữ parameter definitions; script push value vào AudioMixer exposed params hoặc custom DSP.
- Snapshot set: giống State system; mỗi state map sang snapshot, crossfade time 200-500ms.
- Switch container: dùng nhóm AudioSource/clip list theo state/surface; quản lý qua Addressables nếu nhiều clip.

## 7) Ví dụ C# (PlayScheduled + Snapshot crossfade)
```csharp
using UnityEngine;
using UnityEngine.Audio;

public class MusicScheduler : MonoBehaviour
{
    public AudioSource intro;
    public AudioSource loop;
    public AudioMixerSnapshot calm;
    public AudioMixerSnapshot combat;
    public float transitionSeconds = 0.35f;

    double _nextStart;
    bool _loopArmed;

    void Start()
    {
        _nextStart = AudioSettings.dspTime + 0.1f;
        intro.PlayScheduled(_nextStart);
        _nextStart += intro.clip.length;
        _loopArmed = true;
        // Start in calm snapshot
        calm.TransitionTo(0.01f);
    }

    void Update()
    {
        // Arm loop once and keep it playing seamlessly
        if (_loopArmed && AudioSettings.dspTime > _nextStart - 0.1f)
        {
            loop.PlayScheduled(_nextStart);
            loop.loop = true;
            _loopArmed = false;
        }
    }

    public void EnterCombat()
    {
        // Crossfade mixer (boost percussion/SFX via snapshots)
        combat.TransitionTo(transitionSeconds);
    }

    public void ExitCombat()
    {
        calm.TransitionTo(transitionSeconds);
    }
}
```

## 6) Testing
- Beat accuracy: log DSP time vs tempo; check drift sau 5-10 phút.
- Crossfade artifact: nghe pop/click; kiểm tra phasing giữa stems (invert check).
- Performance: profiler CPU (Audio thread), voice count; đảm bảo voice limit không clip abrupt.

## ✅ Apply it
- [ ] Thiết kế state chart (combat/stealth/menu/boss) và mapping snapshot/parameters.
- [ ] Chuẩn hóa BPM/loop length; đặt marker on-bar/on-beat.
- [ ] Implement RTPC/parameters (intensity/speed/health) để drive SFX & music layer.
- [ ] Dùng PlayScheduled + snapshot crossfade để chuyển mượt.
- [ ] QA drift tempo, pop/click, voice limit khi peak combat.