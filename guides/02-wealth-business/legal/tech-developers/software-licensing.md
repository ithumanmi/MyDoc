# ⚖️ Software Licensing cho Developers

> **TL;DR:** MIT = Tự do nhất. Apache = MIT + Patent. GPL = Chia sẻ bắt buộc. Chọn sai license = Legal nightmare. Hiểu để dùng đúng và chọn đúng cho project.

---

## 🎯 Bảng So sánh Nhanh

| License | Tự do sử dụng | Commercial OK? | Phải mở source | Patent | Popularity |
|---------|---------------|----------------|----------------|--------|------------|
| **MIT** | ✅ | ✅ | ❌ | ❌ | ⭐⭐⭐⭐⭐ |
| **Apache 2.0** | ✅ | ✅ | ❌ | ✅ | ⭐⭐⭐⭐ |
| **BSD** | ✅ | ✅ | ❌ | ❌ | ⭐⭐⭐ |
| **GPL v3** | ✅ | ⚠️ | ✅ | ✅ | ⭐⭐⭐ |
| **AGPL** | ✅ | ⚠️ | ✅ (Network) | ✅ | ⭐⭐ |
| **LGPL** | ✅ | ✅ (Link) | ⚠️ | ✅ | ⭐⭐ |

---

## 1. MIT License ⭐ Most Popular

### **Điều khoản chính**

```
✅ CÓ THỂ:
- Sử dụng cho bất kỳ mục đích nào
- Modify code
- Distribute (Cả source và binary)
- Sublicense
- Bán sản phẩm commercial

❌ PHẢI:
- Giữ copyright notice và license text trong code
- Không bảo hành (AS-IS)

❌ KHÔNG BẮT BUỘC:
- Share modifications
- Open source derivative works
```

### **Khi nào dùng MIT?**

✅ **Phù hợp:**
- Muốn adoption rộng rãi
- Không quan tâm derivative works có open hay không
- Dự án community-driven
- Muốn companies sử dụng thoải mái

**Ví dụ nổi tiếng:** React, Vue.js, Rails, jQuery

---

## 2. Apache License 2.0

### **Giống MIT nhưng thêm:**

✅ **Patent Grant:**
- Contributors cấp quyền sử dụng patents
- Bảo vệ users khỏi patent trolls

✅ **Trademark:**
- Không cấp quyền sử dụng trademark (brand name, logo)

### **Khi nào dùng Apache?**

✅ **Phù hợp:**
- Dự án liên quan đến patents
- Muốn bảo vệ tốt hơn MIT
- Enterprise-friendly

**Ví dụ:** Kubernetes, Android, TensorFlow

---

## 3. GPL v3 (GNU General Public License)

### **Điều khoản chính - "Copyleft"**

```
✅ CÓ THỂ:
- Sử dụng miễn phí
- Modify
- Distribute

❗ PHẢI:
- Nếu distribute derivative → Phải open source dưới GPL
- Share source code khi distribute binary
- Ghi rõ thay đổi (CHANGELOG)

❌ KHÔNG THỂ:
- Dùng GPL code trong closed-source product
```

### **Khi nào dùng GPL?**

✅ **Phù hợp:**
- Muốn force derivative works open source
- Ideological (Free software philosophy)
- Không muốn companies "ăn cắp" code

❌ **Không phù hợp:**
- Muốn companies sử dụng
- Muốn adoption rộng

**Ví dụ:** Linux kernel, WordPress, GIMP

---

## 4. AGPL (Affero GPL)

### **GPL + Network Use**

**Khác biệt với GPL:**
- **GPL:** Distribute binary → Phải share source
- **AGPL:** Network use (SaaS) = Distribute → Phải share source

**Ví dụ:**
- Bạn fork AGPL project
- Deploy lên server làm SaaS
- Users dùng qua web (không download)
- **→ Phải share source code** (GPL thì không phải)

### **Khi nào dùng AGPL?**

✅ **Phù hợp:**
- Muốn ngăn "SaaS loophole"
- Force cloud providers share modifications

❌ **Rất khó adoption:**
- Companies tránh AGPL như tránh bệnh dịch

**Ví dụ:** MongoDB (old version, switched to SSPL)

---

## 5. LGPL (Lesser GPL)

### **GPL cho Libraries**

```
✅ CÓ THỂ:
- Link LGPL library vào closed-source app
- KHÔNG cần open source app của bạn

❗ NẾU modify LGPL library:
- Phải share modifications
```

### **Khi nào dùng LGPL?**

✅ **Phù hợp:**
- Building library muốn adoption
- Nhưng vẫn muốn modifications được shared

**Ví dụ:** Qt (dual-license), GStreamer

---

## 6. BSD License (2-Clause/3-Clause)

### **Gần giống MIT**

**Khác biệt nhỏ:**
- BSD 3-Clause: Không được dùng tên author để promote
- MIT: Không có điều này

**Khi nào dùng BSD?**
→ Tương tự MIT, ít phổ biến hơn

**Ví dụ:** FreeBSD, Django

---

## 7. Unlicense / Public Domain

### **Không có bản quyền**

```
✅ CÓ THỂ làm GÌ CŨNG ĐƯỢC
- Không cần credit
- Không cần giữ license
```

**Khi nào dùng?**
→ Muốn "gift to humanity", không quan tâm credit

**Ví dụ:** SQLite (Public domain)

---

## 8. Decision Tree: Chọn License nào?

```
START
│
├─ Muốn derivative works PHẢI open source?
│  ├─ YES → GPL (Desktop/CLI) hoặc AGPL (Web/SaaS)
│  └─ NO ↓
│
├─ Có patent concerns?
│  ├─ YES → Apache 2.0
│  └─ NO → MIT
│
└─ Không quan tâm gì cả? → Unlicense
```

---

## 9. Compliance: Sử dụng Open Source đúng

### **Khi dùng MIT/Apache library:**

✅ **Bạn PHẢI:**
1. Giữ file LICENSE trong code
2. Credit trong About/README
3. Không xóa copyright notice

✅ **KHÔNG PHẢI:**
- Share source code
- Open source project của bạn

---

### **Khi dùng GPL library:**

❗ **PHẢI:**
1. Open source toàn bộ project (nếu distribute)
2. License cũng phải GPL
3. Provide source code

⚠️ **Hoặc:**
- KHÔNG distribute (Internal use OK)
- Mua commercial license (Nếu có dual-license)

---

### **Red Flags - Tránh ngay:**

🚩 **KHÔNG BAO GIỜ:**
- Copy GPL code vào closed-source product (Kiện đến phá sản)
- Xóa license/copyright notice
- Claim code là của bạn

---

## 10. Dual Licensing

### **Ví dụ:** Qt, MySQL (trước đây)

**Model:**
- **GPL:** Free, nhưng phải open source derivative
- **Commercial:** Trả tiền, được dùng trong closed-source

**Khi nào dùng dual-licensing?**
→ Monetize open source project

---

## 11. License Compatibility

### **Có thể mix không?**

| Your Code | Library License | OK? | Note |
|-----------|----------------|-----|------|
| MIT | MIT | ✅ | Perfect |
| MIT | Apache | ✅ | OK |
| MIT | GPL | ❌ | Conflict! |
| Apache | GPL v3 | ✅ | Must become GPL |
| GPL | MIT | ✅ | Result = GPL |
| Closed | GPL | ❌ | Illegal! |

**Rule:** GPL "wins" - Everything becomes GPL

---

## 12. Common Scenarios

### **Q: Tôi fork MIT project, có phải open source không?**
**A:** KHÔNG. MIT cho phép closed-source derivative. Nhưng phải giữ copyright notice.

### **Q: Dùng GPL library trong SaaS có sao không?**
**A:** 
- **GPL:** OK (không distribute binary)
- **AGPL:** PHẢI open source (Network use = distribute)

### **Q: Làm sao biết library dùng license gì?**
**A:** Check file `LICENSE` hoặc `README.md` trong repo

### **Q: Không có license = Miễn phí?**
**A:** **KHÔNG!** Không có license = All rights reserved = Không được dùng

---

## 13. Checklist cho Developers

### **Khi release project:**
- [ ] Chọn license phù hợp
- [ ] Tạo file LICENSE ở root
- [ ] Ghi trong README.md
- [ ] Thêm header vào source files (Nếu GPL/Apache)

### **Khi sử dụng open source:**
- [ ] Check license của dependencies (`npm license-checker`)
- [ ] Đảm bảo compliant (Không mix GPL + Closed)
- [ ] Credit authors (MIT/Apache)
- [ ] Giữ LICENSE files

---

## 14. Tools hữu ích

**Check dependencies:**
```bash
# Node.js
npx license-checker --summary

# Python
pip-licenses

# Go
go-licenses check ./...
```

**Resources:**
- https://choosealicense.com - GitHub's tool
- https://tldrlegal.com - Plain English explanations
- https://opensource.org/licenses - Official OSI list

---

## 🔗 Guides Liên quan

- [IP Ownership](./ip-ownership.md) - Ai sở hữu code?
- [SaaS Legal](./saas-legal.md) - Terms of Service
- [Open Source Compliance](./open-source-compliance.md) - Chi tiết hơn

---

**💡 "License = Legal contract. Read before use. Choose carefully before release!"** ⚖️
