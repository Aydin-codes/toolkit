#!/usr/bin/env python3
"""Check every https link in catalog/ and the .md files. Standard library only.

  python scripts/check_links.py
"""
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"https://[^\s)\"'<>`\]]+")
SKIP = ("github.com/Aydin-codes/toolkit",)  # not public yet
HEADERS = {"User-Agent": "Mozilla/5.0 (toolkit link check)"}


def urls():
    found = {}
    for p in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.yaml")):
        if ".git" in p.parts:
            continue
        for u in URL.findall(p.read_text(encoding="utf-8")):
            u = u.rstrip(".,;:")
            if not any(s in u for s in SKIP):
                found.setdefault(u, p.relative_to(ROOT).as_posix())
    return found


def check(u):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, method=method, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as r:
                return u, r.status
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405):
                return u, e.code
        except Exception as e:
            if method == "GET":
                return u, type(e).__name__
    return u, "?"


def main():
    found = urls()
    bad = []
    with ThreadPoolExecutor(8) as pool:
        for u, code in pool.map(check, found):
            ok = code in (200, 206, 429)
            print("ok " if ok else "BAD", code, u)
            if not ok:
                bad.append((u, code, found[u]))
    print(f"\n{len(found) - len(bad)} ok, {len(bad)} broken")
    for u, code, f in bad:
        print(f"  {code}  {u}  (in {f})")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
