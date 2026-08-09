---
title: "Predictive Processing — xung dự báo của não"
description: "Cơ chế PP: prior → prediction error → update/action; hierarchy; precision weighting; free energy; hệ quả nhận thức–hành vi"
updated: "2026-08-09"
canonical: true
tags: [predictive-processing, neuroscience, predictive-coding, free-energy, precision-weighting, cognition]
audience: [intermediate, advanced]
related:
  - perception-through-models.md
  - cognition.md
  - neuroscience-brain.md
  - ../cognitive-biases.md
  - ../schools-of-thought/cbt.md
  - ../key-concepts.md
  - ../../../04-lifestyle-os/health/dopamine-system.md
  - ../../../03-career-skills/productivity/meta-skills/meta-thinking.md
  - ../../../03-career-skills/productivity/meta-skills/meta-thinking-bias-filter.md
  - ../practical-applications/predictive-processing-anxiety-habits.md
sensitivity: public
---

# Predictive Processing — xung dự báo của não

> [← Psychology](../README.md) · [Perception through models](./perception-through-models.md) · [PP → lo âu & thói quen](../practical-applications/predictive-processing-anxiety-habits.md) · [Neuroscience](./neuroscience-brain.md) · [Cognition](./cognition.md)

**Predictive Processing (PP)** / *predictive coding* (và họ hàng *active inference*) mô tả não như máy **sinh mô hình sinh** (generative model) về thế giới: liên tục **dự báo** tín hiệu cảm giác, so sánh với đầu vào thật, rồi dùng **prediction error (lỗi dự báo)** để cập nhật model — hoặc hành động để làm data khớp dự báo.

Lớp ứng dụng “não nhìn qua model”: [`perception-through-models.md`](./perception-through-models.md).  
Bài này = **cơ chế thần kinh–tính toán** (educational map; đơn giản hóa; không đồng nhất một consensus tuyệt đối trong ngành).

Không thay chẩn đoán y khoa / loạn thần.

## Agent SUMMARY

- Vòng lõi: **Prior/Prediction (top-down) ↔ Sensory input (bottom-up) → Prediction error → Update model hoặc Active inference (act)**.
- **Hierarchy:** layer cao = chậm, trừu tượng; layer thấp = nhanh, cảm giác; PE lan lên khi không giải được ở dưới.
- **Precision weighting:** “độ tin” gán cho PE vs prior — như gain/attention; sai precision → ảo giác / lo âu / cứng model.
- **Free Energy Principle (Friston-style):** tối thiểu surprise dài hạn ≈ giữ model khớp đủ để sống sót (khung thống nhất, tranh luận học thuật còn mở).
- Dopamine / neuromodulators thường được bàn như tín hiệu liên quan **precision / learning from PE** (map thô, không = công thức 1:1).
- Hệ quả: ảo ảnh, bias, CBT (đổi prior), học = tích PE có ích; Meta-Filter = chỉnh precision thủ công.
- **Ứng dụng lo âu / thói quen:** [`predictive-processing-anxiety-habits.md`](../practical-applications/predictive-processing-anxiety-habits.md).
- Đọc kèm: perception-through-models · cognition · dopamine-system · meta-thinking-bias-filter.

---

## 1. Vòng xung dự báo (core loop)

```text
                    ┌──────────────────────────┐
                    │  Generative model / Prior │
                    │  (dự báo: sắp thấy gì?)   │
                    └────────────┬─────────────┘
                                 │ top-down prediction
                                 ▼
              Sensory cascade ◄──────────── ► Predicted sensory state
                                 │
                     Prediction error (PE)
                     = input − prediction
                                 │
              ┌──────────────────┴──────────────────┐
              ▼                                     ▼
     Update beliefs (perception / learning)   Active inference
     (đổi model để khớp data)                 (hành động để data khớp dự báo)
```

| Thành phần | Vai trò |
| --- | --- |
| **Prior / Belief** | Kỳ vọng đã học (thống kê trên kinh nghiệm) |
| **Prediction** | Tín hiệu top-down “mong đợi” ở tầng cảm giác |
| **Likelihood / sensory evidence** | Data bottom-up từ thụ thể / lớp thấp |
| **Prediction error (PE)** | Phần data *không* giải thích được bằng dự báo |
| **Posterior / updated belief** | Model sau khi hấp thụ PE (Bayes-style) |

**Khác camera:** não không “upload” thế giới — não **kiểm tra giả thuyết** liên tục. Nếu dự báo đủ tốt, ít PE, ít tốn bandwidth (hiệu quả sống sót).

---

## 2. Predictive coding trong phân cấp vỏ não (hierarchy)

PP giả định **mô hình sinh dạng tầng** (hierarchical generative model):

| Tầng (khái niệm) | Nội dung dự báo | Tốc độ / phạm vi |
| --- | --- | --- |
| Thấp (gần sensor) | Edge, contrast, speech formant… | Nhanh, cục bộ |
| Trung | Object, phoneme, gesture… | Trung bình |
| Cao (association / PFC–related) | Context, goal, “câu chuyện tình huống” | Chậm, rộng |

**Luồng thường dùng trong predictive coding (Rao & Ballard–style, giản lược):**

- **Top-down:** lớp cao gửi prediction xuống lớp thấp.  
- **Bottom-up:** lớp thấp gửi lên chủ yếu **PE** (phần residual), không phải raw copy toàn bộ.  
- PE giải được ở tầng thấp → dừng; không giải được → đẩy lên tầng cao hơn (cần đổi context/belief lớn hơn).

**Hệ quả trải nghiệm:**
- Phòng quen = ít PE = “không thấy” chi tiết.  
- Thứ lạ / đe dọa = PE lớn = chiếm attention.  
- Mapping ứng dụng: schema / story tầng cao bắt data tầng thấp “khớp vào khuôn” ([`perception-through-models.md`](./perception-through-models.md)).

> Nuance giải phẫu: cortex thật phức tạp hơn sơ đồ “mũi tên chỉ PE”; coi đây là **mô hình tính toán hữu ích**, không atlas 1:1.

---

## 3. Precision weighting — “độ tin” của lỗi vs prior

Não không cộng PE một cách mù. Mỗi tín hiệu có **precision** (nghịch đảo variance — độ tin cậy ước lượng):

| Tình huống | Precision trên PE cao? | Hệ quả |
| --- | --- | --- |
| Cảm giác rõ, tỉnh táo, tin sensor | Cao | Model cập nhật mạnh theo data |
| Cảm giác mơ hồ, fatigue, noise | Thấp | Bám prior / kỳ vọng cũ |
| Attention chọn kênh | Tăng precision kênh đó | “Nhìn thấy” đúng thứ đang expect tìm |
| Prior cực mạnh (niềm tin cứng) | PE bị down-weight | Confirmation-like: bỏ qua trái chiều |

**Attention** trong khung PP ≈ **tăng precision** các kênh / lỗi liên quan mục tiêu — không chỉ “đèn pin” thụ động.

**Lệch precision (map lâm sàng–giáo dục, không chẩn đoán):**

| Pattern (giản lược) | Diễn giải PP |
| --- | --- |
| Prior quá mạnh + PE bị dập | Ảo giác / tin cứng trái evidence (prior “thắng” sensor) |
| PE quá ồn / precision lệch | Lo âu: mọi biến động đều “quan trọng”; khó nghỉ |
| Không học từ PE lặp | Model cứng → bias, khó unlearn |

Liên hệ thực hành: Meta-Filter cố tình **tăng precision** cho evidence phản ([`meta-thinking-bias-filter.md`](../../../03-career-skills/productivity/meta-skills/meta-thinking-bias-filter.md)); arousal SNS cao làm tone precision lệch — phanh trước khi update belief ([`sns-cortisol-brake-playbook.md`](../../../04-lifestyle-os/health/sns-cortisol-brake-playbook.md)).

---

## 4. Active inference — hành động cũng là “dự báo”

Hai cách giảm PE:

1. **Perceptual inference:** đổi belief cho khớp data (*“À, đó là bóng, không phải rắn”*).  
2. **Active inference:** đổi thế giới / thân thể để data khớp prediction (*xoay đầu, sờ, hỏi thêm, tránh*).

Ví dụ:
- Mong “meeting sẽ ổn” → chủ động chuẩn bị slide (làm thế giới khớp prior tích cực).  
- Tránh thông tin trái chiều → active inference **bảo vệ prior** (hành vi confirmation).

Hành vi ≠ chỉ phản xạ S→R; là cách **đóng vòng dự báo** ([behaviorism thuần](../schools-of-thought/behaviorism.md) thiếu tầng này; PP bổ sung).

---

## 5. Free Energy Principle (khung thống nhất — mức cao)

Trong dòng Karl Friston và cộng sự, **Free Energy Principle (FEP)** đề xuất (giản lược giáo dục):

> Hệ sống phải hạn chế trạng thái bất ngờ (surprise / surprise trung bình dài hạn) để tồn tại; **variational free energy** là biên trên có thể tối thiểu hóa thay cho surprise thật (không quan sát trực tiếp).

| Ý FEP (thực dụng) | Đọc nhanh |
| --- | --- |
| Giữ model đủ khớp môi trường | Sống = “không quá bất ngờ mãi” |
| Perception + action = hai cánh | Cùng mục tiêu: giảm free energy / PE kỳ vọng |
| Homeostasis mở rộng | Không chỉ thân nhiệt — cả niềm tin / thói quen |

**Cảnh báo học thuật:** FEP mạnh về toán/khung thống nhất; mức “não thật implement đúng formalisme” vẫn tranh luận. Dùng như **thấu kính**, không dogma.

---

## 6. Neuromodulation & học từ PE (map thô)

| Chất / hệ | Vai trò hay được gắn với PP (đơn giản hóa) |
| --- | --- |
| **Dopamine** | Tín hiệu liên quan reward *prediction error* / salience; và trong một số mô hình = điều chỉnh precision / learning rate ([`dopamine-system.md`](../../../04-lifestyle-os/health/dopamine-system.md)) |
| **Noradrenaline / ACh** (khái niệm) | Gain / attention / precision trên sensory channels (literature neuromodulatory gain) |
| **Plasticity** | PE có weighted → cập nhật synapse (“fire together…” — [`neuroscience-brain.md`](./neuroscience-brain.md)) |

Không rút: “thiếu dopamine = không có predictive processing”. Chỉ: **học & attention gắn hóa chất điều chỉnh độ nhạy với lỗi**.

---

## 7. Hiện tượng nhận thức giải thích bằng PP

| Hiện tượng | Giải PP (rút gọn) |
| --- | --- |
| **Ảo ảnh quang học** | Prior hình học / thống kê thị giác thắng data cục bộ |
| **Điền chữ thiếu vần vẫn đọc được** | Prior ngôn ngữ mạnh |
| **Change blindness** | Ít PE khi expect scene ổn định |
| **Bias confirmation** | Prior mạnh + down-weight PE trái chiều |
| **Availability** | Recent PE lớn → over-precision tạm thời cho class đó |
| **Lo âu lan tỏa** | Nhiều PE được gán precision cao (mọi lệch = quan trọng) |
| **CBT hiệu lực** | Đổi prior / giảm catastrophizing precision ([`cbt.md`](../schools-of-thought/cbt.md)) |
| **Meditation / present focus** | Có thể giảm chatter prior tầng cao; tăng precision vào sensory hiện tại (giả thuyết lối sống) |

---

## 8. So sánh nhanh với khung đã có trong Docs

| Khung Docs | PP đóng góp thêm |
| --- | --- |
| Perception through models | Cơ chế *vì sao* model thống trị cảm giác |
| System 1 / 2 | System 1 ≈ chạy prediction nhanh; System 2 ≈ cập nhật / giả thuyết tốn kém khi PE lớn |
| Meta-thinking | Tầng quan sát: prior nào? precision đang lệch? |
| Stoic Dichotomy | External = sensory flux; Internal = cách cập nhật prior & hành động |

---

## 9. Protocol thực hành (không phải lab)

Mục tiêu: **không tắt PP** — chỉnh *khi nào tin PE* và *khi nào nghi prior*.

| Drill | Cơ chế nhắm | Cách |
| --- | --- | --- |
| **Name the prior** | Đưa prior lên ý thức | Trước phán xét: *“Mình đang predict điều gì?”* |
| **Seek PE có chủ đích** | Tăng precision evidence phản | 1 nguồn trái chiều / quyết định lớn |
| **Precision check** | Affect heuristic | *“Cảm xúc đang tăng gain cho PE nào?”* — trì 24h nếu cực đoan |
| **Active inference lành** | Đóng vòng bằng hành động thông tin | Thí nghiệm nhỏ thay vì rumination |
| **Feynman** | Phơi prior thủng | Giải thích → chỗ khựng = PE chưa hấp thụ |

Stack: STOP–ZOOM–SWITCH ([bias filter](../../../03-career-skills/productivity/meta-skills/meta-thinking-bias-filter.md)).

---

## 10. Giới hạn & đọc tiếp trong repo

- PP/FEP = **khung mạnh + tranh luận**; nhiều chi tiết neural vẫn giả thuyết.  
- Không suy ra chẩn đoán từ “prior mạnh”.  
- Triune brain trong [`neuroscience-brain.md`](./neuroscience-brain.md) = sư phạm thô; PP dùng ngôn ngữ tầng vỏ / neuromodulation tinh hơn.

| Cần | Doc |
| --- | --- |
| Map hành vi / schema | [`perception-through-models.md`](./perception-through-models.md) |
| Ứng dụng lo âu & habit | [`predictive-processing-anxiety-habits.md`](../practical-applications/predictive-processing-anxiety-habits.md) |
| Attention / memory / S1–S2 | [`cognition.md`](./cognition.md) |
| Bias | [`cognitive-biases.md`](../cognitive-biases.md) |
| Dopamine | [`dopamine-system.md`](../../../04-lifestyle-os/health/dopamine-system.md) |
| Giám sát tư duy | [`meta-thinking.md`](../../../03-career-skills/productivity/meta-skills/meta-thinking.md) |

---

## One-liner

> Não không thu thập thế giới — não **đặt cược dự báo**, đo **lỗi**, rồi **sửa model hoặc sửa thế giới**; Predictive Processing là hệ điều hành của vòng đó, còn precision là núm volume quyết định bạn học được gì từ lỗi.
