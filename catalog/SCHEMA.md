# Catalog format

Each file in `catalog/` is one branch. `scripts/build.py` turns it into the matching page in `reference/`. Edit the YAML, never the generated page.

```yaml
branch: frontend/type          # output: reference/frontend/type.md
title: Typography
intro: One or two lines on what this branch covers.
notice: Optional warning shown at the top (e.g. "listed, not endorsed").
sections:
  - name: Font sources
    note: Optional line under the heading.
    default:  { ...entry }      # one pick
    alternatives: [ entry, ... ] # 3-5, each with use_when
    big_lists: [ entry, ... ]    # bigger lists we link to, not copy
    more: [ entry, ... ]         # extra options beyond the 5 alternatives (filled by scripts/merge.py)
    paid: [ entry, ... ]         # listed separately, with a free option in `note`
    list: [ entry, ... ]         # plain list, for sections that don't rank (e.g. style buckets)
```

## Entry fields

| Field | Required | Meaning |
| --- | --- | --- |
| `name` | yes | Tool, library, source or font name |
| `url` | yes | Official page |
| `search` | yes | What to search if the link breaks |
| `license` | yes | e.g. OFL, MIT, CC0, "free, not open source", "paid" |
| `use_when` | for alternatives | One line: when to pick this over the default |
| `install` | no | How an agent gets it: npm package, `npx shadcn add …`, MCP, download, CDN |
| `never_copy` | no | `true` if it may be installed into a project but never copied into another repo |
| `note` | no | Anything else, one line |
| `status` | yes | `candidate` (not checked yet), `verified` (passed the 5 checks), `declining` (still works, no longer recommended) |
| `checked` | no | Date of the last check, `YYYY-MM-DD` |

## The 5 checks for `verified`
1. License read; it's clear whether it can be installed, bundled or only linked.
2. Commits in the last 12 months (or a stable, finished project such as a font).
3. An agent can install or fetch it.
4. Works with the stack it's listed under.
5. A free demo or specimen you can actually see.

## Fields the pipeline adds

| Field | Set by | Meaning |
| --- | --- | --- |
| `repo` | harvester | GitHub `owner/name`, so `enrich.py` can read stars, activity and license |
| `npm` | harvester | npm package name, for license, last publish and weekly downloads |
| `license_url` | harvester / license-checker | The license page; required evidence for anything that isn't code |
| `facts` | `scripts/enrich.py` | What the web says: link status, stars, last push, archived, licenses, downloads, date checked |
| `verified_by` | `scripts/gate.py` or a person | `auto` (passed the gate rules) or `human` (a person checked it) |
| `problems` | `scripts/gate.py` | Why an entry is still a candidate |
| `hold` | auditor or a person | Keeps an entry a candidate until a person removes it |

## The pipeline

```
harvester agents ──► catalog/_inbox/*.yaml
                         │
   enrich.py (facts) ──► gate.py (status) ──► merge.py (place or reject) ──► build.py (pages + index.json)
                                                   │
                                        catalog/_rejected.yaml
```

`python scripts/pipeline.py` runs the four scripts and writes a report to `runs/`. The gate rules are at the top of `scripts/gate.py`. `python scripts/find.py "<need>"` searches every entry.
