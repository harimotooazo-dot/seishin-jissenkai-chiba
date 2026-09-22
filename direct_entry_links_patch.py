from pathlib import Path

SEPTEMBER_FORM = "https://tally.so/r/LZeJ4G"
WORLD_FORM = "https://tally.so/r/WOBDLL"

# Event-specific buttons should go straight to the matching form.
# Generic entry.html links (such as the LINE/menu entry point) are intentionally left unchanged.
for name in ("index.html", "schedule.html", "member.html"):
    p = Path(name)
    if not p.exists():
        continue
    html = p.read_text(encoding="utf-8")
    html = html.replace('href="entry.html#september"', f'href="{SEPTEMBER_FORM}" target="_blank" rel="noopener"')
    html = html.replace('href="./entry.html#september"', f'href="{SEPTEMBER_FORM}" target="_blank" rel="noopener"')
    html = html.replace('href="entry.html#world"', f'href="{WORLD_FORM}" target="_blank" rel="noopener"')
    html = html.replace('href="./entry.html#world"', f'href="{WORLD_FORM}" target="_blank" rel="noopener"')
    p.write_text(html, encoding="utf-8")
