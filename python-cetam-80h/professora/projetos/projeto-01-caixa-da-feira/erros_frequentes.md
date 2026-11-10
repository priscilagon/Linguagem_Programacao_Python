# Erros frequentes – Projeto 1

- **Não zerar `subtotal` e `itens` a cada cliente** (o segundo cliente herda os valores do primeiro).
- **Esquecer `float()`** em `quantidade` ou `recebido` (TypeError na comparação).
- **Usar `or` em vez de `and`** na validação da forma de pagamento (`forma != "1" or forma != "2"` é sempre verdadeiro).
- **Aplicar o desconto sobre o valor errado** (por exemplo, sobre o preço e não sobre o subtotal).
- Usar `if` em vez de `elif` nas faixas de desconto, aplicando a faixa errada.
