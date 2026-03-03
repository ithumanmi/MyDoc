# 🗂️ Information Architecture Playbook

> [← Back to Productivity Core Skills](./README.md) | [Personal Work Framework](./personal-work-framework.md) | [PKM System](../meta-skills/pkm-system.md)

**Mục tiêu:** Xây “Bộ Quy Tắc” quản lý thư mục, tài liệu, dữ liệu và dự án giúp bạn, team và future-you tìm info < 30s.

---

## 1. Nguyên tắc nền tảng

1. **One Source of Truth:** Mỗi loại dữ liệu có 1 nơi chính thức (Repo code, Notion wiki, Google Drive...).
2. **Naming > Decoration:** Tên file/thư mục phản ánh nội dung & trạng thái, ưu tiên máy đọc + người đọc.
3. **Lifecycle rõ ràng:** Biết khi nào create → active → archive → delete.
4. **Access Control:** Quyền truy cập mapping theo vai trò, tránh “mọi thứ đều công khai”.
5. **Automation First:** Sync, backup, template hóa để giảm việc thủ công.

---

## 2. Folder Blueprint 5 tầng

```
/Org
 ├─ 0-Admin (Contracts, Finance, Legal)
 ├─ 1-Strategy (OKR, Roadmap, Market Research)
 ├─ 2-Product (Design, Specs, Release Notes)
 ├─ 3-Delivery (Projects, Sprint, Client folders)
 └─ 4-Learning (Playbooks, Post-mortems, Training)
```

- **Tầng số** đảm bảo sorting nhất quán.
- Mỗi dự án lớn (ví dụ `3-Delivery/2026-01-Platform-Upgrade`) sao chép từ template chuẩn (Checklist, Docs, Data, Comms).

### Sub-folder cho Project

```
Project-Name/
 ├─ 01-Brief
 ├─ 02-Planning
 ├─ 03-Assets (Design, Data, Scripts)
 ├─ 04-Delivery (Releases, Reports)
 └─ 05-Retrospective
```

- Prefix số = luồng thời gian, dễ tìm theo phase.
- Mọi file đều có metadata trong README.md của project (owner, mục tiêu, link quan trọng).

---

## 3. Quy tắc đặt tên (Naming Convention)

| Đối tượng | Template | Ví dụ |
| --- | --- | --- |
| Thư mục dự án | `YYYY-MM-Client-Project` | `2026-03-ACME-CRM-Revamp` |
| Tài liệu chính | `Type_Version_Status` | `Spec_v2_Approved.md` |
| File dữ liệu | `DatasetPurpose_Source_Date.format` | `UserBehavior_Mixpanel_2026-03.csv` |
| Meeting notes | `YYYY-MM-DD_Topic` | `2026-03-03_SprintReview.md` |

- **Suffix trạng thái:** `_draft`, `_review`, `_final`.
- Tránh viết hoa không cần thiết, thay space bằng dấu `-` hoặc `_`.

---

## 4. Tài liệu & Data Governance

### 4.1 Documentation Rule
- **README trong mỗi folder:** liệt kê mục tiêu, chủ sở hữu, link liên quan.
- **Change Log:** khi update file quan trọng, ghi lại `Date - Author - Summary`.
- **Templates:** Chuẩn hóa meeting note, spec, report.

### 4.2 Data Rule
- **Data Catalog:** Bảng Notion/Sheet liệt kê dataset → schema → owner → refresh cadence.
- **Retention Policy:** Log, backup, dữ liệu nhạy cảm có thời hạn lưu trữ + điều kiện xóa.
- **Access Log:** Track ai truy cập dataset quan trọng.

---

## 5. Workflow quản lý dự án

1. **Intake:** Khi có dự án mới, duplicate folder template + form metadata (owner, deadline, stake).
2. **Operate:**
   - Task tracker (Linear/Jira) sync link đến folder.
   - `Docs/Decisions.md` ghi mọi quyết định lớn.
3. **Closeout:**
   - Di chuyển artefact quan trọng vào playbook chung.
   - Archive folder sang `Archive/YYYY` (read-only).
4. **Review:** Hàng quý audit structure: delete redundant, cập nhật template.

---

## 6. Tool Stack gợi ý

- **Storage:** Google Drive + Shared Drive (permission theo team).
- **Docs:** Notion/Confluence (cross-link, search nhanh).
- **Code/Data:** GitHub/GitLab + DVC/Lakehouse.
- **Automation:** Zapier/Make sync form intake → folder → tracker; rclone/gsutil để backup.
- **Search:** Build “Global Index” (Raycast script, Obsidian Dataview) để tìm file theo tag/owner.

---

## 7. Checklist áp dụng

- [ ] Có sơ đồ thư mục 5 tầng chuẩn?
- [ ] Mỗi folder dự án có README + metadata?
- [ ] Naming convention được document và share cho toàn team?
- [ ] Dataset quan trọng có catalog + owner + refresh cadence?
- [ ] Cơ chế archive & backup chạy tự động (ít nhất 1 lần/tuần)?

---

**Next Step:** Workshop 60 phút với team → thống nhất blueprint, tạo template, và rollout bằng cách áp dụng cho 1 dự án pilot trước khi nhân rộng.