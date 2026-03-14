# Challenge: ECS Performance Kata

- **Loại:** kata/project
- **Mảng:** game-dev
- **Mức:** Intermediate
- **Ước lượng thời gian:** 2-3 ngày
- **Prerequisites (tùy chọn):** Hiểu ECS (Entity-Component-System), profiler cơ bản, kiến thức cache/memory layout.

## Mục tiêu học tập
- Tối ưu pipeline ECS cho số lượng entity lớn (vài chục nghìn).
- Nhận diện bottleneck (cache miss, branching, sync) và đo được improvement.
- Áp dụng data-oriented design: struct-of-arrays, archetype/chunk, job/parallel (nếu engine hỗ trợ).

## Đề bài
Tạo một scene với nhiều entity (≥20k) gồm transform, velocity, simple AI/pattern, và render tối giản. Nhiệm vụ:
- Benchmark baseline (FPS/ms) ở số lượng entity cao.
- Tối ưu: chuyển layout phù hợp (SoA/archetype), group systems giảm cache miss, batch update, giảm allocation.
- (Tuỳ chọn) Parallel/job system nếu engine hỗ trợ; tránh false sharing.

## Đầu ra (Output)
- Báo cáo ngắn: baseline vs sau tối ưu (ms/FPS, số entity), mô tả thay đổi.
- Build/scene chạy được để so sánh.

## Tiêu chí chấm (Acceptance)
- Có số đo trước/sau (ms hoặc FPS) ở cùng cấu hình entity.
- Thay đổi code có lý do rõ (layout, batching, parallel), không chỉ “tắt feature”.
- Không phá tính đúng: entity update vẫn đúng logic cơ bản.

## Gợi ý / Hint
- SoA/archetype chunk để giảm cache miss; tránh pointer chasing.
- Giảm branch trong inner loop; precompute; dùng job/parallel cho hệ độc lập.
- Batch render/submit; tránh malloc mỗi frame; cấp phát trước buffers.

## Reference / Solution (tùy chọn)
- ECS micro-optimizations: https://research.swtch.com/sparse
- Unity DOTS samples: https://github.com/Unity-Technologies/EntityComponentSystemSamples
- Data-oriented design notes: https://github.com/terrykeller/research-dod