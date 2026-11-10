"""Projeto 7 – Meu Orçamento Familiar (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Cada lançamento é um dicionário:
    {"tipo": "receita" ou "despesa", "descricao": str, "categoria": str, "valor": float}
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""

CATEGORIAS = ["Moradia", "Alimentação", "Transporte", "Saúde", "Lazer", "Outros"]


def novo_lancamento(tipo, descricao, valor, numero_categoria=None):
    """RF02, RF03, RN01, RN02 e RN03: valida e devolve o dicionário do lançamento.

    - descricao: strip() + capitalize(); não pode ser vazia.
    - valor: maior que zero.
    - despesa: numero_categoria de 1 a 6 (posição em CATEGORIAS, começando em 1).
    - receita: a categoria é sempre "Receita".
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def totais(lancamentos):
    """RF04: retorna (receitas, despesas, saldo) — somas arredondadas em 2 casas."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def percentual_comprometido(receitas, despesas):
    """RN04 e RN05: despesas ÷ receitas × 100. Sem receitas (0), retorna None (sem dividir por zero)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def situacao_orcamento(percentual):
    """RN04: até 70 -> 'Saudável'; acima de 70 até 100 -> 'Atenção – despesas altas';
    acima de 100 -> 'Alerta – despesas maiores que a receita'.

    percentual None (sem receitas): 'Registre ao menos uma receita para analisar o orçamento.'
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def despesas_por_categoria(lancamentos):
    """RF05: dicionário {categoria: total} só com as categorias que têm despesas (ordem de CATEGORIAS)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def categoria_maior_gasto(por_categoria):
    """RF05: retorna (categoria, total) do maior gasto. Dicionário vazio: ('', 0.0)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def percentuais_por_categoria(por_categoria):
    """RF05: {categoria: % do total de despesas}. Dicionário vazio -> {}."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")
