"""Signo do zodíaco a partir da data de nascimento.

Só o signo vai para dados/equipe.json; a data de nascimento nunca entra no repositório.
Uso: python3 signos.py 1990-07-31   ->  Leão
"""
import sys

# (mês, último dia do signo que começa no mês anterior, signo)
_LIMITES = [
    (1, 19, "Capricórnio", "Aquário"), (2, 18, "Aquário", "Peixes"), (3, 20, "Peixes", "Áries"),
    (4, 19, "Áries", "Touro"), (5, 20, "Touro", "Gêmeos"), (6, 20, "Gêmeos", "Câncer"),
    (7, 22, "Câncer", "Leão"), (8, 22, "Leão", "Virgem"), (9, 22, "Virgem", "Libra"),
    (10, 22, "Libra", "Escorpião"), (11, 21, "Escorpião", "Sagitário"), (12, 21, "Sagitário", "Capricórnio"),
]


def signo(data_iso):
    """Recebe 'AAAA-MM-DD' e devolve o nome do signo, ou None se a data estiver vazia."""
    if not data_iso:
        return None
    _, m, d = (int(x) for x in data_iso[:10].split("-"))
    _, corte, antes, depois = _LIMITES[m - 1]
    return antes if d <= corte else depois


if __name__ == "__main__":
    print(signo(sys.argv[1]))
