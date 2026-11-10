# Gabarito – Aula 08: Laço while

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Peça uma nota entre 0 e 10 e repita a pergunta até o valor ser válido.

```python
nota = float(input("Nota (0 a 10): "))
while nota < 0 or nota > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota = float(input("Nota (0 a 10): "))
print(f"Nota registrada: {nota}")
```

**Saída esperada:**

```text
Nota (0 a 10): 11
Nota inválida! Digite um valor entre 0 e 10.
Nota (0 a 10): -2
Nota inválida! Digite um valor entre 0 e 10.
Nota (0 a 10): 8.5
Nota registrada: 8.5
```

> 📝 **Nota ao professor:** O operador deve ser `or` na condição de invalidez. Com `and`, a condição nunca seria verdadeira.

## Atividade 2

> Some gastos digitados pelo usuário até que ele digite 0.

```python
soma = 0
gasto = float(input("Gasto (0 para encerrar): "))
while gasto != 0:
    soma += gasto
    gasto = float(input("Gasto (0 para encerrar): "))
print(f"Total dos gastos: R$ {soma:.2f}")
```

**Saída esperada:**

```text
Gasto (0 para encerrar): 330
Gasto (0 para encerrar): 200
Gasto (0 para encerrar): 150.5
Gasto (0 para encerrar): 0
Total dos gastos: R$ 680.50
```

## Desafio do projeto – Várias viagens em sequência

> Repetir o cálculo, perguntando “Deseja continuar? (s/n)”, com validação dos dias (1 a 30).

```python
continuar = "s"
while continuar == "s":
    dias = int(input("Dias de viagem (1 a 30): "))
    while dias < 1 or dias > 30:
        print("Valor inválido! Digite de 1 a 30.")
        dias = int(input("Dias de viagem (1 a 30): "))
    gasto_dia = float(input("Gasto por dia (R$): "))
    print(f"Total: R$ {dias * gasto_dia:.2f}")
    continuar = input("Deseja continuar? (s/n): ").lower()
print("Obrigado por usar a calculadora!")
```

**Saída esperada:**

```text
Dias de viagem (1 a 30): 40
Valor inválido! Digite de 1 a 30.
Dias de viagem (1 a 30): 3
Gasto por dia (R$): 330
Total: R$ 990.00
Deseja continuar? (s/n): s
Dias de viagem (1 a 30): 2
Gasto por dia (R$): 200
Total: R$ 400.00
Deseja continuar? (s/n): n
Obrigado por usar a calculadora!
```

