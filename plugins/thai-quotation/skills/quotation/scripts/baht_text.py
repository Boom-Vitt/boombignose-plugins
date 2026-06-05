#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""baht_text.py — แปลงจำนวนเงินเป็นข้อความ "บาทถ้วน" ภาษาไทย

ใช้เฉพาะ Python 3 standard library (ZERO external dependencies)

วิธีเรียกใช้:
    python3 baht_text.py <amount>
    เช่น  python3 baht_text.py 10700     -> หนึ่งหมื่นเจ็ดร้อยบาทถ้วน
          python3 baht_text.py 1234.50   -> หนึ่งพันสองร้อยสามสิบสี่บาทห้าสิบสตางค์
          python3 baht_text.py 0.25       -> ยี่สิบห้าสตางค์

อัลกอริทึม (โดยสรุป):
1. parse argument ด้วย decimal.Decimal (กันปัญหา float ปัดเศษเพี้ยน) แล้ว
   quantize เป็น 2 ตำแหน่งแบบ ROUND_HALF_UP (ตามมาตรฐาน Excel BAHTTEXT)
2. แยกเป็นจำนวนเต็ม "บาท" และ "สตางค์" (0–99)
3. อ่านจำนวนเต็มด้วย reader แบบ single-pass ไล่ทีละหลักจากซ้ายไปขวา:
   - ใช้ตำแหน่งจากขวา (pos) -> p = pos % 6 เลือกคำหลัก
     ['','สิบ','ร้อย','พัน','หมื่น','แสน'] และเติม "ล้าน" ทุกครั้งที่
     ข้ามขอบเขตหลักล้าน (pos>0 และ pos%6==0)
   - หลักสิบ: 1->"สิบ", 2->"ยี่สิบ", อื่น ๆ -> <เลข>+"สิบ"
   - หลักหน่วย: เลข 1 จะเป็น "เอ็ด" ก็ต่อเมื่อ "ไม่ใช่หลักซ้ายสุดของทั้งจำนวน"
     (กฎ เอ็ด เป็นกฎระดับทั้งจำนวน ไม่ใช่ต่อกลุ่มล้าน) — ทำให้
     1,000,001 -> "หนึ่งล้านเอ็ดบาทถ้วน" ถูกต้อง
4. ประกอบผลลัพธ์:
   - บาท>0, สตางค์=0  -> "<บาท>บาทถ้วน"
   - บาท>0, สตางค์>0  -> "<บาท>บาท<สตางค์>สตางค์"
   - บาท=0, สตางค์>0  -> "<สตางค์>สตางค์"        (ไม่ขึ้นต้นด้วย "ศูนย์บาท")
   - บาท=0, สตางค์=0  -> "ศูนย์บาทถ้วน"
   - จำนวนติดลบ -> ใส่ "ลบ" นำหน้า

ข้อจำกัด: ดู references/baht-text.md
"""

import sys
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

# คำอ่านเลข 0-9 (ใช้กับทุกหลักยกเว้นกรณีพิเศษหลักสิบ/หลักหน่วย)
DIGITS = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

# คำหลักตามตำแหน่ง (วนซ้ำทุก 6 หลักด้วยหลัก "ล้าน")
# index = ตำแหน่งจากขวา mod 6
PLACES = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน"]


def _read_integer(num: int) -> str:
    """อ่านจำนวนเต็มไม่ติดลบ (num >= 0) เป็นข้อความไทย (ยังไม่รวมคำว่า 'บาท')

    ใช้วิธี single-pass ไล่ทีละหลักของ str(num) จากซ้าย (MSD) ไปขวา (หลักหน่วย)
    กฎ "เอ็ด" เป็นกฎระดับทั้งจำนวน: เลข 1 ในหลักหน่วยจะอ่าน "เอ็ด"
    ก็ต่อเมื่อมันไม่ใช่หลักซ้ายสุด (index i != 0)
    """
    if num == 0:
        return DIGITS[0]  # "ศูนย์"

    s = str(num)
    n = len(s)
    parts = []

    for i, ch in enumerate(s):
        d = ord(ch) - 48  # แปลงตัวอักษรเลขเป็น int เร็ว ๆ
        pos = n - 1 - i    # ตำแหน่งจากขวา (หลักหน่วย = 0)
        p = pos % 6        # หลักภายในกลุ่มล้าน: 0..5

        if d != 0:
            if p == 1:
                # หลักสิบ: 1->"สิบ", 2->"ยี่สิบ", อื่น ๆ -> <เลข>"สิบ"
                if d == 1:
                    parts.append("สิบ")
                elif d == 2:
                    parts.append("ยี่สิบ")
                else:
                    parts.append(DIGITS[d] + "สิบ")
            elif p == 0:
                # หลักหน่วย: เลข 1 -> "เอ็ด" ถ้าไม่ใช่หลักซ้ายสุดของทั้งจำนวน
                if d == 1 and i != 0:
                    parts.append("เอ็ด")
                else:
                    parts.append(DIGITS[d])
            else:
                # หลักร้อย/พัน/หมื่น/แสน: <เลข> + คำหลัก
                parts.append(DIGITS[d] + PLACES[p])

        # เติม "ล้าน" เมื่อจบกลุ่ม  6 หลัก (และยังไม่ถึงหลักหน่วยสุดท้าย)
        # ใช้ pos>0 เพื่อไม่เติมหลังหลักหน่วย; pos%6==0 = ขอบเขตล้าน
        if pos > 0 and pos % 6 == 0:
            parts.append("ล้าน")

    return "".join(parts)


def baht_text(amount: float) -> str:
    """แปลงจำนวนเงิน (รับ float/int/str/Decimal) เป็นข้อความบาทถ้วนภาษาไทย

    ปัดเศษเป็น 2 ตำแหน่งแบบ ROUND_HALF_UP ก่อนแปลงเสมอ
    """
    # รับได้ทั้ง str/int/float/Decimal — แปลงผ่าน str เพื่อให้ Decimal
    # อ่านค่าตามที่พิมพ์มาจริง (กัน float binary repr เพี้ยน เช่น 0.1)
    if isinstance(amount, Decimal):
        value = amount
    else:
        value = Decimal(str(amount))

    # ปัดเป็น 2 ตำแหน่งแบบ half-up ตามมาตรฐาน Excel BAHTTEXT
    value = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    negative = value < 0
    value = abs(value)

    # แยกบาท/สตางค์เป็นจำนวนเต็ม
    baht = int(value)                       # ส่วนจำนวนเต็ม
    satang = int((value - baht) * 100)      # 0..99 (ค่าปัดแล้วจึงลงตัวเสมอ)

    if baht == 0 and satang == 0:
        text = DIGITS[0] + "บาทถ้วน"        # "ศูนย์บาทถ้วน"
    elif satang == 0:
        text = _read_integer(baht) + "บาทถ้วน"
    elif baht == 0:
        # 0 บาทแต่มีสตางค์ -> ขึ้นต้นด้วยสตางค์เลย
        text = _read_integer(satang) + "สตางค์"
    else:
        text = _read_integer(baht) + "บาท" + _read_integer(satang) + "สตางค์"

    if negative:
        text = "ลบ" + text

    return text


def main(argv) -> int:
    if len(argv) != 2:
        sys.stderr.write(
            "ข้อผิดพลาด: ต้องระบุจำนวนเงิน 1 ค่า\n"
            "วิธีใช้: python3 baht_text.py <amount>\n"
            "ตัวอย่าง: python3 baht_text.py 10700\n"
        )
        return 2

    raw = argv[1].strip()
    try:
        # parse ด้วย Decimal — รองรับ int/ทศนิยม และจับ input ผิดรูป
        value = Decimal(raw)
    except (InvalidOperation, ValueError):
        sys.stderr.write(f"ข้อผิดพลาด: '{raw}' ไม่ใช่จำนวนเงินที่ถูกต้อง\n")
        return 1

    # ปฏิเสธค่าที่ไม่ใช่ตัวเลขจำกัด (NaN / Infinity ที่ Decimal ยอมรับ)
    if not value.is_finite():
        sys.stderr.write(f"ข้อผิดพลาด: '{raw}' ไม่ใช่จำนวนเงินที่ถูกต้อง\n")
        return 1

    sys.stdout.write(baht_text(value) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
