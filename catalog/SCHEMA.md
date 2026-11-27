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
