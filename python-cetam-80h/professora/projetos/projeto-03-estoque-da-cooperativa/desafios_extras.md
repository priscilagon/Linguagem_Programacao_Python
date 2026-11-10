# Orientações para os desafios extras – Projeto 3

- **Preço promocional:** em `vender()`, `if qtd >= 10: valor = valor * 0.95`.
- **Persistência:** gravar uma linha `nome;preco;qtd` por produto (modo `"w"`) e recarregar com `split(";")`, convertendo preço para `float` e quantidade para `int`.
- **Histórico:** `historico = []` e `historico.append(f"{qtd} x {nome} = R$ {valor:.2f}")` a cada venda.
