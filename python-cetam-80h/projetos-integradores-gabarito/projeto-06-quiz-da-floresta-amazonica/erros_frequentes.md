# Erros frequentes – Projeto 6

- **Não zerar** `pontos`**,** `acertos` **e** `seguidos` ao iniciar uma nova partida.
- **Usar** `or` **na validação** (`resposta != "A" or resposta != "B"` é sempre verdadeiro) em vez de `and`.
- **Não zerar** `seguidos` **depois do bônus** (o 4º acerto recebe bônus indevido) ou **não zerar após um erro**.
- **Esquecer** `.upper()`: a resposta “b” é considerada errada.
- Usar `range(5)` e exibir “Pergunta 0”, ou `range(1, 5)` e perder a última pergunta.
- Comparar `pontos > 50` em vez de `>= 50` no título.
