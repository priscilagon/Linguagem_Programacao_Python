# Gabarito – Aula 16: Parâmetros, argumentos, retorno e escopo

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Crie `eh_par(n)` que devolva `True` ou `False`.

```python
def eh_par(n):
    return n % 2 == 0

print(eh_par(8))
print(eh_par(7))
```

**Saída esperada:**

```text
True
False
```

## Atividade 2

> Crie `buscar_destino(nome, catalogo)` e teste com um nome existente e outro inexistente.

```python
catalogo = {
    "Parintins": {"preco": 950.00, "dias": 3},
    "Maués": {"preco": 1350.00, "dias": 4},
}

def buscar_destino(nome, catalogo):
    return catalogo.get(nome.strip().title())

print(buscar_destino("maués", catalogo))
print(buscar_destino("Xingu", catalogo))
```

**Saída esperada:**

```text
{'preco': 1350.0, 'dias': 4}
None
```

> 📝 **Nota ao professor:** `dicionario.get(chave)` devolve `None` quando a chave não existe, evitando o `KeyError`.

## Atividade 3

> Explique com suas palavras a diferença entre `print` e `return`.

`print` apenas **mostra** o valor na tela; o programa não consegue usá-lo depois. `return` **devolve** o valor para quem chamou a função, que pode guardá-lo em uma variável, compará-lo ou usá-lo em outros cálculos. Uma função sem `return` devolve `None`.

## Desafio do projeto – Sistema refatorado em funções (busca de destino e validação do orçamento)

> Integrar `calcular_total`, `validar_orcamento`, `buscar_destino` e `cadastrar_cliente` ao menu.

```python
CATALOGO = {
    "Parintins": {"preco": 950.00, "dias": 3},
    "Novo Airão": {"preco": 1200.00, "dias": 4},
    "Presidente Figueiredo": {"preco": 780.00, "dias": 2},
    "Maués": {"preco": 1350.00, "dias": 4},
}

def exibir_menu():
    print("\n=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===")
    print("1 - Calcular viagem")
    print("2 - Cadastrar cliente")
    print("3 - Listar clientes")
    print("4 - Buscar destino")
    print("0 - Sair")
    return input("Escolha: ")

def calcular_total(dias, gasto_dia):
    return dias * gasto_dia

def validar_orcamento(total, limite=1000.00):
    return total <= limite

def buscar_destino(nome):
    return CATALOGO.get(nome.strip().title())

def cadastrar_cliente(clientes):
    nome = input("Nome: ").strip().title()
    destino = input("Destino: ").strip().title()
    dias = int(input("Dias: "))
    clientes.append({"nome": nome, "destino": destino, "dias": dias})
    print("Cliente cadastrado!")

clientes = []
while True:
    opcao = exibir_menu()
    if opcao == "1":
        dias = int(input("Dias: "))
        gasto = float(input("Gasto por dia: "))
        total = calcular_total(dias, gasto)
        print(f"Total: R$ {total:.2f}")
        if validar_orcamento(total):
            print("Dentro do orçamento.")
        else:
            print("Fora do orçamento.")
    elif opcao == "2":
        cadastrar_cliente(clientes)
    elif opcao == "3":
        for cl in clientes:
            print(f"{cl['nome']} -> {cl['destino']} ({cl['dias']} dias)")
    elif opcao == "4":
        dados = buscar_destino(input("Destino: "))
        if dados is None:
            print("Destino não encontrado.")
        else:
            print(f"Preço: R$ {dados['preco']:.2f} | {dados['dias']} dias")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
```

**Saída esperada:**

```text

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Cadastrar cliente
3 - Listar clientes
4 - Buscar destino
0 - Sair
Escolha: 1
Dias: 3
Gasto por dia: 330
Total: R$ 990.00
Dentro do orçamento.

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Cadastrar cliente
3 - Listar clientes
4 - Buscar destino
0 - Sair
Escolha: 2
Nome: marina costa
Destino: parintins
Dias: 3
Cliente cadastrado!

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Cadastrar cliente
3 - Listar clientes
4 - Buscar destino
0 - Sair
Escolha: 3
Marina Costa -> Parintins (3 dias)

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Cadastrar cliente
3 - Listar clientes
4 - Buscar destino
0 - Sair
Escolha: 4
Destino: maués
Preço: R$ 1350.00 | 4 dias

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Cadastrar cliente
3 - Listar clientes
4 - Buscar destino
0 - Sair
Escolha: 4
Destino: xingu
Destino não encontrado.

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Cadastrar cliente
3 - Listar clientes
4 - Buscar destino
0 - Sair
Escolha: 0
```

> 📝 **Nota ao professor:** Use o checklist de code review da apostila: cada função faz uma só coisa? Há `return` onde deve devolver valor? Há código repetido?

