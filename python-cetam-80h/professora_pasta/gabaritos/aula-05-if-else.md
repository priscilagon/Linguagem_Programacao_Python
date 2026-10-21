# Gabarito – Aula 05: Estrutura condicional if / else

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Leia a idade e informe se a pessoa é maior de idade.

```python
idade = int(input("Idade: "))
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

**Saída esperada – idade = 20:**

```text
Idade: 20
Maior de idade.
```

**Saída esperada – idade = 15:**

```text
Idade: 15
Menor de idade.
```

## Atividade 2

> Leia a nota e informe “Aprovado” (nota ≥ 7) ou “Reprovado”.

```python
nota = float(input("Nota: "))
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

**Saída esperada – nota = 7.5:**

```text
Nota: 7.5
Aprovado
```

**Saída esperada – nota = 5:**

```text
Nota: 5
Reprovado
```

> 📝 **Nota ao professor:** Teste o valor limite (`7`): deve resultar em “Aprovado”. Erro comum: usar `>` em vez de `>=`.

## Atividade 3

> Aplique 20% de desconto (fictício) a clientes com 60 anos ou mais ou estudantes.

```python
idade = int(input("Idade: "))
estudante = input("É estudante? (s/n): ").lower()
valor = 150.00

if idade >= 60 or estudante == "s":
    valor = valor * 0.8
    print("Desconto de 20% aplicado.")
else:
    print("Valor integral.")

print(f"Valor do passeio: R$ {valor:.2f}")
```

**Saída esperada – idoso:**

```text
Idade: 65
É estudante? (s/n): n
Desconto de 20% aplicado.
Valor do passeio: R$ 120.00
```

**Saída esperada – estudante:**

```text
Idade: 30
É estudante? (s/n): s
Desconto de 20% aplicado.
Valor do passeio: R$ 120.00
```

**Saída esperada – sem desconto:**

```text
Idade: 30
É estudante? (s/n): n
Valor integral.
Valor do passeio: R$ 150.00
```

> 📝 **Nota ao professor:** Observe o uso de `or` (basta uma das condições). Se o aluno usar `and`, só terá desconto quem for idoso **e** estudante.

## Desafio do projeto – Dentro ou fora do orçamento?

> Informe se o total está dentro ou fora do orçamento de R$ 1.000,00 e, se estiver fora, quanto excede.

```python
LIMITE = 1000.00

dias = int(input("Quantidade de dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))
total = dias * gasto_dia
print(f"Total da viagem: R$ {total:.2f}")

if total <= LIMITE:
    print("Viagem dentro do orçamento de R$ 1000,00.")
else:
    excesso = total - LIMITE
    print(f"Viagem fora do orçamento! Excede em R$ {excesso:.2f}.")
```

**Saída esperada – dentro:**

```text
Quantidade de dias: 3
Gasto por dia (R$): 330
Total da viagem: R$ 990.00
Viagem dentro do orçamento de R$ 1000,00.
```

**Saída esperada – fora:**

```text
Quantidade de dias: 5
Gasto por dia (R$): 400
Total da viagem: R$ 2000.00
Viagem fora do orçamento! Excede em R$ 1000.00.
```

