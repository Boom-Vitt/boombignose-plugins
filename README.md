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

แทนที่ `<owner>` ด้วยชื่อผู้ใช้/องค์กร GitHub ที่ใช้ push repo นี้ (repo ชื่อ `boombignose-plugins`)

```
/plugin marketplace add <owner>/boombignose-plugins
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
