---
title: "Git Mastery cho Web Developer"
description: "Hiểu Git sâu, chọn flow phù hợp, áp dụng best practice để teamwork mượt mà."
last_updated: 2026-03-04
---

# 🔧 Git, Branch Flow & Best Practices cho Web Dev

> Git không chỉ là lệnh `git push`. Nó là cách bạn kể câu chuyện phát triển sản phẩm một cách rõ ràng, giúp team scale nhanh mà vẫn kiểm soát chất lượng. Bài viết này tổng hợp mindset + workflow + checklist giúp bạn làm chủ Git trong mọi dự án web.

---

## 0. Git hoạt động như thế nào?

Git là hệ thống quản lý phiên bản phân tán. Mỗi máy dev chứa toàn bộ lịch sử repo. Khi bạn commit, Git tạo một snapshot của file (thực chất lưu dưới dạng object `blob` + `tree` + `commit`).

**Pipeline cơ bản:**

```
Working Directory → Staging Area → Local Commit → Remote (GitHub/GitLab)
```

- Mọi thứ được tham chiếu bằng SHA-1 hash → đảm bảo toàn vẹn.
- Branch thực chất là con trỏ (pointer) tới commit.
- Merge chỉ là tạo commit mới kết hợp tree từ 2 branch.

> 💡 Hãy tưởng tượng Git như một đồ thị DAG: mỗi commit trỏ về parent(s). Hiểu được “đồ thị” này, bạn sẽ debug được mọi tình huống.

---

## 0.5 Những khái niệm quan trọng

| Khái niệm | Giải thích ngắn | Câu hỏi tự test |
| --- | --- | --- |
| **Repository** | Kho chứa toàn bộ lịch sử, có `.git/`. | `git init` khác `git clone` thế nào? |
| **Commit** | Snapshot của code tại một thời điểm + metadata (author, message). | Commit có thể sửa bằng `git commit --amend`? |
| **Branch** | Con trỏ tới commit, giúp tách luồng phát triển. | Branch có phải bản sao thư mục? |
| **HEAD** | Con trỏ hiện tại bạn đang làm việc. | Khi `git checkout` thì HEAD chuyển ra sao? |
| **Tag** | Nhãn cố định gắn vào commit (thường dùng cho release). | Tag có di chuyển khi commit mới? |
| **Remote** | Repo ở server (GitHub). | `origin` là gì? Có thể có nhiều remote? |

---

## 0.6 Các lệnh Git “must know”

| Nhóm | Lệnh | Dùng khi | Ghi chú |
| --- | --- | --- | --- |
| Inspect | `git status`, `git log --oneline`, `git show <commit>` | Kiểm tra trạng thái, xem lịch sử | Thêm `--graph` để thấy branch |
| Stage/Commit | `git add`, `git add -p`, `git commit -m` | Ghi lại thay đổi | `-p` giúp commit từng phần |
| Branch | `git branch`, `git checkout -b`, `git switch` | Tạo/chuyển branch | `switch` thân thiện hơn |
| Sync | `git fetch`, `git pull --rebase`, `git push` | Đồng bộ với remote | Ưu tiên `pull --rebase` cho branch cá nhân |
| Review | `git diff`, `git diff --staged`, `git blame` | So sánh, truy tìm lỗi | `blame` + IDE hỗ trợ rất hữu ích |
| Cleanup | `git stash`, `git clean`, `git reset --hard` | Dọn trạng thái tạm | Cẩn thận khi reset vì mất dữ liệu |

---

## 1. Git Fundamentals cần nắm vững

| Chủ đề | Mô tả nhanh | Checklist tự test |
| --- | --- | --- |
| **Commit mindset** | Mỗi commit giải quyết 1 vấn đề, mô tả bằng động từ (Fix, Add, Refactor…). Tránh “update”, “wip”. | `git log --oneline` có đọc hiểu được? |
| **Branch naming** | `feature/login-form`, `bugfix/cart-quantity`, `chore/deps-upgrade`. | Team đọc tên branch là biết mục đích? |
| **Staging area** | Quyết định chính xác file nào được commit. Sử dụng `git add -p` để chọn từng hunk. | Có commit từng phần khi file lớn? |
| **Rebase vs Merge** | Merge giữ lịch sử đầy đủ, Rebase tạo history gọn. Dùng Rebase cho branch cá nhân trước khi mở PR. | Biết run `git pull --rebase origin main`? |
| **Diff fluency** | `git diff`, `git diff --staged`, `git blame`, `git show <commit>` | Biết tìm nguyên nhân bug qua blame? |

> 📌 Tip: Thiết lập alias trong `.gitconfig` để thao tác nhanh: `lg = log --oneline --graph --decorate --all`

---

## 2. Chọn Branching Flow phù hợp

### 2.1 GitHub Flow (Simple, Ship nhanh)

**Khi dùng:** Startup nhỏ, product ship liên tục, CI/CD mạnh.

**Quy trình:**

1. `main` luôn deployable.
2. Tạo branch từ `main`: `feature/checkout`
3. Push, mở Pull Request sớm để nhận feedback.
4. Code review + CI pass → Merge → Deploy.

**Ưu điểm:** Nhanh, ít branch. **Nhược điểm:** Khó quản lý release lớn, cần discipline cao.

### 2.2 Trunk-Based Development (Team lớn, release hàng ngày)

1. Dev branch sống tối đa 1-2 ngày.
2. Feature flag bắt buộc để merge code chưa hoàn thiện.
3. CI chạy mọi commit, yêu cầu test tự động.

**Khi phù hợp:** Product-led team, nhiều dev push cùng lúc, muốn tránh merge hell.

### 2.3 Git Flow (Release cadence rõ ràng)

**Branch chính:**

- `main`: lịch sử release.
- `develop`: nơi tích hợp tính năng.
- `feature/*`: tính năng mới.
- `release/*`: tuần cuối chuẩn bị release.
- `hotfix/*`: sửa production khẩn.

**Khi dùng:** Team enterprise, có QA handoff, release 2-4 tuần/lần.

> ✅ Lời khuyên: Đừng chọn Git Flow nếu team <5 người hoặc deploy nhiều lần/ngày. Flow càng phức tạp → overhead càng lớn.

---

## 3. Best Practices ở từng giai đoạn

### 3.1 Mở Pull Request

- **Template rõ ràng:** Summary, ảnh chụp, checklist test, ticket link.
- **PR nhỏ:** 200 dòng code dễ review hơn 2000 dòng.
- **CI bắt buộc:** Không review code chưa pass test.
- **Chia sẻ ngữ cảnh:** Screencast/Loom cho UI change lớn.

### 3.2 Code Review mindset

- Review vì chất lượng sản phẩm, không bắt bẻ cá nhân.
- Ưu tiên logic, bảo mật, performance trước style.
- Dùng ngôn ngữ gợi ý: “Suggestion: …” thay vì “Wrong”.
- Nếu tranh luận kéo dài >3 comment → call nhanh 5 phút.

### 3.3 Tránh merge conflict & chaos

- Pull thường xuyên (`git fetch origin && git rebase origin/main`).
- Viết test để CI bắt lỗi sớm.
- Feature flag giúp merge code nửa chừng mà không phá production.
- Cleanup branch đã merge (`git branch -d feature/foo && git push origin --delete feature/foo`).

### 3.4 Release hygiene

- Tag rõ: `v1.3.0` + release notes (changelog). Tools: `changesets`, `release-please`.
- Deployment checklist: migration, env vars, monitoring.
- Rollback plan: `git revert` hoặc deploy lại tag stable.

---

## 4. Tooling nên bật ngay

| Công cụ | Lợi ích | Setup nhanh |
| --- | --- | --- |
| **Git Hooks (Husky, Lefthook)** | Tự động lint/test trước khi commit/push. | `npx husky-init && npm install` |
| **GitHub Actions** | CI/CD chạy test, lint, build. Tích hợp badge vào README. | `.github/workflows/ci.yml` |
| **Dependabot / Renovate** | Tự động mở PR update dependencies. | Enable trong GitHub Settings |
| **GitLens / VSCode Source Control** | Visualize history, blame nhanh trong IDE. | Install extension |
| **Conventional Commits** | Chuẩn hóa message để auto generate changelog. | `feat:`, `fix:`, `chore:`… |

---

## 5. Checklist áp dụng cho team

### Daily

- [ ] Pull branch mới nhất trước khi code.
- [ ] Commit nhỏ, mô tả rõ.
- [ ] Viết note trong PR nếu còn TODO/Limitations.

### Weekly

- [ ] Review lại lịch sử commit → rút kinh nghiệm.
- [ ] Xóa branch đã merge.
- [ ] Kiểm tra action CI/CD có lỗi pending.

### Monthly

- [ ] Audit `.gitignore`, tránh lộ secrets.
- [ ] Backup repo quan trọng (mirror).
- [ ] Cập nhật guideline Git nếu team mở rộng.

---

## 6. Tài nguyên nên đọc

- [Pro Git Book](https://git-scm.com/book/en/v2) – “Sách giáo khoa” Git nhưng rất thực tế.
- [Trunk-Based Development](https://trunkbaseddevelopment.com/) – Tư duy ship code liên tục.
- [GitHub Flow Guide](https://docs.github.com/en/get-started/using-github/github-flow) – Flow đơn giản nhưng hiệu quả.
- [How Git Actually Works](https://www.youtube.com/watch?v=ZDR433b0HJY) – Talk của Google giải thích internal Git.

---

## 7. Bài tập tự luyện

1. Clone một repo open source → tạo feature nhỏ → mở PR mô phỏng quy trình thật.
2. Thử cả 3 flow (GitHub Flow, Trunk, Git Flow) với project cá nhân để hiểu trade-off.
3. Thiết lập Husky + GitHub Actions cho dự án Next.js/Express bất kỳ.

---

## 8. Khi nào bạn sẽ gặp vấn đề? (Pitfall Radar)

| Tình huống | Dấu hiệu nhận biết | Cách xử lý |
| --- | --- | --- |
| **Merge conflict liên tục** | Pull request nào cũng conflict | Rebase thường xuyên, chia nhỏ PR, thống nhất format code. |
| **Lịch sử commit lộn xộn** | “Fix typo”, “Update”, “final final” | Dùng squash hoặc interactive rebase trước khi merge. |
| **Lộ secrets** | `.env` nằm trong repo public | Thêm `.env` vào `.gitignore`, rotate key, dùng GitGuardian để scan. |
| **Repo quá nặng** | Clone mất 5-10 phút | Dọn file build, dùng Git LFS cho asset lớn. |
| **Không rollback được** | Deploy lỗi mà không biết revert commit nào | Tag release rõ ràng, ghi chú trong PR, luyện `git revert`. |

---

## 9. Git Workflow tổng quát

```
1. Tạo branch từ main
2. Code + test local
3. Commit từng bước nhỏ
4. Pull --rebase để sync
5. Push & mở PR (CI chạy)
6. Review + cập nhật (squash nếu cần)
7. Merge → Deploy (tag release)
8. Xóa branch
```

> 🔄 Mẹo: Nếu đang dở tay nhưng cần switch task → `git stash push -m "context"` rồi quay lại bằng `git stash pop`.

---

## 10. Lộ trình học Git thực tế

### Giai đoạn 1 – Cơ bản (1 tuần)

Mục tiêu: Không còn “sợ Git”.

- `git init`, `git clone`
- `git status`, `git add`, `git commit`
- `git branch`, `git checkout`, `git merge`
- `git push`, `git pull`

**Bài tập:** Tạo repo cá nhân, mô phỏng quy trình “feature → merge → release”.

### Giai đoạn 2 – Trung cấp (2-4 tuần)

Mục tiêu: Làm việc mượt với team, xử lý tình huống.

- `git rebase` (interactive, squash)
- `git stash` (include/untracked)
- `git cherry-pick`
- `git revert`
- `git reset` (soft/mixed/hard)

**Bài tập:**

1. Rebase branch cũ lên `main` mới → giải quyết conflict.
2. Cherry-pick bugfix vào release branch.
3. Reset commit lỗi và cứu bằng `reflog`.

### Giai đoạn 3 – Nâng cao (Liên tục)

Mục tiêu: Tối ưu workflow cho team lớn/đặc thù.

- Git hooks (pre-commit, pre-push) với Husky/Lefthook.
- Git Submodule / Subtree (mono-repo phức tạp).
- Git LFS (Large File Storage) cho asset khủng.
- Git bisect để tìm commit gây bug.

**Git LFS cho Game Dev & Media nặng**

- Game/project có texture, audio, 3D model → file >100MB.
- Git thường lưu snapshot → repo phình to nhanh.
- Dùng `git lfs install` + `git lfs track "*.png"` để chỉ lưu pointer, file thực lưu ngoài.
- Kết hợp với build pipeline (Unity, Unreal) để đảm bảo asset không bị thiếu khi clone.

> 🎮 Rule of thumb: Nếu file >50MB hoặc binary khó diff → cân nhắc LFS.

---

> 🎯 Mục tiêu cuối cùng: Dù join team nào, bạn cũng hiểu ngay cách họ vận hành Git và đóng góp được trong tuần đầu tiên.

---

**Next Steps:**

- Cập nhật CV/Portfolio với highlight “Designed Git branching strategy, automated CI with GitHub Actions → giảm 50% bug production”.
- Hướng dẫn đồng đội mới bằng chính bài viết này.

**Remember:** Git là hệ điều hành của codebase. Làm chủ Git = tăng vận tốc cá nhân + giúp team tin tưởng bạn hơn.