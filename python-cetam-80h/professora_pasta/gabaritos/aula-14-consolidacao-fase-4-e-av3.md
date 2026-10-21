# Gabarito – Aula 14: Consolidação da Fase 4 e AV3

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Dada `nomes = ["Ana", "Bia", "Caio"]`, o que `nomes[-1]` e `nomes[0:2]` mostram?

```python
nomes = ["Ana", "Bia", "Caio"]
print(nomes[-1])
print(nomes[0:2])
```

**Saída esperada:**

```text
Caio
['Ana', 'Bia']
```

> 📝 **Nota ao professor:** `[-1]` é o último item; o fatiamento `[0:2]` pega as posições 0 e 1 (o fim não é incluído).

## Atividade 2

> Qual a diferença entre `lista.append(x)` e `lista.remove(x)`?

`append(x)` **adiciona** `x` ao final da lista; `remove(x)` **retira** a primeira ocorrência de `x`. (Se `x` não existir na lista, `remove` gera `ValueError`.)

## Atividade 3

> Dado `aluno = {"nome": "Ana", "nota": 9}`, como alterar a nota para 10? E como acrescentar a chave `"curso"`?

```python
aluno = {"nome": "Ana", "nota": 9}
aluno["nota"] = 10
aluno["curso"] = "Python"
print(aluno)
```

**Saída esperada:**

```text
{'nome': 'Ana', 'nota': 10, 'curso': 'Python'}
```

## Atividade 4

> O que `"  Maués ".strip().upper()` devolve?

```python
print("  Maués ".strip().upper())
```

**Saída esperada:**

```text
MAUÉS
```

> 📝 **Nota ao professor:** Resposta: `"MAUÉS"`. Os métodos são aplicados em sequência, da esquerda para a direita.

## AV3 – Modelo de resolução do problema em laboratório

> Cadastro de clientes com dicionário e lista.

```python
clientes = []

continuar = "s"
while continuar == "s":
    cliente = {
        "nome": input("Nome: ").strip().title(),
        "destino": input("Destino: ").strip().title(),
        "dias": int(input("Dias: "))
    }
    clientes.append(cliente)
    continuar = input("Cadastrar outro? (s/n): ").lower()

print()
for cl in clientes:
    print(f"{cl['nome']} -> {cl['destino']} ({cl['dias']} dias)")
print(f"Total de clientes: {len(clientes)}")
```

**Saída esperada:**

```text
Nome:  marina costa 
Destino: parintins
Dias: 3
Cadastrar outro? (s/n): s
Nome: joão pedro
Destino: maués
Dias: 4
Cadastrar outro? (s/n): n

Marina Costa -> Parintins (3 dias)
João Pedro -> Maués (4 dias)
Total de clientes: 2
```

> 📝 **Nota ao professor:** Questões objetivas e discursivas da AV3: elabore a partir dos conteúdos das aulas 11 a 13. Itens para correção do problema prático: lista de dicionários, uso de `append`, padronização com `strip`/`title` e percurso com `for`.

