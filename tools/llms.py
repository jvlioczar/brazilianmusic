# -*- coding: utf-8 -*-
"""Música Brasileira para assistentes de IA e buscadores (padrão llmstxt.org). Chamado no fim do build.py.
  llms.txt           índice em Markdown: o que é o site, as páginas principais e as famílias de gêneros (inglês, com seção em português)
  llms-full.txt      todo o catálogo em inglês, em Markdown
  pt/llms-full.txt   todo o catálogo em português
Os números de abertura usam approx() ("+1.600"), como no SEO das páginas."""
import os
import re

L = {
    "en": dict(
        intro="{site} ({other}) is a free, bilingual catalogue of Brazilian music, part of BiblioVerse. English lives at the root and Brazilian Portuguese at /pt/. "
              "Every artist, person, subgenre, award, festival and TV show has its own page with links to Wikipedia, Spotify, Last.fm and YouTube. "
              "Artists are ranked in three tiers: S (legend), A (giant) and B (reference). Song and album credits name the performers, not the composers. Last updated: {built}.",
        full="Full content", full_en="Full catalogue in English", full_en_d="every genre, artist, person, song, album, award, instrument and glossary term, in Markdown",
        full_pt="Catálogo completo em português", full_pt_d="o mesmo conteúdo em português",
        main="Main pages", fams="Genre families", in_pt="Em português", optional="Optional",
        sitemap="Sitemap", sitemap_d="every page in both languages",
        hub="BiblioVerse", hub_d="the library of everything this catalogue belongs to, with its own llms.txt",
        since="since", subs="subgenres", artists="artists",
        genres_h="Genres and subgenres", artists_h="Artists", singers_h="Singers", musicians_h="Instrumentalists", producers_h="Producers",
        influencers_h="Influencers and content creators", songs_h="Songs by year", albums_h="Albums", awards_h="Awards", festivals_h="Festivals",
        shows_h="TV shows", instr_h="Instruments", instr_pop_h="Popular instruments used in Brazilian music", gloss_h="Glossary",
        where="Where", fusion="Fusion genre", debut="debut", tier="tier", org="organiser", city="city", net="network", years="years",
        used="used in", alumni="artists who came through it", s="s", decade="The {d}s",
    ),
    "pt": dict(
        intro="{site} ({other}) é um catálogo gratuito e bilíngue da música brasileira, parte da BiblioVerse. O português fica em /pt/ e o inglês na raiz. "
              "Cada artista, pessoa, subgênero, prêmio, festival e programa de TV tem página própria, com links para Wikipedia, Spotify, Last.fm e YouTube. "
              "Os artistas estão em três níveis: S (lenda), A (gigante) e B (referência). Os créditos de músicas e discos citam os intérpretes, não os compositores. Última atualização: {built}.",
        genres_h="Gêneros e subgêneros", artists_h="Artistas", singers_h="Vocalistas", musicians_h="Instrumentistas", producers_h="Produtores",
        influencers_h="Influenciadores e criadores de conteúdo", songs_h="Músicas por ano", albums_h="Discos", awards_h="Prêmios", festivals_h="Festivais",
        shows_h="Programas de TV", instr_h="Instrumentos", instr_pop_h="Instrumentos populares usados na música brasileira", gloss_h="Glossário",
        where="Onde", fusion="Gênero de fusão", debut="estreia", tier="nível", org="organizador", city="cidade", net="emissora", years="anos",
        used="usado em", alumni="artistas que passaram por lá", since="desde", subs="subgêneros", artists="artistas", decade="Anos {d}",
    ),
}

# página principal: (chave em PATHS, título em UI, descrição em UI)
MAIN = [("genres", "genresH", "genresDesc"), ("map", "mapTitle", "mapDesc"), ("artists", "artistsH2", "artistsDesc"), ("singers", "singersH", "singersDesc"),
        ("musicians", "musiciansH", "musiciansDesc"), ("producers", "producersH", "producersDesc"), ("influencers", "influencersH", "influencersDesc"),
        ("songs", "songsH", "songsDesc"), ("albums", "albumsH", "albumsDesc"), ("awards", "awardsH", "awardsDesc"), ("instruments", "instrH", "instrDesc"),
        ("glossary", "glossH", "glossDesc"), ("media", "mediaH", "mediaDesc"), ("about", "aboutH", "aboutDesc")]


def write_all(B):
    IT, C, t = B.IT, B.C, B.t

    def url(lang, rel):
        return f"{B.SITE}/{'pt/' if lang == 'pt' else ''}{rel}".replace("index.html", "")

    def counts(lang):
        n_mus = len({IT.slugify(r[0]) for _c, _k, rows, _f in B.INSTR for r in rows})
        return B.seo_stats(lang), dict(singers=B.approx(len(B.VOC) + len(B.VOC_ART), lang), musicians=B.approx(n_mus, lang), producers=B.approx(len(B.PROD), lang),
                                                     influencers=B.approx(len(C.CREATORS), lang), instruments=B.approx(len(C.INSTRUMENTS), lang),
                                                     glossary=B.approx(len(C.GLOSSARY), lang))

    def main_pages(lang):
        tt, P = B.UI[lang], B.PATHS[lang]
        st, ns = counts(lang)
        out = []
        for key, h, d in MAIN:
            desc = tt[d].format(**({**st, "n": ns[key]} if key in ns else st))
            out.append(f"- [{tt[h]}]({url(lang, P[key])}): {desc}")
        return out

    def fam_line(lang, f):
        T = L[lang]
        n = sum(1 for a in B.ARTISTS if a["family"] == f["id"])
        return (f"- [{t(f['name'], lang)}]({url(lang, B.PATHS[lang]['gdir'] + '/' + f['id'] + '.html')}): {t(f['blurb'], lang)} "
                f"({T['since']} {f['since']}; {len(f['subs'])} {T['subs']}; {n} {T['artists']})")

    # ── llms.txt (índice) ─────────────────────────────────────────────────────
    en, pt = B.UI["en"], B.UI["pt"]
    T = L["en"]
    st_en = B.seo_stats("en")
    idx = [f"# {en['site']} ({pt['site']})", "", "> " + en["homeDesc"].format(**st_en), "",
           T["intro"].format(site=en["site"], other=pt["site"], built=B.BUILT), "",
           f"## {T['full']}", "",
           f"- [{T['full_en']}]({B.SITE}/llms-full.txt): {T['full_en_d']}",
           f"- [{T['full_pt']}]({B.SITE}/pt/llms-full.txt): {T['full_pt_d']}", "",
           f"## {T['main']}", "", f"- [{en['site']}]({B.SITE}/): " + en["homeDesc"].format(**st_en)] + main_pages("en") + ["",
           f"## {T['fams']}", ""] + [fam_line("en", f) for f in C.FAMILIES] + ["",
           f"## {T['in_pt']}", "", f"- [{pt['site']}]({B.SITE}/pt/): " + pt["homeDesc"].format(**B.seo_stats("pt"))] + main_pages("pt") + ["",
           f"## {T['optional']}", "",
           f"- [{T['sitemap']}]({B.SITE}/sitemap.xml): {T['sitemap_d']}",
           f"- [{T['hub']}](https://biblioverse.org/llms.txt): {T['hub_d']}"]
    save(B.ROOT, "llms.txt", idx)

    # ── llms-full.txt por idioma ──────────────────────────────────────────────
    for lang in ("en", "pt"):
        T, tt = L[lang], B.UI[lang]
        oth = B.UI["pt" if lang == "en" else "en"]
        out = [f"# {tt['site']} ({oth['site']})", "", "> " + tt["homeDesc"].format(**B.seo_stats(lang)), "",
               T["intro"].format(site=tt["site"], other=oth["site"], built=B.BUILT), ""]

        def uf_name(uf):
            loc = IT.UF.get(uf)
            if not loc:
                return ""
            return re.sub(r"^d[oae]s? ", "", loc[0]) if lang == "pt" else re.sub(r"^the ", "", loc[1])

        # gêneros
        out += [f"## {T['genres_h']}", ""]
        for f in C.FAMILIES:
            out += [f"### [{t(f['name'], lang)}]({url(lang, B.PATHS[lang]['gdir'] + '/' + f['id'] + '.html')}) ({T['since']} {f['since']})", "",
                    t(f["blurb"], lang) + f" {T['where']}: {t(f['where'], lang)}.", ""]
            for s in f["subs"]:
                link = url(lang, B.PATHS[lang]['gdir'] + '/' + f['id'] + '.html') if s["id"] in IT.SAME_AS_FAMILY else IT.abs_url(lang, "s", s["id"])
                extra = [f"{T['since']} {s['since']}"]
                if s.get("fusion"):
                    extra.append(f"{T['fusion']}: {t(s['fusion'], lang)}")
                if s.get("heritage"):
                    extra.append(B.heritage_txt(s, lang))
                out.append(f"- [{t(s['name'], lang)}]({link}) ({'; '.join(extra)}): {t(s['blurb'], lang)}")
            out.append("")

        # artistas por família
        out += [f"## {T['artists_h']}", ""]
        for f in C.FAMILIES:
            arts = [a for a in B.ARTISTS if a["family"] == f["id"]]
            if not arts:
                continue
            out += [f"### {t(f['name'], lang)} ({len(arts)})", ""]
            for a in arts:
                bits = [tt["types"].get(a["type"], a["type"])]
                if a["uf"]:
                    bits.append(uf_name(a["uf"]))
                if a["year"]:
                    bits.append(f"{T['debut']} {a['year']}")
                bits.append(f"{T['tier']} {a['tier']} ({tt['tierNames'][a['tier']]})")
                subs = ", ".join(t(B.SUB[g]["name"], lang) for g in a["genres"])
                out.append(f"- [{a['name']}]({IT.abs_url(lang, 'a', a['id'])}): {' · '.join(x for x in bits if x)}. {subs}. {t(a['blurb'], lang)}".rstrip())
            out.append("")

        # pessoas
        def people(title, rows):
            res = [f"## {title} ({len(rows)})", ""]
            for row in rows:
                n, note = row[0], t((row[1], row[2]), lang)
                res.append(f"- [{n}]({IT.abs_url(lang, 'm', IT.slugify(n))})" + (f": {note}" if note else ""))
            return res + [""]

        out += people(T["singers_h"], B.VOC)[:-1]
        out += [f"- [{a['name']}]({IT.abs_url(lang, 'a', a['id'])})" for a in B.VOC_ART] + [""]
        out[out.index(f"## {T['singers_h']} ({len(B.VOC)})")] = f"## {T['singers_h']} ({len(B.VOC) + len(B.VOC_ART)})"
        out += [f"## {T['musicians_h']}", ""]
        for _c, key, rows, _f in B.INSTR:
            out += [f"### {tt[key]} ({len(rows)})", ""] + people(tt[key], rows)[2:]
        out += people(T["producers_h"], B.PROD)
        out += [f"## {T['influencers_h']} ({len(C.CREATORS)})", ""]
        out += [f"- [{n}]({IT.abs_url(lang, 'm', IT.slugify(n))})" + (f" (@{h})" if h else "") for n, h, _g in C.CREATORS] + [""]

        # músicas por década
        out += [f"## {T['songs_h']} ({len(B.SONGS)})", ""]
        dec = None
        for y, title, artist, fid in B.SONGS:
            if y // 10 * 10 != dec:
                dec = y // 10 * 10
                out += ["", f"### {T['decade'].format(d=dec)}", ""] if out[-1] else [f"### {T['decade'].format(d=dec)}", ""]
            fam = t(B.FAM[fid]["name"], lang) if fid in B.FAM else ""
            out.append(f"- {y} · {title} — {artist}" + (f" ({fam})" if fam else ""))
        out.append("")

        # discos
        out += [f"## {T['albums_h']} ({len(B.ALBUMS)})", ""]
        for y, al, ar, fid, npt, nen in B.ALBUMS:
            fam = t(B.FAM[fid]["name"], lang) if fid in B.FAM else ""
            note = t((npt, nen), lang)
            out.append(f"- {y} · {al} — {ar}" + (f" ({fam})" if fam else "") + (f": {note}" if note else ""))
        out.append("")

        # prêmios, festivais, programas
        out += [f"## {T['awards_h']}", ""]
        out += [f"- [{a['name']}]({IT.abs_url(lang, 'aw', a['slug'])}) ({T['since']} {a['since']}; {T['org']}: {t(a['org'], lang)}): {t(a['blurb'], lang)}" for a in C.AWARDS] + [""]
        out += [f"## {T['festivals_h']}", ""]
        out += [f"- [{x['name']}]({IT.abs_url(lang, 'fe', x['slug'])}) ({T['since']} {x['since']}; {T['city']}: {x['city']}): {t(x['blurb'], lang)}" for x in C.FESTIVALS] + [""]
        out += [f"## {T['shows_h']}", ""]
        for s in C.SHOWS:
            line = f"- [{s['name']}]({IT.abs_url(lang, 'sh', s['slug'])}) ({T['net']}: {s['net']}; {T['years']}: {s['years']}): {t(s['blurb'], lang)}"
            if s["alumni"]:
                line += f" {T['alumni'].capitalize()}: {', '.join(s['alumni'])}."
            out.append(line)
        out.append("")

        # instrumentos e glossário
        def instr(rows):
            return [f"- {t(i['name'], lang)} ({tt['kinds'][i['kind']]}; {T['used']}: {', '.join(t(B.FAM[g]['name'], lang) for g in i['genres'])}): {t(i['blurb'], lang)}" for i in rows]
        out += [f"## {T['instr_h']}", ""] + instr(C.INSTRUMENTS) + ["", f"### {T['instr_pop_h']}", ""] + instr(C.POP_INSTRUMENTS) + [""]
        out += [f"## {T['gloss_h']}", ""] + [f"- **{term}**: {t(d, lang)}" for term, d in sorted(C.GLOSSARY, key=lambda x: x[0].lower())] + [""]
        save(B.ROOT, "llms-full.txt" if lang == "en" else os.path.join("pt", "llms-full.txt"), out)


def save(root, rel, lines):
    txt = re.sub(r"\n{3,}", "\n\n", "\n".join(lines).strip() + "\n")
    with open(os.path.join(root, rel), "w", encoding="utf8", newline="\n") as f:
        f.write(txt)
