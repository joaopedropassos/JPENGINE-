#!/usr/bin/env python3
"""Build sober technical Word DOCX for JPDE/INPI dossier pieces 03, 04, 05."""

from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement
import re

BASE = Path("/workspace/03_patente_INPI")
FIG = BASE / "figuras"
AUTHOR = "João Pedro Pereira Passos"
BANNER = "RASCUNHO DE TRABALHO — SEM VALOR DE PROTOCOLO"
FONT = "Times New Roman"
SIZE = 12


def set_run_font(run, bold=False, italic=False, size=SIZE, font=FONT):
    run.font.name = font
    run._element.rPr.rFonts.set(qn("w:eastAsia"), font)
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)


def set_paragraph_format(p, space_after=6, space_before=0, first_line=None):
    pf = p.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    if first_line is not None:
        pf.first_line_indent = Cm(first_line)


def add_header_banner(doc):
    section = doc.sections[0]
    header = section.header
    header.is_linked_to_previous = False
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(BANNER)
    set_run_font(run, bold=True, size=10)
    # subtle bottom border via paragraph border
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), "666666")
    pBdr.append(bottom)
    pPr.append(pBdr)


def setup_doc():
    doc = Document()
    # Core props
    core = doc.core_properties
    core.author = AUTHOR
    core.language = "pt-BR"

    section = doc.sections[0]
    section.page_width = Cm(21.0)   # A4
    section.page_height = Cm(29.7)
    section.left_margin = Cm(3.0)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)

    # Default style
    style = doc.styles["Normal"]
    style.font.name = FONT
    style.font.size = Pt(SIZE)
    style._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE

    for level in range(1, 4):
        hs = doc.styles[f"Heading {level}"]
        hs.font.name = FONT
        hs.font.color.rgb = RGBColor(0, 0, 0)
        hs._element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
        if level == 1:
            hs.font.size = Pt(14)
            hs.font.bold = True
        elif level == 2:
            hs.font.size = Pt(13)
            hs.font.bold = True
        else:
            hs.font.size = Pt(12)
            hs.font.bold = True

    add_header_banner(doc)
    return doc


def add_para(doc, text, bold=False, italic=False, size=SIZE, align=None, space_after=6):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    set_paragraph_format(p, space_after=space_after)
    # handle inline **bold** and *italic* simply
    parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = p.add_run(part[2:-2])
            set_run_font(run, bold=True, size=size)
        elif part.startswith("`") and part.endswith("`"):
            run = p.add_run(part[1:-1])
            set_run_font(run, italic=True, size=size, font="Courier New")
        else:
            run = p.add_run(part)
            set_run_font(run, bold=bold, italic=italic, size=size)
    return p


def add_heading_custom(doc, text, level=1):
    # strip leading markdown hashes already handled by caller
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        set_run_font(run, bold=True, size={1: 14, 2: 13, 3: 12}.get(level, 12))
        run.font.color.rgb = RGBColor(0, 0, 0)
    return h


def add_bullet(doc, text, level=0):
    p = doc.add_paragraph(style="List Bullet")
    set_paragraph_format(p, space_after=3)
    p.clear()
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = p.add_run(part[2:-2])
            set_run_font(run, bold=True)
        else:
            run = p.add_run(part)
            set_run_font(run)
    if level:
        p.paragraph_format.left_indent = Cm(0.75 * level)
    return p


def add_table_from_rows(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        run = p.add_run(h)
        set_run_font(run, bold=True, size=10)
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            # strip markdown bold in cells
            clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", val)
            run = p.add_run(clean)
            set_run_font(run, size=10)
    doc.add_paragraph()  # spacer
    return table


def add_figure(doc, png_path, caption, width_cm=15.5):
    """Caption above figure (Brazilian patent practice OK), then image, then fonte."""
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(cap, space_after=4, space_before=12)
    run = cap.add_run(caption)
    set_run_font(run, bold=True, size=11)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(p, space_after=2)
    run = p.add_run()
    run.add_picture(str(png_path), width=Cm(width_cm))

    fonte = doc.add_paragraph()
    fonte.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_format(fonte, space_after=10)
    run = fonte.add_run("Fonte: elaboração própria.")
    set_run_font(run, italic=True, size=9)


# ─── Markdown → structured blocks (lightweight) ───────────────────────────────

def parse_md_blocks(text):
    """Yield (type, payload) blocks from markdown."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "---":
            yield ("hr", None)
            i += 1
            continue
        if line.startswith("# "):
            yield ("h1", line[2:].strip())
            i += 1
            continue
        if line.startswith("## "):
            yield ("h2", line[3:].strip())
            i += 1
            continue
        if line.startswith("### "):
            yield ("h3", line[4:].strip())
            i += 1
            continue
        # table
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|?\s*-+", lines[i + 1]):
            rows = []
            while i < len(lines) and "|" in lines[i]:
                row = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(row)
                i += 1
            # skip separator already included
            headers = rows[0]
            body = [r for r in rows[1:] if not all(re.match(r"^:?-+:?$", c) for c in r)]
            yield ("table", (headers, body))
            continue
        # bullet
        if re.match(r"^[-*]\s+", line):
            bullets = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i]):
                bullets.append(re.sub(r"^[-*]\s+", "", lines[i]))
                i += 1
            yield ("bullets", bullets)
            continue
        # numbered list
        if re.match(r"^\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i]))
                i += 1
            yield ("numbered", items)
            continue
        # blank
        if not line.strip():
            i += 1
            continue
        # paragraph (accumulate until blank or special)
        para_lines = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("---") and not re.match(r"^[-*]\s+", lines[i]) and not ( "|" in lines[i] and i + 1 < len(lines) and re.match(r"^\s*\|?\s*-+", lines[i + 1])):
            if re.match(r"^\d+\.\s+", lines[i]):
                break
            para_lines.append(lines[i])
            i += 1
        yield ("para", " ".join(l.strip() for l in para_lines))


def render_blocks(doc, blocks, skip_first_banner_h1=True):
    """Render parsed blocks into doc. Skip duplicate banner H1 if already in header."""
    first_h1_done = False
    for kind, payload in blocks:
        if kind == "hr":
            continue
        if kind == "h1":
            if skip_first_banner_h1 and not first_h1_done and BANNER in payload:
                # already in header; skip
                first_h1_done = True
                continue
            first_h1_done = True
            add_heading_custom(doc, payload, 1)
        elif kind == "h2":
            add_heading_custom(doc, payload, 2)
        elif kind == "h3":
            add_heading_custom(doc, payload, 3)
        elif kind == "para":
            # italic-only wrapper like *(Contagem...)*
            t = payload
            if t.startswith("*(") and t.endswith(")*"):
                add_para(doc, t[1:-1], italic=True, size=10)
            elif t.startswith("*") and t.endswith("*") and not t.startswith("**"):
                add_para(doc, t[1:-1], italic=True)
            else:
                add_para(doc, t)
        elif kind == "bullets":
            for b in payload:
                add_bullet(doc, b)
        elif kind == "numbered":
            for n, item in enumerate(payload, 1):
                p = doc.add_paragraph()
                set_paragraph_format(p, space_after=3)
                # number + text with bold
                parts = re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", f"{n}. {item}")
                for part in parts:
                    if part.startswith("**") and part.endswith("**"):
                        run = p.add_run(part[2:-2])
                        set_run_font(run, bold=True)
                    elif part.startswith("`") and part.endswith("`"):
                        run = p.add_run(part[1:-1])
                        set_run_font(run, italic=True, font="Courier New")
                    else:
                        run = p.add_run(part)
                        set_run_font(run)
        elif kind == "table":
            headers, body = payload
            add_table_from_rows(doc, headers, body)


# ─── Build 03 ─────────────────────────────────────────────────────────────────

def build_03():
    md = (BASE / "03_memorial_descritivo.md").read_text(encoding="utf-8")
    doc = setup_doc()
    doc.core_properties.title = "03 — Memorial descritivo (rascunho) | ETAPA 2"
    doc.core_properties.subject = "JPDE/INPI — memorial descritivo (rascunho)"
    render_blocks(doc, parse_md_blocks(md))
    out = BASE / "03_memorial_descritivo.docx"
    doc.save(out)
    return out


# ─── Build 04 ─────────────────────────────────────────────────────────────────

def build_04():
    md = (BASE / "04_reivindicacoes_rascunho.md").read_text(encoding="utf-8")
    doc = setup_doc()
    doc.core_properties.title = "04 — Reivindicações (rascunho) | ETAPA 3"
    doc.core_properties.subject = "JPDE/INPI — reivindicações (rascunho)"
    render_blocks(doc, parse_md_blocks(md))
    out = BASE / "04_reivindicacoes_rascunho.docx"
    doc.save(out)
    return out


# ─── Build 05 with figures ────────────────────────────────────────────────────

# Mapping: MD Fig N → list of (png, caption override or None)
# Follow MANIFEST for Fig numbers when stated; content match otherwise.
# Optional MD Fig.10 (positioning table) — NOT embedded (no invent; not requested).

FIG_MAP = [
    # Figura 1 — offline + online flows (two delivered PNGs)
    {
        "md_num": 1,
        "title": "Visão geral offline / online",
        "desc": (
            "Fluxograma em caixas: Entrada do mapa → Grafo → Seleção de landmarks "
            "geométricos → Tabelas de distância → Prior persistido → (seta) Consulta O-D → "
            "Busca informada tipo ALT → Caminho ótimo. Nota lateral: «invalidação se layout mudar»."
        ),
        "images": [
            ("fig01_fluxo_offline.png",
             "Figura 1a — Fluxo offline: layout → grafo → seleção de k landmarks geométricos (FPS) → tabelas de distância / prior estrutural."),
            ("fig02_fluxo_online.png",
             "Figura 1b — Fluxo online: consulta O–D → heurística tipo ALT (landmarks) → busca informada → rota; invalidação do prior se o mapa mudar."),
        ],
    },
    {
        "md_num": 2,
        "title": "Layout esquemático de armazém (DG ilustrativo)",
        "desc": (
            "Planta esquemática com corredores em «U»/«S», obstáculos retangulares, origem O e destino D. "
            "Indicar caminho de grafo vs linha Manhattan. Rótulo: «DG = d_grafo / d_Manhattan elevado»."
        ),
        "images": [
            ("fig03_mapa_DG_alto.png",
             "Figura 2 — Esquema de planta com corredor tortuoso; anotação conceitual DG = d_grafo / d_Manhattan."),
        ],
    },
    {
        "md_num": 3,
        "title": "Landmarks geométricos (FPS — esquemático)",
        "desc": "Mesmo layout da Fig. 2 com k pontos marcados como L1…Lk espalhados; sem revelar pseudocódigo.",
        "images": [
            ("fig09_landmarks_FPS.png",
             "Figura 3 — Landmarks geométricos (FPS): mesma planta esquemática com k landmarks L1…Lk espalhados (farthest-point sampling)."),
        ],
    },
    {
        "md_num": 4,
        "title": "Uso da desigualdade triangular (ALT)",
        "desc": (
            "Diagrama de três pontos: nó u, destino t, landmark L; setas com distâncias pré-computadas; "
            "caixa «heurística admissível h(u)»."
        ),
        "images": [
            ("fig06_admissibilidade.png",
             "Figura 4 — Desigualdade triangular com landmark (origem–landmark–destino) e admissibilidade da heurística."),
        ],
    },
    {
        "md_num": 5,
        "title": "Comparativo qualitativo de expansão (v5/v7)",
        "desc": (
            "Dois painéis lado a lado: «A* heurística fixa» (nuvem de nós maior) vs «busca com prior de "
            "landmarks geométricos» (nuvem menor). Rodapé: «ilustração qualitativa — dados internos v5/v7; "
            "não é certificado INPI»."
        ),
        "images": [
            ("fig10_expansao_Astar_vs_prior.png",
             "Figura 5 — Comparativo qualitativo de expansão: A* heurística fixa (nuvem maior) vs busca com prior de landmarks (nuvem menor); ilustração qualitativa — dados internos v5/v7; não é certificado INPI."),
        ],
    },
    {
        "md_num": 6,
        "title": "Amortização do pré-processamento (Q*)",
        "desc": (
            "Gráfico esquemático eixo X = número de consultas; eixo Y = custo médio por consulta; "
            "curva caindo até patamar; marcar Q* de break-even como «PENDENTE DE MEDIÇÃO em mapa-alvo»."
        ),
        "images": [
            ("fig04_amortizacao_consultas.png",
             "Figura 6 — Q* (nº de consultas) vs custo acumulado: curvas conceituais A* fixo vs prior+landmarks (amortização)."),
        ],
    },
    {
        "md_num": 7,
        "title": "Invalidação do prior",
        "desc": (
            "Diagrama de estados: Prior válido → Evento de mudança de layout → Prior inválido → "
            "Reexecução offline → Prior válido."
        ),
        "images": [
            ("fig11_invalidacao_prior.png",
             "Figura 7 — Diagrama de estados: Prior válido → Evento de mudança de layout → Prior inválido → Reexecução offline → Prior válido."),
        ],
    },
    {
        "md_num": 8,
        "title": "Integração lógica (API sem código)",
        "desc": (
            "Caixas: «Cliente de consulta O-D» → «Interface de serviço (sem listar endpoints secretos)» → "
            "«Motor offline/online» → «Armazenamento do prior». Proibir listagem de código."
        ),
        "images": [
            ("fig05_api_blocos.png",
             "Figura 8 — Arquitetura em blocos: Layout | Grafo | Prior | Planner | Rota."),
        ],
    },
    {
        "md_num": 9,
        "title": "Fronteira do que não se reivindica como essencial",
        "desc": (
            "Nuvem tracejada «TDA / homologia / Wasserstein / persistência» com carimbo "
            "«não essencial — ver nota v6/v7»."
        ),
        "images": [
            ("fig12_fronteira_TDA.png",
             "Figura 9 — Fronteira do que não se reivindica: nuvem tracejada TDA / homologia / Wasserstein / persistência com carimbo «não essencial — ver nota v6/v7»."),
        ],
    },
]

SKIPPED = [
    ("fig07_checklist_trilho_A.png", "Não mapeada às Figs. 1–9 do md §Figuras (checklist Trilho A — auxiliar de processo)."),
    ("fig08_trilhos_AB.png", "Não mapeada às Figs. 1–9 do md §Figuras (trilhos A/B — auxiliar de processo)."),
    ("Figura 10 (opcional md)", "Posicionamento frente ao estado da técnica — NÃO solicitada; sem PNG de tabela de posicionamento; não inventada/embutida."),
]


def build_05():
    md = (BASE / "05_resumo_e_figuras.md").read_text(encoding="utf-8")
    doc = setup_doc()
    doc.core_properties.title = "05 — Resumo e figuras | ETAPA 4"
    doc.core_properties.subject = "JPDE/INPI — resumo e figuras (rascunho)"

    # Title block (skip duplicate banner)
    add_heading_custom(doc, "05 — Resumo e figuras | ETAPA 4", 1)
    add_para(doc, f"**Autor / Inventor:** {AUTHOR}", space_after=8)

    # Resumo section — extract from md between ## Resumo and ## Figuras
    m = re.search(r"## Resumo[^\n]*\n+(.*?)\n+## Figuras", md, re.S)
    add_heading_custom(doc, "Resumo (≈ 210 palavras)", 2)
    if m:
        resumo_block = m.group(1).strip()
        for para in resumo_block.split("\n\n"):
            para = para.strip()
            if not para:
                continue
            if para.startswith("*(") and para.endswith(")*"):
                add_para(doc, para[1:-1], italic=True, size=10)
            else:
                add_para(doc, para)
    else:
        add_para(doc, "(Resumo não encontrado no markdown.)", italic=True)

    add_heading_custom(doc, "Figuras (desenhos técnicos — linhas pretas; sem foto de cliente; sem logo)", 2)
    add_para(
        doc,
        "Instruções ao desenhista: traço preto em fundo branco; tipografia legível; sem logotipos; "
        "sem fotografias de instalações de terceiros; sem dados de cliente. "
        "Figuras embutidas conforme «Figuras» do memorial e MANIFEST_figuras.md. "
        "Figura 10 (opcional — posicionamento frente ao estado da técnica) não foi solicitada e não está embutida.",
        size=10,
        italic=True,
    )

    embedded = []
    for entry in FIG_MAP:
        add_heading_custom(doc, f"Figura {entry['md_num']} — {entry['title']}", 3)
        add_para(doc, entry["desc"], size=11)
        for fname, caption in entry["images"]:
            path = FIG / fname
            if not path.exists():
                add_para(doc, f"[ARQUIVO AUSENTE: {fname}]", italic=True, bold=True)
                continue
            add_figure(doc, path, caption)
            embedded.append((entry["md_num"], fname, caption))

    # Note on optional Fig 10
    add_heading_custom(doc, "Figura 10 — (Opcional) Posicionamento frente ao estado da técnica — NÃO EMBUTIDA", 3)
    add_para(
        doc,
        "Descrição no rascunho (não solicitada para desenho entregue): tabela visual simples: "
        "Dijkstra | A* | ALT | JPS | CH | Presente proposta (offline/online + landmarks geométricos + "
        "reuso/invalidação). Sem números de patente inventados na figura. "
        "**Status:** opcional não solicitada pelo orquestrador; nenhum PNG de tabela de posicionamento "
        "foi inventado ou embutido. (Nota: o arquivo fig10_expansao_Astar_vs_prior.png corresponde à "
        "Figura 5 do memorial, conforme MANIFEST, e foi embutido acima.)",
        size=11,
    )

    # Annex note: skipped process figures available on Drive
    add_heading_custom(doc, "Anexo — PNGs entregues não mapeados às Figs. 1–9", 2)
    add_para(
        doc,
        "Os seguintes arquivos foram baixados do Drive mas não embutidos neste documento porque "
        "não correspondem às Figuras 1–9 da seção «Figuras» do markdown (são auxiliares de processo "
        "Trilho A / A–B):",
        size=10,
    )
    for fname, reason in SKIPPED:
        if fname.startswith("Figura"):
            continue
        add_bullet(doc, f"`{fname}` — {reason}")

    out = BASE / "05_resumo_e_figuras.docx"
    doc.save(out)

    # write embedding report sidecar for parent
    report = {
        "embedded": embedded,
        "skipped": SKIPPED,
        "media_count": len(embedded),
    }
    return out, report


def main():
    o3 = build_03()
    o4 = build_04()
    o5, report = build_05()
    print("BUILT:")
    for p in (o3, o4, o5):
        print(f"  {p}  size={p.stat().st_size}")
    print(f"MEDIA_COUNT_05={report['media_count']}")
    for md_n, fname, cap in report["embedded"]:
        print(f"  EMBEDDED Fig.{md_n}: {fname}")
    for item, reason in report["skipped"]:
        print(f"  SKIPPED: {item} — {reason}")


if __name__ == "__main__":
    main()
