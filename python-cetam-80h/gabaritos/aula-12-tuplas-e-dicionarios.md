# Gabarito – Aula 12: Tuplas e dicionários

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Crie um dicionário com nome, preço e duração de um passeio e percorra-o com `.items()`.

```python
passeio = {"nome": "Passeio de barco", "preco": 120.00, "duracao": 3}

for chave, valor in passeio.items():
    print(f"{chave}: {valor}")
```

**Saída esperada:**

```text
nome: Passeio de barco
preco: 120.0
duracao: 3
```

## Atividade 2

> Explique a diferença entre uma lista e uma tupla e dê um exemplo de uso de cada uma.

A **lista** (`[ ]`) é **mutável**: é possível adicionar, remover e alterar itens. Exemplo: a lista de clientes cadastrados, que muda a todo momento.

A **tupla** (`( )`) é **imutável**: depois de criada, não pode ser alterada. Exemplo: as coordenadas de uma cidade, `(-3.119, -60.021)`, que são dados fixos.

## Desafio do projeto – Catálogo de pacotes da agência

> Montar o catálogo em um dicionário e exibi-lo com `.items()`.

```python
catalogo = {
    "Parintins": {"preco": 950.00, "dias": 3},
    "Novo Airão": {"preco": 1200.00, "dias": 4},
    "Presidente Figueiredo": {"preco": 780.00, "dias": 2},
    "Maués": {"preco": 1350.00, "dias": 4},
}

for nome, dados in catalogo.items():
    print(f"{nome}: R$ {dados['preco']:.2f} em {dados['dias']} dias")
```

**Saída esperada:**

```text
Parintins: R$ 950.00 em 3 dias
Novo Airão: R$ 1200.00 em 4 dias
Presidente Figueiredo: R$ 780.00 em 2 dias
Maués: R$ 1350.00 em 4 dias
```

