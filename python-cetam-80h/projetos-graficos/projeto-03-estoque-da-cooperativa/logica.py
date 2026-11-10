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
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def cadastrar_produto(estoque, nome, preco, qtd):
    """RF04, RN02 e RN03: cadastra o produto e retorna o nome padronizado.

    Erros (ValueError): nome vazio, produto repetido, preço <= 0, quantidade < 0.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def vender(estoque, nome, qtd):
    """RF05 e RN04: baixa o estoque e devolve o valor da venda (preço × qtd, 2 casas).

    Erros: produto inexistente, qtd <= 0, qtd maior que o estoque disponível.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def repor(estoque, nome, qtd):
    """RF06 e RN05: soma qtd ao estoque. Erros: produto inexistente ou qtd <= 0."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def valor_total(estoque):
    """Soma de preço × quantidade de todos os produtos (2 casas)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def estoque_baixo(estoque):
    """RN06: lista (em ordem alfabética) dos nomes com quantidade menor que MINIMO."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def relatorio(estoque, total_vendido):
    """RF07: dicionário com 'produtos', 'valor_estoque', 'total_vendido', 'mais_caro' e 'baixo'.

    'mais_caro' é o nome do produto de maior preço ('' se o estoque estiver vazio).
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")
