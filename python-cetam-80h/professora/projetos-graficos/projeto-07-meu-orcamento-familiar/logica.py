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
    # >>> SOLUCAO
    descricao = descricao.strip().capitalize()
    if descricao == "":
        raise ValueError("A descrição não pode ser vazia.")
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    if tipo == "receita":
        categoria = "Receita"
    else:
        if numero_categoria is None or numero_categoria < 1 or numero_categoria > len(CATEGORIAS):
            raise ValueError("Escolha uma categoria de 1 a 6.")
        categoria = CATEGORIAS[numero_categoria - 1]
    return {"tipo": tipo, "descricao": descricao, "categoria": categoria, "valor": valor}
    # <<< SOLUCAO


def totais(lancamentos):
    """RF04: retorna (receitas, despesas, saldo) — somas arredondadas em 2 casas."""
    # >>> SOLUCAO
    receitas = sum(l["valor"] for l in lancamentos if l["tipo"] == "receita")
    despesas = sum(l["valor"] for l in lancamentos if l["tipo"] == "despesa")
    return round(receitas, 2), round(despesas, 2), round(receitas - despesas, 2)
    # <<< SOLUCAO


def percentual_comprometido(receitas, despesas):
    """RN04 e RN05: despesas ÷ receitas × 100. Sem receitas (0), retorna None (sem dividir por zero)."""
    # >>> SOLUCAO
    if receitas == 0:
        return None
    return despesas / receitas * 100
    # <<< SOLUCAO


def situacao_orcamento(percentual):
    """RN04: até 70 -> 'Saudável'; acima de 70 até 100 -> 'Atenção – despesas altas';
    acima de 100 -> 'Alerta – despesas maiores que a receita'.

    percentual None (sem receitas): 'Registre ao menos uma receita para analisar o orçamento.'
    """
    # >>> SOLUCAO
    if percentual is None:
        return "Registre ao menos uma receita para analisar o orçamento."
    if percentual <= 70:
        return "Saudável"
    if percentual <= 100:
        return "Atenção – despesas altas"
    return "Alerta – despesas maiores que a receita"
    # <<< SOLUCAO


def despesas_por_categoria(lancamentos):
    """RF05: dicionário {categoria: total} só com as categorias que têm despesas (ordem de CATEGORIAS)."""
    # >>> SOLUCAO
    totais_cat = {nome: 0.0 for nome in CATEGORIAS}
    for l in lancamentos:
        if l["tipo"] == "despesa":
            totais_cat[l["categoria"]] += l["valor"]
    return {nome: round(v, 2) for nome, v in totais_cat.items() if v > 0}
    # <<< SOLUCAO


def categoria_maior_gasto(por_categoria):
    """RF05: retorna (categoria, total) do maior gasto. Dicionário vazio: ('', 0.0)."""
    # >>> SOLUCAO
    maior_valor = 0.0
    maior_categoria = ""
    for nome, valor in por_categoria.items():
        if valor > maior_valor:
            maior_valor = valor
            maior_categoria = nome
    return maior_categoria, maior_valor
    # <<< SOLUCAO


def percentuais_por_categoria(por_categoria):
    """RF05: {categoria: % do total de despesas}. Dicionário vazio -> {}."""
    # >>> SOLUCAO
    total = sum(por_categoria.values())
    if total == 0:
        return {}
    return {nome: valor / total * 100 for nome, valor in por_categoria.items()}
    # <<< SOLUCAO
