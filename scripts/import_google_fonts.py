#!/usr/bin/env python3
"""Import every Google Fonts family from Google's own metadata (github.com/google/fonts).

  python scripts/import_google_fonts.py              download the metadata, then write the catalog files
  python scripts/import_google_fonts.py <path>       use an existing checkout of google/fonts

Writes catalog/frontend/fonts/<style>.yaml (sans-serif, serif, display, handwriting, monospace).
Each family gets its specimen link, its license (OFL, Apache or UFL, from the metadata), the license
file in google/fonts as evidence, and the Fontsource install command. Run it again to refresh.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from catalog import CATALOG, save, today

STYLES = {
    "SANS_SERIF": ("sans-serif", "Sans-serif"),
    "SERIF": ("serif", "Serif"),
    "DISPLAY": ("display", "Display"),
    "HANDWRITING": ("handwriting", "Handwriting"),
    "MONOSPACE": ("monospace", "Monospace"),
}
LICENSES = {
    "OFL": ("OFL-1.1", "OFL.txt"),
    "APACHE2": ("Apache-2.0", "LICENSE.txt"),
    "UFL": ("UFL-1.0", "UFL.txt"),
}
LICENSE_DIR = {"OFL": "ofl", "APACHE2": "apache", "UFL": "ufl"}
# Same list as design-studio's font picker: fine on purpose, not as a default.
AI_PICKS = {"Inter", "Geist", "Space Grotesk", "Instrument Serif", "Outfit", "Plus Jakarta Sans", "DM Sans",
            "Manrope", "Bricolage Grotesque", "Sora", "Urbanist", "Poppins", "Montserrat", "Roboto",
            "Open Sans", "Lato", "Playfair Display", "IBM Plex Mono", "JetBrains Mono"}


def fetch():
    tmp = Path(tempfile.mkdtemp()) / "fonts"
    run = lambda *a: subprocess.run(a, cwd=tmp if tmp.exists() else None, check=True)
    run("git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--no-checkout",
        "https://github.com/google/fonts", str(tmp))
    run("git", "sparse-checkout", "init", "--no-cone")
    run("git", "sparse-checkout", "set", "/*/*/METADATA.pb")
    run("git", "checkout", "-q", "main")
    return tmp


def field(text, key):
    m = re.search(rf'^{key}: "(.*)"', text, re.M)
    return m.group(1) if m else None


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else fetch()
    groups = {k: {"Latin": [], "Noto": [], "Other scripts": []} for k in STYLES}
    for meta in sorted(root.glob("*/*/METADATA.pb")):
        t = meta.read_text(encoding="utf-8")
        name, lic, cat = field(t, "name"), field(t, "license"), field(t, "category")
        if not name or lic not in LICENSES or cat not in STYLES:
            continue
        spdx, lic_file = LICENSES[lic]
        folder = meta.parent.name
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        bits = []
        if "axes {" in t:
            bits.append("variable")
        if field(t, "primary_script"):
            bits.append(f"script {field(t, 'primary_script')}")
        bits.append(f"by {field(t, 'designer')}")
        bits.append(f"added {(field(t, 'date_added') or '')[:4]}")
        if name in AI_PICKS:
            bits.append("**common AI pick**")
        entry = {
            "name": name,
            "url": "https://fonts.google.com/specimen/" + name.replace(" ", "+"),
            "search": f"{name} font",
            "license": spdx,
            "license_url": f"https://github.com/google/fonts/blob/main/{LICENSE_DIR[lic]}/{folder}/{lic_file}",
            "install": f"npm i @fontsource/{slug}",
            "note": ", ".join(bits),
            "status": "verified",
            "verified_by": "auto",
            "source": "google/fonts metadata",
            "checked": today(),
        }
        group = "Noto" if "is_noto: true" in t else ("Other scripts" if field(t, "primary_script") else "Latin")
        groups[cat][group].append(entry)
    total = 0
    for cat, (slug, title) in STYLES.items():
        g = groups[cat]
        n = sum(len(v) for v in g.values())
        total += n
        sections = []
        for gname, label in (("Latin", "Latin families, A-Z"), ("Other scripts", "Other scripts"), ("Noto", "Noto (language coverage)")):
            if g[gname]:
                sections.append({"name": f"{label} ({len(g[gname])})", "list": sorted(g[gname], key=lambda e: e["name"].lower())})
        save(CATALOG / "frontend" / "fonts" / f"{slug}.yaml", {
            "branch": f"frontend/fonts/{slug}",
            "title": f"All Google Fonts: {title.lower()} ({n} families)",
            "intro": "Every family in this style on Google Fonts, imported from Google's own metadata "
                     "(github.com/google/fonts). Open the specimen and test with real text before choosing. "
                     "Fonts marked common AI pick are fine on purpose but shouldn't be a default. "
                     "For curated starting picks, see reference/frontend/type.md.",
            "compact": True,
            "sections": sections,
        })
        print(f"{slug}: {n}")
    print("total:", total)


if __name__ == "__main__":
    main()
