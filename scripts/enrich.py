#!/usr/bin/env python3
"""Collect facts about each entry from the web, with no AI involved.

For every entry in catalog/ and catalog/_inbox/ it records, under `facts:`:
  link         HTTP status of `url` (and `license_link` for `license_url`)
  stars, pushed, archived, gh_license      from the GitHub API, if the entry is a GitHub repo
  npm_license, npm_modified, npm_weekly    from the npm registry, if the entry has `npm:`

  python scripts/enrich.py            refresh facts older than 7 days
  python scripts/enrich.py --force    refresh everything
  python scripts/enrich.py --inbox    only the inbox (fast, used by the fill loop)

Set GITHUB_TOKEN (or be logged in with `gh`) to get 5,000 GitHub calls an hour instead of 60.
"""
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

from catalog import branch_files, inbox_files, load, repo_of, save, today, walk

UA = {"User-Agent": "Mozilla/5.0 (toolkit enrich)"}


def token():
    if os.environ.get("GITHUB_TOKEN"):
        return os.environ["GITHUB_TOKEN"]
    try:
        return subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10).stdout.strip() or None
    except Exception:
        return None


TOKEN = token()


def get_json(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def link_status(u):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(u, method=method, headers=UA)
            with urllib.request.urlopen(req, timeout=15) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "GET" or e.code not in (403, 405):
                return e.code
        except Exception as e:
            if method == "GET":
                return type(e).__name__
    return "?"


def facts_for(e):
    f = {"checked": today(), "link": link_status(e["url"])}
    if e.get("license_url"):
        f["license_link"] = link_status(e["license_url"])
    repo = repo_of(e)
    if repo:
        h = {"Accept": "application/vnd.github+json"}
        if TOKEN:
            h["Authorization"] = f"Bearer {TOKEN}"
        try:
            g = get_json(f"https://api.github.com/repos/{repo}", h)
            f.update(stars=g.get("stargazers_count"), pushed=(g.get("pushed_at") or "")[:10],
                     archived=bool(g.get("archived")),
                     gh_license=(g.get("license") or {}).get("spdx_id"))
        except urllib.error.HTTPError as err:
            f["github_error"] = err.code
        except Exception as err:
            f["github_error"] = type(err).__name__
    if e.get("npm"):
        pkg = e["npm"]
        try:
            n = get_json(f"https://registry.npmjs.org/{pkg}")
            lic = n.get("license")
            f["npm_license"] = lic.get("type") if isinstance(lic, dict) else lic
            f["npm_modified"] = (n.get("time", {}).get("modified") or "")[:10]
            d = get_json(f"https://api.npmjs.org/downloads/point/last-week/{pkg}")
            f["npm_weekly"] = d.get("downloads")
        except Exception as err:
            f["npm_error"] = getattr(err, "code", type(err).__name__)
    return f


def stale(e, force):
    if force or not isinstance(e.get("facts"), dict):
        return True
    try:
        return date.fromisoformat(e["facts"]["checked"]) < date.today() - timedelta(days=7)
    except Exception:
        return True


def main():
    force, inbox_only = "--force" in sys.argv, "--inbox" in sys.argv
    docs = []
    for p in inbox_files():
        docs.append((p, load(p), "inbox"))
    if not inbox_only:
        for p in branch_files():
            docs.append((p, load(p), "branch"))
    todo = []
    for path, doc, kind in docs:
        entries = (doc.get("proposals") or []) if kind == "inbox" else [e for _, _, e in walk(doc)]
        todo += [e for e in entries if e.get("url") and stale(e, force)]
    print(f"enriching {len(todo)} entries (GitHub token: {'yes' if TOKEN else 'no, 60 calls/hour'})")
    with ThreadPoolExecutor(8) as pool:
        for e, f in zip(todo, pool.map(facts_for, todo)):
            e["facts"] = f
    touched = {id(e) for e in todo}
    for path, doc, kind in docs:
        entries = (doc.get("proposals") or []) if kind == "inbox" else [e for _, _, e in walk(doc)]
        if any(id(e) in touched for e in entries):
            save(path, doc)
    bad = [e["name"] for e in todo if e["facts"].get("link") not in (200, 206, 429)]
    print(f"done; {len(bad)} with a broken or blocked link")


if __name__ == "__main__":
    main()
