#!/usr/bin/env python3
"""One command for the machine part of the fill loop:
   enrich (facts from the web) -> gate (status from rules) -> merge (inbox -> branches) -> build (pages + index)
and a short report in runs/.

  python scripts/pipeline.py            full run
  python scripts/pipeline.py --inbox    only enrich/gate the inbox, then merge and build (fast)
  python scripts/pipeline.py --offline  skip enrich (no network)
"""
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from catalog import REJECTED, ROOT, branch_files, inbox_files, load, walk

PY = sys.executable


def run(*args):
    r = subprocess.run([PY, *args], cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(out)
    return r.returncode, out


def counts():
    c = {"verified": 0, "candidate": 0, "declining": 0}
    for p in branch_files():
        for _, _, e in walk(load(p)):
            c[e.get("status")] = c.get(e.get("status"), 0) + 1
    waiting = sum(len(load(p).get("proposals") or []) for p in inbox_files())
    rejected = len(load(REJECTED).get("rejected") or []) if REJECTED.exists() else 0
    return c, waiting, rejected


def main():
    inbox = ["--inbox"] if "--inbox" in sys.argv else []
    before, _, _ = counts()
    log = []
    if "--offline" not in sys.argv:
        log.append(run("scripts/enrich.py", *inbox)[1])
    log.append(run("scripts/gate.py", *inbox)[1])
    log.append(run("scripts/merge.py")[1])
    code, out = run("scripts/build.py")
    log.append(out)
    after, waiting, rejected = counts()
    added = sum(after.values()) - sum(before.values())
    Path(ROOT / "runs").mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    report = ROOT / "runs" / f"{stamp}.md"
    report.write_text(
        f"# Pipeline run {stamp}\n\n"
        f"- Entries: {sum(after.values())} (+{added}); verified {after['verified']}, "
        f"candidate {after['candidate']}, declining {after['declining']}\n"
        f"- Inbox waiting: {waiting}; rejected so far: {rejected}\n\n"
        "```\n" + "\n".join(log) + "\n```\n", encoding="utf-8")
    print(f"\nreport: {report.relative_to(ROOT)}")
    sys.exit(code)


if __name__ == "__main__":
    main()
