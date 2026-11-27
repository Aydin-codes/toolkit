#!/usr/bin/env python3
"""Move gated proposals from catalog/_inbox/ into the branch files.

  verified (auto)  -> placed in its branch/section/tier
  duplicate        -> dropped (same url or same name already in the catalog)
  candidate        -> stays in the inbox for the next round; after 3 failed rounds
                      it moves to catalog/_rejected.yaml with its reasons

Placement: a section gets at most 1 default and 5 alternatives; extra ones go to
"More options" (tier `more`), so quantity never breaks the tiers.

  python scripts/merge.py
"""
from catalog import CATALOG, REJECTED, branch_files, inbox_files, load, norm_name, norm_url, save, today, walk

PROPOSAL_ONLY = ("branch", "branch_title", "section", "tier", "attempts")
MAX_ATTEMPTS = 3


def existing():
    urls, names = {}, {}
    for p in branch_files():
        doc = load(p)
        for _, _, e in walk(doc):
            urls[norm_url(e.get("url"))] = e["name"]
            names[norm_name(e.get("name"))] = e["name"]
    return urls, names


def place(prop):
    branch = prop["branch"].strip("/")
    path = CATALOG / f"{branch}.yaml"
    doc = load(path) if path.exists() else {
        "branch": branch,
        "title": prop.get("branch_title") or branch.split("/")[-1].replace("-", " ").capitalize(),
        "intro": "",
        "sections": [],
    }
    secs = doc.setdefault("sections", [])
    sec = next((s for s in secs if s["name"].lower() == prop["section"].lower()), None)
    if sec is None:
        sec = {"name": prop["section"]}
        secs.append(sec)
    entry = {k: v for k, v in prop.items() if k not in PROPOSAL_ONLY}
    tier = prop.get("tier", "more")
    if tier == "default":
        tier = "default" if not sec.get("default") else "alternatives"
    if tier == "alternatives" and len(sec.get("alternatives") or []) >= 5:
        tier = "more"
    if tier == "default":
        sec["default"] = entry
    else:
        sec.setdefault(tier, []).append(entry)
    save(path, doc)
    return f"{branch} > {sec['name']} > {tier}"


def main():
    urls, names = existing()
    rejected = load(REJECTED).get("rejected", []) if REJECTED.exists() else []
    added = dup = kept = rej = 0
    for p in inbox_files():
        doc = load(p)
        keep = []
        for prop in doc.get("proposals") or []:
            missing = [k for k in ("branch", "section", "name", "url") if not prop.get(k)]
            if missing:
                rejected.append({**prop, "rejected": today(), "reasons": [f"missing {', '.join(missing)}"]})
                rej += 1
                continue
            if prop["url"].startswith("http://"):
                prop["url"] = "https://" + prop["url"][7:]
            hit = urls.get(norm_url(prop["url"])) or names.get(norm_name(prop["name"]))
            if hit:
                dup += 1
                continue
            if prop.get("status") == "verified":
                where = place(prop)
                urls[norm_url(prop["url"])] = names[norm_name(prop["name"])] = prop["name"]
                print("added", prop["name"], "->", where)
                added += 1
                continue
            prop["attempts"] = prop.get("attempts", 0) + 1
            if prop.get("status") == "declining" or prop["attempts"] >= MAX_ATTEMPTS:
                rejected.append({**prop, "rejected": today(), "reasons": prop.get("problems", [])})
                rej += 1
            else:
                keep.append(prop)
                kept += 1
        if keep:
            doc["proposals"] = keep
            save(p, doc)
        else:
            p.unlink()
    if rejected:
        save(REJECTED, {"rejected": rejected})
    print(f"merge: added {added}, duplicates {dup}, waiting {kept}, rejected {rej}")


if __name__ == "__main__":
    main()
