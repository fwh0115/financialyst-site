"""Build marlow/privacy/index.html and marlow/terms/index.html from the app's Markdown.

The app repo's ft_app/assets/legal/*.md is the one source of truth. To update the site:
  1. copy privacy-policy.md and terms-of-use.md from the app repo into source/
  2. run:  python3 build.py
  3. commit and push; GitHub Pages republishes in a minute or two.
"""
import html
import re
from pathlib import Path

import markdown  # pip install markdown

ROOT = Path(__file__).parent
SITE = ROOT / "marlow"  # served at https://fwh0115.github.io/marlow/
PAGES = [
    ("privacy-policy.md", "privacy", "Privacy Policy"),
    ("terms-of-use.md", "terms", "Terms of Use"),
]
EMAIL = re.compile(r"(?<![\w.+-])([\w.+-]+@[\w-]+\.[\w.]+\w)")

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Marlow</title>
<meta name="description" content="The Marlow {title}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" type="image/png" sizes="32x32" href="../assets/icon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="../assets/icon-192.png">
<link rel="apple-touch-icon" href="../assets/icon-180.png">
<link rel="stylesheet" href="../style.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="wordmark" href="../"><img src="../assets/icon-96.png" alt="" width="32" height="32">Marlow</a>
    <nav class="site-nav" aria-label="Site">
      <a href="../privacy/"{privacy_current}>Privacy Policy</a>
      <a href="../terms/"{terms_current}>Terms of Use</a>
    </nav>
  </div>
</header>
<main class="wrap">
  <article class="doc">
    <h1>{title}</h1>
    <p class="updated">{updated}</p>
    <nav class="contents" aria-label="Contents">
      <p>Contents</p>
      <ul>{toc}</ul>
    </nav>
{body}
  </article>
</main>
<footer class="site-foot">
  <div class="wrap">
    <span>© 2026 Marlow. Published by Fong Whye Hin, Singapore.</span>
    <nav aria-label="Footer">
      <a href="../privacy/">Privacy Policy</a>
      <a href="../terms/">Terms of Use</a>
      <a href="mailto:fwh0115@gmail.com">fwh0115@gmail.com</a>
    </nav>
  </div>
</footer>
</body>
</html>
"""


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def build(src: str, folder: str, title: str) -> None:
    md = (ROOT / "source" / src).read_text(encoding="utf-8")
    lines = md.splitlines()
    # The page supplies the title and the date line itself.
    assert lines[0] == f"# {title}", f"{src}: first line should be '# {title}'"
    updated = next(l for l in lines[1:6] if l.startswith("Last updated:"))
    rest = "\n".join(l for l in lines[1:] if l != updated)

    body = markdown.markdown(rest, output_format="html5")
    toc = []

    def add_id(m: re.Match) -> str:
        level, inner = m.group(1), m.group(2)
        text = html.unescape(re.sub(r"<[^>]+>", "", inner))
        anchor = slug(text)
        if level == "2":
            toc.append(f'<li><a href="#{anchor}">{html.escape(text)}</a></li>')
        return f'<h{level} id="{anchor}">{inner}</h{level}>'

    body = re.sub(r"<h([23])>(.*?)</h\1>", add_id, body)
    body = re.sub(r"<p>\s*([\s\S]*?)</p>", lambda m: "<p>" + m.group(1) + "</p>", body)
    # Plain email addresses become mail links (skipping ones already inside a link).
    body = EMAIL.sub(lambda m: f'<a href="mailto:{m.group(1)}">{m.group(1)}</a>', body)
    body = re.sub(r'(<a [^>]*href="https?://[^"]+")', r'\1 rel="noopener"', body)

    page = TEMPLATE.format(
        title=title,
        updated=html.escape(updated),
        toc="".join(toc),
        body="\n".join("    " + l if l else l for l in body.splitlines()),
        privacy_current=' aria-current="page"' if folder == "privacy" else "",
        terms_current=' aria-current="page"' if folder == "terms" else "",
    )
    out = SITE / folder / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"{out.relative_to(ROOT)}: {len(toc)} sections, {updated}")


if __name__ == "__main__":
    for args in PAGES:
        build(*args)
