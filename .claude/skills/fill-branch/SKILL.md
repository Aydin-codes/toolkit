---
name: fill-branch
description: Fill toolkit branches with many checked entries. Runs parallel harvester subagents, the scripts pipeline (enrich, gate, merge, build), license checks and an independent audit, in a loop with stop rules. Use when asked to fill, grow or harvest a branch or the whole catalog.
---

# Fill a branch

Goal: as many good entries as possible without a person reviewing each one. Machines check facts (link, license, activity, popularity, duplicates); an independent auditor spot-checks a sample; a person only reads the run report.

## Inputs
- Branch(es): from the user, or the next unfinished one in **Order** below.
- Target per section: from the user, default 15.

## Loop

0. `git checkout -b fill/<branch-with-dashes>-<YYYY-MM-DD>` (or continue the branch if it exists). `pip install pyyaml` if needed.
1. For each round, up to **3 rounds**:
   1. Count what each section already has: `python scripts/find.py "<section name>" --branch <branch> -n 100`. Skip sections already at target.
   2. Spawn one **harvester** per section that still needs entries, **in parallel** (at most 8 at once). Tell each: branch, section, how many more it needs, and the section hints below.
   3. Run `python scripts/pipeline.py --inbox`.
   4. If any waiting proposals have license problems, spawn one **license-checker** per inbox file, in parallel, then run `python scripts/pipeline.py --inbox` again.
   5. Commit: `Fill <branch>: +<added> entries (round <n>)`. No co-author or AI attribution lines.
   6. **Stop** when every section is at target, or this round added fewer than 3 entries, or this was round 3.
2. **Audit.** From this run's additions (`git diff main --stat -- catalog` and the run reports), pick 10% at random (at least 5, at most 20). Spawn the **auditor** with that list. It must be a fresh auditor, not a harvester.
3. If the audit fail rate is **over 10%**, stop and say so first in the summary. Leave everything committed so the person can look.
4. Run `python scripts/build.py --check` and `agentskills validate "$PWD"`. Commit `Audit fill run` if anything changed.
5. Summarise in 5 lines: entries added per section, verified vs candidate, rejected count, audit fail rate, report paths in `runs/`. **Never push.**

## Rules
- Only harvesters write to `catalog/_inbox/`. Only scripts and the auditor change entries in branch files. You (the orchestrator) may set a branch's `intro` and `notice` in one plain sentence each.
- Don't edit `SKILL.md`, `README.md` or the maintainer's wording.
- Don't raise the thresholds in `scripts/gate.py` to get more entries through.
- If the GitHub API rate limit is hit, say so: the person should run `gh auth login` or set `GITHUB_TOKEN`.

## Order and sections

| Branch | Sections (hints in brackets) |
| --- | --- |
| frontend/ui | Base kits (shadcn/ui, Radix, React Aria) · Animated kits (Magic UI, Aceternity, React Bits, Animate UI, Motion Primitives, Cult UI, Watermelon UI, Skiper UI; check never_copy) · Blocks and sections · Icons · Color and tokens (tweakcn, Radix Colors) · Component registries |
| frontend/motion | Animation libraries · Text and background effects · Shaders and WebGL backgrounds · Smooth scroll · Lottie and Rive |
| assets/ready-made | Photos · Public domain · Illustration · 3D models · Textures and HDRIs · Video · Music · Sound effects · Animation files |
| frontend/ux | Real-app references (paid ones to paid) · Patterns and flows · Forms and inputs · Accessibility tools · Copy and microcopy |
| frontend/frameworks | Web frameworks · Static site generators · Build tools · Styling · State and data fetching · Forms and validation |
| frontend/3d | Engines · React helpers · Physics · Model tools and compression · Performance |
| assets/ai-generators | Image · 3D · Video · Voice · Music (mostly paid; say what the free tier allows) |
| print-pdf | Make PDFs · Edit and merge · Read and extract · OCR · Templates · Print and layout tools |
| platforms | Mobile · Desktop · Browser extensions · Games · MCP servers |
| ship | Hosting · CI · Domains and DNS · Analytics · Error tracking · SEO and sharing |
| quality | Testing · Accessibility checks · Performance · Security · Linting and formatting |
| backend | Databases · ORMs · Auth · Payments · Email · File storage · Search · Realtime · Background jobs · AI features · Public APIs. Set the branch `notice` to: Listed, not endorsed. No security guarantee: use managed providers for auth and payments and review before going live. |
| assets/make-your-own | 3D · Vector · Painting · Photo editing · Video editing · Audio · Design tools |
| frontend/dataviz | Charts · Maps · Diagrams · Tables |
| agent-tooling | MCP servers and connectors · Skills · Plugins · Docs for agents |
| learn | Repos to read · Awesome lists · Courses · References |
