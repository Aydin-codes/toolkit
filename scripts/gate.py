#!/usr/bin/env python3
"""Set each entry's status from its facts. No AI involved; the rules are below.

An entry is auto-verified (status: verified, verified_by: auto) when ALL of these hold:
  1. its link works (200, 206 or 429)
  2. it has a license, and the license is backed by evidence:
       - code: the GitHub or npm license matches what the entry says, or
       - anything else: a `license_url` that opens
  3. code only: not archived, pushed in the last 365 days,
     and at least 100 GitHub stars or 500 npm downloads a week
Code that is archived or untouched for 2+ years becomes `declining`.
Everything else stays `candidate`, with the reasons in `problems:`.
Entries with `hold:` stay candidate until a person removes it.
Entries marked `verified_by: human` keep their status unless the code is archived or abandoned.

  python scripts/gate.py           gate catalog/ and the inbox
  python scripts/gate.py --inbox   only the inbox
"""
import sys
from datetime import date, timedelta

from catalog import branch_files, inbox_files, is_code, load, save, walk

OK_LINK = (200, 206, 429)
MIN_STARS, MIN_WEEKLY = 100, 500
UNKNOWN = {"", "unknown", "noassertion", "other", "none"}


def days_since(d):
    try:
        return (date.today() - date.fromisoformat(d)).days
    except Exception:
        return None


def license_backed(e, f):
    lic = str(e.get("license") or "").lower()
    if lic in UNKNOWN:
        return False, "no license"
    if is_code(e):
        for key in ("gh_license", "npm_license"):
            spdx = str(f.get(key) or "").lower()
            if spdx and spdx not in UNKNOWN:
                if spdx.replace("-", "") in lic.replace("-", "") or lic.replace("-", "") in spdx.replace("-", ""):
                    return True, None
                return False, f"license says '{e['license']}' but {key} is {f[key]}"
    if e.get("license_url") and f.get("license_link") in OK_LINK:
        return True, None
    return False, "license has no evidence (add license_url)"


def decide(e):
    f = e.get("facts") or {}
    problems = []
    if f.get("link") not in OK_LINK:
        problems.append(f"link returned {f.get('link', 'nothing (run enrich.py)')}")
    ok, why = license_backed(e, f)
    if not ok:
        problems.append(why)
    if is_code(e):
        if f.get("archived"):
            return "declining", ["archived on GitHub"]
        age = days_since(f.get("pushed") or f.get("npm_modified") or "")
        if age is not None and age > 730:
            return "declining", [f"no updates for {age} days"]
        if age is None or age > 365:
            problems.append("no updates in the last year" if age else "no activity data")
        if (f.get("stars") or 0) < MIN_STARS and (f.get("npm_weekly") or 0) < MIN_WEEKLY:
            problems.append(f"under {MIN_STARS} stars and {MIN_WEEKLY} weekly downloads")
    return ("verified" if not problems else "candidate"), problems


def gate(e):
    if e.get("hold"):  # set by the auditor or a person; only a person removes it
        e["status"] = "candidate"
        e.pop("verified_by", None)
        e["problems"] = [f"on hold: {e['hold']}"]
        return "candidate"
    if e.get("source"):  # imported from an official dataset (e.g. Google's font metadata)
        ok = e.get("license") and e.get("license_url")
        e["status"] = "verified" if ok else "candidate"
        if ok:
            e["verified_by"] = "auto"
        return e["status"]
    status, problems = decide(e)
    if e.get("verified_by") == "human" and status != "declining":
        e.pop("problems", None)
        return e["status"]
    e["status"] = status
    if status == "verified":
        e["verified_by"] = "auto"
        e.pop("problems", None)
    else:
        e.pop("verified_by", None)
        e["problems"] = problems
    return status


def main():
    counts = {}
    paths = list(inbox_files()) + ([] if "--inbox" in sys.argv else branch_files())
    for p in paths:
        doc = load(p)
        entries = (doc.get("proposals") or []) if p.parent.name == "_inbox" else [e for _, _, e in walk(doc)]
        for e in entries:
            s = gate(e)
            counts[s] = counts.get(s, 0) + 1
        save(p, doc)
    print("gate:", ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "nothing to gate")


if __name__ == "__main__":
    main()
