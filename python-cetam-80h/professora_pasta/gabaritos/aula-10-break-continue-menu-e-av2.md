# Gabarito – Aula 10: break, continue, pass, menu interativo e AV2

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Em um `for` de 1 a 5, se o número for 3 use `continue`; se for 5 use `break`; nos demais casos, mostre o número. Qual é a saída?

```python
for numero in range(1, 6):
    if numero == 3:
        continue
    if numero == 5:
        break
    print(numero)
```

**Saída esperada:**

```text
1
2
4
```

> 📝 **Nota ao professor:** Saída: 1, 2 e 4. O 3 é pulado (`continue`) e o laço termina no 5 antes de imprimi-lo (`break`).

## Atividade 2

> Acrescente ao menu a opção “3 – Ver orçamento limite” que mostre o valor de R$ 1.000,00.

```python
LIMITE = 1000.00
destinos = ["Parintins", "Novo Airão", "Presidente Figueiredo", "Maués"]

while True:
    print("\n=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===")
    print("1 - Calcular viagem")
    print("2 - Ver destinos")
    print("3 - Ver orçamento limite")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        dias = int(input("Dias: "))
        gasto_dia = float(input("Gasto por dia: "))
        print(f"Total: R$ {dias * gasto_dia:.2f}")
    elif opcao == "2":
        for destino in destinos:
            print("-", destino)
    elif opcao == "3":
        print(f"Orçamento limite: R$ {LIMITE:.2f}")
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
        continue
```

**Saída esperada:**

```text

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Ver destinos
3 - Ver orçamento limite
0 - Sair
Escolha uma opção: 3
Orçamento limite: R$ 1000.00

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Ver destinos
3 - Ver orçamento limite
0 - Sair
Escolha uma opção: 1
Dias: 3
Gasto por dia: 330
Total: R$ 990.00

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Ver destinos
3 - Ver orçamento limite
0 - Sair
Escolha uma opção: 2
- Parintins
- Novo Airão
- Presidente Figueiredo
- Maués

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Ver destinos
3 - Ver orçamento limite
0 - Sair
Escolha uma opção: 9
Opção inválida!

=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===
1 - Calcular viagem
2 - Ver destinos
3 - Ver orçamento limite
0 - Sair
Escolha uma opção: 0
Até logo!
```

> 📝 **Nota ao professor:** Este código também é o modelo de referência do **menu interativo** (entrega da Fase 3) e da **AV2**.

## AV2 – Matriz de correção

A AV2 é feita em duplas; avalie também o registro de colaboração de cada integrante.

| Critério | Atende plenamente | Atende parcialmente | Não atende |
| --- | --- | --- | --- |
| **Funcionamento** | Menu repete até a opção de sair; todas as opções executam. | Menu funciona, mas alguma opção falha. | Menu não repete ou não executa. |
| **Validação de entrada** | Entradas inválidas tratadas sem encerrar o programa. | Validação apenas em parte das entradas. | Sem validação. |
| **Controle de fluxo** | `break` e `continue` usados no lugar certo. | Uso parcial ou desnecessário. | Ausente ou incorreto. |
| **Colaboração** | Tarefas divididas e contribuição de cada um registrada. | Registro incompleto ou desigual. | Sem registro de colaboração. |

