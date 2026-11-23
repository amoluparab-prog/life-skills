#!/usr/bin/env python3
"""Rebuilds downloads/<skill>.zip for every skill. Run after changing a skill."""
import os, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(ROOT, "downloads"), exist_ok=True)
for name in sorted(os.listdir(os.path.join(ROOT, "skills"))):
    with zipfile.ZipFile(os.path.join(ROOT, "downloads", name + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for base, _, files in sorted(os.walk(os.path.join(ROOT, "skills", name))):
            for fn in sorted(files):
                p = os.path.join(base, fn)
                info = zipfile.ZipInfo(os.path.relpath(p, os.path.join(ROOT, "skills")), date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                z.writestr(info, open(p, "rb").read())
print("zips rebuilt")
