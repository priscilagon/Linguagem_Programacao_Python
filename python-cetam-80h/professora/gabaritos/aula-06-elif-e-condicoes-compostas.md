# Gabarito – Aula 06: elif, condições encadeadas e compostas

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Classifique a média de um aluno: ≥ 7 “Aprovado”, ≥ 5 “Recuperação”, senão “Reprovado”.

```python
media = float(input("Média: "))
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

**Saída esperada – média 8:**

```text
Média: 8
Aprovado
```

**Saída esperada – média 6:**

```text
Média: 6
Recuperação
```

**Saída esperada – média 3:**

```text
Média: 3
Reprovado
```

## Atividade 2

> Um cliente ganha cortesia (um passeio grátis) se `dias >= 5` e `total <= 1500`. Escreva a condição.

A condição é `dias >= 5 and total <= 1500`. Exemplo completo:

```python
dias = int(input("Dias: "))
total = float(input("Total (R$): "))

if dias >= 5 and total <= 1500:
    print("Cliente ganha cortesia: um passeio grátis!")
else:
    print("Sem cortesia.")
```

**Saída esperada – ganha cortesia:**

```text
Dias: 6
Total (R$): 1200
Cliente ganha cortesia: um passeio grátis!
```

**Saída esperada – total alto:**

```text
Dias: 6
Total (R$): 1800
Sem cortesia.
```

**Saída esperada – poucos dias:**

```text
Dias: 3
Total (R$): 900
Sem cortesia.
```

## Desafio do projeto – Classificação por faixa e sugestão de destino

> Classifique a viagem (Econômico, Conforto ou Premium) e sugira um destino compatível.

```python
dias = int(input("Dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))
total = dias * gasto_dia

if total <= 800:
    pacote = "Econômico"
elif total <= 1500:
    pacote = "Conforto"
else:
    pacote = "Premium"

if pacote == "Econômico" and dias <= 3:
    sugestao = "Presidente Figueiredo"
elif pacote == "Conforto":
    sugestao = "Novo Airão"
else:
    sugestao = "Parintins"

print(f"Total: R$ {total:.2f} - Pacote {pacote}")
print(f"Sugestão de destino: {sugestao}")
```

**Saída esperada – econômico:**

```text
Dias: 2
Gasto por dia (R$): 300
Total: R$ 600.00 - Pacote Econômico
Sugestão de destino: Presidente Figueiredo
```

**Saída esperada – conforto:**

```text
Dias: 4
Gasto por dia (R$): 300
Total: R$ 1200.00 - Pacote Conforto
Sugestão de destino: Novo Airão
```

**Saída esperada – premium:**

```text
Dias: 6
Gasto por dia (R$): 400
Total: R$ 2400.00 - Pacote Premium
Sugestão de destino: Parintins
```

> 📝 **Nota ao professor:** As faixas e os destinos sugeridos são livres: valorize a **coerência** entre faixa e sugestão. Aceite outras escolhas de destino.

