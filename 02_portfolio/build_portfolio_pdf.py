#!/usr/bin/env python3
"""Build A4 PDF portfolio from markdown — no invented data."""
from pathlib import Path
import re
import markdown
from weasyprint import HTML, CSS

SRC = Path("/workspace/02_portfolio/2026-09-22_portfolio_JP.md")
OUT = Path("/workspace/02_portfolio/2026-09-22_portfolio_JP.pdf")
OUT_HTML = Path("/workspace/02_portfolio/2026-09-22_portfolio_JP.html")

md_text = SRC.read_text(encoding="utf-8")

# Convert markdown → HTML (tables, fenced code, nl2br-ish via extras)
html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "sane_lists", "smarty"],
)

# Wrap section 4 aviso + results table so they stay on the same page.
# Structure after md: h2 "4. Prova...", then content, h3 Aviso, blockquote,
# h3 Tabela, table, h3 Como usar...
# We wrap from h3 Aviso through the first table after it.

def wrap_aviso_table(html: str) -> str:
    # Find start of "Aviso obrigatório" h3
    start = re.search(
        r'<h3[^>]*>\s*Aviso obrigatório\s*</h3>',
        html,
        flags=re.I,
    )
    if not start:
        raise SystemExit("Could not find 'Aviso obrigatório' heading")
    # Find the table that follows (results table)
    table_m = re.search(r'<table>.*?</table>', html[start.start():], flags=re.S)
    if not table_m:
        raise SystemExit("Could not find results table after aviso")
    end = start.start() + table_m.end()
    chunk = html[start.start():end]
    wrapped = (
        '<div class="prova-keep">'
        + chunk
        + '</div>'
    )
    return html[: start.start()] + wrapped + html[end:]

html_body = wrap_aviso_table(html_body)

# Soft page break before section 4 so aviso+table land together on a fresh page
html_body = re.sub(
    r'(<h2[^>]*>\s*4\.\s*Prova)',
    r'<div class="page-break"></div>\1',
    html_body,
    count=1,
    flags=re.I,
)

# Mark CENARIO SINTETICO blockquote / section for dashed box styling
html_body = re.sub(
    r'(<h2[^>]*>\s*8\.\s*CENARIO SINTETICO\s*</h2>)(.*?)(?=<h2|\Z)',
    r'<section class="cenario">\1\2</section>',
    html_body,
    count=1,
    flags=re.S | re.I,
)

# Lead callout (first blockquote after title area) — already blockquotes

CSS_TEXT = r"""
@page {
  size: A4;
  margin: 1.6cm 1.5cm 2.0cm 1.5cm;
  @bottom-center {
    content: "Laboratório ≠ operação · 2026-09-22 · JP Decision Engine";
    font-family: "DejaVu Sans", "Liberation Sans", sans-serif;
    font-size: 7.5pt;
    color: #5a6578;
  }
  @bottom-right {
    content: counter(page);
    font-family: "DejaVu Sans", "Liberation Sans", sans-serif;
    font-size: 7.5pt;
    color: #5a6578;
  }
}

html, body {
  font-family: "DejaVu Sans", "Liberation Sans", "Noto Sans", sans-serif;
  font-size: 9.5pt;
  line-height: 1.38;
  color: #141C2B;
  background: #F7F4EC;
}

/* Watermark on every page */
body::before {
  content: "LABORATÓRIO — NÃO É OPEX";
  position: fixed;
  top: 42%;
  left: -8%;
  width: 120%;
  text-align: center;
  font-size: 28pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: #141C2B;
  opacity: 0.055;
  transform: rotate(-38deg);
  z-index: 0;
  pointer-events: none;
  white-space: nowrap;
}

body > * {
  position: relative;
  z-index: 1;
}

h1 {
  font-size: 18pt;
  font-weight: 700;
  color: #1B2A41;
  margin: 0 0 0.35em 0;
  letter-spacing: -0.01em;
}

h2 {
  font-size: 12pt;
  font-weight: 700;
  color: #1B2A41;
  margin: 1.15em 0 0.4em 0;
  padding-bottom: 0.15em;
  border-bottom: 1.5px solid #C8A024;
  page-break-after: avoid;
}

h3 {
  font-size: 10pt;
  font-weight: 700;
  color: #1B2A41;
  margin: 0.85em 0 0.3em 0;
  page-break-after: avoid;
}

p {
  margin: 0.35em 0;
}

strong { font-weight: 700; }
em { font-style: italic; }

ul, ol {
  margin: 0.3em 0 0.5em 1.2em;
  padding: 0;
}
li { margin: 0.15em 0; }

hr {
  border: none;
  border-top: 1px solid #c9c4b4;
  margin: 0.9em 0;
}

blockquote {
  margin: 0.5em 0;
  padding: 0.45em 0.7em;
  border-left: 3px solid #C8A024;
  background: #fff;
  color: #1B2A41;
  font-size: 8.8pt;
  page-break-inside: avoid;
}

code {
  font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
  font-size: 8.2pt;
  background: #fff;
  padding: 0.05em 0.25em;
  border-radius: 2px;
}

pre {
  background: #fff;
  border: 1px solid #ddd8c8;
  padding: 0.5em 0.7em;
  font-size: 7.5pt;
  line-height: 1.3;
  white-space: pre-wrap;
  page-break-inside: avoid;
}
pre code { background: none; padding: 0; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.45em 0 0.7em 0;
  font-size: 8pt;
  background: #fff;
  page-break-inside: avoid;
}

th, td {
  border: 1px solid #c9c4b4;
  padding: 0.28em 0.4em;
  text-align: left;
  vertical-align: top;
}

th {
  background: #1B2A41;
  color: #F7F4EC;
  font-weight: 600;
}

tr:nth-child(even) td { background: #faf8f2; }

/* Keep aviso + results table together */
.prova-keep {
  page-break-inside: avoid;
  break-inside: avoid;
  background: #fff;
  border: 1px solid #ddd8c8;
  border-radius: 3px;
  padding: 0.55em 0.7em 0.35em 0.7em;
  margin: 0.5em 0 0.8em 0;
}
.prova-keep h3 { margin-top: 0.4em; }
.prova-keep h3:first-child { margin-top: 0; }
.prova-keep blockquote {
  background: #F7F4EC;
  border-left-color: #C8A024;
}
.prova-keep table { margin-bottom: 0.2em; }

.page-break {
  page-break-before: always;
  break-before: page;
  height: 0;
  margin: 0;
  padding: 0;
}

.cenario {
  border: 1.5px dashed #8a7a3a;
  background: #fff;
  padding: 0.55em 0.75em;
  margin: 0.7em 0;
  page-break-inside: avoid;
}
.cenario h2 {
  border-bottom-color: #8a7a3a;
  margin-top: 0.2em;
}

/* Hero / wordmark strip */
h1 {
  background: #1B2A41;
  color: #F7F4EC;
  padding: 0.55em 0.7em;
  margin: -0.2em -0.1em 0.5em -0.1em;
}

/* Slightly tighten long meta paragraphs under h1 */
h1 + p { margin-top: 0.2em; }
"""

full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8"/>
<title>JP Decision Engine — Portfólio técnico-comercial · 2026-09-22</title>
</head>
<body>
{html_body}
</body>
</html>
"""

OUT_HTML.write_text(full_html, encoding="utf-8")

HTML(string=full_html, base_url=str(SRC.parent)).write_pdf(
    OUT,
    stylesheets=[CSS(string=CSS_TEXT)],
)

print(f"Wrote {OUT}")
print(f"HTML debug: {OUT_HTML}")
