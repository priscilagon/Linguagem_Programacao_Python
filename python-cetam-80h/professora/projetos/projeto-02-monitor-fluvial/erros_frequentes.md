# Erros frequentes – Projeto 2

- **Inicializar `maior_subida` com o primeiro valor do nível** em vez de 0, ou comparar com `>=`, registrando subidas nulas.
- **Esquecer `float()`** na leitura, ou usar `int()` e rejeitar valores como 26,1.
- **Usar `range(12)` fixo** e quebrar se a lista mudar de tamanho: prefira `range(len(meses))`.
- **Não padronizar a consulta** (“jun” ≠ “Jun”).
- Confundir `index()` (posição) com o valor, ou chamar `niveis.index()` com o mês.
