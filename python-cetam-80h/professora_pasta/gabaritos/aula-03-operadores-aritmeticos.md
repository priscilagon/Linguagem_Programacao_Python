# Gabarito – Aula 03: Operadores aritméticos

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Leia três notas e mostre a média.

```python
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3) / 3
print(f"Média: {media:.2f}")
```

**Saída esperada:**

```text
Nota 1: 8
Nota 2: 7
Nota 3: 9
Média: 8.00
```

> 📝 **Nota ao professor:** Erro típico: escrever `n1 + n2 + n3 / 3` sem parênteses (a divisão é feita antes da soma).

## Atividade 2

> Leia o valor de uma compra e o valor pago e calcule o troco.

```python
compra = float(input("Valor da compra (R$): "))
pago = float(input("Valor pago (R$): "))
troco = pago - compra
print(f"Troco: R$ {troco:.2f}")
```

**Saída esperada:**

```text
Valor da compra (R$): 87.5
Valor pago (R$): 100
Troco: R$ 12.50
```

## Atividade 3

> Com orçamento de R$ 1.000,00 e diária de R$ 330,00, mostre quantos dias inteiros cabem no orçamento e quanto sobra.

```python
orcamento = 1000
diaria = 330
dias_inteiros = orcamento // diaria
sobra = orcamento % diaria
print(f"Dias inteiros: {dias_inteiros}")
print(f"Sobra: R$ {sobra:.2f}")
```

**Saída esperada:**

```text
Dias inteiros: 3
Sobra: R$ 10.00
```

## Atividade 4

> Sem executar, calcule `2 + 3 * 4 ** 2`.

**50.** Primeiro a potência (`4 ** 2 = 16`), depois a multiplicação (`3 * 16 = 48`) e por fim a soma (`2 + 48 = 50`).

## Desafio do projeto – Custo total da viagem

> Peça dias, hospedagem, transporte e alimentação por dia; mostre o gasto diário e o total.

```python
dias = int(input("Quantidade de dias: "))
hospedagem = float(input("Hospedagem por dia (R$): "))
transporte = float(input("Transporte por dia (R$): "))
alimentacao = float(input("Alimentação por dia (R$): "))

gasto_dia = hospedagem + transporte + alimentacao
total = dias * gasto_dia

print(f"Gasto por dia: R$ {gasto_dia:.2f}")
print(f"Total da viagem: R$ {total:.2f}")
```

**Saída esperada:**

```text
Quantidade de dias: 3
Hospedagem por dia (R$): 200
Transporte por dia (R$): 50
Alimentação por dia (R$): 80
Gasto por dia: R$ 330.00
Total da viagem: R$ 990.00
```

