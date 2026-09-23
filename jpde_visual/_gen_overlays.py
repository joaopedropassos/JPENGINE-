#!/usr/bin/env python3
"""Generate JPDE video overlays CV-01..07 — B2B industrial 9:16."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("/workspace/jpde_visual/video")
MIRROR = Path("/workspace/jpde_visual/video_overlays_9x16")
OUT.mkdir(parents=True, exist_ok=True)
MIRROR.mkdir(parents=True, exist_ok=True)

W, H = 1080, 1920
DPI = (300, 300)

NAVY = (10, 18, 36)
CHARCOAL = (22, 28, 40)
PANEL = (18, 28, 48)
CYAN = (0, 200, 220)
WHITE = (245, 248, 252)
AMBER = (230, 180, 80)
MUTED = (160, 175, 195)
RED_SEAL = (200, 60, 50)
SEAL_BG = (180, 40, 40)

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def save(img, name):
    path = OUT / name
    img.save(path, "PNG", dpi=DPI)
    mirror = MIRROR / name
    img.save(mirror, "PNG", dpi=DPI)
    print(f"saved {path}")


def bg_gradient():
    img = Image.new("RGB", (W, H), NAVY)
    px = img.load()
    for y in range(H):
        t = y / H
        r = int(NAVY[0] * (1 - t) + CHARCOAL[0] * t)
        g = int(NAVY[1] * (1 - t) + CHARCOAL[1] * t)
        b = int(NAVY[2] * (1 - t) + CHARCOAL[2] * t)
        for x in range(W):
            px[x, y] = (r, g, b)
    return img


def draw_accent_bar(draw, y, x0=80, x1=W - 80, color=CYAN, h=4):
    draw.rectangle([x0, y, x1, y + h], fill=color)


def text_size(draw, text, fnt):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def centered_text(draw, text, y, fnt, fill=WHITE):
    tw, th = text_size(draw, text, fnt)
    draw.text(((W - tw) // 2, y), text, font=fnt, fill=fill)
    return th


def wrap_centered(draw, text, y, fnt, fill=WHITE, max_w=900, line_gap=12):
    words = text.split()
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        tw, _ = text_size(draw, trial, fnt)
        if tw <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    cy = y
    for line in lines:
        th = centered_text(draw, line, cy, fnt, fill)
        cy += th + line_gap
    return cy


def seal_laboratorio(draw, cx, cy, scale=1.0):
    """Circular-ish seal LABORATÓRIO."""
    r = int(70 * scale)
    # outer ring
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=AMBER, width=max(3, int(4 * scale)))
    draw.ellipse([cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8], outline=AMBER, width=2)
    fnt = font(int(18 * scale), bold=True)
    tw, th = text_size(draw, "LABORATÓRIO", fnt)
    draw.text((cx - tw // 2, cy - th // 2), "LABORATÓRIO", font=fnt, fill=AMBER)


# ---------- CV-01 lower-third ----------
def make_cv01():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    # translucent lower panel
    panel_top = int(H * 0.68)
    draw.rectangle([0, panel_top, W, H], fill=PANEL)
    draw_accent_bar(draw, panel_top, 0, W, CYAN, 6)
    # left cyan strip
    draw.rectangle([0, panel_top, 12, H], fill=CYAN)

    f1 = font(52, bold=True)
    f2 = font(34, bold=False)
    y = panel_top + 70
    centered_text(draw, "JP Decision Engine", y, f1, WHITE)
    y += 80
    draw_accent_bar(draw, y, 200, W - 200, CYAN, 3)
    y += 30
    wrap_centered(draw, "Motor plugável de rota intramuros", y, f2, CYAN, max_w=920)
    save(img, "CV-01_lower_third.png")


# ---------- CV-02 tipográfico ----------
def make_cv02():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    lines = [
        "O mapa quase não muda.",
        "A consulta se repete.",
        "A rota continua ótima.",
        "O planner para de começar do zero.",
    ]
    fnt = font(42, bold=True)
    # vertical stack centered
    total_h = 0
    sizes = []
    for line in lines:
        tw, th = text_size(draw, line, fnt)
        sizes.append((tw, th))
        total_h += th
    gap = 48
    total_h += gap * (len(lines) - 1)
    y = (H - total_h) // 2 - 40
    draw_accent_bar(draw, y - 40, 180, W - 180, CYAN, 4)
    for i, line in enumerate(lines):
        tw, th = sizes[i]
        draw.text(((W - tw) // 2, y), line, font=fnt, fill=WHITE)
        y += th + gap
        if i < len(lines) - 1:
            # subtle separator
            mid = y - gap // 2
            draw.line([340, mid, W - 340, mid], fill=(50, 70, 95), width=1)
    draw_accent_bar(draw, y + 20, 180, W - 180, CYAN, 4)
    save(img, "CV-02_tipografico.png")


# ---------- CV-03 lab v5 ----------
def make_cv03():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    # card panel
    margin_x, margin_y = 70, 220
    draw.rounded_rectangle(
        [margin_x, margin_y, W - margin_x, H - margin_y],
        radius=24,
        fill=PANEL,
        outline=CYAN,
        width=3,
    )
    seal_laboratorio(draw, W // 2, margin_y + 110, scale=1.15)

    f_title = font(44, bold=True)
    f_body = font(32, bold=False)
    f_num = font(36, bold=True)

    y = margin_y + 220
    centered_text(draw, "Laboratório v5", y, f_title, WHITE)
    y += 70
    draw_accent_bar(draw, y, 200, W - 200, AMBER, 3)
    y += 50

    bullets = [
        ("1000 consultas", WHITE),
        ("JP-Geo cerca de 28% mais rápido que A* fixo", CYAN),
        ("cerca de 31% menos nós", CYAN),
        ("100% de otimalidade", WHITE),
    ]
    for text, color in bullets:
        # bullet diamond
        bx = 140
        draw.polygon([(bx, y + 14), (bx + 10, y + 4), (bx + 20, y + 14), (bx + 10, y + 24)], fill=AMBER)
        # wrap manually from left indent
        f = f_num if "28%" in text or "31%" in text or "100%" in text else f_body
        # simple left-aligned wrap
        words = text.split()
        cur = ""
        lines_out = []
        for w in words:
            trial = (cur + " " + w).strip()
            tw, _ = text_size(draw, trial, f)
            if tw <= 720:
                cur = trial
            else:
                lines_out.append(cur)
                cur = w
        if cur:
            lines_out.append(cur)
        for j, ln in enumerate(lines_out):
            draw.text((180, y), ln, font=f, fill=color)
            _, th = text_size(draw, ln, f)
            y += th + 8
        y += 28

    # footer
    f_foot = font(22, bold=False)
    centered_text(draw, "Prova de laboratório — não é case de opex", H - margin_y - 60, f_foot, MUTED)
    save(img, "CV-03_lab_v5.png")


# ---------- CV-04 lab v7 ----------
def make_cv04():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    margin_x, margin_y = 70, 280
    draw.rounded_rectangle(
        [margin_x, margin_y, W - margin_x, H - margin_y],
        radius=24,
        fill=PANEL,
        outline=CYAN,
        width=3,
    )
    seal_laboratorio(draw, W // 2, margin_y + 110, scale=1.15)

    f_title = font(44, bold=True)
    f_body = font(34, bold=False)
    f_big = font(40, bold=True)

    y = margin_y + 220
    centered_text(draw, "Laboratório v7", y, f_title, WHITE)
    y += 70
    draw_accent_bar(draw, y, 200, W - 200, AMBER, 3)
    y += 60

    y = wrap_centered(draw, "Decepção geométrica alta", y, f_body, MUTED, max_w=820)
    y += 50
    y = wrap_centered(
        draw,
        "Geo vs A* até cerca de 73% menos nós",
        y,
        f_big,
        CYAN,
        max_w=820,
        line_gap=16,
    )

    f_foot = font(22, bold=False)
    centered_text(draw, "Prova de laboratório — não é case de opex", H - margin_y - 60, f_foot, MUTED)
    save(img, "CV-04_lab_v7.png")


# ---------- CV-05 banner ----------
def make_cv05():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    # horizontal banner band mid
    band_top = H // 2 - 140
    band_bot = H // 2 + 140
    draw.rectangle([0, band_top, W, band_bot], fill=PANEL)
    draw.rectangle([0, band_top, W, band_top + 6], fill=AMBER)
    draw.rectangle([0, band_bot - 6, W, band_bot], fill=AMBER)

    fnt = font(36, bold=True)
    text = "Prova de laboratório · não é case de opex"
    # may need wrap
    y = band_top + 70
    wrap_centered(draw, text, y, fnt, WHITE, max_w=960, line_gap=14)
    save(img, "CV-05_banner_lab.png")


# ---------- CV-06 faixa alvos ----------
def make_cv06():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    band_top = H // 2 - 180
    band_bot = H // 2 + 180
    draw.rectangle([0, band_top, W, band_bot], fill=PANEL)
    draw_accent_bar(draw, band_top, 0, W, CYAN, 5)
    draw_accent_bar(draw, band_bot - 5, 0, W, CYAN, 5)

    f1 = font(40, bold=True)
    f2 = font(32, bold=False)
    y = band_top + 70
    wrap_centered(draw, "Delage · Automni · AGVS · 3PL · CD", y, f1, WHITE, max_w=960, line_gap=12)
    y = band_top + 200
    centered_text(draw, "layout estável", y, f2, CYAN)
    save(img, "CV-06_faixa_alvos.png")


# ---------- CV-07 CTA ----------
def make_cv07():
    img = bg_gradient()
    draw = ImageDraw.Draw(img)
    margin_x, margin_y = 60, 400
    draw.rounded_rectangle(
        [margin_x, margin_y, W - margin_x, H - margin_y],
        radius=24,
        fill=PANEL,
        outline=CYAN,
        width=3,
    )
    draw_accent_bar(draw, margin_y + 40, 200, W - 200, CYAN, 4)

    f1 = font(38, bold=True)
    f2 = font(34, bold=False)

    y = margin_y + 100
    y = wrap_centered(
        draw,
        "Quero o diagnóstico de duas semanas no mapa de vocês.",
        y,
        f1,
        WHITE,
        max_w=880,
        line_gap=14,
    )
    y += 50
    draw_accent_bar(draw, y, 320, W - 320, AMBER, 2)
    y += 40
    centered_text(draw, "ou 30 minutos", y, f2, CYAN)
    save(img, "CV-07_cta.png")


if __name__ == "__main__":
    make_cv01()
    make_cv02()
    make_cv03()
    make_cv04()
    make_cv05()
    make_cv06()
    make_cv07()
    print("DONE")
