# -*- coding: utf-8 -*-
"""Resolve o artigo certo da Wikipedia (pt e en) para artistas, instrumentistas, programas, prêmios e festivais.
Testa o nome puro e variantes com qualificador ("(banda)", "(cantor)"...) e só aceita a página cuja descrição
(Wikidata) seja de música/TV/prêmio e que não seja desambiguação. Resultado em tools/wiki_links.json.
Uso: python tools/fetch_wiki.py   (rode de novo quando entrarem nomes novos; o build usa o JSON)"""
import json, os, re, sys, time, types, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "wiki_links.json")
UA = "BrazilianMusicCatalogue/1.0 (https://brazilianmusic.biblioverse.org)"

QUAL = {
    "pt": dict(group=["(banda)", "(grupo)", "(grupo musical)", "(dupla)", "(banda brasileira)"], person=["(cantor)", "(cantora)", "(músico)", "(rapper)", "(DJ)", "(compositor)"],
               musician=["(músico)", "(guitarrista)", "(baixista)", "(baterista)", "(produtor musical)", "(cantor)"], show=["(programa de televisão)", "(Brasil)", "(programa)"],
               award=["(prêmio)", "(premiação)"], fest=["(festival)", "(Brasil)"]),
    "en": dict(group=["(band)", "(Brazilian band)", "(group)", "(duo)", "(musical group)"], person=["(singer)", "(musician)", "(rapper)", "(DJ)", "(Brazilian singer)", "(composer)"],
               musician=["(musician)", "(guitarist)", "(bassist)", "(drummer)", "(record producer)", "(Brazilian musician)"], show=["(Brazilian TV series)", "(TV series)", "(Brazil)"],
               award=["(award)", "(awards)"], fest=["(festival)", "(Brazil)"]),
}
OK = {
    "pt": re.compile(r"banda|cantor|cantora|músic|music|grupo|dupla|rapper|compositor|compositora|\bdj\b|guitarr|baixista|baterista|produtor|produtora|sambista|"
                     r"instrumentista|conjunto|orquestra|pianista|violonista|percussionista|\bmc\b|trio|coral|vocal|festival|programa|reality|televis|prêmio|premiação|carnaval|maestr|regente", re.I),
    "en": re.compile(r"band|singer|musician|music|rapper|duo|group|songwriter|\bdj\b|guitarist|bassist|drummer|producer|composer|pianist|percussionist|\bmc\b|trio|"
                     r"choir|vocal|orchestra|festival|television|tv series|show|award|carnival|conductor|rodeo|parade|samba school", re.I),
}


def api(lang, titles):
    q = urllib.parse.urlencode({"action": "query", "format": "json", "redirects": 1, "prop": "description|pageprops", "ppprop": "disambiguation", "titles": "|".join(titles)})
    req = urllib.request.Request(f"https://{lang}.wikipedia.org/w/api.php?{q}", headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as ex:  # rede instável: tenta de novo
            time.sleep(2 + attempt * 3)
            err = ex
    raise err


def resolve(lang, items):
    """items: lista de (key, name, kind). Devolve {key: título}."""
    cands = {}
    for key, name, kind in items:
        cands[key] = [name] + [f"{name} {q}" for q in QUAL[lang][kind]]
    all_titles = sorted({c for v in cands.values() for c in v})
    info = {}
    for i in range(0, len(all_titles), 50):
        chunk = all_titles[i:i + 50]
        data = api(lang, chunk).get("query", {})
        norm = {n["from"]: n["to"] for n in data.get("normalized", [])}
        redir = {r["from"]: r["to"] for r in data.get("redirects", [])}
        pages = {p["title"]: p for p in data.get("pages", {}).values()}
        for t in chunk:
            final = norm.get(t, t)
            final = redir.get(final, final)
            p = pages.get(final)
            if not p or "missing" in p or "invalid" in p:
                continue
            if "disambiguation" in p.get("pageprops", {}):
                continue
            info[t] = (p["title"], p.get("description", ""))
        time.sleep(.3)
        sys.stdout.write(f"\r{lang}: {min(i + 50, len(all_titles))}/{len(all_titles)}"); sys.stdout.flush()
    print()
    # sem descrição no Wikidata: usa as primeiras frases do artigo
    empty = sorted({info[c][0] for c in info if not info[c][1]})
    intro = {}
    for i in range(0, len(empty), 20):
        chunk = empty[i:i + 20]
        q = urllib.parse.urlencode({"action": "query", "format": "json", "prop": "extracts", "exintro": 1, "explaintext": 1, "exsentences": 2, "exlimit": 20, "titles": "|".join(chunk)})
        req = urllib.request.Request(f"https://{lang}.wikipedia.org/w/api.php?{q}", headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                for pg in json.load(r).get("query", {}).get("pages", {}).values():
                    intro[pg.get("title")] = pg.get("extract", "")[:400]
        except Exception:
            pass
        time.sleep(.3)
    for c, (title, desc) in list(info.items()):
        if not desc and title in intro:
            info[c] = (title, intro[title])
    out = {}
    for key, name, kind in items:
        for c in cands[key]:
            if c in info and (kind in ("show", "award", "fest") and c == name or OK[lang].search(info[c][1] or "")):
                out[key] = info[c][0]
                break
    return out


def main():
    src = open(os.path.join(HERE, "build.py"), encoding="utf8").read().replace('if __name__ == "__main__":\n    main()', "")
    B = types.ModuleType("b"); B.__file__ = os.path.join(HERE, "build.py")
    sys.path.insert(0, HERE)
    exec(compile(src, "build.py", "exec"), B.__dict__)
    import items as IT
    IT.setup(B)
    items = []
    for a in B.ARTISTS:
        items.append(("a:" + a["id"], a["name"], "group" if a["type"] in ("band", "group", "duo", "collective") else "person"))
    for m in IT.MUS_LIST:
        items.append(("m:" + m["slug"], m["name"], "musician"))
    for s in B.C.SHOWS:
        items.append(("sh:" + s["slug"], s["name"], "show"))
    for a in B.C.AWARDS:
        items.append(("aw:" + a["slug"], a["name"].split(" / ")[0], "award"))
    for f in B.C.FESTIVALS:
        items.append(("fe:" + f["slug"], f["name"], "fest"))
    res = {}
    for lang in ("pt", "en"):
        res[lang] = resolve(lang, items)
        print(f"{lang}: {len(res[lang])}/{len(items)} resolvidos")
    json.dump(res, open(OUT, "w", encoding="utf8"), ensure_ascii=False, indent=0, sort_keys=True)
    print("ok ->", OUT)


if __name__ == "__main__":
    main()
