"""Projeto 1 – Caixa da Feira do Produtor (regras de negócio).

Esta é a PARTE LÓGICA: nenhuma função aqui usa print() ou input().
A tela (app.py) já está pronta e chama estas funções.
Quando uma regra for violada, gere  raise ValueError("mensagem para o usuário").

Teste seu trabalho com:   python -m unittest -v testes_logica.py
Abra a tela com:          python app.py
"""

PRODUTOS = {
    1: ("Tambaqui", 28.00),
    2: ("Pirarucu", 45.00),
    3: ("Tucunaré", 32.00),
    4: ("Farinha de mandioca", 9.00),
}


def validar_quantidade(qtd):
    """RN01: a quantidade em kg deve ser maior que zero. Retorna a quantidade."""
    # >>> SOLUCAO
    if qtd <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    return qtd
    # <<< SOLUCAO


def valor_item(preco, qtd):
    """RF02: valor da linha = preço × quantidade, arredondado em 2 casas."""
    # >>> SOLUCAO
    return round(preco * qtd, 2)
    # <<< SOLUCAO


def percentual_desconto(subtotal):
    """RN02 e RN03: 0 (abaixo de 100), 5 (de 100 a menos de 200) ou 10 (200 ou mais)."""
    # >>> SOLUCAO
    if subtotal >= 200:
        return 10
    if subtotal >= 100:
        return 5
    return 0
    # <<< SOLUCAO


def calcular_resumo(itens):
    """RF03–RF05: recebe a lista de itens [(produto, qtd, preco), ...].

    RN05: sem itens, gere ValueError("Registre ao menos um item.").
    Retorna um dicionário com as chaves:
    'itens', 'subtotal', 'percentual', 'desconto' e 'total'.
    """
    # >>> SOLUCAO
    if not itens:
        raise ValueError("Registre ao menos um item.")
    subtotal = round(sum(valor_item(preco, qtd) for _, qtd, preco in itens), 2)
    percentual = percentual_desconto(subtotal)
    desconto = round(subtotal * percentual / 100, 2)
    return {
        "itens": len(itens),
        "subtotal": subtotal,
        "percentual": percentual,
        "desconto": desconto,
        "total": round(subtotal - desconto, 2),
    }
    # <<< SOLUCAO


def calcular_troco(total, recebido):
    """RF06 e RN06: troco do pagamento em dinheiro.

    Se recebido < total, gere ValueError(f"Faltam R$ {falta:.2f}.") com a diferença.
    """
    # >>> SOLUCAO
    if recebido < total:
        raise ValueError(f"Faltam R$ {total - recebido:.2f}.")
    return round(recebido - total, 2)
    # <<< SOLUCAO


def fechamento(vendas):
    """RF08: recebe a lista de totais pagos [12.5, 80.0, ...].

    Retorna (clientes_atendidos, total_vendido).
    """
    # >>> SOLUCAO
    return len(vendas), round(sum(vendas), 2)
    # <<< SOLUCAO
