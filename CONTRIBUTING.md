# Contributing

The easiest way to help: open a **Suggest a tool** issue with the link and one line on when you'd pick it.

## Editing directly

1. Find the branch file in `catalog/` (for example `catalog/frontend/type.yaml`).
2. Add the entry. Required: `name`, `url`, `search`, `licence`, `status: candidate`. See `catalog/SCHEMA.md`.
3. Run `pip install pyyaml` once, then `python scripts/build.py`.
4. Open a pull request.

## How an entry becomes verified

All five must be true:
1. Licence read; it's clear whether it can be installed, bundled or only linked.
2. Commits in the last 12 months (or a stable, finished project such as a font).
3. An agent can install or fetch it.
4. Works with the stack it's listed under.
5. A free demo or specimen you can actually see.

Links are checked every Monday by a workflow; broken ones open an issue.
