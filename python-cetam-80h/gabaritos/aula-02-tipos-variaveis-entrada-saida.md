# Gabarito – Aula 02: Tipos de dados, variáveis, entrada e saída

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Crie um programa que receba nome, destino e dias de viagem e exiba a frase “Fulano viajará para X por Y dias.”

```python
nome = input("Nome do cliente: ")
destino = input("Destino: ")
dias = int(input("Dias de viagem: "))
print(f"{nome} viajará para {destino} por {dias} dias.")
```

**Saída esperada:**

```text
Nome do cliente: Marina
Destino: Presidente Figueiredo
Dias de viagem: 3
Marina viajará para Presidente Figueiredo por 3 dias.
```

> 📝 **Nota ao professor:** Verifique a conversão de `dias` com `int()`. Soluções com concatenação (`nome + " viajará..."`) também são válidas, desde que `dias` seja convertido com `str()`.

## Atividade 2

> Caça aos erros: (a) `dias = input("Dias: ") + 1`  (b) `1destino = "Parintins"`  (c) `print("Total: " + 150)`.

**(a)** `input()` devolve texto (`str`) e não é possível somar texto com número (**TypeError**). Correção: `dias = int(input("Dias: ")) + 1`.

**(b)** Nomes de variáveis não podem começar com número (**SyntaxError**). Correção: `destino1 = "Parintins"` (ou `destino_1`).

**(c)** Não se concatena texto com número (**TypeError**). Correções possíveis: `print("Total: " + str(150))` ou `print(f"Total: {150}")`.

