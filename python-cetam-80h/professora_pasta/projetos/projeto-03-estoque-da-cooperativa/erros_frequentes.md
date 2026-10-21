# Erros frequentes – Projeto 3

- **Esquecer o `return` em `vender()`** e tentar somar `None` ao total (TypeError).
- **Usar `estoque[nome]` sem verificar `nome in estoque`** (KeyError).
- **Baixar o estoque antes de validar a quantidade**, deixando-o negativo.
- **Não padronizar o nome** (“açaí” ≠ “Açaí”) e não encontrar produtos existentes.
- **Modificar a lista ou o dicionário dentro de um `for` sobre ele mesmo** em extensões do projeto.
- Colocar o `print` no lugar do `return` e perder o valor da venda.
