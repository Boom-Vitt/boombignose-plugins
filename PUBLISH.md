# คู่มือเผยแพร่ marketplace ขึ้น GitHub

เอกสารนี้อธิบายขั้นตอนการ push marketplace **`boombignose-plugins`** ขึ้น GitHub ด้วยตัวเอง
เพื่อให้ผู้ใช้คนอื่นติดตั้งปลั๊กอิน `thai-quotation` ได้

> ทำตามทีละขั้น คำสั่งทั้งหมดรันจาก terminal ในโฟลเดอร์ `boombignose-marketplace`

---

## ก่อนเริ่ม: เช็กลิสต์ก่อน publish

- [ ] **กรอกข้อมูลจริงของบริษัท** แทน placeholder ในเทมเพลต
      เช่น `[เลขประจำตัวผู้เสียภาษี 13 หลัก — โปรดระบุ]`, `[ที่อยู่บริษัท — โปรดระบุ]`, `[เบอร์โทร — โปรดระบุ]`
      (ดูไฟล์เทมเพลตใน `plugins/thai-quotation/skills/quotation/assets/`)
- [ ] ตรวจ **brand voice** ให้ตรงตาม `CLAUDE.md` — ทางการ อ่านง่าย น่าเชื่อถือ ไม่ overpromise
- [ ] ตรวจ JSON manifest ผ่าน (ดูหัวข้อ "ตรวจสอบก่อน push" ด้านล่าง)

---

## ขั้นที่ 0 — ตรวจว่าอยู่ในโฟลเดอร์ที่ถูกต้อง

ต้องอยู่ในโฟลเดอร์ `boombignose-marketplace` (โฟลเดอร์ที่มีไฟล์ `README.md` และโฟลเดอร์ `.claude-plugin/` นี้)

```bash
pwd
# ควรลงท้ายด้วย /boombignose-marketplace

ls
# ควรเห็น: README.md  PUBLISH.md  .gitignore  plugins/  (และ .claude-plugin/ แบบซ่อน)
```

---

## ขั้นที่ 1 — ตรวจสอบก่อน push (แนะนำ)

```bash
# ตรวจ JSON manifest ว่า valid (ไม่มี syntax error)
python3 -m json.tool .claude-plugin/marketplace.json > /dev/null && echo "marketplace.json OK"
python3 -m json.tool plugins/thai-quotation/.claude-plugin/plugin.json > /dev/null && echo "plugin.json OK"

# ตรวจด้วย Claude Code CLI (ถ้าติดตั้งไว้)
claude plugin validate .
claude plugin validate ./plugins/thai-quotation
```

---

## ขั้นที่ 2 — สร้าง git repo และ commit

```bash
git init
git add -A
git commit -m "feat: thai-quotation plugin"
```

---

## ขั้นที่ 3 — สร้าง repo บน GitHub แล้ว push

เลือกวิธีใดวิธีหนึ่ง

### วิธี A — ใช้ GitHub CLI (`gh`) — เร็วที่สุด

ถ้ามี [`gh`](https://cli.github.com/) ติดตั้งและ login แล้ว สร้าง repo + push ในคำสั่งเดียว:

```bash
gh repo create boombignose-plugins --public --source=. --remote=origin --push
```

> ต้องการ repo แบบส่วนตัว ให้เปลี่ยน `--public` เป็น `--private`

### วิธี B — สร้าง repo บนเว็บ GitHub แล้วเชื่อม remote เอง

1. ไปที่ https://github.com/new สร้าง repo ชื่อ **`boombignose-plugins`**
   - **อย่า** เลือกสร้าง README / .gitignore / license อัตโนมัติ (เรามีในเครื่องแล้ว เพื่อเลี่ยง conflict)
2. กลับมาที่ terminal แล้วเชื่อม remote + push:

```bash
git remote add origin https://github.com/Boom-Vitt/boombignose-plugins.git
git branch -M main
git push -u origin main
```

---

## ขั้นที่ 4 — ผู้ใช้คนอื่นติดตั้งได้แล้ว

หลัง push สำเร็จ แชร์คำสั่งนี้ให้ผู้ใช้คนอื่นติดตั้ง:

```
/plugin marketplace add Boom-Vitt/boombignose-plugins
/plugin install thai-quotation@boombignose-plugins
```

จากนั้นเรียกใช้งานด้วย `/thai-quotation:quote`

---

## ปล่อยอัปเดตเวอร์ชันใหม่ (สำคัญ)

> **ทุกครั้งที่แก้ไขปลั๊กอินแล้วต้องการให้ผู้ใช้เดิมได้ของใหม่ ต้อง bump `version` เสมอ**
> ถ้าไม่เพิ่มเลขเวอร์ชัน ผู้ใช้ที่ติดตั้งไว้แล้วจะ **ไม่ได้รับอัปเดต**

แก้ค่า `version` ให้ **ตรงกันทั้งสองไฟล์** (เช่น `0.1.0` → `0.1.1`):

1. `plugins/thai-quotation/.claude-plugin/plugin.json` → ฟิลด์ `version`
2. `.claude-plugin/marketplace.json` → ทั้งฟิลด์ `version` ระดับ marketplace **และ** `plugins[].version` ของ `thai-quotation`

แล้ว commit + push ตามปกติ:

```bash
git add -A
git commit -m "chore: bump thai-quotation to v0.1.1"
git push
```

> แนะนำให้ใช้ [Semantic Versioning](https://semver.org/lang/th/): แก้บั๊กเล็ก = patch (0.1.x), เพิ่มฟีเจอร์ = minor (0.x.0), เปลี่ยนแบบ breaking = major (x.0.0)

---

## ทดสอบ local ก่อน push (ทางเลือก)

อยากลองติดตั้งจากเครื่องก่อนเผยแพร่จริง ทำได้ — แต่ต้องมี git context ก่อน
(ปลั๊กอินใช้ `source` แบบ relative ซึ่งต้องการ git):

```bash
git init && git add -A && git commit -m "init"
```

จากนั้นใน Claude Code:

```
/plugin marketplace add /absolute/path/to/boombignose-marketplace
/plugin install thai-quotation@boombignose-plugins
```

หากแก้ไฟล์แล้วต้องการให้ Claude Code เห็นของใหม่ ใช้ `/reload-plugins`
