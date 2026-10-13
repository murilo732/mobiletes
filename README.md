# Mapa da Equipe Mobi

Mapa interativo de onde moram os colaboradores ativos da Mobi. Publicado via GitHub Pages e embedado no Notion.

## Atualização semanal (toda segunda)

1. Ler a base **💵 Fin Mobi** (`appi3j4m3s7i41R5B`), tabela **👩🏻‍💻 Colaboradores** (`tblI5ylai9O8vuCzc`).
   Campos: `Status` (`fldmcW6BKkvvMyEQI`), `Fname` (`fldduDYDMVgmKK9Kf`), `Emoji Text` (`fldWbwUe0KPERxtZW`),
   `Endereço - Município` (`fldPqDnvKcyXtIiWZ`, vínculo com nome "Cidade - UF"), `Data de Nascimento` (`fldPaVSRHaf3SQ4y3`).
2. Manter só `Status = Ativo` **com** município preenchido. Ignorar Desligado, Inativo e Frila Externo.
3. Reescrever `dados/equipe.json` com `{"emoji", "nome" (Fname, sem espaços sobrando), "cidade", "uf", "signo"}`.
   O signo sai de `signos.signo("AAAA-MM-DD")`. **A data de nascimento nunca vai para o repositório**, só o signo.
   Sem data cadastrada, omitir `signo`.
4. Rodar `python3 build.py`. Se ele listar cidades sem coordenada, acrescentar `"Cidade - UF": [lat, lon]`
   (centro do município) em `dados/cidades.json` e rodar de novo.
5. Commit e push na branch `main` só se `dados/` ou `index.html` mudaram.

Nada de sobrenome, endereço ou outros dados pessoais no repositório: o site é público para quem tiver o link.
