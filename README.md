<!-- BBN:HEADER:START -->
<div align="center">

<img src=".github/brand/banner.svg" width="100%" alt="BoomBigNose Plugins — Claude Code plugin for Thai quotations: HTML/PDF, VAT 7%" />

<a href="https://github.com/Boom-Vitt/boombignose-plugins/stargazers"><img src="https://img.shields.io/github/stars/Boom-Vitt/boombignose-plugins?style=flat-square&color=14b8a6&labelColor=0b1220" alt="stars" /></a>
<a href="https://github.com/Boom-Vitt/boombignose-plugins/commits/main"><img src="https://img.shields.io/github/last-commit/Boom-Vitt/boombignose-plugins?style=flat-square&color=14b8a6&labelColor=0b1220" alt="last commit" /></a>
<a href="https://github.com/Boom-Vitt"><img src="https://img.shields.io/badge/by-BoomBigNose-14b8a6?style=flat-square&labelColor=0b1220" alt="by BoomBigNose" /></a>

</div>
<!-- BBN:HEADER:END -->

# boombignose-plugins

Marketplace รวมปลั๊กอิน (plugins) สำหรับ **Claude Code** ของ **BoomBigNose** — เครื่องมือช่วยงานด้านเอกสารและการตลาด เพื่อให้ทีมทำงานได้เร็วขึ้นและได้ผลลัพธ์ที่สอดคล้องกับแบรนด์

- **เจ้าของ:** BoomBigNose
- **เว็บไซต์:** https://boombignose.org
- **อีเมล:** vittawat.soo@boombignose.org

---

## ปลั๊กอินใน marketplace นี้

### `thai-quotation` — ใบเสนอราคา (Thai Quotation)

สร้างใบเสนอราคาภาษาไทยอย่างมืออาชีพจากในแชต Claude Code โดยตรง

- คำนวณยอดรวม ส่วนลด และ **VAT 7%** ให้อัตโนมัติ
- แปลงจำนวนเงินรวมเป็น **ตัวอักษรภาษาไทย** (เช่น "หนึ่งหมื่นเจ็ดร้อยบาทถ้วน")
- ส่งออกเป็นไฟล์ **HTML** ที่จัดหน้าสวยงาม เปิดในเบราว์เซอร์แล้วสั่ง **พิมพ์เป็น PDF** (A4) ได้ทันที

เมื่อติดตั้งแล้ว เรียกใช้งานด้วยคำสั่ง:

```
/thai-quotation:quote
```

> ดูรายละเอียดการใช้งานเต็มได้ที่ [`plugins/thai-quotation/README.md`](./plugins/thai-quotation/README.md)

---

## การติดตั้ง

### 1) ติดตั้งจาก GitHub (สำหรับใช้งานจริง)

repo เผยแพร่แล้วที่ **https://github.com/Boom-Vitt/boombignose-plugins** — ติดตั้งได้ทันที:

```
/plugin marketplace add Boom-Vitt/boombignose-plugins
/plugin install thai-quotation@boombignose-plugins
```

> รูปแบบหลัง `@` คือ **ชื่อ marketplace** (`boombignose-plugins`) ไม่ใช่ path ของ repo

### 2) ติดตั้งจากเครื่อง local (สำหรับทดสอบ/พัฒนา)

```
/plugin marketplace add /absolute/path/to/boombignose-marketplace
/plugin install thai-quotation@boombignose-plugins
```

> **หมายเหตุสำคัญ:** ปลั๊กอินใน marketplace นี้ใช้ `source` แบบ relative (`./plugins/thai-quotation`)
> ซึ่ง **ต้องการ git context** ดังนั้นถ้าทดสอบจาก local ให้ init git ก่อน มิฉะนั้นอาจติดตั้งไม่สำเร็จ:
>
> ```bash
> git init
> git add -A
> git commit -m "init"
> ```

---

## คำสั่งที่ใช้บ่อย

| ต้องการ | คำสั่ง |
|---------|--------|
| รีโหลดปลั๊กอินหลังแก้ไฟล์ | `/reload-plugins` |
| ตรวจสอบความถูกต้องของ marketplace (รันจากโฟลเดอร์นี้) | `claude plugin validate .` |
| ตรวจสอบความถูกต้องของปลั๊กอิน | `claude plugin validate ./plugins/thai-quotation` |

---

## เผยแพร่ขึ้น GitHub

ขั้นตอนละเอียดในการ push marketplace นี้ขึ้น GitHub ด้วยตัวเอง อยู่ที่ [`PUBLISH.md`](./PUBLISH.md)

---

## โครงสร้างโฟลเดอร์

```
boombignose-marketplace/
├── .claude-plugin/
│   └── marketplace.json          # manifest ของ marketplace
├── plugins/
│   └── thai-quotation/
│       ├── .claude-plugin/
│       │   └── plugin.json        # manifest ของปลั๊กอิน
│       ├── commands/              # คำสั่ง (เช่น /thai-quotation:quote)
│       ├── skills/                # ความสามารถ + เทมเพลต + สคริปต์
│       └── README.md              # คู่มือระดับปลั๊กอิน
├── .gitignore
├── README.md                      # ไฟล์นี้
└── PUBLISH.md                     # ขั้นตอนเผยแพร่ขึ้น GitHub
```

---

## License

MIT

<!-- BBN:FOOTER:START -->
---

<div align="center">

**สร้างโดย [BoomBigNose](https://github.com/Boom-Vitt)** · [Kruoop.com](https://kruoop.com) แหล่งเรียน AI + คอมมูนิตี้ · [Seeneo.ai](https://seeneo.ai) · [YouTube 220K](https://www.youtube.com/@BoomBigNose)

<sub>ถ้าโปรเจกต์นี้มีประโยชน์ กด ⭐ ให้กำลังใจกันได้เลย</sub>

</div>
<!-- BBN:FOOTER:END -->
