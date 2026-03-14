# Challenge: Tool Pipeline Mini (Asset/Level Flow)

- **Loại:** project
- **Mảng:** game-dev
- **Mức:** Intermediate
- **Ước lượng thời gian:** 2-4 ngày
- **Prerequisites (tùy chọn):** Kiến thức cơ bản về build pipeline, import asset, scripting tool trong engine (Unity Editor tooling/Godot Editor/Unreal Editor Utility) hoặc tool ngoại (Python CLI).

## Mục tiêu học tập
- Xây một pipeline nhỏ để import/process asset hoặc build level nhanh chóng.
- Tự động hóa bước lặp: convert/optimize asset, generate data (JSON/ScriptableObject), kiểm tra lỗi.
- Viết doc để teammate sử dụng tool.

## Đề bài (chọn 1 hướng)
1) **Asset import tool**: script tự động rename, atlas/packing, LOD gen (nếu 3D), hoặc nén texture; xuất log lỗi (thiếu file, sai naming).
2) **Level builder**: nhập JSON/CSV và tạo level prefab/scene; validate schema; preview trong editor.
3) **Data pipeline**: tool tạo config (items/quests/enemy waves) từ bảng (CSV/Google Sheets export) → sinh file asset (JSON/ScriptableObject) + kiểm tra trùng ID.

## Đầu ra (Output)
- Tool chạy được (editor script hoặc CLI) + README hướng dẫn.
- Ví dụ đầu vào/đầu ra (sample asset hoặc sample CSV/JSON).

## Tiêu chí chấm (Acceptance)
- Tool chạy thành công trên sample, phát hiện và báo lỗi rõ ràng.
- Có bước validate schema/naming; log hoặc report gọn.
- Doc ngắn: cách chạy, input format, giới hạn.

## Gợi ý / Hint
- Với Unity: EditorWindow + AssetPostprocessor; với Godot: EditorScript/EditorPlugin; với Unreal: Editor Utility Widget/Blueprint/Python.
- Nếu làm CLI: Python + Pillow/assimp/aseprite CLI, hoặc node + sharp.
- Thêm CI nhỏ: script kiểm tra sample input để tránh regress.

## Reference / Solution (tùy chọn)
- Unity editor tooling samples: https://github.com/UnityTechnologies/UnityCsReference (Editor scripts), https://github.com/UnityTechnologies/open-project-1
- Godot editor plugin example: https://github.com/godotengine/godot-demo-projects/tree/master/plugins
- Asset pipeline idea: https://github.com/aseprite/aseprite (sprite workflow inspiration)