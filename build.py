#!/usr/bin/env python3
"""Gera index.html do Mapa da Equipe Mobi.

Entradas:
  dados/equipe.json   lista de {"emoji", "nome", "cidade", "uf"} (colaboradores ativos)
  dados/cidades.json  {"Cidade - UF": [lat, lon]}  (cache de coordenadas)
  base/mapa-brasil.json  contornos dos estados já projetados
  template.html

Uso: python3 build.py [AAAA-MM-DD]
Sai com erro (código 2) listando as cidades sem coordenada em dados/cidades.json.
"""
import json, math, os, sys, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: json.load(open(os.path.join(ROOT, p), encoding="utf-8"))

equipe = rd("dados/equipe.json")
cidades = rd("dados/cidades.json")
base = rd("base/mapa-brasil.json")
pj = base["proj"]
kx = math.cos(math.radians(pj["lat_ref"]))

def proj(lat, lon):
    return round((lon - pj["lon0"]) * pj["k"] * kx, 1), round((pj["lat0"] - lat) * pj["k"], 1)

faltando = sorted({f'{p["cidade"]} - {p["uf"]}' for p in equipe} - set(cidades))
if faltando:
    print("Cidades sem coordenada em dados/cidades.json:", *faltando, sep="\n  ")
    sys.exit(2)

ppl = []
for p in equipe:
    x, y = proj(*cidades[f'{p["cidade"]} - {p["uf"]}'])
    ppl.append({"e": p["emoji"] or "🙂", "n": p["nome"], "c": p["cidade"], "uf": p["uf"], "x": x, "y": y, "s": p.get("signo")})

data = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
data_br = "/".join(reversed(data.split("-")))

svg = '<svg id="land" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg"><g id="g">%s</g></svg>' % (
    base["w"], base["h"], "".join('<path d="%s"/>' % d for d in base["paths"] if d))
html = (open(os.path.join(ROOT, "template.html"), encoding="utf-8").read()
        .replace("%%SVG%%", svg)
        .replace("%%DATA%%", json.dumps({"w": base["w"], "h": base["h"], "p": ppl}, ensure_ascii=False))
        .replace("%%N%%", str(len(ppl)))
        .replace("%%C%%", str(len({(p["c"], p["uf"]) for p in ppl})))
        .replace("%%U%%", str(len({p["uf"] for p in ppl})))
        .replace("%%ATUALIZADO%%", data_br))
open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
    "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"robots\" content=\"noindex, nofollow\">\n"
    "<style>body{margin:0}[hidden]{display:none!important}img{max-width:100%}</style>\n</head>\n<body>\n" + html + "\n</body>\n</html>\n")
print(f"index.html gerado: {len(ppl)} pessoas, atualizado em {data_br}")
