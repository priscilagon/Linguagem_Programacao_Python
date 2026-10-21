# Orientações para os desafios extras – Projeto 1

- **Nota detalhada:** crie `itens_compra = []` e, a cada produto, `itens_compra.append(f"{nome}: {quantidade:.2f} kg = R$ {valor:.2f}")`; ao final, percorra a lista com `for`.
- **Cupom:** `cupom = input("Cupom: ").strip().upper()`; se `cupom == "FEIRA10"`, `total = total * 0.90`.
- **Fechamento em arquivo:** `with open("fechamento.txt", "w", encoding="utf-8") as f:` e `f.write(...)` com clientes e total do dia.
