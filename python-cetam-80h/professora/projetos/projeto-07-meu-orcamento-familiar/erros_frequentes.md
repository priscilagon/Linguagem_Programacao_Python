# Erros frequentes – Projeto 7

- **Dividir por** `receitas` **sem testar se é zero** (ZeroDivisionError).
- **Usar** `categorias[numero]` **em vez de** `categorias[numero - 1]` (a lista começa em 0).
- **Esquecer de zerar o dicionário de totais** a cada consulta, acumulando valores repetidos.
- **Somar receitas nas categorias de despesa** por não filtrar por `tipo`.
- **Comparar** `percentual < 70` quando o limite é inclusivo (`<= 70`).
- Usar o mesmo nome (`valor`) para variáveis diferentes dentro do mesmo laço, sobrescrevendo dados.
