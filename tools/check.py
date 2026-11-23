#!/usr/bin/env python3
"""Checks every skill folder before a change is accepted.

Fails if a skill's name does not match its folder, a description is missing
or too long, a docs or testing page is missing, a download zip is missing,
or a file contains something that looks like an email address, a secret or
a private session link.
"""
import os, re, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
problems = []

def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and re.match(r"^[a-z-]+$", k):
            out[k] = v.strip().strip('"').replace('\\"', '"')
    return out

skills = sorted(os.listdir(os.path.join(ROOT, "skills")))
for name in skills:
    path = os.path.join(ROOT, "skills", name, "SKILL.md")
    if not os.path.isfile(path):
        problems.append(f"{name}: no SKILL.md"); continue
    fm = front_matter(open(path, encoding="utf-8").read())
    if fm is None:
        problems.append(f"{name}: no front matter"); continue
    if fm.get("name") != name:
        problems.append(f"{name}: front matter name is {fm.get('name')!r}")
    d = fm.get("description", "")
    if not d or len(d) > 1024:
        problems.append(f"{name}: description missing or over 1,024 characters ({len(d)})")
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
        problems.append(f"{name}: folder name is not lowercase-with-hyphens")
    for sub in ("docs", "testing"):
        if not os.path.isfile(os.path.join(ROOT, sub, name + ".md")):
            problems.append(f"{name}: missing {sub}/{name}.md")
    z = os.path.join(ROOT, "downloads", name + ".zip")
    if not os.path.isfile(z):
        problems.append(f"{name}: missing downloads/{name}.zip")
    else:
        with zipfile.ZipFile(z) as f:
            if f"{name}/SKILL.md" not in f.namelist():
                problems.append(f"{name}: zip has no {name}/SKILL.md")
            elif f.read(f"{name}/SKILL.md") != open(path, "rb").read():
                problems.append(f"{name}: zip is out of date; rebuild it")

readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
for name in skills:
    if f"(skills/{name}/)" not in readme:
        problems.append(f"{name}: not listed in README")

PATTERNS = {
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@(?!example\.|users\.noreply\.)[A-Za-z0-9-]+\.[A-Za-z]{2,}"),
    "session link": re.compile(r"claude\.ai/(code|chat)/"),
    "secret-like token": re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY)"),
}
for base, _, files in os.walk(ROOT):
    if ".git" in base.split(os.sep):
        continue
    for fn in files:
        if not fn.endswith((".md", ".py", ".json", ".html", ".yml")):
            continue
        p = os.path.join(base, fn)
        if os.path.relpath(p, ROOT) == os.path.join("tools", "check.py"):
            continue
        text = open(p, encoding="utf-8", errors="replace").read()
        for label, rx in PATTERNS.items():
            for m in rx.finditer(text):
                if label == "email address" and re.search(r"(\.example|@example\.(com|org|net))$", m.group(0)):
                    continue
                problems.append(f"{os.path.relpath(p, ROOT)}: {label}: {m.group(0)[:40]}")

if problems:
    print("\n".join(problems)); sys.exit(1)
print(f"OK: {len(skills)} skills checked")
