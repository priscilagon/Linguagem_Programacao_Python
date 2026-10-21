# Gabarito – Aula 11: Listas

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Crie uma lista com 4 destinos. Mostre o primeiro e o último, adicione um quinto e ordene a lista.

```python
destinos = ["Parintins", "Novo Airão", "Maués", "Presidente Figueiredo"]
print(destinos[0], destinos[-1])

destinos.append("Encontro das Águas")
destinos.sort()
print(destinos)
```

**Saída esperada:**

```text
Parintins Presidente Figueiredo
['Encontro das Águas', 'Maués', 'Novo Airão', 'Parintins', 'Presidente Figueiredo']
```

## Atividade 2

> Dada a lista de gastos `[990, 1250.5, 780]`, mostre o maior, o menor e a média.

```python
gastos = [990, 1250.5, 780]
print(f"Maior: R$ {max(gastos):.2f}")
print(f"Menor: R$ {min(gastos):.2f}")
print(f"Média: R$ {sum(gastos) / len(gastos):.2f}")
```

**Saída esperada:**

```text
Maior: R$ 1250.50
Menor: R$ 780.00
Média: R$ 1006.83
```

## Desafio do projeto – Cadastro de destinos e média de gastos

> Cadastrar vários destinos e gastos em duas listas e calcular a média.

```python
destinos = []
gastos = []

continuar = "s"
while continuar == "s":
    destinos.append(input("Destino: "))
    gastos.append(float(input("Gasto total (R$): ")))
    continuar = input("Cadastrar outro? (s/n): ").lower()

print(f"Destinos cadastrados: {destinos}")
print(f"Média dos gastos: R$ {sum(gastos) / len(gastos):.2f}")
```

**Saída esperada:**

```text
Destino: Parintins
Gasto total (R$): 990
Cadastrar outro? (s/n): s
Destino: Maués
Gasto total (R$): 1350
Cadastrar outro? (s/n): n
Destinos cadastrados: ['Parintins', 'Maués']
Média dos gastos: R$ 1170.00
```

