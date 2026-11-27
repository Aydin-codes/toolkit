# Changelog

## Unreleased

- Fill pipeline: `scripts/enrich.py` (facts from GitHub, npm and the link), `gate.py` (status from fixed rules), `merge.py` (inbox to branches, duplicates dropped, rejects kept with reasons), `pipeline.py` (runs all four and writes a report to `runs/`).
- `scripts/find.py` searches every entry; `build.py` also writes `catalog/index.json`.
- New tier **More options** so sections can grow past 5 alternatives.
- Claude Code: `fill-branch` skill plus `harvester`, `license-checker` and `auditor` subagents.

## 0.1.0 (draft, not released)

- Toolkit moves from `Aydin-codes/skills/toolkit` to its own repo.
- Short core `SKILL.md` with a decision model, an index of branch files and top rules with sources.
- `scripts/check_links.py`: checks every link with no extra installs.
- `catalog/` + `scripts/build.py`: branch pages are generated from YAML entries with link, search term, license and status.
- First branch: `reference/frontend/type.md` (font sources, starting picks by style, type-scale tools, common AI picks).
- CI validates `SKILL.md` against the Agent Skills spec and checks the catalog; a weekly job checks every link.
- Removed: plain-English glossary, K-12-specific lines.
