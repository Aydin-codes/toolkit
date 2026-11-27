# For agents editing this repo

- `SKILL.md` is the core. Keep it under 200 lines; put detail in a branch file.
- `reference/` pages are generated. Edit `catalog/**/*.yaml`, then run `python scripts/build.py`. Never hand-edit a generated page.
- Every entry needs `name`, `url`, `search`, `license`, `status`. New entries start as `candidate`. See `catalog/SCHEMA.md`.
- Alternatives per section: 1-5. Free options before paid ones; paid entries go in `paid`.
- To add many entries, use the `fill-branch` skill (`.claude/skills/fill-branch`): harvester subagents write to `catalog/_inbox/`, then `python scripts/pipeline.py` checks and places them. Don't hand-place entries in bulk.
- Search the catalog with `python scripts/find.py "<need>"`.
- Before finishing: `agentskills validate "$PWD"` and `python scripts/build.py --check` both pass.
- Don't rewrite the maintainer's wording in `SKILL.md` or `README.md` without asking.
- Commits: no AI co-author lines.
