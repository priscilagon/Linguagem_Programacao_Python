"""Projeto 2 – Monitor Fluvial: Nível do Rio Negro (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""

MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]


def validar_nivel(nivel):
    """RN01: o nível deve estar entre 0 e 40 metros (inclusive). Retorna o nível."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def classificar(nivel):
    """RN02: 'Cheia' (>= 29), 'Enchente/Vazante' (>= 26 e < 29) ou 'Seca' (< 26)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def barra(nivel):
    """RN03: um '#' para cada metro inteiro (use int(nivel))."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def estatisticas(niveis):
    """RF02: retorna um dicionário com 'media', 'maior', 'mes_maior', 'menor' e 'mes_menor'.

    O nome do mês vem da lista MESES (mesma posição do nível).
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def contar_classificacoes(niveis):
    """RF04: dicionário contador {'Cheia': n, 'Enchente/Vazante': n, 'Seca': n}."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def maior_subida(niveis):
    """RF05 e RN05: retorna (valor, mes) da maior subida POSITIVA em relação ao mês anterior.

    Se nenhum mês subiu, retorne (0.0, "").
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def consultar_mes(texto, niveis):
    """RF06 e RN04: busca o mês ignorando maiúsculas/minúsculas e espaços.

    Retorna (mes, nivel, classificacao). Mês inexistente: ValueError("Mês não encontrado.").
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")
