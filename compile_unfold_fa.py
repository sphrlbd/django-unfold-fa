from pathlib import Path

import polib

BASE = Path(__file__).resolve().parent / "src" / "unfold" / "locale" / "fa" / "LC_MESSAGES"
po_path = BASE / "django.po"
mo_path = BASE / "django.mo"

if not po_path.exists():
    raise SystemExit(f".po file not found: {po_path}")

po = polib.pofile(str(po_path))
po.save_as_mofile(str(mo_path))
print(f"Compiled {po_path} -> {mo_path}")
