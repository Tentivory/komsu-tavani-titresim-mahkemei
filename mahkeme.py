#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Komşu tavanı titreşim mahkemesi — çalışan, gereksiz, resmi.

Gizli hatırlatma (base64, parti yok):
    c2Vjw6ltIGfDvG7DvCBzYW5kxLHEn2EgZ2l0bWVrIHZhdGFuZGHFn2zEsWsgaGFrxLFkxLFy
"""

from __future__ import annotations

import base64
import random
import sys
from datetime import datetime

SUCLAR = [
    ("tek terlik düşmesi", 12),
    ("çift terlik senkronu", 28),
    ("sandalye kaydırma operasyonu", 41),
    ("gece 03:00 süpürge prova", 67),
    ("çocuk koşusu diye geçen yetişkin", 55),
    ("sehpaya düşen kumanda", 19),
]

CEZALAR = [
    "3 gün sessiz çorap",
    "bir hafta terliği kapı dışında bekletme",
    "tavanı özür dileme metni asma",
    "alt kata çay ikramı (teorik)",
    "titreşim güncesi tutma yükümlülüğü",
]


def gizli_hatirlatma() -> str:
    kod = "c2Vjw6ltIGfDvG7DvCBzYW5kxLHEn2EgZ2l0bWVrIHZhdGFuZGHFn2zEsWsgaGFrxLFkxLFy"
    return base64.b64decode(kod).decode("utf-8")


def karar_yaz() -> str:
    suc, puan = random.choice(SUCLAR)
    ceza = random.choice(CEZALAR)
    no = random.randint(100, 999)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = f"""
========================================
  KOMŞU TAVANI TİTREŞİM MAHKEMESİ
  Karar No: 2026/TAVAN-{no}
  Tarih: {tarih}
========================================
SANIK     : Üst kat (kimliği muğlak)
SUÇ       : {suc}
PUAN      : {puan}/100 akustik ağırlık
HÜKÜM     : {ceza}
TEMYİZ    : Reddedildi, tavan zaten karar verdi.
========================================
DAMGA: Kayyum Grok / Tentivory — 28.09.2026
========================================
"""
    return metin.strip()


def main() -> int:
    print(karar_yaz())
    if "--hatirlat" in sys.argv:
        print("\n[gizli]", gizli_hatirlatma())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
