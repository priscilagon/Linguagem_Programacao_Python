# Projeto 7 – Meu Orçamento Familiar

| **Ficha do projeto** |  |
| --- | --- |
| **Tema** | Controle de receitas e despesas por categoria |
| **Nível** | ★★☆☆☆ |
| **Tempo sugerido** | 6 a 8 horas |
| **Forma de trabalho** | individual ou dupla |
| **Aulas relacionadas** | Aulas 1 a 14 |
| **Conteúdos** | listas, dicionários, listas de dicionários, strings, `for/range`, decisões e validações |

## Cenário

Muitas famílias não sabem **para onde vai o dinheiro** no fim do mês. Você vai criar o **Meu Orçamento Familiar**, um programa em que a pessoa registra suas **receitas** e **despesas por categoria**, e o sistema mostra o **saldo**, a **porcentagem da renda comprometida**, o **gasto por categoria** e qual categoria pesa mais.

Todos os valores usados nos testes são **fictícios**.

## Objetivos de aprendizagem

Ao concluir este projeto, você será capaz de:

- Guardar lançamentos em uma **lista de dicionários**.
- Usar uma **lista de categorias** e um **dicionário** de totais.
- Percorrer listas com `for` e `range(len(...))`.
- Calcular totais, saldos e porcentagens.
- Padronizar textos e validar entradas.

## Dados de partida

| **Nº** | **Categoria de despesa** | **Exemplo** |
| --- | --- | --- |
| 1 | Moradia | aluguel, energia, água |
| 2 | Alimentação | feira, mercado |
| 3 | Transporte | barco, ônibus, combustível |
| 4 | Saúde | consulta, remédio |
| 5 | Lazer | cinema, passeio |
| 6 | Outros | demais gastos |

## Requisitos funcionais

| **Código** | **Requisito** |
| --- | --- |
| RF01 | **Menu**: 1 – Registrar receita, 2 – Registrar despesa, 3 – Resumo do mês, 4 – Despesas por categoria, 5 – Listar lançamentos, 0 – Sair. |
| RF02 | **Receita**: pedir descrição e valor e guardar o lançamento (tipo “receita”). |
| RF03 | **Despesa**: pedir descrição, **categoria (pelo número)** e valor e guardar o lançamento (tipo “despesa”). |
| RF04 | **Resumo**: total de receitas, total de despesas, saldo, **porcentagem da renda comprometida** e a situação do orçamento. |
| RF05 | **Despesas por categoria**: total de cada categoria com despesas, a **porcentagem** em relação ao total de despesas e a **categoria de maior gasto**. |
| RF06 | **Listar** todos os lançamentos, numerados, com categoria, descrição, sinal (+ ou −) e valor. |

## Regras de negócio

| **Código** | **Regra** |
| --- | --- |
| RN01 | A descrição não pode ser vazia; padronize com `strip()` e `capitalize()`. |
| RN02 | O valor deve ser **maior que zero**; caso contrário, pedir de novo. |
| RN03 | A categoria deve ser um número de **1 a 6**; caso contrário, pedir de novo. Receitas usam a categoria “Receita”. |
| RN04 | Comprometimento = despesas ÷ receitas × 100. **Até 70%**: “Saudável”. **Mais de 70% até 100%**: “Atenção – despesas altas”. **Acima de 100%**: “Alerta – despesas maiores que a receita”. |
| RN05 | Sem receitas registradas, o resumo mostra os totais e avisa “Registre ao menos uma receita para analisar o orçamento.” (sem dividir por zero). |
| RN06 | Sem despesas ou sem lançamentos, as opções 4 e 5 avisam, sem gerar erro. |

## Exemplo de execução

Trecho de uma execução do programa (o que o usuário digita aparece depois dos dois-pontos de cada pergunta):

**Saída esperada**

```text

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 3

--- RESUMO DO MÊS ---
Receitas: R$ 0.00
Despesas: R$ 0.00
Saldo: R$ 0.00
Registre ao menos uma receita para analisar o orçamento.

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 4
Nenhuma despesa registrada.

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
```

## O que entregar

- Arquivo `projeto07_orcamento.py` ou notebook `Projeto07_Orcamento.ipynb`, com nomes dos integrantes no topo.
- Quadro de **testes** com, no mínimo, 6 casos (inclua os três níveis de situação do orçamento e os casos “sem dados”).

## Critérios de avaliação

| **Critério** | **O que será observado** |
| --- | --- |
| Funcionamento | Todas as opções do menu funcionam com os dados de teste. |
| Estruturas de dados | Lista de dicionários, lista de categorias e dicionário de totais. |
| Cálculos | Totais, saldo e porcentagens corretos. |
| Regras de negócio | RN01 a RN06 implementadas. |
| Organização e testes | Código legível, comentado e quadro de testes coerente. |

## Dicas

- Cada lançamento: `{"tipo": "despesa", "descricao": "Aluguel", "categoria": "Moradia", "valor": 1200.0}`.
- Mostre as categorias com `for i in range(len(categorias)):` e use `categorias[numero - 1]`.
- Crie o dicionário de totais zerado com um `for` sobre `categorias` e some com `totais[categoria] += valor`.
- Para a categoria de maior gasto, guarde `maior_valor` e `maior_categoria` enquanto percorre.
- Teste `receitas == 0` **antes** de dividir.

## Desafios extras (opcionais)

- **Gráfico de barras:** mostre `"#" * int(percentual / 5)` ao lado de cada categoria.
- **Meta de poupança:** peça uma meta e informe se o saldo a atingiu.
- **Remover lançamento:** escolha pelo número da listagem.
- **Persistência:** salve os lançamentos em arquivo (estude a Aula 17).

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto07_orcamento.py`](starter/projeto07_orcamento.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
