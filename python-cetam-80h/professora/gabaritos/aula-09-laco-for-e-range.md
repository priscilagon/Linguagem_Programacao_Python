# Gabarito – Aula 09: Laço for e range()

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Mostre a tabuada de um número lido (de 1 a 10).

```python
n = int(input("Tabuada de qual número? "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Saída esperada:**

```text
Tabuada de qual número? 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

> 📝 **Nota ao professor:** Erro comum: `range(1, 10)` (para no 9). O fim do `range` não é incluído.

## Atividade 2

> Some as diárias de 1 a `dias`, sendo que a diária do dia 1 é R$ 100 e aumenta R$ 20 por dia.

```python
dias = int(input("Dias: "))
diaria = 100
soma = 0

for dia in range(1, dias + 1):
    print(f"Dia {dia}: R$ {diaria:.2f}")
    soma += diaria
    diaria += 20

print(f"Soma das diárias: R$ {soma:.2f}")
```

**Saída esperada:**

```text
Dias: 3
Dia 1: R$ 100.00
Dia 2: R$ 120.00
Dia 3: R$ 140.00
Soma das diárias: R$ 360.00
```

## Atividade 3

> Faça uma contagem regressiva de 10 até 1 e, no final, mostre “Embarcar!”.

```python
for i in range(10, 0, -1):
    print(i)
print("Embarcar!")
```

**Saída esperada:**

```text
10
9
8
7
6
5
4
3
2
1
Embarcar!
```

## Desafio do projeto – Extrato da viagem

> Exibir o gasto de cada dia e o valor acumulado.

```python
dias = int(input("Dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))
acumulado = 0

for dia in range(1, dias + 1):
    acumulado += gasto_dia
    print(f"Dia {dia}: R$ {gasto_dia:.2f} | Acumulado: R$ {acumulado:.2f}")
```

**Saída esperada:**

```text
Dias: 3
Gasto por dia (R$): 330
Dia 1: R$ 330.00 | Acumulado: R$ 330.00
Dia 2: R$ 330.00 | Acumulado: R$ 660.00
Dia 3: R$ 330.00 | Acumulado: R$ 990.00
```

