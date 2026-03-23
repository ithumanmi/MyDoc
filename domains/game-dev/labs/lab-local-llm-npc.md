---
title: "Lab 9 - Local LLM NPC Quest Giver"
description: "Tích hợp NPC dùng LLM local (Ollama) với fallback FSM, telemetry và UI bubble streaming."
tags:
  - lab
  - ai
  - npc
  - llm
updated: 2026-03-23
---

# 🧪 Lab 9: Local LLM NPC Quest Giver

> **Level:** Senior/Technical Director track (AI integration).
> **Goal:** Gắn NPC unity với mô hình LLM chạy local (Ollama) + fallback FSM để đảm bảo gameplay không bị block.
> **Deliverables:** Unity scene demo, `NPCDialogueService.cs`, telemetry log, retro doc.
> **Success Criteria:**
> - Response < 1.5s (text streaming), fallback <10%.
> - NPC có trạng thái cảm xúc (JSON) điều khiển UI/animation.
> - Telemetry log `llm_latency`, `token_count` gửi về console/datalayer.

## 1. Chuẩn bị
- **Engine:** Unity 2022 LTS, URP.
- **Ollama:** cài `llama3` hoặc `phi3` local. Run `ollama run llama3 --keepalive 5m`.
- **Packages:** `com.unity.nuget.newtonsoft-json`, `TextMeshPro`.

## 2. Data & Prompt
```json
// system_prompt.json
{
  "persona": "Guard of Ember City, religious zealot, sarcastic",
  "lore": "Player stabbed you, -20 HP. Remaining 80 HP.",
  "rules": "Respond <= 1 sentence, include emotion tag"
}
```

Prompt structure gửi đến Ollama:
```
You are {{persona}}. Lore: {{lore}}. Rules: {{rules}}.
Output JSON: {"emotion": "...", "line": "..."}
```

## 3. Unity Implementation

### 3.1 NPCDialogueService skeleton
```csharp
public class NPCDialogueService : MonoBehaviour
{
    [SerializeField] private string ollamaModel = "llama3";
    [SerializeField] private string endpoint = "http://localhost:11434/api/generate";
    [SerializeField] private TMP_Text bubbleText;
    [SerializeField] private Animator animator;

    private CancellationTokenSource cts;

    public async Task SpeakAsync(string personaContext)
    {
        cts?.Cancel();
        cts = new CancellationTokenSource();

        try
        {
            await foreach (var chunk in StreamResponse(personaContext, cts.Token))
            {
                bubbleText.text = chunk.Text;
            }

            ApplyEmotion(chunk.Emotion);
            Telemetry.LogLLM(chunk.LatencyMs, chunk.TokenCount);
        }
        catch (Exception ex)
        {
            FallbackFSM();
        }
    }
}
```

### 3.2 Streaming
- Dùng `UnityWebRequest` với `DownloadHandlerBuffer` hoặc `HttpClient` (.NET 4.x) + `IAsyncEnumerable`.
- Parse chunk JSON theo định dạng streaming của Ollama (`data: {...}` per line).

### 3.3 Emotion & Animation
- Map `emotion` → animator parameter (`Angry`, `Fear`, `Calm`).
- UI bubble đổi màu/texture theo emotion.

### 3.4 Fallback FSM
- Nếu LLM lỗi >5s, gọi `FallbackFSM()` dùng state machine có sẵn (Idle, Chase, Enrage) hiển thị câu thoại pre-script.
- Log `LLM_FALLBACK=true` để retro.

## 4. Telemetry
- Create ScriptableObject `LLMTelemetryChannel` ghi metrics.
- Output to console + send to [Unity Impact Metrics](../production/metrics/unity-impact-metrics.md) sheet.
- Fields: `npc_id`, `latency_ms`, `token_count`, `fallback_used`.

## 5. Testing Checklist
- [ ] Simulate network loss (tắt Ollama) → ensure fallback ok.
- [ ] Spam multiple players -> queue/cancel token not leak.
- [ ] Profiler: check GC alloc <1KB/frame khi idle.
- [ ] Localization: ensure accent characters hiển thị đúng.

## 6. Deliverables
- Video/GIF demo NPC phản ứng.
- Source code (repo) + README.
- Retro file theo [Retro Template](../production/metrics/retro-template.md).

## 🔗 Related
- [AI for Game Dev](../ai-for-game-dev.md)
- [Lab 3: Máy trạng thái của Boss](./README.md#-lab-2)