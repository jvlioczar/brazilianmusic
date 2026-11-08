# -*- coding: utf-8 -*-
"""Gera favicon.svg, ícones PNG e imagens de compartilhamento (share-en.png, share-pt.png). Requer Pillow.
Logo: bandeira do Brasil com uma nota musical no círculo azul."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
VERDE, AMARELO, AZUL, BRANCO, INK, PAPER = (0, 151, 57), (254, 221, 0), (1, 33, 105), (255, 255, 255), (21, 32, 26), (253, 248, 239)

SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 49"><rect width="70" height="49" rx="10" fill="#009739"/><path d="M35 4.5 65.5 24.5 35 44.5 4.5 24.5z" fill="#fedd00"/><circle cx="35" cy="24.5" r="12.5" fill="#012169"/><circle cx="31.3" cy="30.2" r="3.7" fill="#fff"/><path d="M34.6 29.6V16.2" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><path d="M34.6 16.2c4.2 1.4 6.4 4.3 5.2 8.4" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/></svg>"""
open(os.path.join(ASSETS, "favicon.svg"), "w", encoding="utf8").write(SVG)


def flag(w, square=False):
    """Bandeira com nota; square=True desenha em um quadrado w×w (ícones)."""
    h = w if square else int(w * 0.7)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w, h), radius=w // 7, fill=VERDE)
    cx, cy = w / 2, h / 2
    rw, rh = w * .43, h * .41
    d.polygon([(cx, cy - rh), (cx + rw, cy), (cx, cy + rh), (cx - rw, cy)], fill=AMARELO)
    r = min(w, h) * .255
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=AZUL)
    # nota musical simplificada: cabeça redonda, haste e bandeirola arredondadas
    k = r / 12.5
    w2 = max(2, int(2.6 * k))
    hx, hy = cx - 3.7 * k, cy + 5.7 * k
    d.ellipse((hx - 3.7 * k, hy - 3.7 * k, hx + 3.7 * k, hy + 3.7 * k), fill=BRANCO)
    sx = cx - 0.4 * k
    d.line((sx, cy + 5.1 * k, sx, cy - 8.3 * k), fill=BRANCO, width=w2)
    d.ellipse((sx - w2 / 2, cy - 8.3 * k - w2 / 2, sx + w2 / 2, cy - 8.3 * k + w2 / 2), fill=BRANCO)
    top = cy - 8.3 * k
    pts = [(sx, top), (sx + 2.8 * k, top + 1.6 * k), (sx + 4.6 * k, top + 4.2 * k), (sx + 5.2 * k, top + 8.4 * k)]
    d.line(pts, fill=BRANCO, width=w2, joint="curve")
    ex, ey = pts[-1]
    d.ellipse((ex - w2 / 2, ey - w2 / 2, ex + w2 / 2, ey + w2 / 2), fill=BRANCO)
    return im


for s in (180, 192, 512):
    flag(s, square=True).save(os.path.join(ASSETS, f"icon-{s}.png"))


def font(size, bold=True):
    for name in (["seguibl.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"]):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def share(lang):
    W, H = 1200, 630
    im = Image.new("RGB", (W, H), VERDE)
    d = ImageDraw.Draw(im)
    d.ellipse((880, -200, 1400, 320), fill=(0, 178, 74))
    d.ellipse((-160, 420, 240, 820), fill=(1, 33, 105))
    im.paste(flag(230), (70, 80), flag(230))
    title = "Brazilian Music" if lang == "en" else "Música Brasileira"
    sub = "The catalogue of Brazil's music" if lang == "en" else "O catálogo da música do Brasil"
    kick = "20 FAMILIES · 105 SUBGENRES · 961 ARTISTS · 1,010 SONGS" if lang == "en" else "20 FAMÍLIAS · 105 SUBGÊNEROS · 961 ARTISTAS · 1.010 MÚSICAS"
    d.text((340, 90), title, font=font(84), fill=BRANCO)
    d.text((340, 200), sub, font=font(40, False), fill=AMARELO)
    d.rounded_rectangle((70, 350, 70 + 24 + len(kick) * 15.5, 404), radius=27, fill=AMARELO)
    d.text((84, 360), kick, font=font(24), fill=(11, 42, 22))
    d.text((70, 470), "brazilianmusic.biblioverse.org", font=font(30, False), fill=BRANCO)
    im.save(os.path.join(ASSETS, f"share-{lang}.png"), optimize=True)


share("en")
share("pt")
print("icons ok")
