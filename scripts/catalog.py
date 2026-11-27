"""Shared helpers for the catalog scripts (load, walk, save, normalise)."""
import re
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
INBOX = CATALOG / "_inbox"
REJECTED = CATALOG / "_rejected.yaml"
TIERS = ("default", "alternatives", "more", "big_lists", "paid", "list")
GITHUB = re.compile(r"^https://github\.com/([^/\s]+)/([^/\s#?]+)")


def today():
    return date.today().isoformat()


def load(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


def save(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8"
    )


def branch_files():
    """Catalog files the site is built from (skips _inbox, _rejected and other _ files)."""
    return [p for p in sorted(CATALOG.rglob("*.yaml"))
            if not any(part.startswith("_") for part in p.relative_to(CATALOG).parts)]


def inbox_files():
    return sorted(INBOX.glob("*.yaml")) if INBOX.exists() else []


def walk(doc):
    """Yield (section, tier, entry) for every entry in a branch doc."""
    for sec in doc.get("sections") or []:
        for tier in TIERS:
            items = sec.get(tier)
            if items is None:
                continue
            for e in items if isinstance(items, list) else [items]:
                yield sec, tier, e


def norm_url(u):
    u = (u or "").strip().lower().rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u


def norm_name(n):
    return re.sub(r"[^a-z0-9]", "", (n or "").lower())


def repo_of(e):
    if e.get("repo"):
        return e["repo"]
    m = GITHUB.match(e.get("url", ""))
    return f"{m.group(1)}/{m.group(2).removesuffix('.git')}" if m else None


def is_code(e):
    return bool(repo_of(e) or e.get("npm"))
