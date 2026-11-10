"""Projeto 3 – Estoque da Cooperativa Ribeirinha (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
O estoque é um dicionário  {nome: {"preco": float, "qtd": int}}.
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""

MINIMO = 10  # RN06: estoque baixo = menos de 10 unidades


def estoque_inicial():
    """RF01: devolve um NOVO dicionário com os quatro produtos iniciais."""
    return {
        "Açaí": {"preco": 18.50, "qtd": 40},
        "Castanha": {"preco": 32.00, "qtd": 15},
        "Tapioca": {"preco": 12.00, "qtd": 8},
        "Cupuaçu": {"preco": 15.00, "qtd": 25},
    }


def padronizar_nome(nome):
    """RN01: strip() e title()  ('  AÇAÍ ' -> 'Açaí')."""
    # >>> SOLUCAO
    return nome.strip().title()
    # <<< SOLUCAO


def cadastrar_produto(estoque, nome, preco, qtd):
    """RF04, RN02 e RN03: cadastra o produto e retorna o nome padronizado.

    Erros (ValueError): nome vazio, produto repetido, preço <= 0, quantidade < 0.
    """
    # >>> SOLUCAO
    nome = padronizar_nome(nome)
    if nome == "":
        raise ValueError("O nome do produto não pode ser vazio.")
    if nome in estoque:
        raise ValueError(f"O produto {nome} já está cadastrado.")
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")
    if qtd < 0:
        raise ValueError("A quantidade inicial não pode ser negativa.")
    estoque[nome] = {"preco": preco, "qtd": qtd}
    return nome
    # <<< SOLUCAO


def vender(estoque, nome, qtd):
    """RF05 e RN04: baixa o estoque e devolve o valor da venda (preço × qtd, 2 casas).

    Erros: produto inexistente, qtd <= 0, qtd maior que o estoque disponível.
    """
    # >>> SOLUCAO
    nome = padronizar_nome(nome)
    if nome not in estoque:
        raise ValueError("Produto inexistente.")
    if qtd <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    if qtd > estoque[nome]["qtd"]:
        raise ValueError(f"Estoque insuficiente (disponível: {estoque[nome]['qtd']}).")
    estoque[nome]["qtd"] -= qtd
    return round(estoque[nome]["preco"] * qtd, 2)
    # <<< SOLUCAO


def repor(estoque, nome, qtd):
    """RF06 e RN05: soma qtd ao estoque. Erros: produto inexistente ou qtd <= 0."""
    # >>> SOLUCAO
    nome = padronizar_nome(nome)
    if nome not in estoque:
        raise ValueError("Produto inexistente.")
    if qtd <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    estoque[nome]["qtd"] += qtd
    # <<< SOLUCAO


def valor_total(estoque):
    """Soma de preço × quantidade de todos os produtos (2 casas)."""
    # >>> SOLUCAO
    return round(sum(d["preco"] * d["qtd"] for d in estoque.values()), 2)
    # <<< SOLUCAO


def estoque_baixo(estoque):
    """RN06: lista (em ordem alfabética) dos nomes com quantidade menor que MINIMO."""
    # >>> SOLUCAO
    return sorted(nome for nome, d in estoque.items() if d["qtd"] < MINIMO)
    # <<< SOLUCAO


def relatorio(estoque, total_vendido):
    """RF07: dicionário com 'produtos', 'valor_estoque', 'total_vendido', 'mais_caro' e 'baixo'.

    'mais_caro' é o nome do produto de maior preço ('' se o estoque estiver vazio).
    """
    # >>> SOLUCAO
    mais_caro = max(estoque, key=lambda n: estoque[n]["preco"]) if estoque else ""
    return {
        "produtos": len(estoque),
        "valor_estoque": valor_total(estoque),
        "total_vendido": round(total_vendido, 2),
        "mais_caro": mais_caro,
        "baixo": estoque_baixo(estoque),
    }
    # <<< SOLUCAO
