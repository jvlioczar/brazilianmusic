# -*- coding: utf-8 -*-
"""Gera o site Música Brasileira: EN na raiz, PT em /pt/. Rode: python tools/build.py"""
import html, json, os, re, shutil, sys
from urllib.parse import quote_plus

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import data_core as C  # noqa: E402
import data_songs as S  # noqa: E402
import data_musicians as M  # noqa: E402
import data_artists_rock as AR  # noqa: E402
import data_artists_other as AO  # noqa: E402
import data_hits as HI  # noqa: E402
import items as IT  # noqa: E402
import data_albums as AL  # noqa: E402
import data_artists_more as AM  # noqa: E402

SITE, BUILT, UI, PATHS = C.SITE, C.BUILT, C.UI, C.PATHS
L = {"pt": 0, "en": 1}
# a família começa no subgênero mais antigo
for _f in C.FAMILIES:
    _f["since"] = min([_f["since"]] + [_s["since"] for _s in _f["subs"]])
FAM = {f["id"]: f for f in C.FAMILIES}
SUB = {}
for f in C.FAMILIES:
    for s in f["subs"]:
        s["family"] = f["id"]
        SUB[s["id"]] = s


def e(s):
    return html.escape(str(s), quote=True)


def t(x, lang):
    return x[L[lang]] if isinstance(x, (tuple, list)) else x


def yt(q):
    return "https://www.youtube.com/results?search_query=" + quote_plus(q)


# ── artistas ──────────────────────────────────────────────────────────────────
def parse_artists(block):
    out = []
    for line in block.strip().splitlines():
        if not line.strip():
            continue
        name, typ, genres, year, uf, tier, tags, pt, en = [x.strip() for x in line.split("|")]
        g = [x for x in genres.split(",") if x]
        for x in g:
            assert x in SUB, (name, x)
        out.append(dict(name=name, type=typ, genres=g, year=int(year) if year else 0, uf=uf, tier=tier,
                        tags=[x for x in tags.split(",") if x], blurb=(pt, en), family=SUB[g[0]]["family"]))
    return out


ARTISTS = parse_artists(AR.ROCK) + parse_artists(AO.OTHER) + parse_artists(AM.MORE)
assert len({a["name"].lower() for a in ARTISTS}) == len(ARTISTS)
FAM_ORDER = [f["id"] for f in C.FAMILIES]
TIER_ORDER = {"S": 0, "A": 1, "B": 2, "": 3}
ARTISTS.sort(key=lambda a: (FAM_ORDER.index(a["family"]), TIER_ORDER[a["tier"]], a["year"] or 9999, a["name"].lower()))
counter = {}
for a in ARTISTS:
    code = FAM[a["family"]]["code"]
    counter[code] = counter.get(code, 0) + 1
    a["code"] = f"{code}-{counter[code]:03d}"
    a["id"] = IT.slugify(a["name"])
assert len({a["id"] for a in ARTISTS}) == len(ARTISTS)
BY_SUB = {}
for a in ARTISTS:
    for g in a["genres"]:
        BY_SUB.setdefault(g, []).append(a)

ROCK_SONGS = [(int(y), s, a, "rock") for y, s, a in S.rows(S.ROCK_SONGS, 3)]
FUNK_SONGS = [(int(y), s, a, "funk") for y, s, a in S.rows(S.FUNK_SONGS, 3)]
HITS = [(int(y), s_, a, f) for y, s_, a, f in S.rows(HI.HITS, 4)]
for _r in HITS:
    assert _r[3] in FAM, _r
SONGS = sorted(ROCK_SONGS + FUNK_SONGS + HITS, key=lambda x: (x[0], x[3], x[1]))
ROCK_ALBUMS = S.rows(S.ROCK_ALBUMS, 5)
ALBUMS = sorted([(int(y), al, ar, "rock", pt, en) for y, al, ar, pt, en in ROCK_ALBUMS] +
                [(int(y), al, ar, f, pt, en) for y, al, ar, f, pt, en in S.rows(AL.ALBUMS, 6)], key=lambda r: (r[0], r[3], r[1]))
for _r in ALBUMS:
    assert _r[3] in FAM, _r
SERTANEJO = sorted(S.rows(S.SERTANEJO, 3), key=lambda r: (int(r[0]), r[1]))
GUIT, BASS, DRUM, PROD = M.rows(M.GUITARISTS), M.rows(M.BASSISTS), M.rows(M.DRUMMERS), M.rows(M.PRODUCERS)
ACOU, KEYS, ACC, CHOS, WIND, PERC = (M.rows(M.ACOUSTIC), M.rows(M.KEYS), M.rows(M.ACCORDION), M.rows(M.CHORO_STRINGS), M.rows(M.WINDS), M.rows(M.PERCUSSION))
# grupos da página de instrumentistas: (código, chave do texto, linhas, nº em destaque)
INSTR = [("gtr", "guitar", GUIT, 9), ("vio", "acoustic", ACOU, 6), ("bss", "bass", BASS, 8), ("drm", "drums", DRUM, 7), ("per", "percussion", PERC, 4),
         ("tec", "keys", KEYS, 5), ("san", "accordion", ACC, 4), ("cho", "choroStrings", CHOS, 3), ("sop", "winds", WIND, 5)]
VOC = M.rows(M.VOCALISTS)
N_MUS = len({IT.slugify(n) for rows_ in [VOC, PROD] + [r for _c, _k, r, _f in INSTR] for n, _a, _b in rows_})
N_SUBS = len(SUB)
STATS = dict(f=len(C.FAMILIES), s=N_SUBS, a=len(ARTISTS), m=N_MUS, n=len(SONGS), d=len(ALBUMS))


def approx(n, lang):
    """Número aproximado para SEO e textos de abertura: '+1.400' (pt) / '+1,400' (en)."""
    step = 10 if n < 200 else 50 if n < 1000 else 100
    v = n // step * step
    txt = f"{v:,}".replace(",", "." if lang == "pt" else ",")
    return "+" + txt


def n_music_artists():
    """Artistas do catálogo mais pessoas (vocalistas, instrumentistas, produtores), sem repetir quem está nas duas listas."""
    names = {IT.norm(a["name"]) for a in ARTISTS}
    for rows_ in [VOC, PROD] + [r for _c, _k, r, _f in INSTR]:
        names |= {IT.norm(n) for n, _a, _b in rows_}
    return len(names)


def seo_stats(lang):
    return {k: approx(v, lang) for k, v in STATS.items()} | {"gs": approx(STATS["f"] + STATS["s"], lang), "am": approx(n_music_artists(), lang),
            "y0": SONGS[0][0], "y1": SONGS[-1][0], "ay0": ALBUMS[0][0], "ay1": ALBUMS[-1][0]}

LOGO = '<svg viewBox="0 0 70 49" aria-hidden="true"><rect width="70" height="49" rx="10" fill="#009739"/><path d="M35 4.5 65.5 24.5 35 44.5 4.5 24.5z" fill="#fedd00"/><circle cx="35" cy="24.5" r="12.5" fill="#012169"/><circle cx="31.3" cy="30.2" r="3.7" fill="#fff"/><path d="M34.6 29.6V16.2" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/><path d="M34.6 16.2c4.2 1.4 6.4 4.3 5.2 8.4" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/></svg>'
URLS = []

# ── azulejos (painéis geométricos à Athos Bulcão) ─────────────────────────────
import random as _rnd

MOTIFS = {
    "tri": '<path d="M0 0H1V1Z"/>', "quarter": '<path d="M0 0H1A1 1 0 0 1 0 1Z"/>', "half": '<rect width="1" height=".5"/>',
    "dot": '<circle cx=".5" cy=".5" r=".3"/>', "corner": '<path d="M0 0H.5A.5 .5 0 0 1 0 .5Z"/>', "bar": '<rect x=".35" width=".3" height="1"/>',
}
MOTIF_KEYS = ["tri", "tri", "quarter", "quarter", "half", "dot", "corner", "bar"]


def mosaic(cols, rows, bg, inks, seed, cls="mosaic", density=.82, anim=True, label=""):
    """SVG de cols×rows azulejos. bg = cor do azulejo; inks = cores dos motivos (escolhidas ao acaso)."""
    r = _rnd.Random(seed)
    cls = f"{cls} anim" if anim else cls
    out = [f'<svg class="{cls}" viewBox="0 0 {cols} {rows}" preserveAspectRatio="{'xMinYMin slice' if rows == 1 else 'xMidYMid slice'}" aria-hidden="true" role="img"{" aria-label=" + chr(34) + e(label) + chr(34) if label else ""}>',
           f'<rect width="{cols}" height="{rows}" fill="{bg}"/>']
    for y in range(rows):
        for x in range(cols):
            if r.random() > density:
                continue
            m = r.choice(MOTIF_KEYS)
            rot = r.choice((0, 90, 180, 270))
            ink = r.choice(inks)
            delay = f' style="--d:{r.uniform(0, 14):.1f}s;--p:{r.choice((10, 14, 18))}s"' if anim else ""
            out.append(f'<g class="tile" transform="translate({x} {y})"><g class="tin"{delay}><g transform="rotate({rot} .5 .5)" fill="{ink}">{MOTIFS[m]}</g></g></g>')
    out.append("</svg>")
    return "".join(out)


def strip(seed, bg, inks, cols=36, cls="tstrip", anim=False):
    """Faixa de azulejos: desenha azulejos de sobra e o CSS mostra só azulejos inteiros (largura múltipla do lado do azulejo)."""
    if "foot" not in cls and cols < 80:
        cols = 80
    return mosaic(cols, 1, bg, inks, seed, cls=cls, density=.9, anim=anim)


FLAG_INKS = ["#fedd00", "#ffffff", "#012169"]
SHAPES = ('<div class="shapes" aria-hidden="true">'
          '<svg class="shape s1" viewBox="0 0 100 100"><path d="M50 4 96 50 50 96 4 50z" fill="#fedd00"/><circle cx="50" cy="50" r="19" fill="#012169"/><path d="M52 36v20" stroke="#fff" stroke-width="3" stroke-linecap="round"/><ellipse cx="47.5" cy="57" rx="6" ry="4.2" transform="rotate(-22 47.5 57)" fill="#fff"/><path d="M52 36c5 2 8.5 5 8.5 10 0 2.3-.8 4-2 5.4 1.8-3.8.3-7.5-6.5-9.7z" fill="#fff"/></svg>'
          '<svg class="shape s2" viewBox="0 0 100 100"><path d="M50 6c22-4 44 12 44 36 0 26-20 52-46 52S4 70 6 44C8 22 28 10 50 6z" fill="#ff5fa2"/></svg>'
          '<svg class="shape s3" viewBox="0 0 100 100"><path d="M10 90C10 40 40 10 92 8c2 52-28 82-82 82z" fill="#d9ff5c"/><path d="M14 86C34 60 58 36 88 12" stroke="#009739" stroke-width="3" fill="none" stroke-linecap="round"/></svg>'
          '<svg class="shape s4" viewBox="0 0 60 60"><path d="M34 6v32" stroke="#fff" stroke-width="5" stroke-linecap="round"/><ellipse cx="26" cy="41" rx="10" ry="7" transform="rotate(-22 26 41)" fill="#fff"/><path d="M34 6c8 3 13 8 13 16 0 4-1.3 6.5-3.3 8.5 3-6 .5-12-9.7-15.5z" fill="#fff"/></svg>'
          '<svg class="shape s5" viewBox="0 0 60 60"><circle cx="30" cy="30" r="28" fill="#ff7a00"/></svg>'
          '</div>')


class Page:
    def __init__(self, lang):
        self.lang, self.t, self.p = lang, UI[lang], PATHS[lang]

    def href(self, depth, target):
        if target == "index.html":
            return "../" * depth or "./"
        return "../" * depth + target

    def menu(self, depth, cur):
        """Menu do topo em categorias com submenus."""
        tt, p = self.t, self.p
        chev = '<svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        aw = self.href(depth, p["awards"])
        groups = [
            ("genres", ["genres", "map"], None),
            ("music", ["songs", "albums"], [(tt["nav"]["songs"], self.href(depth, p["songs"]), "songs"), (tt["nav"]["albums"], self.href(depth, p["albums"]), "albums")]),
            ("people", ["artists", "singers", "musicians", "producers", "influencers"], [(tt["nav"][k], self.href(depth, p[k]), k) for k in ("artists", "singers", "musicians", "producers", "influencers")]),
            ("scene", ["awards", "media"], [(tt["awA"], aw + "#awards", ""), (tt["awF"], aw + "#festivals", ""), (tt["awS"], aw + "#shows", ""), (tt["nav"]["media"], self.href(depth, p["media"]), "media")]),
            ("learn", ["instruments", "glossary"], [(tt["nav"]["instruments"], self.href(depth, p["instruments"]), "instruments"), (tt["nav"]["glossary"], self.href(depth, p["glossary"]), "glossary")]),
        ]
        out = f'<a class="nav-a" href="{self.href(depth, p["home"])}"{" aria-current=page" if cur == "home" else ""}>{e(tt["nav"]["home"])}</a>'
        for gi, (g, keys, items) in enumerate(groups):
            here = " cur" if cur in keys else ""
            if g == "genres":
                fams = "".join(f'<a href="{self.fam_url(depth, f["id"])}"><i style="background:{f["color"]}"></i>{e(t(f["name"], self.lang))}</a>' for f in C.FAMILIES)
                drop = f'<div class="nav-drop mega"><div class="drop-tops"><a class="drop-all" href="{self.href(depth, p["genres"])}">{e(tt["allGenres"])} →</a><a class="drop-all" href="{self.href(depth, p["map"])}">{e(tt["mapNav"])} →</a></div><div class="drop-grid">{fams}</div></div>'
            else:
                drop = '<div class="nav-drop">' + "".join(f'<a href="{u}"{" class=here" if k and k == cur else ""}>{e(lbl)}</a>' for lbl, u, k in items) + "</div>"
            side = " right" if gi >= 3 else ""
            out += f'<div class="nav-g{here}{side}"><button class="nav-a nav-btn" type="button" aria-expanded="false">{e(tt["menu_g"][g])}{chev}</button>{drop}</div>'
        out += f'<a class="nav-a" href="{self.href(depth, p["about"])}"{" aria-current=page" if cur == "about" else ""}>{e(tt["nav"]["about"])}</a>'
        return out

    def fam_url(self, depth, fid):
        return self.href(depth, f"{self.p['gdir']}/{fid}.html")

    def write(self, rel, other, depth, title, desc, body, cur="", kind="WebPage", extra_head="", entity=None):
        lang, tt, p = self.lang, self.t, self.p
        prefix = "" if lang == "en" else "pt/"
        canonical = f"{SITE}/{prefix}{rel}".replace("index.html", "")
        other_url = f"{SITE}/{'pt/' if lang == 'en' else ''}{other}".replace("index.html", "")
        pt_url, en_url = (canonical, other_url) if lang == "pt" else (other_url, canonical)
        assets = "../" * (depth + (1 if lang == "pt" else 0))
        other_href = ("../" * depth + "pt/" + other) if lang == "en" else ("../" * (depth + 1) + other)
        other_href = other_href.replace("index.html", "") or "./"
        nav = self.menu(depth, cur)
        og = f"{SITE}/assets/share-{lang}.png"
        home_url = SITE + "/" + prefix
        graph = [{"@type": kind, "@id": canonical + "#page", "name": title, "headline": title, "description": desc, "url": canonical, "image": og, "inLanguage": tt["html"],
                  "dateModified": BUILT, "isPartOf": {"@id": home_url + "#website"}, "author": {"@type": "Organization", "name": "BiblioVerse", "url": "https://biblioverse.org"},
                  "publisher": {"@type": "Organization", "name": "BiblioVerse", "url": "https://biblioverse.org"}},
                 {"@type": "WebSite", "@id": home_url + "#website", "name": tt["site"], "url": home_url, "inLanguage": tt["html"], "description": tt["homeDesc"].format(**seo_stats(lang))}]
        if entity:
            graph[0]["mainEntity"] = entity
        ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
        full_title = title if title.startswith(tt["site"]) else f"{title} · {tt['site']}"
        doc = f"""<!doctype html>
<html lang="{tt['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="BiblioVerse">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="pt-BR" href="{pt_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(tt['site'])}">
<meta property="og:locale" content="{tt['locale']}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(tt['ogAlt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#009739">
<link rel="icon" href="{assets}assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{assets}assets/icon-180.png">
<link rel="manifest" href="{assets}site.webmanifest">
<script type="application/ld+json">{ld}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Momo+Trust+Display&family=Instrument+Sans:wght@400;500;600;700&family=Google+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{assets}assets/style.css">
<script src="https://biblioverse.org/superbar.js" defer></script>{extra_head}
</head>
<body class="lang-{lang}">
<nav id="bvbar" class="bvbar" data-current="brazilianmusic" data-offset="none" aria-label="BiblioVerse" style="position:relative;height:36px;z-index:9000;background:linear-gradient(90deg,#4f7cff,#7a5cff)"><a href="https://biblioverse.org" style="color:#fff;line-height:36px;padding:0 14px;font-weight:700;text-decoration:none">BiblioVerse</a></nav>
<a class="skip" href="#main">{e(tt['skip'])}</a>
<header class="top"><div class="wrap">
<a class="logo" href="{self.href(depth, p['home'])}">{LOGO}<span><b>{e(tt['site'])}</b></span></a>
<nav class="nav" id="siteNav" aria-label="{e(tt['menu'])}">{nav}</nav>
<a class="lang" href="{other_href}" hreflang="{'en' if lang == 'pt' else 'pt-BR'}" lang="{'en' if lang == 'pt' else 'pt-BR'}">{tt['switch']}</a>
<button class="menu-btn" id="menuBtn" type="button" aria-expanded="false" aria-controls="siteNav" aria-label="{e(tt['menu'])}"><span></span><span></span><span></span></button>
</div></header>
<main id="main">
{body}
</main>
<footer><img class="tstrip foot-tiles" src="{assets}assets/footer-tiles.svg" alt="" aria-hidden="true" width="2112" height="44"><div class="wrap">
<div class="foot-brand">{LOGO}<div><b>{e(tt['site'])}</b><p>{e(tt['footer'])}</p></div></div>
<div class="foot-links"><a href="{self.href(depth, p['about'])}">{e(tt['nav']['about'])}</a><a href="{self.href(depth, p['privacy'])}">{e(tt['privacyH'])}</a><a href="https://biblioverse.org">BiblioVerse</a><a href="{other_href}" hreflang="{'en' if lang == 'pt' else 'pt-BR'}">{tt['switch']}</a></div>
<div class="foot-meta mono">© {BUILT[:4]} BiblioVerse · {e(tt["updated"])} {BUILT[5:7]}/{BUILT[:4]}</div>
</div></footer>
<script src="{assets}assets/app.js" defer></script>
</body>
</html>
"""
        path = os.path.join(ROOT, prefix, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf8", newline="\n") as f:
            f.write(doc)
        URLS.append((canonical, pt_url, en_url))


def other(lang, key):
    return PATHS["en" if lang == "pt" else "pt"][key]


def head_block(kicker, h1, lead, extra="", seed=5):
    return f'<div class="page-head"><span class="kicker mono">{kicker}</span><h1>{h1}</h1><p class="lead">{e(lead)}</p>{extra}{strip(seed, "#007d36", FLAG_INKS, cols=40, cls="tstrip head-strip", anim=True)}</div>'


def chips(pg, depth, ids, cls="chips"):
    return f'<div class="{cls}">' + "".join(f'<a class="chip" style="--c:{FAM[SUB[i]["family"]]["color"]}" href="{IT.sub_url(pg, depth, i)}">{e(t(SUB[i]["name"], pg.lang))}</a>' for i in ids) + "</div>"


def artist_card(pg, depth, a, compact=False):
    lang, tt = pg.lang, pg.t
    f = FAM[a["family"]]
    meta = " · ".join(x for x in [tt["types"].get(a["type"], a["type"]), str(a["year"]) if a["year"] else "", a["uf"]] if x)
    tier = f'<span class="tier t-{a["tier"]}" title="{e(tt["tiers"][a["tier"]])}">{a["tier"]}</span>' if a["tier"] else ""
    blurb = t(a["blurb"], lang)
    search = e((a["name"] + " " + " ".join(t(SUB[g]["name"], lang) for g in a["genres"]) + " " + blurb).lower())
    decade = f"{a['year'] // 10 * 10}s" if a["year"] else ""
    body = f'<div class="ac-top"><span class="code mono" style="color:var(--cx)">{e(t(f["name"], lang))}</span>{tier}</div><h3><a href="{IT.art_url(pg, depth, a)}">{e(a["name"])}</a></h3><div class="meta mono">{e(meta)}</div>'
    if not compact:
        body += f'<p>{e(blurb)}</p>' if blurb else ""
        body += chips(pg, depth, a["genres"])
        body += f'<a class="yt" href="{yt(a["name"] + " música")}" target="_blank" rel="noopener">▶ {e(tt["listen"])}</a>'
    return (f'<article class="acard{" compact" if compact else ""}" id="{a["id"]}" style="--c:{f["color"]}" data-f="{f["code"]}" data-type="{a["type"]}" data-tier="{a["tier"]}" '
            f'data-dec="{decade}" data-tags="{" ".join(a["tags"])}" data-name="{e(a["name"].lower())}" data-year="{a["year"]}" data-tierord="{TIER_ORDER[a["tier"]]}" data-search="{search}">{body}</article>')


# ── mapa dos gêneros (SVG) ────────────────────────────────────────────────────
def genre_map(pg, depth, local=False):
    lang = pg.lang
    fams = sorted(C.FAMILIES, key=lambda f: f["since"])
    y0, y1 = 1860, 2030
    W, LAB, ROW, TOP = 1100, 320, 30, 34
    H = TOP + ROW * len(fams) + 10

    def x(year):
        year = max(y0, min(y1, year))
        return LAB + (year - y0) / (y1 - y0) * (W - LAB - 20)
    s = [f'<svg class="gmap" viewBox="0 0 {W} {H}" role="img" aria-label="{e(pg.t["mapH"])}">']
    for yr in range(1880, 2030, 20):
        s.append(f'<line class="grid" x1="{x(yr):.0f}" y1="{TOP - 8}" x2="{x(yr):.0f}" y2="{H}"/><text class="axis mono" x="{x(yr):.0f}" y="{TOP - 14}" text-anchor="middle">{yr}</text>')
    for i, f in enumerate(fams):
        cy = TOP + i * ROW + ROW / 2
        url = f'#m-{f["id"]}' if local else pg.fam_url(depth, f["id"])
        s.append(f'<a href="{url}" class="grow"><rect x="0" y="{cy - ROW / 2:.0f}" width="{W}" height="{ROW}" fill="transparent"/>')
        s.append(f'<text class="glab" x="{LAB - 14}" y="{cy + 4.5:.1f}" text-anchor="end">{e(t(f["name"], lang))}</text>')
        s.append(f'<text class="gcode mono" x="8" y="{cy + 4:.1f}">{f["code"]} · {f["since"]}</text>')
        s.append(f'<line x1="{x(f["since"]):.1f}" y1="{cy:.1f}" x2="{x(2026):.1f}" y2="{cy:.1f}" class="bar" stroke="{f["color"]}" stroke-width="6" stroke-linecap="round" opacity=".9"/>')
        s.append(f'<circle class="dot" cx="{x(f["since"]):.1f}" cy="{cy:.1f}" r="8" fill="{f["color"]}" stroke="var(--paper)" stroke-width="2"/>')
        for sub in f["subs"]:
            if sub["since"] > f["since"]:
                s.append(f'<circle class="dot" cx="{x(sub["since"]):.1f}" cy="{cy:.1f}" r="4" fill="var(--paper)" stroke="{f["color"]}" stroke-width="2"><title>{e(t(sub["name"], lang))} · {sub["since"]}</title></circle>')
        s.append("</a>")
    s.append("</svg>")
    return "".join(s)


def heritage_txt(s, lang):
    h = s.get("heritage")
    return t(C.HERITAGE[h[0]], lang).format(y=h[1]) if h else ""


def fusion_txt(s, lang):
    """Rótulo dos gêneros de fusão: os estilos que se misturam (fusion=(pt, en))."""
    return t(C.FUSION, lang).format(x=t(s["fusion"], lang)) if s.get("fusion") else ""


def family_map(pg, f):
    """Gráfico expandido de uma família: uma linha por subgênero, do mais antigo ao mais novo."""
    lang = pg.lang
    subs = sorted(f["subs"], key=lambda s: (s["since"], t(s["name"], lang)))
    first = subs[0]["since"]
    y0, y1 = (1860 if first >= 1860 else max(1740, first // 20 * 20)), 2030
    W, LAB, ROW, TOP = 1100, 360, 30, 34
    H = TOP + ROW * len(subs) + 10

    def x(year):
        year = max(y0, min(y1, year))
        return LAB + (year - y0) / (y1 - y0) * (W - LAB - 20)
    out = [f'<svg class="gmap fmap" viewBox="0 0 {W} {H}" role="img" aria-label="{e(t(f["name"], lang))}">']
    for yr in range(y0 + 20, 2030, 20):
        out.append(f'<line class="grid" x1="{x(yr):.0f}" y1="{TOP - 8}" x2="{x(yr):.0f}" y2="{H}"/><text class="axis mono" x="{x(yr):.0f}" y="{TOP - 14}" text-anchor="middle">{yr}</text>')
    for i, s in enumerate(subs):
        cy = TOP + i * ROW + ROW / 2
        her = heritage_txt(s, lang)
        fus = fusion_txt(s, lang)
        out.append(f'<a href="{IT.sub_url(pg, 0, s["id"])}" class="grow"><rect x="0" y="{cy - ROW / 2:.0f}" width="{W}" height="{ROW}" fill="transparent"/>')
        out.append(f'<text class="glab" x="{LAB - 14}" y="{cy + 4.5:.1f}" text-anchor="end">{e(t(s["name"], lang))}</text>')
        out.append(f'<text class="gcode mono" x="8" y="{cy + 4:.1f}">{s["since"]}{" ★" if her else ""}</text>')
        out.append(f'<line x1="{x(s["since"]):.1f}" y1="{cy:.1f}" x2="{x(2026):.1f}" y2="{cy:.1f}" class="bar" stroke="{f["color"]}" stroke-width="6" stroke-linecap="round" opacity=".9"/>')
        out.append(f'<circle class="dot" cx="{x(s["since"]):.1f}" cy="{cy:.1f}" r="7" fill="{f["color"]}" stroke="var(--paper)" stroke-width="2"><title>{e(t(s["name"], lang))} · {s["since"]}{" · " + e(her) if her else ""}{" · " + e(fus) if fus else ""}</title></circle>')
        out.append("</a>")
    out.append("</svg>")
    return "".join(out)


def page_map(pg):
    lang, tt = pg.lang, pg.t
    secs = ""
    for f in C.FAMILIES:
        secs += (f'<section class="sec-in fam-map" id="m-{f["id"]}" style="--c:{f["color"]}"><h2>{e(t(f["name"], lang))}</h2>'
                 f'<p class="mono small">{e(f["code"])} · {e(tt["since"])} {f["since"]} · {e(tt["mapFamP"].format(n=len(f["subs"])))}</p>'
                 f'<div class="gmap-wrap">{family_map(pg, f)}</div>'
                 f'<p class="more-link"><a class="btn" href="{pg.fam_url(0, f["id"])}">{e(tt["mapOpen"])}: {e(t(f["name"], lang))} →</a></p></section>')
    body = (f'<div class="wrap">{head_block(f"{STATS["f"]} {e(tt["stats"]["families"])} · {STATS["s"]} {e(tt["stats"]["subs"])}", e(tt["mapTitle"]), tt["mapLead"], seed=17)}'
            f'<section class="sec-in"><h2>{e(tt["mapAllH"])}</h2><p class="lead">{e(tt["mapAllP"])}</p><div class="gmap-wrap">{genre_map(pg, 0, local=True)}</div></section>'
            f'{secs}</div>')
    pg.write(pg.p["map"], other(lang, "map"), 0, tt["mapTitle"], tt["mapDesc"].format(**seo_stats(lang)), body, "map", kind="CollectionPage")


# ── páginas ───────────────────────────────────────────────────────────────────
def stats_grid(tt):
    """O catálogo em números: contagem exata, com animação de contagem (fica na página Sobre)."""
    return "".join(f'<div class="stat"><b data-count="{v}">{v}</b><span>{e(tt["stats"][k])}</span></div>' for k, v in
                   [("families", STATS["f"]), ("subs", STATS["s"]), ("artists", STATS["a"]), ("musicians", STATS["m"]), ("songs", STATS["n"]), ("albums", STATS["d"])])


def hero_stats(lang, tt):
    """Números de abertura no hero: arredondados com '+', como no SEO."""
    st = seo_stats(lang)
    return "".join(f'<li><b>{e(st[k])}</b><span>{e(tt["heroStats"][k])}</span></li>' for k in ("gs", "am", "n", "d"))


def page_home(pg):
    lang, tt = pg.lang, pg.t
    like = "".join(
        f'<button type="button" class="like-btn" style="--c:{FAM[fams[0]]["color"]}" data-fams="{" ".join(fams)}">{strip(sum(map(ord, lbl[0])) % 1000, FAM[fams[0]]["color"], ["#ffffff", "#fedd00"], cols=8, cls="tstrip card-strip")}'
        f'<span class="mono code">→ {e(" · ".join(t(FAM[x]["name"], lang) for x in fams))}</span><b class="like-t">{e(t(lbl, lang))}</b><small>{e(t(who, lang))}</small></button>'
        for lbl, fams, who in C.IF_YOU_LIKE)
    fam_cards = "".join(
        f'<a class="fcard" style="--c:{f["color"]}" href="{pg.fam_url(0, f["id"])}" data-fam="{f["id"]}">{strip(sum(map(ord, f["id"])) % 1000, f["color"], ["#ffffff", "#fedd00"], cols=8, cls="tstrip card-strip")}<span class="mono code">{f["code"]} · {f["since"]}</span><h3>{e(t(f["name"], lang))}</h3><p>{e(t(f["where"], lang))}</p><span class="mono small">{len(f["subs"])} {e(tt["stats"]["subs"])} · {sum(1 for a in ARTISTS if a["family"] == f["id"])} {e(tt["stats"]["artists"])}</span></a>'
        for f in C.FAMILIES)
    doors = "".join(f'<a class="door" href="{pg.p[k]}"><span class="mono">{e(m)}</span><h3>{e(h)}</h3><p>{e(d)}</p></a>' for k, m, h, d in tt["doors"])
    ticker = " · ".join(e(a["name"]) for a in ARTISTS if a["tier"] == "S")
    body = f"""<section class="hero"><div class="wrap hero-grid"><div class="hero-txt">
<h1>{tt['heroH']}</h1>
<p class="lead">{e(tt['heroP'])}</p>
<div class="cta"><a class="btn pri" href="{pg.p['genres']}">{e(tt['ctaGenres'])}</a><a class="btn" href="#like">{e(tt['ctaLike'])}</a></div>
<ul class="hero-stats" aria-label="{e(tt['statsH'])}">{hero_stats(lang, tt)}</ul>
</div><div class="hero-panel">{mosaic(7, 9, "#007d36", FLAG_INKS, 7, cls="mosaic hero-mosaic")}</div></div><svg class="badge" viewBox="0 0 130 130" aria-hidden="true"><defs><path id="bc" d="M65 65m-50 0a50 50 0 1 1 100 0a50 50 0 1 1-100 0"/></defs><text textLength="310" lengthAdjust="spacingAndGlyphs"><textPath href="#bc" textLength="310" lengthAdjust="spacingAndGlyphs">{e(tt['heroBadge'])} ·</textPath></text></svg><div class="ticker" aria-hidden="true"><div class="ticker-in">{ticker} · {ticker}</div></div></section>
<section class="sec s-like" id="like"><div class="wrap"><h2>{e(tt['likeH'])}</h2><p class="lead">{e(tt['likeP'])}</p>
<div class="like-grid" id="likeGrid">{like}</div></div></section>
{strip(12, "#012169", ["#fedd00", "#ffffff"])}
<section class="sec s-map"><div class="wrap"><h2>{e(tt['famH'])}</h2><p class="lead">{e(tt['famP'].format(**STATS))}</p>
<div class="fgrid" id="famGrid">{fam_cards}</div>
<p class="more-link"><a class="btn pri" href="{pg.p['genres']}">{e(tt['allGenres'])} →</a><a class="btn" href="{pg.p['map']}">{e(tt['mapBtn'])} →</a></p></div></section>
<section class="sec s-doors"><div class="wrap"><h2>{e(tt['doorsH'])}</h2><div class="doors">{doors}</div></div></section>"""
    pg.write("index.html", "index.html", 0, tt["site"] + " · " + tt["homeTitle"], tt["homeDesc"].format(**seo_stats(lang)), body, "home")


def page_genres(pg):
    lang, tt = pg.lang, pg.t
    cards = ""
    for f in C.FAMILIES:
        n = sum(1 for a in ARTISTS if a["family"] == f["id"])
        subs = ", ".join(t(s["name"], lang) for s in f["subs"][:6]) + ("…" if len(f["subs"]) > 6 else "")
        cards += (f'<a class="gcard" style="--c:{f["color"]}" href="{pg.p["gdir"]}/{f["id"]}.html">{strip(sum(map(ord, f["id"])) % 1000, f["color"], ["#ffffff", "#fedd00"], cols=10, cls="tstrip card-strip")}<div class="gc-top"><span class="mono code">{f["code"]}</span><span class="mono">{e(tt["since"])} {f["since"]}</span></div>'
                  f'<h2>{e(t(f["name"], lang))}</h2><p class="where mono">{e(t(f["where"], lang))}</p><p>{e(t(f["blurb"], lang))}</p><p class="subs"><b>{len(f["subs"])} {e(tt["stats"]["subs"])}:</b> {e(subs)}</p>'
                  f'<span class="mono small">{n} {e(tt["stats"]["artists"])}</span></a>')
    fus = sorted(((s, f) for f in C.FAMILIES for s in f["subs"] if s.get("fusion")), key=lambda x: (x[0]["since"], t(x[0]["name"], lang)))
    fus_html = "".join(
        f'<li style="--c:{f["color"]}"><a href="{IT.sub_url(pg, 0, s["id"])}"><b>{e(t(s["name"], lang))}</b><span class="fus-mix">{e(t(s["fusion"], lang))}</span>'
        f'<span class="mono small">{e(t(f["name"], lang))} · {s["since"]}</span></a></li>' for s, f in fus)
    fus_sec = f'<section class="sec-in" id="fusion"><h2>{e(tt["fusionH"])} <span class="mono small">{len(fus)}</span></h2><p class="lead">{e(tt["fusionP"])}</p><ul class="fus-list">{fus_html}</ul></section>'
    body = f'<div class="wrap">{head_block(f"{STATS["f"]} {e(tt["stats"]["families"])} · {STATS["s"]} {e(tt["stats"]["subs"])}", e(tt["genresH"]), tt["genresLead"], extra=f'<p class="head-cta"><a class="btn" href="{pg.p["map"]}">{e(tt["mapBtn"])} →</a></p>')}<div class="ggrid">{cards}</div>{fus_sec}</div>'
    pg.write(pg.p["genres"], other(lang, "genres"), 0, tt["genresH"], tt["genresDesc"].format(**seo_stats(lang)), body, "genres", kind="CollectionPage")


def page_family(pg, f, i):
    lang, tt = pg.lang, pg.t
    fid = f["id"]
    subs_html = ""
    for s in f["subs"]:
        arts = BY_SUB.get(s["id"], [])
        names = "".join(f'<a class="chip plain" href="{IT.art_url(pg, 1, a)}">{e(a["name"])}</a>' for a in arts)
        more = ""
        subs_html += f'<article class="sub" id="{s["id"]}"><div class="sub-h"><h3><a href="{IT.sub_url(pg, 1, s["id"])}">{e(t(s["name"], lang))}</a></h3><span class="mono">{e(tt["since"])} {s["since"]} · {len(arts)} {e(tt["stats"]["artists"])}</span></div>{f'<span class="her">{e(heritage_txt(s, lang))}</span>' if s.get("heritage") else ""}{f'<span class="her fus">{e(fusion_txt(s, lang))}</span>' if s.get("fusion") else ""}<p>{e(t(s["blurb"], lang))}</p><div class="chips">{names}{more}</div></article>'
    songs = "".join(f'<li><span class="y mono">{y}</span><a href="{yt(a + " " + s)}" target="_blank" rel="noopener">{e(s)}</a><small>{IT.link_credit(pg, 1, a)}</small></li>' for s, a, y in f["songs"])
    fam_artists = [a for a in ARTISTS if a["family"] == fid]
    top = [a for a in fam_artists if a["tier"] in ("S", "A")][:24] or fam_artists[:12]
    # todos os artistas da família: os de nível S e A em ficha completa, os demais em ficha compacta
    cards = "".join(artist_card(pg, 1, a) for a in top) + "".join(artist_card(pg, 1, a, compact=True) for a in fam_artists if a not in top)
    sert = ""
    if fid == "sertanejo":
        dec = {}
        for y, n, h in SERTANEJO:
            dec.setdefault(int(y) // 10 * 10, []).append((n, h == "1"))
        sert = '<section class="sec-in"><h2>' + ("Artistas por década de estreia" if lang == "pt" else "Artists by debut decade") + '</h2><p class="lead">' + (
            "Toda a linhagem do sertanejo, de 1920 aos anos 2020; em destaque, os nomes mais populares de cada década." if lang == "pt" else
            "The whole sertanejo lineage, from 1920 to the 2020s; the most popular names of each decade are highlighted.") + '</p><div class="decades">'
        for d in sorted(dec):
            sert += f'<div class="dec"><h3 class="mono">{d}s</h3><div class="chips">' + "".join(f'<a class="chip plain{" hot" if h else ""}" href="{yt(n)}" target="_blank" rel="noopener">{e(n)}</a>' for n, h in dec[d]) + "</div></div>"
        sert += "</div></section>"
    falb = [r for r in ALBUMS if r[3] == fid]
    fam_albums = f'<section class="sec-in"><h2>{e(tt["famAlbums"])} <span class="mono small">{len(falb)}</span></h2>{IT.album_items(pg, 1, falb)}<p class="more-link"><a class="btn" href="../{pg.p["albums"]}?g={fid}">{e(tt["nav"]["albums"])} →</a></p></section>' if falb else ""
    prev, nxt = C.FAMILIES[i - 1] if i else None, C.FAMILIES[i + 1] if i + 1 < len(C.FAMILIES) else None
    pager = '<div class="pager">' + (f'<a class="btn" href="{prev["id"]}.html">← {e(t(prev["name"], lang))}</a>' if prev else "<span></span>") + (f'<a class="btn" href="{nxt["id"]}.html">{e(t(nxt["name"], lang))} →</a>' if nxt else "<span></span>") + "</div>"
    body = f"""<div class="fam-head" style="--c:{f['color']}"><div class="wrap fam-grid"><div class="fam-txt">
<a class="mono back" href="../{pg.p['genres']}">← {e(tt['nav']['genres'])}</a>
<div class="fam-code mono">{f['code']}</div>
<h1>{e(t(f['name'], lang))}</h1>
<div class="facts"><span>{e(tt['since'])} <b>{f['since']}</b></span><span>{e(tt['where'])} <b>{e(t(f['where'], lang))}</b></span><span>{e(tt['subsH'])} <b>{len(f['subs'])}</b></span><span>{e(tt['artistsH'])} <b>{len(fam_artists)}</b></span></div>
<p class="lead">{e(t(f['blurb'], lang))}</p>
<div class="like-tag"><span class="mono">{e(tt['likeTag'])}</span><p>{e(t(f['like'], lang))}</p></div>
</div><div class="fam-panel">{mosaic(6, 8, f['color'], ["#ffffff", "#fedd00"], sum(map(ord, fid)), cls="mosaic fam-mosaic")}</div></div></div>
<div class="wrap">
{f'<section class="sec-in"><h2>{e(tt["startH"])}</h2><ul class="songs">{songs}</ul></section>' if songs else ""}
<section class="sec-in"><h2>{e(tt['subsH'])}</h2><div class="subs">{subs_html}</div></section>
{fam_albums}
{sert}
<section class="sec-in"><h2>{e(tt['artistsH'])}</h2><div class="agrid">{cards}</div>
<p class="more-link dir-tip"><a href="../{pg.p['artists']}?f={f['code']}">{e(tt['allArtists'])} →</a></p></section>
{pager}</div>"""
    pg.write(f"{pg.p['gdir']}/{fid}.html", f"{other(lang, 'gdir')}/{fid}.html", 1, t(f["name"], lang), t(f["blurb"], lang)[:300], body, "genres", kind="Article")


def page_artists(pg):
    lang, tt = pg.lang, pg.t
    cards = "".join(artist_card(pg, 0, a) for a in ARTISTS)
    fam_opts = "".join(f'<option value="{f["code"]}">{e(t(f["name"], lang))} ({sum(1 for a in ARTISTS if a["family"] == f["id"])})</option>' for f in C.FAMILIES)
    type_opts = "".join(f'<option value="{k}">{e(v)}</option>' for k, v in tt["types"].items())
    tier_opts = "".join(f'<option value="{k}">{e(v)}</option>' for k, v in tt["tiers"].items())
    decs = sorted({f"{a['year'] // 10 * 10}s" for a in ARTISTS if a["year"]})
    dec_opts = "".join(f'<option value="{d}">{d}</option>' for d in decs)
    tag_opts = "".join(f'<option value="{k}">{e(v)}</option>' for k, v in tt["tags"].items())
    body = f"""<div class="wrap">{head_block(f'{STATS["a"]} {e(tt["stats"]["artists"])}', e(tt["artistsH2"]), tt["artistsLead"], seed=31)}
<div class="filters" id="filters">
<input id="q" type="search" placeholder="{e(tt['search'])}" aria-label="{e(tt['search'])}">
<select id="fFam" aria-label="{e(tt['fGenre'])}"><option value="">{e(tt['fGenre'])}: {e(tt['all'])}</option>{fam_opts}</select>
<select id="fType" aria-label="{e(tt['fType'])}"><option value="">{e(tt['fType'])}: {e(tt['all'])}</option>{type_opts}</select>
<select id="fTier" aria-label="{e(tt['fTier'])}"><option value="">{e(tt['fTier'])}: {e(tt['all'])}</option>{tier_opts}</select>
<select id="fDec" aria-label="{e(tt['fDecade'])}"><option value="">{e(tt['fDecade'])}: {e(tt['all'])}</option>{dec_opts}</select>
<select id="fTag" aria-label="{e(tt['fTag'])}"><option value="">{e(tt['fTag'])}: {e(tt['all'])}</option>{tag_opts}</select>
<select id="fSort" aria-label="{e(tt['sort'])}"><option value="code">{e(tt['sort'])}: {e(tt['sortDefault'])}</option><option value="name">{e(tt['sortName'])}</option><option value="year">{e(tt['sortYear'])}</option><option value="tier">{e(tt['sortTier'])}</option></select>
<button class="btn" id="fReset" type="button">{e(tt['reset'])}</button>
<span class="mono count"><b id="count">{STATS['a']}</b> {e(tt['results'])}</span>
</div>
<div class="agrid" id="agrid">{cards}</div><p class="none mono" id="noneMsg" hidden>{e(tt['none'])}</p></div>"""
    pg.write(pg.p["artists"], other(lang, "artists"), 0, tt["artistsH2"], tt["artistsDesc"].format(**seo_stats(lang)), body, "artists", kind="CollectionPage")


def mus_section(pg, hid, title, rows, featured):
    lang = pg.lang
    cards = "".join(f'<article class="mcard"><h3><a href="{IT.mus_url(pg, 0, IT.MUS[IT.slugify(n)])}">{e(n)}</a></h3><p>{e(t((pt, en), lang))}</p></article>' for i, (n, pt, en) in enumerate(rows[:featured]))
    rest = "".join(f'<li><a href="{IT.mus_url(pg, 0, IT.MUS[IT.slugify(n)])}">{e(n)}</a></li>' for i, (n, pt, en) in enumerate(sorted(rows[featured:], key=lambda r: IT.norm(r[0]))))
    return f'<section class="sec-in" id="{hid}"><h2>{e(title)} <span class="mono small">{len(rows)}</span></h2><div class="mgrid">{cards}</div><ol class="mlist">{rest}</ol></section>'


def page_musicians(pg):
    lang, tt = pg.lang, pg.t
    n = len({IT.slugify(r[0]) for _, _, rows, _ in INSTR for r in rows})
    body = f'<div class="wrap">{head_block(f"{n} {e(tt["nav"]["musicians"]).lower()}", e(tt["musiciansH"]), tt["musiciansLead"], seed=41)}'
    body += "".join(mus_section(pg, code, tt[key], rows, feat) for code, key, rows, feat in INSTR) + "</div>"
    pg.write(pg.p["musicians"], other(lang, "musicians"), 0, tt["musiciansH"], tt["musiciansDesc"].format(n=approx(n, lang)), body, "musicians", kind="CollectionPage")


def page_singers(pg):
    lang, tt = pg.lang, pg.t
    body = f'<div class="wrap">{head_block(f"{len(VOC)} {e(tt["nav"]["singers"]).lower()}", e(tt["singersH"]), tt["singersLead"], seed=43)}'
    body += mus_section(pg, "voc", tt["nav"]["singers"], VOC, 15) + "</div>"
    pg.write(pg.p["singers"], other(lang, "singers"), 0, tt["singersH"], tt["singersDesc"].format(n=approx(len(VOC), lang)), body, "singers", kind="CollectionPage")


def page_producers(pg):
    lang, tt = pg.lang, pg.t
    body = f'<div class="wrap">{head_block(f"{len(PROD)} {e(tt["nav"]["producers"]).lower()}", e(tt["producersH"]), tt["producersLead"], seed=47)}'
    body += mus_section(pg, "prd", tt["prod"], PROD, 15) + "</div>"
    pg.write(pg.p["producers"], other(lang, "producers"), 0, tt["producersH"], tt["producersDesc"].format(n=approx(len(PROD), lang)), body, "producers", kind="CollectionPage")


def page_influencers(pg):
    lang, tt = pg.lang, pg.t
    body = f'<div class="wrap">{head_block(f"{len(C.CREATORS)} {e(tt["nav"]["influencers"]).lower()}", e(tt["influencersH"]), tt["influencersLead"], seed=49)}'
    for grp, lbl in (("vj", tt["mVj"]), ("crit", tt["mCrit"]), ("edu", tt["mEdu"])):
        items = [(n, h) for n, h, g in C.CREATORS if g == grp]
        body += f'<section class="sec-in"><h2>{e(lbl)} <span class="mono small">{len(items)}</span></h2><div class="chips big">' + "".join(
            f'<a class="chip plain" href="{IT.mus_url(pg, 0, IT.MUS[IT.slugify(n)])}">{e(n)}{f" <small>@{e(h)}</small>" if h else ""}</a>' for n, h in items) + "</div></section>"
    body += f'<section class="sec-in"><h2>{e(tt["mChan"])} <span class="mono small">{len(C.CHANNELS)}</span></h2><div class="mgrid">' + "".join(
        f'<article class="mcard"><h3><a href="{u}" target="_blank" rel="noopener">{e(n)} ↗</a></h3><p>{e(t(d, lang))}</p></article>' for n, u, d in C.CHANNELS) + "</div></section>"
    body += "</div>"
    pg.write(pg.p["influencers"], other(lang, "influencers"), 0, tt["influencersH"], tt["influencersDesc"].format(n=approx(len(C.CREATORS), lang)), body, "influencers", kind="CollectionPage")


def page_songs(pg):
    lang, tt = pg.lang, pg.t
    decs = sorted({y // 10 * 10 for y, *_ in SONGS})
    tabs = f'<button type="button" aria-pressed="true" data-dec="">{e(tt["all"])}</button>' + "".join(f'<button type="button" aria-pressed="false" data-dec="{d}">{d}s</button>' for d in decs)
    items = ""
    cur = None
    for y, s, a, g in SONGS:
        if y != cur:
            cur = y
            items += f'<li class="yhead mono" data-year="{y}" data-dec="{y // 10 * 10}">{y}</li>'
        items += f'<li class="song" data-g="{g}" data-dec="{y // 10 * 10}" data-search="{e((s + " " + a + " " + t(FAM[g]["name"], lang)).lower())}"><span class="g mono" style="--c:{FAM[g]["color"]}" title="{e(t(FAM[g]["name"], lang))}">{FAM[g]["code"]}</span><a href="{yt(a + " " + s)}" target="_blank" rel="noopener">{e(s)}</a><small>{IT.link_credit(pg, 0, a)}</small></li>'
    counts = {}
    for *_, g in SONGS:
        counts[g] = counts.get(g, 0) + 1
    gopts = "".join(f'<option value="{fid}">{e(t(FAM[fid]["name"], lang))} ({counts[fid]})</option>' for fid in sorted(counts, key=lambda k: -counts[k]))
    body = f"""<div class="wrap">{head_block(f'{STATS["n"]} {e(tt["stats"]["songs"])} · {SONGS[0][0]}–{SONGS[-1][0]}', e(tt["songsH"]), tt["songsLead"], seed=21)}
<div class="filters sticky" id="sfilters"><input id="sq" type="search" placeholder="{e(tt['songSearch'])}" aria-label="{e(tt['songSearch'])}">
<select id="gsel" aria-label="{e(tt['fGenre'])}"><option value="">{e(tt['fGenre'])}: {e(tt['all'])}</option>{gopts}</select>
<span class="mono count"><b id="scount">{STATS['n']}</b> {e(tt['results'])}</span></div>
<div class="tabs" id="decTabs">{tabs}</div>
<ol class="songlist" id="songlist">{items}</ol></div>"""
    pg.write(pg.p["songs"], other(lang, "songs"), 0, tt["songsH"], tt["songsDesc"].format(**seo_stats(lang)), body, "songs", kind="CollectionPage")


def _unused_album_list(pg, rows, prefix):
    lang = pg.lang
    return "".join(f'<li class="album"><span class="y mono">{y}</span><div><h3><a href="{yt(ar + " " + al + " album")}" target="_blank" rel="noopener">{e(al)}</a></h3><div class="meta">{IT.link_credit(pg, 0, ar)}</div><p>{e(t((pt, en), lang))}</p></div></li>' for i, (y, al, ar, pt, en) in enumerate(rows))


def page_albums(pg):
    lang, tt = pg.lang, pg.t
    decs = sorted({r[0] // 10 * 10 for r in ALBUMS})
    tabs = f'<button type="button" aria-pressed="true" data-dec="">{e(tt["all"])}</button>' + "".join(f'<button type="button" aria-pressed="false" data-dec="{d}">{d}s</button>' for d in decs)
    counts = {}
    for r in ALBUMS:
        counts[r[3]] = counts.get(r[3], 0) + 1
    gopts = "".join(f'<option value="{fid}">{e(t(FAM[fid]["name"], lang))} ({counts[fid]})</option>' for fid in sorted(counts, key=lambda k: -counts[k]))
    items, cur = "", None
    for y, al, ar, g, pt, en in ALBUMS:
        d = y // 10 * 10
        if d != cur:
            cur = d
            items += f'<li class="dhead mono" data-dec="{d}">{d}s</li>'
        items += (f'<li class="album" data-g="{g}" data-dec="{d}" data-search="{e((al + " " + ar + " " + t(FAM[g]["name"], lang)).lower())}"><span class="y mono">{y}</span><div>'
                  f'<span class="g mono" style="--c:{FAM[g]["color"]}">{e(t(FAM[g]["name"], lang))}</span><h3><a href="{yt(ar + " " + al + " album")}" target="_blank" rel="noopener">{e(al)}</a></h3>'
                  f'<div class="meta">{IT.link_credit(pg, 0, ar)}</div><p>{e(t((pt, en), lang))}</p></div></li>')
    body = f"""<div class="wrap">{head_block(f'{STATS["d"]} {e(tt["stats"]["albums"])} · {ALBUMS[0][0]}–{ALBUMS[-1][0]}', e(tt["albumsH"]), tt["albumsLead"], seed=51)}
<div class="filters sticky" id="afilters"><input id="aq" type="search" placeholder="{e(tt['albumSearch'])}" aria-label="{e(tt['albumSearch'])}">
<select id="agsel" aria-label="{e(tt['fGenre'])}"><option value="">{e(tt['fGenre'])}: {e(tt['all'])}</option>{gopts}</select>
<span class="mono count"><b id="acount">{STATS['d']}</b> {e(tt['results'])}</span></div>
<div class="tabs" id="adecTabs">{tabs}</div>
<ol class="albums" id="alist">{items}</ol></div>"""
    pg.write(pg.p["albums"], other(lang, "albums"), 0, tt["albumsH"], tt["albumsDesc"].format(**seo_stats(lang)), body, "albums", kind="CollectionPage")


def page_awards(pg):
    lang, tt = pg.lang, pg.t
    aw = "".join(f'<article class="card"><span class="mono code">{e(tt["since"])} {a["since"]}</span><h3><a href="{IT.iurl(pg, 0, "aw", a["slug"])}">{e(a["name"])}</a></h3><div class="meta mono">{e(tt["org"])}: {e(t(a["org"], lang))}</div><p>{e(t(a["blurb"], lang))}</p></article>' for a in C.AWARDS)
    fe = "".join(f'<article class="card"><span class="mono code">{e(tt["since"])} {f["since"]} · {e(f["city"])}</span><h3><a href="{IT.iurl(pg, 0, "fe", f["slug"])}">{e(f["name"])}</a></h3><p>{e(t(f["blurb"], lang))}</p></article>' for f in sorted(C.FESTIVALS, key=lambda f: f["since"]))
    sh = "".join(f'<article class="card"><span class="mono code">{e(s["net"])} · {e(s["years"])}</span><h3><a href="{IT.iurl(pg, 0, "sh", s["slug"])}">{e(s["name"])}</a></h3><p>{e(t(s["blurb"], lang))}</p>{f"<div class=meta><b>{e(tt['alumni'])}:</b> {', '.join(IT.link_name(pg, 0, x) for x in s['alumni'])}</div>" if s["alumni"] else ""}</article>' for s in C.SHOWS)
    body = f"""<div class="wrap">{head_block(f'{len(C.AWARDS)} + {len(C.FESTIVALS)} + {len(C.SHOWS)}', e(tt["awardsH"]), tt["awardsLead"], seed=61)}
<nav class="subnav mono"><a href="#awards">{e(tt['awA'])}</a><a href="#festivals">{e(tt['awF'])}</a><a href="#shows">{e(tt['awS'])}</a></nav>
<section class="sec-in" id="awards"><h2>{e(tt['awA'])}</h2><div class="cards3">{aw}</div></section>
<section class="sec-in" id="festivals"><h2>{e(tt['awF'])}</h2><div class="cards3">{fe}</div></section>
<section class="sec-in" id="shows"><h2>{e(tt['awS'])}</h2><div class="cards3">{sh}</div></section></div>"""
    pg.write(pg.p["awards"], other(lang, "awards"), 0, tt["awardsH"], tt["awardsDesc"], body, "awards", kind="CollectionPage")


def page_instruments(pg):
    lang, tt = pg.lang, pg.t
    body = f'<div class="wrap">{head_block(f"{len(C.INSTRUMENTS)} {e(tt["nav"]["instruments"]).lower()}", e(tt["instrH"]), tt["instrLead"], seed=71)}'
    for kind in ("perc", "cordas", "sopro", "teclas"):
        items = [i for i in C.INSTRUMENTS if i["kind"] == kind]
        if not items:
            continue
        cards = "".join(f'<article class="card icard" id="{i["id"]}"><span class="mono code">{e(tt["kinds"][kind])}</span><h3>{e(t(i["name"], lang))}</h3><p>{e(t(i["blurb"], lang))}</p><div class="chips">' + "".join(f'<a class="chip" style="--c:{FAM[g]["color"]}" href="{pg.fam_url(0, g)}">{e(t(FAM[g]["name"], lang))}</a>' for g in i["genres"]) + "</div></article>" for i in items)
        body += f'<section class="sec-in"><h2>{e(tt["kinds"][kind])} <span class="mono small">{len(items)}</span></h2><div class="cards3">{cards}</div></section>'
    pops = "".join(f'<article class="card icard pop" id="{i["id"]}"><span class="mono code">{e(tt["kinds"][i["kind"]])}</span><h3>{e(t(i["name"], lang))}</h3><p>{e(t(i["blurb"], lang))}</p><div class="chips">' + "".join(f'<a class="chip" style="--c:{FAM[g]["color"]}" href="{pg.fam_url(0, g)}">{e(t(FAM[g]["name"], lang))}</a>' for g in i["genres"]) + "</div></article>" for i in C.POP_INSTRUMENTS)
    body += f'<section class="sec-in" id="populares"><h2>{e(tt["instrPopH"])} <span class="mono small">{len(C.POP_INSTRUMENTS)}</span></h2><p class="lead">{e(tt["instrPopLead"])}</p><div class="cards3">{pops}</div></section>'
    body += "</div>"
    pg.write(pg.p["instruments"], other(lang, "instruments"), 0, tt["instrH"], tt["instrDesc"].format(n=approx(len(C.INSTRUMENTS), lang)), body, "instruments", kind="CollectionPage")


def page_glossary(pg):
    lang, tt = pg.lang, pg.t
    items = "".join(f'<div class="term" id="g-{re.sub(r"[^a-z0-9]+", "-", term.lower())}"><dt>{e(term)}</dt><dd>{e(t(d, lang))}</dd></div>' for term, d in sorted(C.GLOSSARY, key=lambda x: x[0].lower()))
    body = f'<div class="wrap">{head_block(f"{len(C.GLOSSARY)} {e(tt["nav"]["glossary"]).lower()}", e(tt["glossH"]), tt["glossLead"], seed=81)}<dl class="gloss">{items}</dl></div>'
    pg.write(pg.p["glossary"], other(lang, "glossary"), 0, tt["glossH"], tt["glossDesc"].format(n=approx(len(C.GLOSSARY), lang)), body, "glossary")


def page_media(pg):
    lang, tt = pg.lang, pg.t
    main = "".join(f'<article class="mcard"><h3><a href="{u}" target="_blank" rel="noopener">{e(n)} ↗</a></h3><p>{e(t(d, lang))}</p></article>' for n, u, d in C.MAINSTREAM)
    body = (f'<div class="wrap">{head_block(f"{len(C.MAINSTREAM) + len(C.BLOGS)} sites", e(tt["mediaH"]), tt["mediaLead"], seed=91)}'
            f'<section class="sec-in"><h2>{e(tt["mMain"])} <span class="mono small">{len(C.MAINSTREAM)}</span></h2><div class="mgrid">{main}</div></section>'
            f'<section class="sec-in"><h2>{e(tt["mBlogs"])} <span class="mono small">{len(C.BLOGS)}</span></h2>')
    for foc in ("geral", "samba", "sertanejo", "rap", "rock", "metal", "indie", "pop", "ref"):
        items = [b for b in C.BLOGS if b[2] == foc]
        if not items:
            continue
        body += f'<h3 class="mono">{e(tt["focus"][foc])}</h3><div class="chips big">' + "".join(f'<a class="chip plain" href="{u}" target="_blank" rel="noopener">{e(n)} ↗</a>' for n, u, _ in items) + "</div>"
    body += '</section>'
    body += f'<section class="sec-in"><h2>{e(tt["mGone"])}</h2><p class="mono small gone">{e(" · ".join(C.BLOGS_GONE))}</p></section></div>'
    pg.write(pg.p["media"], other(lang, "media"), 0, tt["mediaH"], tt["mediaDesc"], body, "media", kind="CollectionPage")


def page_about(pg):
    lang, tt = pg.lang, pg.t
    secs = [f'<section class="sec-in"><h2>{e(h)}</h2><p>{e(p)}</p></section>' for h, p in tt["about"]]
    secs.insert(1, f'<section class="sec-in about-stats"><h2>{e(tt["statsH"])}</h2><div class="stats">{stats_grid(tt)}</div></section>')
    secs = "".join(secs)
    body = f'<div class="wrap narrow">{head_block("BiblioVerse", e(tt["aboutH"]), tt["footer"], seed=101)}{secs}<p><a class="btn" href="https://www.linkedin.com/company/biblioverse.org" target="_blank" rel="noopener">BiblioVerse · LinkedIn</a></p></div>'
    pg.write(pg.p["about"], other(lang, "about"), 0, tt["aboutH"], tt["aboutDesc"], body, "about", kind="AboutPage")


def page_privacy(pg):
    lang, tt = pg.lang, pg.t
    body = f'<div class="wrap narrow">{head_block("BiblioVerse", e(tt["privacyH"]), tt["privacyLead"], seed=111)}<section class="sec-in"><p>{e(tt["privacy"])}</p><p class="mono small">{e(tt["updated"])} {BUILT[5:7]}/{BUILT[:4]}</p></section></div>'
    pg.write(pg.p["privacy"], other(lang, "privacy"), 0, tt["privacyH"], tt["privacyLead"], body, "privacy")


def page_404(pg):
    tt = pg.t
    body = f'<div class="wrap narrow"><div class="page-head"><span class="kicker mono">404</span><h1>{e(tt["notfound"])}</h1><p class="lead">{e(tt["notfoundP"])}</p><p><a class="btn pri" href="{"/" if pg.lang == "en" else "/pt/"}">{e(tt["backHome"])}</a></p></div>{mosaic(12, 3, "#007d36", FLAG_INKS, 404, cls="mosaic nf-mosaic")}</div>'
    pg.write("404.html", "404.html", 0, tt["notfound"], tt["notfoundP"], body)
    URLS.pop()


def footer_tiles():
    svg = strip(99, "#012169", ["#fedd00", "#007d36", "#ffffff"], cols=48, cls="foot").replace('<svg class="foot"', '<svg xmlns="http://www.w3.org/2000/svg"', 1)
    svg = svg.replace(" aria-hidden=\"true\" role=\"img\">", ">", 1)  # rodapé estático, sem animação
    open(os.path.join(ROOT, "assets", "footer-tiles.svg"), "w", encoding="utf8", newline="\n").write(svg)


def main():
    IT.setup(sys.modules[__name__])
    footer_tiles()
    n_items = 0
    for lang in ("en", "pt"):
        pg = Page(lang)
        n_items += IT.build_all(pg)
        page_home(pg)
        page_genres(pg)
        page_map(pg)
        for i, f in enumerate(C.FAMILIES):
            page_family(pg, f, i)
        page_artists(pg)
        page_singers(pg)
        page_musicians(pg)
        page_producers(pg)
        page_influencers(pg)
        page_songs(pg)
        page_albums(pg)
        page_awards(pg)
        page_instruments(pg)
        page_glossary(pg)
        page_media(pg)
        page_about(pg)
        page_privacy(pg)
        page_404(pg)
    # sitemap / robots / manifest / CNAME
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n')
        for u, pt, en in URLS:
            f.write(f'<url><loc>{u}</loc><lastmod>{BUILT}</lastmod><xhtml:link rel="alternate" hreflang="pt-BR" href="{pt}"/><xhtml:link rel="alternate" hreflang="en" href="{en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{en}"/></url>\n')
        f.write("</urlset>\n")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf8", newline="\n").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(ROOT, "CNAME"), "w", encoding="utf8", newline="\n").write("brazilianmusic.biblioverse.org\n")
    man = {"name": "Brazilian Music · Música Brasileira", "short_name": "BR Music", "start_url": "/", "display": "standalone", "background_color": "#f4efe4", "theme_color": "#c62828",
           "icons": [{"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"}]}
    json.dump(man, open(os.path.join(ROOT, "site.webmanifest"), "w", encoding="utf8"), ensure_ascii=False, indent=1)
    print(f"ok: {len(URLS)} pages ({n_items} item pages) · {STATS}")


if __name__ == "__main__":
    main()
