"""Projeto 2 – Monitor Fluvial: Nível do Rio Negro (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""

MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]


def validar_nivel(nivel):
    """RN01: o nível deve estar entre 0 e 40 metros (inclusive). Retorna o nível."""
    # >>> SOLUCAO
    if nivel < 0 or nivel > 40:
        raise ValueError("Valor inválido! Digite entre 0 e 40 metros.")
    return nivel
    # <<< SOLUCAO


def classificar(nivel):
    """RN02: 'Cheia' (>= 29), 'Enchente/Vazante' (>= 26 e < 29) ou 'Seca' (< 26)."""
    # >>> SOLUCAO
    if nivel >= 29:
        return "Cheia"
    if nivel >= 26:
        return "Enchente/Vazante"
    return "Seca"
    # <<< SOLUCAO


def barra(nivel):
    """RN03: um '#' para cada metro inteiro (use int(nivel))."""
    # >>> SOLUCAO
    return "#" * int(nivel)
    # <<< SOLUCAO


def estatisticas(niveis):
    """RF02: retorna um dicionário com 'media', 'maior', 'mes_maior', 'menor' e 'mes_menor'.

    O nome do mês vem da lista MESES (mesma posição do nível).
    """
    # >>> SOLUCAO
    maior = max(niveis)
    menor = min(niveis)
    return {
        "media": sum(niveis) / len(niveis),
        "maior": maior,
        "mes_maior": MESES[niveis.index(maior)],
        "menor": menor,
        "mes_menor": MESES[niveis.index(menor)],
    }
    # <<< SOLUCAO


def contar_classificacoes(niveis):
    """RF04: dicionário contador {'Cheia': n, 'Enchente/Vazante': n, 'Seca': n}."""
    # >>> SOLUCAO
    contagem = {"Cheia": 0, "Enchente/Vazante": 0, "Seca": 0}
    for nivel in niveis:
        contagem[classificar(nivel)] += 1
    return contagem
    # <<< SOLUCAO


def maior_subida(niveis):
    """RF05 e RN05: retorna (valor, mes) da maior subida POSITIVA em relação ao mês anterior.

    Se nenhum mês subiu, retorne (0.0, "").
    """
    # >>> SOLUCAO
    melhor = 0.0
    mes = ""
    for i in range(1, len(niveis)):
        variacao = niveis[i] - niveis[i - 1]
        if variacao > melhor:
            melhor = variacao
            mes = MESES[i]
    return round(melhor, 2), mes
    # <<< SOLUCAO


def consultar_mes(texto, niveis):
    """RF06 e RN04: busca o mês ignorando maiúsculas/minúsculas e espaços.

    Retorna (mes, nivel, classificacao). Mês inexistente: ValueError("Mês não encontrado.").
    """
    # >>> SOLUCAO
    mes = texto.strip().title()
    if mes not in MESES:
        raise ValueError("Mês não encontrado.")
    i = MESES.index(mes)
    return mes, niveis[i], classificar(niveis[i])
    # <<< SOLUCAO
