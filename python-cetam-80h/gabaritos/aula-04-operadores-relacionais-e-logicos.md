# Gabarito – Aula 04: Operadores relacionais e lógicos; estrutura de um algoritmo

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Sendo `tem_orcamento = True` e `tem_vaga = False`, qual o resultado de `tem_orcamento and tem_vaga`, `tem_orcamento or tem_vaga` e `not tem_vaga`?

```python
tem_orcamento = True
tem_vaga = False
print(tem_orcamento and tem_vaga)
print(tem_orcamento or tem_vaga)
print(not tem_vaga)
```

**Saída esperada:**

```text
False
True
True
```

> 📝 **Nota ao professor:** Resultado: `False`, `True` e `True`. O `and` exige as duas condições verdadeiras; o `or` basta uma.

## Atividade 2

> Escreva uma expressão que seja verdadeira quando `dias` estiver entre 1 e 30.

`1 <= dias <= 30`, ou, de forma equivalente, `dias >= 1 and dias <= 30`.

```python
dias = int(input("Dias: "))
print(1 <= dias <= 30)
```

**Saída esperada – dias = 15:**

```text
Dias: 15
True
```

**Saída esperada – dias = 45:**

```text
Dias: 45
False
```

## Desafio do projeto – Entrega da Fase 1 – Calculadora de viagem v1

> Programa completo com entrada, processamento e saída.

```python
# Agência Amazônia Tur Digital - Calculadora de viagem v1

# ----- ENTRADA -----
print("=== Agência Amazônia Tur Digital ===")
nome = input("Nome do cliente: ")
destino = input("Destino: ")
dias = int(input("Quantidade de dias: "))
hospedagem = float(input("Hospedagem por dia (R$): "))
transporte = float(input("Transporte por dia (R$): "))
alimentacao = float(input("Alimentação por dia (R$): "))

# ----- PROCESSAMENTO -----
gasto_dia = hospedagem + transporte + alimentacao
total = dias * gasto_dia

# ----- SAÍDA -----
print()
print(f"Cliente: {nome}")
print(f"Destino: {destino}")
print(f"Gasto por dia: R$ {gasto_dia:.2f}")
print(f"Total da viagem ({dias} dias): R$ {total:.2f}")
```

**Saída esperada:**

```text
=== Agência Amazônia Tur Digital ===
Nome do cliente: Marina
Destino: Parintins
Quantidade de dias: 3
Hospedagem por dia (R$): 200
Transporte por dia (R$): 50
Alimentação por dia (R$): 80

Cliente: Marina
Destino: Parintins
Gasto por dia: R$ 330.00
Total da viagem (3 dias): R$ 990.00
```

> 📝 **Nota ao professor:** Na revisão cruzada, observe: o programa roda? Os nomes são claros? Há comentários? Os tipos foram convertidos (`int` e `float`)?

