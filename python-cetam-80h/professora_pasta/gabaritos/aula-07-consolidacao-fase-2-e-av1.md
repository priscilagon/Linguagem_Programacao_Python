# Gabarito – Aula 07: Consolidação da Fase 2 e AV1

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## AV1 – Modelo de resolução (Calculadora v2)

> Desenvolver o programa da agência: entrada de nome, dias e gasto por dia, cálculo do total, decisão sobre o orçamento e `elif` para a faixa do pacote.

```python
# Agência Amazônia Tur Digital - Calculadora de viagem v2
LIMITE = 1000.00

nome = input("Nome do cliente: ")
dias = int(input("Quantidade de dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))

total = dias * gasto_dia

if total <= 800:
    pacote = "Econômico"
elif total <= 1500:
    pacote = "Conforto"
else:
    pacote = "Premium"

print(f"\nCliente: {nome}")
print(f"Total: R$ {total:.2f} - Pacote {pacote}")

if total <= LIMITE:
    print("Dentro do orçamento de R$ 1000,00.")
else:
    print(f"Fora do orçamento! Excede em R$ {total - LIMITE:.2f}.")
```

**Saída esperada – Conforto, dentro do orçamento:**

```text
Nome do cliente: Marina
Quantidade de dias: 3
Gasto por dia (R$): 330

Cliente: Marina
Total: R$ 990.00 - Pacote Conforto
Dentro do orçamento de R$ 1000,00.
```

**Saída esperada – Premium, fora do orçamento:**

```text
Nome do cliente: Carlos
Quantidade de dias: 5
Gasto por dia (R$): 400

Cliente: Carlos
Total: R$ 2000.00 - Pacote Premium
Fora do orçamento! Excede em R$ 1000.00.
```

**Saída esperada – Econômico, dentro do orçamento:**

```text
Nome do cliente: Ana
Quantidade de dias: 2
Gasto por dia (R$): 300

Cliente: Ana
Total: R$ 600.00 - Pacote Econômico
Dentro do orçamento de R$ 1000,00.
```

## AV1 – Matriz de correção

Os descritores abaixo orientam a correção. A atribuição de notas é de competência exclusiva do professor.

| Critério | Atende plenamente | Atende parcialmente | Não atende |
| --- | --- | --- | --- |
| **Funcionamento** | Roda sem erros e resultados corretos nos três cenários de teste. | Roda, mas erra em algum cenário (ex.: limite). | Não executa ou não produz o resultado. |
| **Lógica** | `if/elif/else` corretos, faixas e orçamento coerentes. | Faixas ou orçamento com falha parcial. | Decisões ausentes ou incorretas. |
| **Legibilidade** | Nomes claros, indentação correta e comentários. | Nomes pouco claros ou sem comentários. | Código confuso, sem organização. |
| **Tratamento dos tipos** | `int()` e `float()` aplicados corretamente. | Conversão em parte das entradas. | Sem conversões; erros de tipo. |

