# Projeto 2 – Monitor Fluvial: Nível do Rio Negro

| Ficha do projeto |  |
| --- | --- |
| **Tema** | Análise de medições do nível de um rio |
| **Nível** | ★★★★★ |
| **Conteúdos** | Aulas 1 a 14: listas, dicionários, strings, `for`/`range`, decisões, métodos de listas e funções internas |
| **Tempo sugerido** | 2 a 4 horas |
| **Organização** | individual ou dupla |

## Cenário

Pesquisadores e comunidades ribeirinhas acompanham o **nível do Rio Negro** em Manaus mês a mês, pois ele determina a navegação, a pesca e a vida às margens. Você vai criar um **monitor fluvial**: o programa recebe as 12 medições do ano, analisa os dados e permite consultar qualquer mês.

Use **dados fictícios** na hora de testar (sugestão: 26,1 / 27,4 / 28,3 / 29,0 / 29,6 / 29,8 / 29,2 / 27,9 / 25,7 / 23,8 / 23,1 / 24,0 metros).

## Objetivos de aprendizagem

- Armazenar e processar dados em **listas** paralelas.
- Percorrer listas com `for` e `range(len(...))`.
- Usar **dicionários** como contadores.
- Manipular **strings** para padronizar buscas.
- Usar `sum`, `max`, `min`, `len` e `index`.

## Requisitos funcionais

| Código | O sistema deve... |
| --- | --- |
| RF01 | Criar a lista `meses` (Jan a Dez) e ler, com `for`, o **nível em metros** de cada mês, guardando-os na lista `niveis`. |
| RF02 | Calcular e mostrar a **média anual**, o **maior** e o **menor** nível, informando **em qual mês** ocorreram. |
| RF03 | Classificar cada mês (**Cheia**, **Enchente/Vazante** ou **Seca**) e mostrar um **relatório** com mês, nível, classificação e uma **barra de caracteres** proporcional ao nível. |
| RF04 | Usar um **dicionário** para contar quantos meses há em cada classificação. |
| RF05 | Descobrir o **mês de maior subida** do nível em relação ao mês anterior e quanto subiu. |
| RF06 | **Consulta por mês**: o usuário digita o nome do mês (com qualquer combinação de maiúsculas, minúsculas e espaços) e o programa mostra nível e classificação; “fim” encerra. |

## Regras de negócio

| Código | Regra |
| --- | --- |
| RN01 | Níveis válidos: de **0 a 40 metros**. Valor fora da faixa: avisar e pedir de novo. |
| RN02 | Nível **a partir de 29 m**: “Cheia”. **De 26 m até menos de 29 m**: “Enchente/Vazante”. **Abaixo de 26 m**: “Seca”. |
| RN03 | A barra do relatório tem **um caractere `#` para cada metro inteiro** (use `int(nivel)`). |
| RN04 | Na consulta, mês inexistente: mostrar “Mês não encontrado.” |
| RN05 | A maior subida considera apenas variações **positivas** (de um mês para o seguinte). |

## Exemplo de execução

Trecho de uma execução (o que o usuário digita aparece após os dois pontos):

```text
=== MONITOR FLUVIAL - RIO NEGRO ===
Nível em Jan (m): 45
Valor inválido! Digite entre 0 e 40 metros.
Nível em Jan (m): 26.1
Nível em Fev (m): 27.4
Nível em Mar (m): 28.3
Nível em Abr (m): 29
Nível em Mai (m): 29.6
```

## O que entregar

- Arquivo `projeto2_monitor.py` ou notebook `Projeto2_Monitor.ipynb`, com nomes dos integrantes no topo.
- Quadro de **testes** com, no mínimo, 5 casos (inclua um valor inválido e uma consulta com mês inexistente).

## Critérios de avaliação

| Critério | O que será observado |
| --- | --- |
| Funcionamento | Leitura, análises e consulta funcionando com os dados de teste. |
| Estruturas de dados | Listas paralelas, dicionário contador e uso correto de índices. |
| Strings | Padronização da busca com `strip()` e `title()`. |
| Regras de negócio | Faixas de classificação, validação e maior subida corretas. |
| Organização e testes | Código legível, comentado e quadro de testes coerente. |

## Dicas

- `meses[niveis.index(maior)]` informa o mês de um valor da lista `niveis`.
- Para a barra: `"#" * int(nivel)` repete o caractere.
- A maior subida usa `for i in range(1, len(niveis))` e compara `niveis[i]` com `niveis[i - 1]`.
- Padronize a consulta com `.strip().title()`: “  jun ” vira “Jun”.

## Desafios extras (opcionais)

- **Gráfico:** gere um gráfico de linhas com `matplotlib` (no Colab já vem instalada; no VS Code, `pip install matplotlib`).
- **Meses críticos:** liste os meses com nível abaixo de 24 m.
- **Comparação de anos:** leia um segundo ano e diga qual teve a maior média.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto02_monitor.py`](starter/projeto02_monitor.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
