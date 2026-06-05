---
name: quotation
description: ใช้เมื่อผู้ใช้ต้องการสร้าง ออก หรือทำใบเสนอราคา (quotation) ภาษาไทยสำหรับลูกค้า — auto-invoke เมื่อผู้ใช้พิมพ์ทำนองว่า "ออกใบเสนอราคา", "ทำใบเสนอราคา", "สร้างใบเสนอราคา", "สร้าง quotation", "ขอใบเสนอราคา", "เสนอราคาลูกค้า", "ทำใบเสนอราคาให้ลูกค้า X", "quote ราคา", "ใบ quotation", "เสนอราคางาน". สร้างเอกสารใบเสนอราคา HTML (พิมพ์เป็น PDF ได้) คิด VAT 7% และจำนวนเงินเป็นตัวอักษร (บาทถ้วน) อัตโนมัติ. Use when the user wants to create or issue a Thai-language price quotation.
---

# ออกใบเสนอราคาภาษาไทย (Thai Quotation)

Skill นี้ช่วยสร้าง **ใบเสนอราคา (Quotation)** ภาษาไทยให้ลูกค้า ในรูปแบบไฟล์ HTML ที่ออกแบบมาให้พิมพ์เป็น PDF ขนาด A4 ได้สวยงาม คิด VAT 7% และแปลงยอดรวมเป็นตัวอักษรไทย (บาทถ้วน) อัตโนมัติ โดยมีข้อมูลผู้ขาย BoomBigNose ตั้งต้นให้แล้ว

## 1. เมื่อไรใช้ skill นี้
ใช้เมื่อผู้ใช้ต้องการ **สร้าง / ออก / ทำใบเสนอราคาให้ลูกค้า** ไม่ว่าจะพูดว่า "ออกใบเสนอราคา", "ทำ quotation", "เสนอราคาลูกค้า X เป็นเงินเท่านี้" ฯลฯ ผลลัพธ์คือไฟล์ `ใบเสนอราคา-{DOC_NO}.html` ที่ผู้ใช้เปิดในเบราว์เซอร์แล้ว Save เป็น PDF ส่งลูกค้าได้

## 2. ข้อมูลที่ต้องเก็บจากผู้ใช้ (ถ้าขาด ให้ถามก่อนสร้าง)
ก่อนสร้างเอกสาร ตรวจว่ามีข้อมูลครบ ถ้าขาดส่วนที่จำเป็น **ให้ถามผู้ใช้ทีละขั้นสั้น ๆ** (อย่าเดา อย่าแต่งตัวเลข):

**จำเป็น (ขาดไม่ได้ — ต้องถาม):**
- **ข้อมูลลูกค้า (ผู้ซื้อ):** ชื่อ/บริษัท → `{{BUYER_NAME}}`. ถ้ามี: ที่อยู่ → `{{BUYER_ADDRESS}}`, ผู้ติดต่อ → `{{BUYER_CONTACT}}`, เลขประจำตัวผู้เสียภาษี → `{{BUYER_TAXID}}`
- **รายการสินค้า/บริการ อย่างน้อย 1 รายการ** แต่ละรายการต้องมี: รายละเอียด (desc), จำนวน (qty), หน่วย (unit เช่น ชิ้น/งาน/ชั่วโมง), ราคาต่อหน่วย (unit_price)

**มีค่า default (ถ้าผู้ใช้ไม่ระบุ ใช้ค่า default ได้เลย ไม่ต้องถาม):**
- **ส่วนลด** → ถ้าไม่ระบุ = `0`
- **VAT 7%** → ค่าเริ่มต้น **คิด** (`VAT_RATE = 7`). คิดก็ต่อเมื่อผู้ใช้บอกว่า "ไม่คิด VAT" จึงตั้ง vat = 0 (ดูข้อ 4)
- **เลขที่เอกสาร** → ถ้าไม่ระบุ ให้ generate รูปแบบ `QT-2569-NNN` (พ.ศ. + running 3 หลัก เช่น `QT-2569-001`) → `{{DOC_NO}}`
- **วันที่ออก** → default = วันนี้ (2026-06-05 = 5 มิถุนายน 2569) → `{{DOC_DATE}}` (รูปแบบไทย พ.ศ.)
- **ยืนราคาถึง** → default = วันที่ออก + 30 วัน → `{{VALID_UNTIL}}` (รูปแบบไทย พ.ศ.)
- **เงื่อนไขการชำระเงิน** → `{{PAYMENT_TERMS}}` (ถ้าไม่ระบุ ใส่ค่ากลาง ๆ เช่น "ชำระเต็มจำนวนภายใน 7 วันหลังตอบรับใบเสนอราคา" — หรือถามถ้าผู้ใช้อยากระบุเอง)
- **กำหนดส่งมอบ** → `{{DELIVERY_TERMS}}` (ถ้าไม่ระบุ ใส่ "ตามตกลง")
- **หมายเหตุ** → `{{NOTES}}` (ถ้าไม่มี เว้น "-")
- **ผู้เสนอราคา** → `{{PREPARED_BY}}` (default จากผู้ขาย เช่น "BoomBigNose")

## 3. ข้อมูลผู้ขาย (seller) — ค่าตั้งต้น BoomBigNose
ใช้ค่าตั้งต้นจาก CLAUDE.md (single source of truth):
- `{{SELLER_NAME}}`   = `BoomBigNose`
- `{{SELLER_EMAIL}}`  = `vittawat.soo@boombignose.org`
- `{{SELLER_WEBSITE}}`= `https://boombignose.org`

**ข้อมูลที่ไม่มีใน CLAUDE.md — ห้ามแต่งขึ้นเอง** ให้ใส่ placeholder ที่มองเห็นชัด หรือถามผู้ใช้ก่อน:
- `{{SELLER_ADDRESS}}` = `[ที่อยู่บริษัท — โปรดระบุ]`
- `{{SELLER_TAXID}}`   = `[เลขประจำตัวผู้เสียภาษี 13 หลัก — โปรดระบุ]`
- `{{SELLER_PHONE}}`   = `[เบอร์โทร — โปรดระบุ]`

> ถ้าผู้ใช้ให้เลขภาษี/ที่อยู่/เบอร์จริงมา ให้แทนค่าจริง มิฉะนั้นคง placeholder ไว้และแจ้งผู้ใช้ว่าให้กรอกก่อนส่งจริง **ห้าม hallucinate ตัวเลขหรือข้อเท็จจริงใด ๆ** (CLAUDE.md ข้อ 3)

## 4. การคำนวณ (ทำตามนี้เป๊ะ)
ทำตามลำดับ และปัดทศนิยม **2 ตำแหน่ง**:
1. แต่ละรายการ: `amount = qty × unit_price` (ปัด 2 ตำแหน่ง)
2. `subtotal = Σ amount` (ผลรวม amount ทุกแถว) → `{{SUBTOTAL}}`
3. `after_discount = subtotal − discount` (discount default 0) → `{{DISCOUNT}}`, `{{AFTER_DISCOUNT}}`
4. **VAT (ค่าเริ่มต้นคิด 7%):** `vat = round(after_discount × 0.07, 2)` → `{{VAT}}`, `{{VAT_RATE}}` = `7`
   - ถ้าผู้ใช้ระบุ **ไม่คิด VAT** → `vat = 0` และ `{{VAT_RATE}}` = `0`
5. `grand_total = after_discount + vat` → `{{GRAND_TOTAL}}`
6. **format เงินทุกช่อง:** คั่นหลักพันด้วย comma + ทศนิยม 2 ตำแหน่งเสมอ (เช่น `1500` → `1,500.00`; `10700` → `10,700.00`)
   - ใช้กับทุก token เงิน: `{{SUBTOTAL}}`,`{{DISCOUNT}}`,`{{AFTER_DISCOUNT}}`,`{{VAT}}`,`{{GRAND_TOTAL}}` และค่า `{{qty}}`/`{{unit_price}}`/`{{amount}}` ในแต่ละแถว
7. `amount_in_words` = บาทถ้วนของ `grand_total` — **ต้องได้จากการรัน baht_text.py เท่านั้น (ดูข้อ 5)** ห้ามคำนวณ/เดาด้วยมือ

## 5. จำนวนเงินเป็นตัวอักษร — บังคับรัน baht_text.py (ห้ามเดามือ)
หลังได้ `grand_total` (ตัวเลขดิบ ไม่ใส่ comma) ให้รันสคริปต์เพื่อได้ `{{AMOUNT_IN_WORDS}}`:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/quotation/scripts/baht_text.py" <grand_total>
```

ตัวอย่าง: ถ้า grand_total = 10700 →
```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/quotation/scripts/baht_text.py" 10700
# output: หนึ่งหมื่นเจ็ดร้อยบาทถ้วน
```
เอาต์พุตเป็นข้อความบรรทัดเดียว (บาทถ้วนภาษาไทย) → นำไปใส่ `{{AMOUNT_IN_WORDS}}` ตรง ๆ

**Fallback ถ้า `$CLAUDE_PLUGIN_ROOT` ว่าง/ไม่ตั้ง:** สคริปต์ `baht_text.py` อยู่ในโฟลเดอร์ `scripts/` ข้าง ๆ ไฟล์ SKILL.md นี้ (คือ `skills/quotation/scripts/baht_text.py`). หา absolute path จริงของไฟล์นั้น (เช่น `find` ใต้ marketplace หรือเทียบจากตำแหน่ง SKILL.md) แล้วรัน:
```bash
python3 "/absolute/path/.../skills/quotation/scripts/baht_text.py" <grand_total>
```

> **ห้ามแปลงตัวเลขเป็นคำด้วยตัวเองเด็ดขาด** — baht_text.py คือแหล่งความจริงเดียวของ `{{AMOUNT_IN_WORDS}}` (contract ข้อ 4.7 + ข้อ 5)

## 6. สร้างไฟล์ output
1. **อ่าน** `assets/template.html` (อยู่ใน `skills/quotation/assets/template.html`) — **ห้ามแก้ไฟล์ต้นฉบับ** อ่านมาเป็น string เท่านั้น
2. **สร้างแถวรายการ** สำหรับ `{{ITEMS_ROWS}}`: ต่อ 1 รายการ = 1 `<tr>` ตามรูปแบบนี้เป๊ะ (class names ห้ามเปลี่ยน — template มี CSS รองรับ):
   ```html
   <tr>
     <td class="col-no">{{no}}</td>
     <td class="col-desc">{{desc}}</td>
     <td class="col-qty">{{qty}}</td>
     <td class="col-unit">{{unit}}</td>
     <td class="col-price">{{unit_price}}</td>
     <td class="col-amount">{{amount}}</td>
   </tr>
   ```
   - `{{no}}` = ลำดับ 1,2,3...; `{{qty}}`,`{{unit_price}}`,`{{amount}}` = string ที่ format แล้ว (comma + 2 ทศนิยม เช่น `1,500.00`)
   - นำทุก `<tr>` มาต่อกันแล้วใช้แทน token `{{ITEMS_ROWS}}` ทั้งก้อน
3. **แทน token `{{...}}` ทุกตัวด้วยค่าจริง** ในเนื้อ template ครบทั้ง 25 token:
   `{{DOC_NO}}`,`{{DOC_DATE}}`,`{{VALID_UNTIL}}`,`{{SELLER_NAME}}`,`{{SELLER_ADDRESS}}`,`{{SELLER_TAXID}}`,`{{SELLER_PHONE}}`,`{{SELLER_EMAIL}}`,`{{SELLER_WEBSITE}}`,`{{BUYER_NAME}}`,`{{BUYER_ADDRESS}}`,`{{BUYER_CONTACT}}`,`{{BUYER_TAXID}}`,`{{ITEMS_ROWS}}`,`{{SUBTOTAL}}`,`{{DISCOUNT}}`,`{{AFTER_DISCOUNT}}`,`{{VAT_RATE}}`,`{{VAT}}`,`{{GRAND_TOTAL}}`,`{{AMOUNT_IN_WORDS}}`,`{{PAYMENT_TERMS}}`,`{{DELIVERY_TERMS}}`,`{{NOTES}}`,`{{PREPARED_BY}}`
4. **เขียนไฟล์ใหม่** ที่ **working directory ของผู้ใช้** (ไม่ใช่ในโฟลเดอร์ plugin) ชื่อ:
   ```
   ใบเสนอราคา-{DOC_NO}.html
   ```
   เช่น `ใบเสนอราคา-QT-2569-001.html`

## 7. ปิดท้าย — บอกผู้ใช้วิธีทำเป็น PDF
หลังเขียนไฟล์เสร็จ แจ้งผู้ใช้:
1. เปิดไฟล์ `ใบเสนอราคา-{DOC_NO}.html` ในเบราว์เซอร์ (ดับเบิลคลิก)
2. กด **Print** (Cmd+P บน Mac / Ctrl+P บน Windows)
3. เลือก **Save as PDF**
4. ตั้งค่า: ขนาด **A4**, ขอบ (Margins) = **Default**, **เปิด Background graphics** เพื่อให้สี/พื้นหลังติดในไฟล์ PDF

## 8. กฎ DRAFT และความปลอดภัย (สำคัญ)
- ทุกใบที่สร้างถือเป็น **DRAFT — ยังไม่ได้อนุมัติ** จนกว่าผู้ใช้จะยืนยัน (CLAUDE.md ข้อ 4) — แจ้งสถานะนี้ชัดเจนทุกครั้งที่ส่งมอบไฟล์
- **template.html มีลายน้ำ (watermark) "DRAFT — ยังไม่ได้อนุมัติ" ฝังอยู่ในตัวเอกสารแล้ว** (element `<div class="draft-watermark">`) ดังนั้นไฟล์ผลลัพธ์/PDF จะมีเครื่องหมาย DRAFT ติดไปด้วยเสมอ — **ห้ามลบลายน้ำนี้ออกเองโดยพลการ**
- **วิธีถอดลายน้ำเมื่ออนุมัติแล้ว:** ต่อเมื่อผู้ใช้ยืนยัน/อนุมัติชัดเจน ให้ลบทั้ง `<div class="draft-watermark">...</div>` (และคอมเมนต์เหนือมัน) ออกจากไฟล์ผลลัพธ์ แล้วบันทึกเป็นฉบับจริง (เช่น `ใบเสนอราคา-{DOC_NO}-final.html`) — CSS `.draft-watermark` ที่เหลือใน `<style>` ไม่ต้องลบก็ได้ (ไม่มีผลเมื่อไม่มี element)
- **ห้ามส่งออกภายนอก** (อีเมล/โพสต์/ส่งลูกค้า) โดยไม่ได้รับอนุมัติจากผู้ใช้ก่อน (CLAUDE.md ข้อ 1)
- **ห้าม hallucinate** ตัวเลข ราคา หรือข้อมูลบริษัท — ใช้เฉพาะข้อมูลที่ผู้ใช้ให้/CLAUDE.md/ผลจากสคริปต์ (CLAUDE.md ข้อ 3)
- ถ้าใช้ placeholder ผู้ขาย (`[... — โปรดระบุ]`) ค้างอยู่ ให้เตือนผู้ใช้ว่าต้องกรอกเลขภาษี/ที่อยู่/เบอร์จริงก่อนนำไปใช้จริง

## 9. Checklist ก่อนส่งมอบ
ตรวจให้ครบทุกข้อก่อนแจ้งผู้ใช้ว่าเสร็จ:
- [ ] แทน token ครบ — ค้นไฟล์ผลลัพธ์แล้ว **ไม่เหลือ `{{` หรือ `}}`** ใด ๆ
- [ ] ยอดรวมถูกต้อง — `grand_total = after_discount + vat`; ทุกช่องเงินมี comma + 2 ทศนิยม
- [ ] `{{AMOUNT_IN_WORDS}}` มาจากการรัน `baht_text.py` จริง (ไม่ได้พิมพ์เอง)
- [ ] ข้อมูลบริษัทไม่ได้แต่งขึ้น — placeholder ที่ไม่มีข้อมูลจริงยังเป็น `[... — โปรดระบุ]`
- [ ] ไฟล์ชื่อ `ใบเสนอราคา-{DOC_NO}.html` อยู่ที่ working directory ของผู้ใช้
- [ ] ไฟล์ผลลัพธ์ยังมีลายน้ำ `<div class="draft-watermark">` ติดอยู่ (ฉบับร่าง)
- [ ] แจ้งสถานะ **DRAFT — ยังไม่ได้อนุมัติ** + วิธี Save as PDF
