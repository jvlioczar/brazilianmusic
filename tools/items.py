# -*- coding: utf-8 -*-
"""Páginas individuais: artistas, instrumentistas, subgêneros, programas, prêmios, festivais e instrumentos.
Importado por build.py depois que os dados e helpers estão prontos (recebe o módulo build como `B`).
A descrição geral é composta só com o que o catálogo sabe de cada item; nada é inventado."""
import re
import unicodedata
from urllib.parse import quote, quote_plus

B = None  # módulo build, injetado em setup()
import json as _json, os as _os
_WL_PATH = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "wiki_links.json")
WL = _json.load(open(_WL_PATH, encoding="utf8")) if _os.path.exists(_WL_PATH) else {"pt": {}, "en": {}}


# links fixados à mão; valem nos dois idiomas e não são trocados pelo fetch_wiki.py
WIKI_FIX = {"m:luciano-carlos-cunha": "https://pt.wikipedia.org/wiki/Luciano_Carlos_Cunha",
            "a:mel-duarte": "https://pt.wikipedia.org/wiki/Mel_Duarte",
            "a:pepita": "https://pt.wikipedia.org/wiki/Pepita_(artista)",
            "a:nikki-valentine": "https://pt.wikipedia.org/wiki/Nikki_(cantora)",
            "m:hugo-rafael": "https://pt.wikipedia.org/wiki/Hugo_Rafael",
            "m:marimoon": "https://pt.wikipedia.org/wiki/MariMoon",
            "m:gastao-moreira": "https://pt.wikipedia.org/wiki/Gast%C3%A3o_Moreira",
            "m:fabio-massari": "https://pt.wikipedia.org/wiki/Fabio_Massari",
            "m:luiz-thunderbird": "https://pt.wikipedia.org/wiki/Luiz_Thunderbird",
            "m:edgard-piccoli": "https://pt.wikipedia.org/wiki/Edgard_Piccoli",
            "m:sarah-oliveira": "https://pt.wikipedia.org/wiki/Sarah_Oliveira",
            "m:roberta-martinelli": "https://pt.wikipedia.org/wiki/Roberta_Martinelli"}


def wiki_for(lang, key, name, extra):
    """Artigo confirmado (tools/fetch_wiki.py) ou, sem confirmação, uma busca com qualificador (nunca um 'go' às cegas)."""
    if key in WIKI_FIX:
        return WIKI_FIX[key]
    title = WL.get(lang, {}).get(key)
    host = "pt" if lang == "pt" else "en"
    if title:
        return f"https://{host}.wikipedia.org/wiki/" + quote(title.replace(" ", "_"), safe="()_,'!-.")
    return wiki(lang, name, False, extra)

def wiki_same(*keys):
    """Só artigos confirmados (WIKI_FIX ou tools/fetch_wiki.py), nunca buscas: vão no sameAs do JSON-LD."""
    out = []
    for key in keys:
        if key in WIKI_FIX and WIKI_FIX[key] not in out:
            out.append(WIKI_FIX[key])
        for lg in ("pt", "en"):
            title = WL.get(lg, {}).get(key)
            if title:
                u = f"https://{lg}.wikipedia.org/wiki/" + quote(title.replace(" ", "_"), safe="()_,'!-.")
                if u not in out:
                    out.append(u)
    return out


def abs_url(lang, kind, slug):
    return f"{B.SITE}/{'pt/' if lang == 'pt' else ''}{DIRS[lang][kind]}/{slug}.html"


def plain(html_txt):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", html_txt)).strip()


def state_ld(uf, lang):
    loc = UF.get(uf)
    if not loc:
        return None
    name = re.sub(r"^d[oae]s? ", "", loc[0]) if lang == "pt" else re.sub(r"^the ", "", loc[1])
    return {"@type": "State", "name": name, "containedInPlace": {"@type": "Country", "name": "Brasil" if lang == "pt" else "Brazil"}}


def ld_compact(d):
    return {k: v for k, v in d.items() if v not in (None, "", [])}


DIRS = {"pt": dict(a="artistas", m="pessoas", s="subgeneros", sh="programas", aw="premiacoes", fe="festivais", ins="instrumentos"),
        "en": dict(a="artists", m="people", s="subgenres", sh="shows", aw="awards", fe="festivals", ins="instruments")}

UF = {
    "AC": ("do Acre", "Acre"), "AL": ("de Alagoas", "Alagoas"), "AM": ("do Amazonas", "Amazonas"), "AP": ("do Amapá", "Amapá"),
    "BA": ("da Bahia", "Bahia"), "CE": ("do Ceará", "Ceará"), "DF": ("do Distrito Federal", "the Federal District (Brasília)"),
    "ES": ("do Espírito Santo", "Espírito Santo"), "GO": ("de Goiás", "Goiás"), "MA": ("do Maranhão", "Maranhão"),
    "MG": ("de Minas Gerais", "Minas Gerais"), "MS": ("de Mato Grosso do Sul", "Mato Grosso do Sul"), "MT": ("de Mato Grosso", "Mato Grosso"),
    "PA": ("do Pará", "Pará"), "PB": ("da Paraíba", "Paraíba"), "PE": ("de Pernambuco", "Pernambuco"), "PI": ("do Piauí", "Piauí"),
    "PR": ("do Paraná", "Paraná"), "RJ": ("do Rio de Janeiro", "Rio de Janeiro"), "RN": ("do Rio Grande do Norte", "Rio Grande do Norte"),
    "RO": ("de Rondônia", "Rondônia"), "RR": ("de Roraima", "Roraima"), "RS": ("do Rio Grande do Sul", "Rio Grande do Sul"),
    "SC": ("de Santa Catarina", "Santa Catarina"), "SE": ("de Sergipe", "Sergipe"), "SP": ("de São Paulo", "São Paulo"), "TO": ("do Tocantins", "Tocantins"),
}

ITXT = {
    "pt": dict(
        typeN=dict(band="Banda", solo="Artista solo", duo="Dupla", group="Grupo", mc="MC", dj="DJ", collective="Coletivo"),
        debut=", com estreia registrada em {y}", fam1="Está no catálogo na família {f}, no subgênero {s}.", famN="Está no catálogo na família {f}, nos subgêneros {s}.",
        tier=dict(S="Está entre as lendas do catálogo (nível S).", A="Está entre os gigantes do catálogo (nível A).", B="É uma referência no seu campo (nível B)."),
        songs=("{n} música", "{n} músicas"), albums=("{n} disco essencial", "{n} discos essenciais"),
        have_both="Tem {s} na linha do tempo e {a}.", have_s="Tem {s} na linha do tempo do catálogo.", have_a="Tem {a} na lista do catálogo.",
        tags="Faz parte das coleções: {x}.", shows="Passou pelo programa {x}.", showsN="Passou pelos programas {x}.",
        and_=" e ", about="Sobre", links="Ouça e saiba mais", inTimeline="Na linha do tempo", essAlbums="Discos essenciais",
        related="Artistas relacionados", linkedMus="Instrumentistas e produtores ligados", linkedArt="Bandas e artistas ligados",
        alsoArtist="Ver também no diretório de artistas", shows_h="Programas de TV", family="Família", subgenres="Subgêneros", debutL="Estreia",
        stateL="Estado", tierL="Nível", typeL="Tipo", roleL="Listas", roles=dict(voc="Vocalistas", gtr="Guitarristas", bss="Baixistas", drm="Bateristas", prd="Produtores", inf="Influenciadores", vio="Violão e viola", tec="Teclados e piano", san="Sanfona e gaita", cho="Bandolim e cavaquinho", sop="Sopros", per="Percussão"),
        roleSing=dict(voc="Voz", gtr="Guitarra", bss="Baixo", drm="Bateria", prd="Produção", inf="Criação de conteúdo", vio="Violão e viola", tec="Teclados e piano", san="Sanfona", cho="Bandolim e cavaquinho", sop="Sopros", per="Percussão"),
        infNote=dict(vj="Ex-VJ ou apresentador de programa musical que segue produzindo conteúdo sobre música.", crit="Jornalismo e crítica musical no Instagram: resenhas, fatos e curiosidades.", edu="Ensina teoria, instrumento e produção musical no Instagram."), listed="Aparece nas listas {x}.", featured="Tem ficha de destaque na lista.",
        sameRole="Na mesma lista", sub_desc="Subgênero da família {f}, com registro desde {y}.", sub_count="O catálogo reúne {a} e {s} ligadas a ele.",
        sub_count_a="O catálogo reúne {a} ligados a ele.", artistsN=("{n} artista", "{n} artistas"), siblings="Outros subgêneros da família",
        artistsH="Artistas", songsH="Músicas na linha do tempo", sinceL="Desde", netL="Emissora", yearsL="Anos", orgL="Organiza", cityL="Cidade",
        alumni="Artistas que passaram pelo programa", kindL="Tipo", whereL="Onde aparece", wiki_extra="música brasileira", instr_extra="instrumento musical",
        sub_extra="gênero musical", listenYT="ouvir no YouTube", prev="Anterior", next="Próximo", winners="Vencedores e finalistas",
    ),
    "en": dict(
        typeN=dict(band="Band", solo="Solo artist", duo="Duo", group="Group", mc="MC", dj="DJ", collective="Collective"),
        debut=", on record since {y}", fam1="Listed in the {f} family, under {s}.", famN="Listed in the {f} family, under {s}.",
        tier=dict(S="Ranked among the catalogue's legends (tier S).", A="Ranked among the catalogue's giants (tier A).", B="A reference in the field (tier B)."),
        songs=("{n} song", "{n} songs"), albums=("{n} essential album", "{n} essential albums"),
        have_both="Has {s} in the timeline and {a}.", have_s="Has {s} in the catalogue timeline.", have_a="Has {a} in the catalogue list.",
        tags="Part of the collections: {x}.", shows="Appeared on {x}.", showsN="Appeared on {x}.",
        and_=" and ", about="About", links="Listen and learn more", inTimeline="In the timeline", essAlbums="Essential albums",
        related="Related artists", linkedMus="Linked musicians and producers", linkedArt="Linked bands and artists",
        alsoArtist="See also in the artist directory", shows_h="TV shows", family="Family", subgenres="Subgenres", debutL="Debut",
        stateL="State", tierL="Tier", typeL="Type", roleL="Lists", roles=dict(voc="Singers", gtr="Guitarists", bss="Bassists", drm="Drummers", prd="Producers", inf="Influencers", vio="Acoustic guitar and viola", tec="Keyboards and piano", san="Accordion", cho="Mandolin and cavaquinho", sop="Winds", per="Percussion"),
        roleSing=dict(voc="Vocals", gtr="Guitar", bss="Bass", drm="Drums", prd="Production", inf="Content creation", vio="Acoustic guitar and viola", tec="Keyboards and piano", san="Accordion", cho="Mandolin and cavaquinho", sop="Winds", per="Percussion"),
        infNote=dict(vj="A former VJ or music-show presenter who still makes music content.", crit="Music journalism and criticism on Instagram: reviews, facts and trivia.", edu="Teaches music theory, instruments and production on Instagram."), listed="Listed under {x}.", featured="Featured with a full profile in the list.",
        sameRole="In the same list", sub_desc="Subgenre of the {f} family, on record since {y}.", sub_count="The catalogue lists {a} and {s} linked to it.",
        sub_count_a="The catalogue lists {a} linked to it.", artistsN=("{n} artist", "{n} artists"), siblings="Other subgenres in the family",
        artistsH="Artists", songsH="Songs in the timeline", sinceL="Since", netL="Network", yearsL="Years", orgL="Organizer", cityL="City",
        alumni="Artists who came through the show", kindL="Type", whereL="Where it appears", wiki_extra="Brazilian music", instr_extra="musical instrument",
        sub_extra="music genre", listenYT="listen on YouTube", prev="Previous", next="Next", winners="Winners and finalists",
    ),
}

ROLE_COLOR = dict(voc="#a52755", gtr="#b02732", bss="#344cad", drm="#915127", prd="#1d7b86", inf="#8d389f", vio="#8c6921", tec="#3b5a7d", san="#a85a14", cho="#915127", sop="#218376", per="#bf4c22")
ROLE_PAGE = dict(voc="singers", gtr="musicians", bss="musicians", drm="musicians", prd="producers", inf="influencers", vio="musicians", tec="musicians", san="musicians", cho="musicians", sop="musicians", per="musicians")
STOP = {"Zero", "Isso", "Gram", "Cine", "Raça", "Girls", "Ella", "Maria", "Luka", "Clau", "Cleo", "Silva", "Pablo", "Benin", "Huey", "Inky",
        "Hover", "Heaven", "Fluxe", "Npkn", "Blear", "Cruz", "Soro", "Canil", "Pluma", "Stela", "Daniel", "Leonardo", "Gloria", "Melody",
        "Malta", "Lagum", "Brava", "Girls", "Banana Split", "Ravena", "Paquitas", "Twister", "Polegar", "Ludov", "Mafius", "Quasar", "Magnólia"}
ALIASES = {"mc kevin o chris": "kevin o chris", "valeska popozuda": "valesca popozuda", "mc beyonce": "ludmilla", "nacao zumbi": "chico science & nacao zumbi",
           "chico science": "chico science & nacao zumbi", "detonautas": "detonautas roque clube", "hevo 84": "hevo84", "jorge ben": "jorge ben jor",
           "kevinho": "mc kevinho", "thaeme": "thaeme & thiago", "biquini": "biquini cavadao", "lobao & os ronaldos": "lobao & os ronaldos",
           "sergio mendes & brasil '66": "sergio mendes", "brasil '66": "sergio mendes", "frejat": "frejat", "roberto frejat": "frejat",
           "pedra leticia": "pedra leticia", "turma do balao magico": "a turma do balao magico",
           "mr catra": "mr. catra", "os havaianos": "os hawaianos", "biel": "mc biel", "dennis": "dennis dj", "mc loma": "mc loma e as gemeas lacracao",
           "melody": "melody", "mc melody": "melody", "the clevers": "os incriveis", "menos e mais": "grupo menos e mais", "ws da igrejinha": "ws da igrejinha"}


def slugify(s):
    s = unicodedata.normalize("NFKD", s.replace("&", " e ")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()


def plural(pair, n):
    return (pair[0] if n == 1 else pair[1]).format(n=n)


def joinand(items, lang):
    items = list(items)
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + ITXT[lang]["and_"] + items[-1]


def wiki(lang, name, direct=True, extra=""):
    host = "pt" if lang == "pt" else "en"
    q = name + (" " + extra if extra else "")
    return f"https://{host}.wikipedia.org/w/index.php?search={quote_plus(q)}" + ("&go=Go" if direct else "&fulltext=1")


def spotify(name):
    return "https://open.spotify.com/search/" + quote(name)


def lastfm(name, direct=True):
    return ("https://www.last.fm/music/" + quote_plus(name)) if direct else ("https://www.last.fm/search?q=" + quote_plus(name))


# ── índices (preenchidos em setup) ─────────────────────────────────────────────
ABN, SONGS_BY, ALBUMS_BY, MUS, MUS_LIST, MUS_BY_ART, SHOWS_BY_ART, SAME_AS_FAMILY, FAM_ARTS = {}, {}, {}, {}, [], {}, {}, set(), {}


def find_artist(name):
    k = norm(name)
    k = ALIASES.get(k, k)
    a = ABN.get(k)
    if a is None and k:  # créditos de funk citam o MC sem o prefixo ("Kako" = MC Kako) ou com "MCs"
        k2 = re.sub(r"^mcs? ", "", k)
        a = ABN.get(k2) or ABN.get("mc " + k2) or ABN.get("dj " + k2)
    return a


def credit_artists(text):
    found = []
    whole = find_artist(text)
    if whole:
        return [whole]
    inner = re.findall(r"\(([^)]+)\)", text)
    text = re.sub(r"\s*\([^)]*\)", "", text)
    parts = re.split(r"\s*(?:;|,| e | feat\.? | ft\.? | part\.? | com | x )\s*", text) + inner
    for p in parts:
        p = re.sub(r"^(?:com )?participação de ", "", p.strip())
        a = find_artist(p) if p else None
        cands = [a] if a else [find_artist(q) for q in re.split(r"\s+&\s+", p)] if " & " in p else []
        for c in cands:
            if c and c not in found:
                found.append(c)
    return found


def setup(build):
    global B
    B = build
    for a in B.ARTISTS:
        ABN[norm(a["name"])] = a
        FAM_ARTS.setdefault(a["family"], []).append(a)
    for sid in B.SUB:
        if sid in B.FAM and len(B.FAM[sid]["subs"]) == 1:
            SAME_AS_FAMILY.add(sid)
    for row in B.SONGS:
        for a in credit_artists(row[2]):
            SONGS_BY.setdefault(a["id"], []).append(row)
    for row in B.ALBUMS:
        for a in credit_artists(row[2]):
            ALBUMS_BY.setdefault(a["id"], []).append(row)
    # instrumentistas: uma página por pessoa, com todas as listas em que aparece
    creators = [(n,) + B.C.CREATOR_FOCUS.get(n, (ITXT["pt"]["infNote"][g], ITXT["en"]["infNote"][g])) for n, h, g in B.C.CREATORS]
    handles = {slugify(n): h for n, h, g in B.C.CREATORS if h}
    handles.update({slugify(n): h for n, h in getattr(B.M, "HANDLES", {}).items()})
    for role, rows, feat in [("voc", B.VOC, 15)] + [(c, r, f) for c, _, r, f in B.INSTR] + [("prd", B.PROD, 15), ("inf", creators, 0)]:
        for i, (n, pt, en) in enumerate(rows):
            sl = slugify(n)
            m = MUS.get(sl)
            if not m:
                m = dict(name=n, slug=sl, roles=[], notes=[], featured=False, handle=handles.get(sl))
                MUS[sl] = m
                MUS_LIST.append(m)
            if role not in m["roles"]:
                m["roles"].append(role)
            if pt or en:
                m["notes"].append((role, pt, en))
            if i < feat:
                m["featured"] = True
    names = sorted((a["name"] for a in B.ARTISTS if len(a["name"]) >= 4 and a["name"] not in STOP), key=len, reverse=True)
    extra = {"Nação Zumbi": "chico science & nacao zumbi", "Paralamas": "os paralamas do sucesso", "Mutantes": "os mutantes"}
    names = sorted(set(names) | set(extra), key=len, reverse=True)
    rx = re.compile(r"(?<![\w])(" + "|".join(re.escape(n) for n in names) + r")(?![\w])")
    for m in MUS_LIST:
        linked = []
        own = find_artist(m["name"])
        m["self_artist"] = own
        for _, pt, _en in m["notes"]:
            for hit in rx.findall(pt):
                a = ABN[extra[hit]] if hit in extra else ABN[norm(hit)]
                if a not in linked and a is not own:
                    linked.append(a)
        m["artists"] = linked
        if own:
            MUS_BY_ART.setdefault(own["id"], []).append(m)
        for a in linked:
            MUS_BY_ART.setdefault(a["id"], []).append(m)
    for s in B.C.SHOWS:
        s["slug"] = slugify(s["name"])
        s["alumni_a"] = [find_artist(x) for x in s["alumni"]]
        for a in s["alumni_a"]:
            if a:
                SHOWS_BY_ART.setdefault(a["id"], []).append(s)
    for x in B.C.AWARDS + B.C.FESTIVALS:
        x["slug"] = slugify(x["name"])
    assert len({s["slug"] for s in B.C.SHOWS}) == len(B.C.SHOWS)
    assert len({x["slug"] for x in B.C.AWARDS}) == len(B.C.AWARDS)
    assert len({x["slug"] for x in B.C.FESTIVALS}) == len(B.C.FESTIVALS)


# ── URLs ──────────────────────────────────────────────────────────────────────
def iurl(pg, depth, kind, slug):
    return pg.href(depth, f"{DIRS[pg.lang][kind]}/{slug}.html")


def art_url(pg, depth, a):
    return iurl(pg, depth, "a", a["id"])


def mus_url(pg, depth, m):
    return iurl(pg, depth, "m", m["slug"])


def sub_url(pg, depth, sid):
    if sid in SAME_AS_FAMILY:
        return pg.fam_url(depth, sid)
    return iurl(pg, depth, "s", sid)


def link_name(pg, depth, name):
    a = find_artist(name)
    e = B.e
    return f'<a href="{art_url(pg, depth, a)}">{e(name)}</a>' if a else e(name)


def link_credit(pg, depth, text):
    found = credit_artists(text)
    e = B.e
    return f'<a href="{art_url(pg, depth, found[0])}">{e(text)}</a>' if found else e(text)


# ── blocos de página ──────────────────────────────────────────────────────────
def item_head(pg, depth, color, kicker, title, facts, lead, seed, back_label, back_href):
    e = B.e
    return (f'<div class="fam-head item-head" style="--c:{color}"><div class="wrap fam-grid"><div class="fam-txt">'
            f'<a class="mono back" href="{back_href}">← {e(back_label)}</a>'
            f'<div class="item-kicker mono">{kicker}</div><h1>{e(title)}</h1>'
            f'<div class="facts">{facts}</div>' + (f'<p class="lead">{e(lead)}</p>' if lead else "") +
            f'</div><div class="fam-panel">{B.mosaic(4, 4, color, ["#ffffff", "#fedd00"], seed, cls="mosaic item-mosaic")}</div></div></div>')


def fact(label, value_html):
    return f'<span>{B.e(label)} <b>{value_html}</b></span>' if value_html else ""


def ext_links(items):
    e = B.e
    return '<div class="ext-links">' + "".join(f'<a class="btn ext" href="{u}" target="_blank" rel="noopener">{e(l)} ↗</a>' for l, u in items) + "</div>"


def desc_block(pg, paras, links):
    e = B.e
    T = ITXT[pg.lang]
    body = "".join(f"<p>{p if p.startswith('<') else e(p)}</p>" for p in paras if p)
    return f'<section class="sec-in desc"><h2>{e(T["about"])}</h2>{body}<h3 class="mono links-h">{e(T["links"])}</h3>{ext_links(links)}</section>'


def song_list(pg, depth, rows, limit=60):
    e, yt = B.e, B.yt
    rows = sorted(rows)[:limit]
    return '<ul class="songs">' + "".join(
        f'<li><span class="y mono">{y}</span><a href="{yt(a + " " + s)}" target="_blank" rel="noopener">{e(s)}</a><small>{link_credit(pg, depth, a)}</small></li>'
        for y, s, a, *_ in rows) + "</ul>"


def album_items(pg, depth, rows):
    e, yt, t = B.e, B.yt, B.t
    return '<ol class="albums">' + "".join(
        f'<li class="album"><span class="y mono">{y}</span><div><h3><a href="{yt(ar + " " + al + " album")}" target="_blank" rel="noopener">{e(al)}</a></h3><div class="meta">{link_credit(pg, depth, ar)}</div><p>{e(t((pt, en), pg.lang))}</p></div></li>'
        for y, al, ar, _g, pt, en in sorted(rows)) + "</ol>"


def name_chips(items):
    e = B.e
    return '<div class="chips">' + "".join(f'<a class="chip plain" href="{u}">{e(n)}</a>' for n, u in items) + "</div>"


def pager(prev, nxt):
    e = B.e
    return ('<div class="pager">' + (f'<a class="btn" href="{prev[1]}">← {e(prev[0])}</a>' if prev else "<span></span>") +
            (f'<a class="btn" href="{nxt[1]}">{e(nxt[0])} →</a>' if nxt else "<span></span>") + "</div>")


# ── artista ───────────────────────────────────────────────────────────────────
def artist_paras(a, lang):
    T, t = ITXT[lang], B.t
    tt = B.UI[lang]
    f = B.FAM[a["family"]]
    s1 = T["typeN"].get(a["type"], a["type"])
    loc = UF.get(a["uf"])
    if loc:
        s1 += " " + (loc[0] if lang == "pt" else "from " + loc[1])
    if a["year"]:
        s1 += T["debut"].format(y=a["year"])
    out = [s1 + "."]
    subs = [t(B.SUB[g]["name"], lang) for g in a["genres"]]
    out.append((T["fam1"] if len(subs) == 1 else T["famN"]).format(f=t(f["name"], lang), s=joinand(subs, lang)))
    if a["tier"]:
        out.append(T["tier"][a["tier"]])
    ns, na = len(SONGS_BY.get(a["id"], [])), len(ALBUMS_BY.get(a["id"], []))
    if ns and na:
        out.append(T["have_both"].format(s=plural(T["songs"], ns), a=plural(T["albums"], na)))
    elif ns:
        out.append(T["have_s"].format(s=plural(T["songs"], ns)))
    elif na:
        out.append(T["have_a"].format(a=plural(T["albums"], na)))
    if a["tags"]:
        out.append(T["tags"].format(x=joinand([tt["tags"][x] for x in a["tags"]], lang)))
    shows = SHOWS_BY_ART.get(a["id"], [])
    if shows:
        out.append((T["shows"] if len(shows) == 1 else T["showsN"]).format(x=joinand([s["name"] for s in shows], lang)))
    return [" ".join(out)]


def page_artist(pg, a, prev, nxt):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    f = B.FAM[a["family"]]
    loc = UF.get(a["uf"])
    facts = (fact(T["typeL"], e(T["typeN"].get(a["type"], a["type"]))) +
             fact(T["family"], f'<a href="{pg.fam_url(1, f["id"])}">{e(t(f["name"], lang))}</a>') +
             fact(T["debutL"], str(a["year"]) if a["year"] else "") +
             fact(T["stateL"], e(loc[1]) if loc else "") +
             fact(T["tierL"], e(tt["tiers"][a["tier"]]) if a["tier"] else ""))
    kicker = e(t(f["name"], lang)) + " · " + ", ".join(f'<a href="{sub_url(pg, 1, g)}">{e(t(B.SUB[g]["name"], lang))}</a>' for g in a["genres"])
    links = [("Wikipedia", wiki_for(lang, "a:" + a["id"], a["name"], T["wiki_extra"])), ("Spotify", spotify(a["name"])),
             ("Last.fm", lastfm(a["name"])), ("YouTube", B.yt(a["name"] + " música"))]
    body = item_head(pg, 1, f["color"], kicker, a["name"], facts, t(a["blurb"], lang), sum(map(ord, a["id"])), tt["nav"]["artists"], pg.href(1, pg.p["artists"]))
    body += '<div class="wrap">' + desc_block(pg, artist_paras(a, lang), links)
    songs = SONGS_BY.get(a["id"], [])
    if songs:
        body += f'<section class="sec-in"><h2>{e(T["inTimeline"])} <span class="mono small">{len(songs)}</span></h2>{song_list(pg, 1, songs)}</section>'
    albums = ALBUMS_BY.get(a["id"], [])
    if albums:
        body += f'<section class="sec-in"><h2>{e(T["essAlbums"])}</h2>{album_items(pg, 1, albums)}</section>'
    mus = MUS_BY_ART.get(a["id"], [])
    if mus:
        body += f'<section class="sec-in"><h2>{e(T["linkedMus"])}</h2>{name_chips([(m["name"], mus_url(pg, 1, m)) for m in mus])}</section>'
    shows = SHOWS_BY_ART.get(a["id"], [])
    if shows:
        body += f'<section class="sec-in"><h2>{e(T["shows_h"])}</h2>{name_chips([(s["name"], iurl(pg, 1, "sh", s["slug"])) for s in shows])}</section>'
    rel = [x for x in B.BY_SUB.get(a["genres"][0], []) if x is not a]
    rel += [x for x in FAM_ARTS[a["family"]] if x is not a and x not in rel]
    rel.sort(key=lambda x: (B.TIER_ORDER[x["tier"]], x["year"] or 9999))
    body += f'<section class="sec-in"><h2>{e(T["related"])}</h2><div class="agrid">{"".join(B.artist_card(pg, 1, x, compact=True) for x in rel[:8])}</div></section>'
    body += pager(prev, nxt) + "</div>"
    desc = f'{a["name"]}: {t(a["blurb"], lang) or artist_paras(a, lang)[0]}'[:300]
    url = abs_url(lang, "a", a["id"])
    entity = ld_compact({"@type": "MusicGroup", "@id": url + "#artist", "name": a["name"], "url": url,
                         "description": t(a["blurb"], lang) or plain(artist_paras(a, lang)[0]),
                         "genre": [t(B.SUB[g]["name"], lang) for g in a["genres"]],
                         "foundingDate": str(a["year"]) if a["year"] else None, "foundingLocation": state_ld(a["uf"], lang),
                         "sameAs": wiki_same("a:" + a["id"]),
                         "track": [{"@type": "MusicRecording", "name": r[1], "datePublished": str(r[0])} for r in songs[:30]],
                         "album": [{"@type": "MusicAlbum", "name": r[1], "datePublished": str(r[0])} for r in albums]})
    oth = "en" if lang == "pt" else "pt"
    pg.write(f"{DIRS[lang]['a']}/{a['id']}.html", f"{DIRS[oth]['a']}/{a['id']}.html", 1, a["name"], desc, body, "artists", kind="ProfilePage", entity=entity)


# ── instrumentista / produtor ─────────────────────────────────────────────────
def page_musician(pg, m, prev, nxt):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    color = ROLE_COLOR[m["roles"][0]]
    roles = [T["roles"][r] for r in m["roles"]]
    facts = fact(T["roleL"], e(", ".join(roles)))
    if m["self_artist"]:
        sa = m["self_artist"]
        facts += fact(T["family"], f'<a href="{pg.fam_url(1, sa["family"])}">{e(t(B.FAM[sa["family"]]["name"], lang))}</a>')
    lead = t(m["notes"][0][1:], lang) if m["notes"] else ""
    paras = [T["listed"].format(x=joinand(roles, lang)) + (" " + T["featured"] if m["featured"] else "")]
    if len(m["notes"]) > 1:
        paras += [f'<b>{e(T["roleSing"][r])}</b> · {e(t((pt, en), lang))}' for r, pt, en in m["notes"]]
    if m["self_artist"]:
        paras.append(f'<a class="btn pri" href="{art_url(pg, 1, m["self_artist"])}">{e(T["alsoArtist"])} →</a>')
    links = [("Wikipedia", wiki_for(lang, "m:" + m["slug"], m["name"], T["wiki_extra"])), ("Spotify", spotify(m["name"])),
             ("Last.fm", lastfm(m["name"], direct=False)), ("YouTube", B.yt(m["name"]))]
    if m.get("handle"):
        links.insert(0, ("Instagram", f"https://www.instagram.com/{m['handle']}/"))
    kicker = e(" · ".join(T["roleSing"][r] for r in m["roles"]))
    body = item_head(pg, 1, color, kicker, m["name"], facts, lead, sum(map(ord, m["slug"])), tt["nav"][ROLE_PAGE[m["roles"][0]]], pg.href(1, pg.p[ROLE_PAGE[m["roles"][0]]]))
    body += '<div class="wrap">' + desc_block(pg, paras, links)
    if m["artists"]:
        body += f'<section class="sec-in"><h2>{e(T["linkedArt"])}</h2>{name_chips([(a["name"], art_url(pg, 1, a)) for a in m["artists"]])}</section>'
    same = [x for x in MUS_LIST if x is not m and x["featured"] and m["roles"][0] in x["roles"]][:14]
    if same:
        body += f'<section class="sec-in"><h2>{e(T["sameRole"])} · {e(T["roles"][m["roles"][0]])}</h2>{name_chips([(x["name"], mus_url(pg, 1, x)) for x in same])}</section>'
    body += pager(prev, nxt) + "</div>"
    oth = "en" if lang == "pt" else "pt"
    url = abs_url(lang, "m", m["slug"])
    entity = ld_compact({"@type": "Person", "@id": url + "#person", "name": m["name"], "url": url, "jobTitle": ", ".join(roles),
                         "description": lead or plain(paras[0]),
                         "sameAs": wiki_same("m:" + m["slug"], *(["a:" + m["self_artist"]["id"]] if m["self_artist"] else []))})
    pg.write(f"{DIRS[lang]['m']}/{m['slug']}.html", f"{DIRS[oth]['m']}/{m['slug']}.html", 1, m["name"], (lead or paras[0])[:300], body, ROLE_PAGE[m["roles"][0]], kind="ProfilePage", entity=entity)


# ── subgênero ─────────────────────────────────────────────────────────────────
def page_subgenre(pg, s, prev, nxt):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    f = B.FAM[s["family"]]
    arts = B.BY_SUB.get(s["id"], [])
    songs = []
    for a in arts:
        for r in SONGS_BY.get(a["id"], []):
            if r not in songs:
                songs.append(r)
    facts = (fact(T["family"], f'<a href="{pg.fam_url(1, f["id"])}">{e(t(f["name"], lang))}</a>') + fact(T["sinceL"], str(s["since"])) +
             fact(T["artistsH"], str(len(arts))) + fact(tt["stats"]["songs"].capitalize(), str(len(songs)) if songs else "") +
             fact(tt["heritageL"], e(B.heritage_txt(s, lang)) if s.get("heritage") else "") +
             fact(tt["fusionL"], e(t(s["fusion"], lang)) if s.get("fusion") else ""))
    paras = [T["sub_desc"].format(f=t(f["name"], lang), y=s["since"])]
    if arts and songs:
        paras[0] += " " + T["sub_count"].format(a=plural(T["artistsN"], len(arts)), s=plural(T["songs"], len(songs)))
    elif arts:
        paras[0] += " " + T["sub_count_a"].format(a=plural(T["artistsN"], len(arts)))
    name = t(s["name"], lang)
    links = [("Wikipedia", wiki(lang, name, False, T["sub_extra"])), ("YouTube", B.yt(name + " música brasileira")), ("Spotify", spotify(name))]
    body = item_head(pg, 1, f["color"], e(f["code"] + " · " + t(f["name"], lang)), name, facts, t(s["blurb"], lang), sum(map(ord, s["id"])) + 7, tt["nav"]["genres"], pg.fam_url(1, f["id"]))
    body += '<div class="wrap">' + desc_block(pg, paras, links)
    if arts:
        body += f'<section class="sec-in"><h2>{e(T["artistsH"])} <span class="mono small">{len(arts)}</span></h2><div class="agrid">{"".join(B.artist_card(pg, 1, a, compact=True) for a in arts)}</div></section>'
    if songs:
        body += f'<section class="sec-in"><h2>{e(T["songsH"])} <span class="mono small">{len(songs)}</span></h2>{song_list(pg, 1, songs)}</section>'
    sib = [x for x in f["subs"] if x is not s]
    if sib:
        body += f'<section class="sec-in"><h2>{e(T["siblings"])}</h2>{name_chips([(t(x["name"], lang), sub_url(pg, 1, x["id"])) for x in sib])}</section>'
    body += pager(prev, nxt) + "</div>"
    oth = "en" if lang == "pt" else "pt"
    url = abs_url(lang, "s", s["id"])
    entity = ld_compact({"@type": "DefinedTerm", "@id": url + "#genre", "name": name, "url": url, "description": t(s["blurb"], lang) or plain(paras[0]),
                         "inDefinedTermSet": {"@type": "DefinedTermSet", "name": tt["genresH"], "url": f"{B.SITE}/{'pt/' if lang == 'pt' else ''}{pg.p['genres']}"}})
    pg.write(f"{DIRS[lang]['s']}/{s['id']}.html", f"{DIRS[oth]['s']}/{s['id']}.html", 1, name, (t(s["blurb"], lang) or paras[0])[:300], body, "genres", kind="Article", entity=entity)


# ── programas, prêmios, festivais, instrumentos ───────────────────────────────
def simple_page(pg, kind, slug, color, kicker, title, facts, lead, paras, links, extra, cur, back, entity=None):
    e = B.e
    lang = pg.lang
    body = item_head(pg, 1, color, kicker, title, facts, lead, sum(map(ord, slug)) + 3, back[0], back[1])
    body += '<div class="wrap">' + desc_block(pg, paras, links) + extra + "</div>"
    oth = "en" if lang == "pt" else "pt"
    if entity:
        url = abs_url(lang, kind, slug)
        entity = ld_compact({"@id": url + "#thing", "name": title, "url": url, "description": lead} | entity)
    pg.write(f"{DIRS[lang][kind]}/{slug}.html", f"{DIRS[oth][kind]}/{slug}.html", 1, title, (lead or title)[:300], body, cur, kind="Article", entity=entity)


def page_show(pg, s):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    facts = fact(T["netL"], e(s["net"])) + fact(T["yearsL"], e(s["years"]))
    extra = ""
    alumni = [(n, a) for n, a in zip(s["alumni"], s["alumni_a"])]
    if alumni:
        extra += f'<section class="sec-in"><h2>{e(T["alumni"])}</h2><div class="chips">' + "".join(
            f'<a class="chip plain" href="{art_url(pg, 1, a)}">{e(n)}</a>' if a else f'<span class="chip plain">{e(n)}</span>' for n, a in alumni) + "</div></section>"
    links = [("Wikipedia", wiki_for(lang, "sh:" + s["slug"], s["name"], "")), ("YouTube", B.yt(s["name"]))]
    simple_page(pg, "sh", s["slug"], "#012169", e(tt["awS"]), s["name"], facts, t(s["blurb"], lang), [], links, extra, "awards", (tt["nav"]["awards"], pg.href(1, pg.p["awards"]) + "#shows"),
                entity={"@type": "TVSeries", "sameAs": wiki_same("sh:" + s["slug"])})


def page_award(pg, a):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    facts = fact(T["sinceL"], str(a["since"])) + fact(T["orgL"], e(t(a["org"], lang)))
    links = [("Wikipedia", wiki_for(lang, "aw:" + a["slug"], a["name"], "")), ("YouTube", B.yt(a["name"]))]
    if a.get("ig"):
        links.append(("Instagram", f"https://www.instagram.com/{a['ig']}/"))
    simple_page(pg, "aw", a["slug"], "#1f8441", e(tt["awA"]), a["name"], facts, t(a["blurb"], lang), [], links, "", "awards", (tt["nav"]["awards"], pg.href(1, pg.p["awards"]) + "#awards"))


def page_festival(pg, f):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    facts = fact(T["sinceL"], str(f["since"])) + fact(T["cityL"], e(f["city"]))
    links = [("Wikipedia", wiki_for(lang, "fe:" + f["slug"], f["name"], "")), ("YouTube", B.yt(f["name"]))]
    simple_page(pg, "fe", f["slug"], "#bf4c22", e(tt["awF"]), f["name"], facts, t(f["blurb"], lang), [], links, "", "awards", (tt["nav"]["awards"], pg.href(1, pg.p["awards"]) + "#festivals"),
                entity={"@type": "Festival", "location": {"@type": "Place", "name": f["city"], "address": {"@type": "PostalAddress", "addressCountry": "BR"}},
                        "sameAs": wiki_same("fe:" + f["slug"])})


def page_instrument(pg, i):
    e, t = B.e, B.t
    lang, tt, T = pg.lang, pg.t, ITXT[pg.lang]
    fams = "".join(f'<a href="{pg.fam_url(1, g)}">{e(t(B.FAM[g]["name"], lang))}</a> ' for g in i["genres"])
    facts = fact(T["kindL"], e(tt["kinds"][i["kind"]])) + fact(T["whereL"], fams.strip())
    name = t(i["name"], lang)
    links = [("Wikipedia", wiki(lang, t(i["name"], "pt"), False, T["instr_extra"])), ("YouTube", B.yt(t(i["name"], "pt") + " instrumento"))]
    extra = f'<section class="sec-in"><h2>{e(T["whereL"])}</h2><div class="chips">' + "".join(
        f'<a class="chip" style="--c:{B.FAM[g]["color"]}" href="{pg.fam_url(1, g)}">{e(t(B.FAM[g]["name"], lang))}</a>' for g in i["genres"]) + "</div></section>"
    simple_page(pg, "ins", i["id"], "#1f8441", e(tt["kinds"][i["kind"]]), name, facts, t(i["blurb"], lang), [], links, extra, "instruments", (tt["nav"]["instruments"], pg.href(1, pg.p["instruments"])))


def build_all(pg):
    """Gera todas as páginas de itens para um idioma. Devolve a contagem."""
    lang = pg.lang
    n = 0
    for fid, arts in FAM_ARTS.items():
        for i, a in enumerate(arts):
            prev = (arts[i - 1]["name"], f'{arts[i - 1]["id"]}.html') if i else None
            nxt = (arts[i + 1]["name"], f'{arts[i + 1]["id"]}.html') if i + 1 < len(arts) else None
            page_artist(pg, a, prev, nxt)
            n += 1
    for i, m in enumerate(MUS_LIST):
        prev = (MUS_LIST[i - 1]["name"], f'{MUS_LIST[i - 1]["slug"]}.html') if i else None
        nxt = (MUS_LIST[i + 1]["name"], f'{MUS_LIST[i + 1]["slug"]}.html') if i + 1 < len(MUS_LIST) else None
        page_musician(pg, m, prev, nxt)
        n += 1
    subs = [s for f in B.C.FAMILIES for s in f["subs"] if s["id"] not in SAME_AS_FAMILY]
    for i, s in enumerate(subs):
        prev = (B.t(subs[i - 1]["name"], lang), f'{subs[i - 1]["id"]}.html') if i else None
        nxt = (B.t(subs[i + 1]["name"], lang), f'{subs[i + 1]["id"]}.html') if i + 1 < len(subs) else None
        page_subgenre(pg, s, prev, nxt)
        n += 1
    for s in B.C.SHOWS:
        page_show(pg, s); n += 1
    for a in B.C.AWARDS:
        page_award(pg, a); n += 1
    for f in B.C.FESTIVALS:
        page_festival(pg, f); n += 1
    return n
