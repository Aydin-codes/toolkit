#!/usr/bin/env python3
"""Build reference/*.md from catalog/*.yaml.

  python scripts/build.py          write the pages
  python scripts/build.py --check  fail if a page is out of date or an entry is invalid (used in CI)
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
OUT = ROOT / "reference"
REQUIRED = ("name", "url", "search", "license", "status")
STATUSES = {"candidate", "verified", "declining"}
TIERS = ("default", "alternatives", "big_lists", "paid", "list")


def entry_errors(e, where):
    errs = [f"{where}: missing '{k}'" for k in REQUIRED if not e.get(k)]
    if e.get("status") and e["status"] not in STATUSES:
        errs.append(f"{where}: status must be one of {sorted(STATUSES)}")
    if e.get("url") and not str(e["url"]).startswith("https://"):
        errs.append(f"{where}: url must start with https://")
    return errs


def line(e, with_use_when=False):
    s = f"- [{e['name']}]({e['url']}) (search: {e['search']})"
    if with_use_when and e.get("use_when"):
        s += f": use when {e['use_when']}"
    s += f". License: {e['license']}."
    if e.get("install"):
        s += f" Install: `{e['install']}`." if not str(e["install"]).startswith(("download", "CDN", "self-host")) else f" Get it: {e['install']}."
    if e.get("never_copy"):
        s += " **Use only from the source; never copy its files or code into another repo.**"
    if e.get("note"):
        s += f" {e['note']}"
    if e["status"] != "verified":
        s += f" *({e['status']})*"
    return s


def render(doc, src):
    out = [
        f"# {doc['title']}",
        "",
        f"<!-- Generated from {src}. Edit the YAML, then run: python scripts/build.py -->",
        "",
        doc.get("intro", "").strip(),
    ]
    if doc.get("notice"):
        out += ["", f"> **Note:** {doc['notice'].strip()}"]
    out.append("")
    for sec in doc.get("sections", []):
        out += [f"## {sec['name']}", ""]
        if sec.get("note"):
            out += [sec["note"].strip(), ""]
        if sec.get("default"):
            out += ["**Default**", "", line(sec["default"]), ""]
        if sec.get("alternatives"):
            out += ["**Strong alternatives**", ""] + [line(e, True) for e in sec["alternatives"]] + [""]
        if sec.get("big_lists"):
            out += ["**Big lists**", ""] + [line(e) for e in sec["big_lists"]] + [""]
        if sec.get("list"):
            out += [line(e, True) for e in sec["list"]] + [""]
        if sec.get("paid"):
            out += ["**Paid** (only when asked, or when no free option fits)", ""] + [line(e) for e in sec["paid"]] + [""]
    return "\n".join(out).rstrip() + "\n"


def main():
    check = "--check" in sys.argv
    errors, stale, counts = [], [], {s: 0 for s in STATUSES}
    for path in sorted(CATALOG.rglob("*.yaml")):
        rel = path.relative_to(ROOT).as_posix()
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        for k in ("branch", "title", "sections"):
            if not doc.get(k):
                errors.append(f"{rel}: missing '{k}'")
        names = set()
        for i, sec in enumerate(doc.get("sections") or []):
            for tier in TIERS:
                items = sec.get(tier)
                if items is None:
                    continue
                if tier == "alternatives" and not 1 <= len(items) <= 5:
                    errors.append(f"{rel} > {sec.get('name', i)}: alternatives must be 1-5 (has {len(items)})")
                for j, e in enumerate(items if isinstance(items, list) else [items]):
                    where = f"{rel} > {sec.get('name', i)} > {tier}[{j}]"
                    errors += entry_errors(e, where)
                    if e.get("name") in names:
                        errors.append(f"{where}: duplicate name '{e['name']}'")
                    names.add(e.get("name"))
                    if e.get("status") in counts:
                        counts[e["status"]] += 1
        if errors:
            continue
        target = OUT / f"{doc['branch']}.md"
        text = render(doc, rel)
        if check:
            if not target.exists() or target.read_text(encoding="utf-8") != text:
                stale.append(target.relative_to(ROOT).as_posix())
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            print("wrote", target.relative_to(ROOT).as_posix())
    for e in errors:
        print("ERROR", e)
    for s in stale:
        print("OUT OF DATE", s, "(run: python scripts/build.py)")
    print("entries:", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    sys.exit(1 if errors or stale else 0)


if __name__ == "__main__":
    main()
