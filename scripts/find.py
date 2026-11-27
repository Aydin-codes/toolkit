#!/usr/bin/env python3
"""Search the whole catalog without reading every page.

  python scripts/find.py "animated text effect react"
  python scripts/find.py "pdf from html" --free --verified -n 5
  python scripts/find.py fonts --branch frontend/type

Ranks by: words matched (name and use_when count most), then tier (default first),
verified before candidate, then popularity. Reads catalog/index.json (built by build.py).
"""
import argparse
import json
import math
import re
from pathlib import Path

INDEX = Path(__file__).resolve().parent.parent / "catalog" / "index.json"
TIER = {"default": 3, "alternatives": 2, "more": 1, "list": 1, "big_lists": 0.5, "paid": 0}
PAID = re.compile(r"\b(paid|commercial|subscription|proprietary)\b", re.I)


def score(e, words):
    fields = {"name": 3, "use_when": 2, "section": 2, "note": 1, "branch": 1, "install": 1, "license": 0.5}
    hit = 0.0
    for w in words:
        for k, weight in fields.items():
            if w in str(e.get(k, "")).lower():
                hit += weight
    if not hit:
        return 0
    pop = math.log10(1 + (e.get("stars") or 0) + (e.get("npm_weekly") or 0) / 10)
    return hit * 10 + TIER.get(e.get("tier"), 0) * 2 + (3 if e.get("status") == "verified" else 0) + pop


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--branch")
    ap.add_argument("--free", action="store_true", help="skip paid entries")
    ap.add_argument("--verified", action="store_true", help="only verified entries")
    ap.add_argument("-n", type=int, default=8)
    a = ap.parse_args()
    words = [w for w in re.split(r"\W+", a.query.lower()) if len(w) > 1]
    rows = []
    for e in json.loads(INDEX.read_text(encoding="utf-8")):
        if a.branch and not e.get("branch", "").startswith(a.branch):
            continue
        if a.free and (e.get("tier") == "paid" or PAID.search(str(e.get("license", "")))):
            continue
        if a.verified and e.get("status") != "verified":
            continue
        s = score(e, words)
        if s:
            rows.append((s, e))
    for s, e in sorted(rows, key=lambda r: -r[0])[: a.n]:
        extra = f" — use when {e['use_when']}" if e.get("use_when") else ""
        flags = " [never copy]" if e.get("never_copy") else ""
        print(f"{e['name']} <{e['url']}> [{e.get('branch')} > {e.get('section')} > {e.get('tier')}] "
              f"license: {e.get('license')}; {e.get('status')}{flags}{extra}")
    if not rows:
        print("no match; try fewer or broader words, or open the branch page")


if __name__ == "__main__":
    main()
