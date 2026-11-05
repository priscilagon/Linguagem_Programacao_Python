# Erros frequentes – Projeto 8

- **Descontar vida de letra repetida** por não verificar a lista de tentadas.
- **Esquecer** `.lower()`: “A” e “a” são tratados como letras diferentes.
- **Não validar o tamanho** (aceitar “ab” ou texto vazio) ou aceitar números e símbolos (`isalpha`).
- **Esquecer o** `return` **em** `venceu` ou colocar `return True` dentro do `for` (a função encerra na primeira letra).
- **Usar** `acertadas` **global** em vez de recebê-la por parâmetro: a lista “vaza” entre rodadas.
- **Posição incorreta na rodada**: sem `% len(PALAVRAS)` ocorre IndexError na 7ª rodada.
