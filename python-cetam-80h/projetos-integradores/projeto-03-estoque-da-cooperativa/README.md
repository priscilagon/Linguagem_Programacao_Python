# Projeto 3 – Estoque da Cooperativa Ribeirinha

| Ficha do projeto |  |
| --- | --- |
| **Tema** | Controle de estoque e vendas com funções |
| **Nível** | ★★★★★ |
| **Conteúdos** | Aulas 1 a 16: dicionários aninhados, funções com parâmetros e retorno, menu com `while`, validações, strings |
| **Tempo sugerido** | 8 a 10 horas |
| **Organização** | dupla |

## Cenário

Uma **cooperativa de produtores ribeirinhos** vende açaí, castanha, tapioca e cupuaçu. O controle é feito em caderno e frequentemente falta produto ou há venda além do estoque. Sua missão é construir o **sistema de estoque**, organizado em **funções**, para cadastrar produtos, registrar vendas e reposições e emitir um relatório.

Todos os preços e quantidades são **fictícios**.

## Objetivos de aprendizagem

- Modelar dados com **dicionários aninhados**.
- Dividir o programa em **funções** com parâmetros e retorno.
- Validar entradas e regras de negócio.
- Construir um menu completo e um relatório gerencial.

## Dados de partida

| Produto inicial | Preço unitário | Quantidade |
| --- | --- | --- |
| Açaí | R$ 18,50 | 40 |
| Castanha | R$ 32,00 | 15 |
| Tapioca | R$ 12,00 | 8 |
| Cupuaçu | R$ 15,00 | 25 |

## Requisitos funcionais

| Código | O sistema deve... |
| --- | --- |
| RF01 | Iniciar o programa com o **estoque inicial** da tabela, em um dicionário `{nome: {"preco": ..., "qtd": ...}}`. |
| RF02 | **Menu** com: 1 – Listar estoque, 2 – Cadastrar produto, 3 – Registrar venda, 4 – Repor estoque, 5 – Relatório, 0 – Sair. |
| RF03 | **Listar** todos os produtos com preço e quantidade. |
| RF04 | **Cadastrar** produto novo (nome, preço, quantidade inicial). |
| RF05 | **Vender**: informar produto e quantidade, baixar o estoque e **devolver o valor da venda**, acumulando o total vendido na sessão. |
| RF06 | **Repor**: somar uma quantidade ao estoque de um produto existente. |
| RF07 | **Relatório**: número de produtos, valor total em estoque, total vendido, produto mais caro e lista de produtos com **estoque baixo**. |
| RF08 | O programa deve ser organizado em **funções** (no mínimo: `exibir_menu`, `listar_estoque`, `cadastrar_produto`, `vender`, `repor`, `valor_total` e `relatorio`). |

## Regras de negócio

| Código | Regra |
| --- | --- |
| RN01 | Nomes de produtos são padronizados com `strip()` e `title()` (“AÇAÍ” e “  açaí” são o mesmo produto). |
| RN02 | Não cadastrar produto **repetido** nem com nome vazio. |
| RN03 | Preço deve ser **maior que zero**; quantidade inicial **não pode ser negativa**. |
| RN04 | Não vender produto inexistente, quantidade menor ou igual a zero ou **quantidade maior que o estoque**. |
| RN05 | Reposição exige produto existente e quantidade **maior que zero**. |
| RN06 | **Estoque baixo**: menos de 10 unidades. |

## Exemplo de execução

Trecho de uma execução (o que o usuário digita aparece após os dois pontos):

```text

=== COOPERATIVA RIBEIRINHA - ESTOQUE ===
1 - Listar estoque
2 - Cadastrar produto
3 - Registrar venda
4 - Repor estoque
5 - Relatório
0 - Sair
Escolha: 1

--- ESTOQUE ATUAL ---
Açaí: R$ 18.50 | 40 un.
Castanha: R$ 32.00 | 15 un.
Tapioca: R$ 12.00 | 8 un.
Cupuaçu: R$ 15.00 | 25 un.

=== COOPERATIVA RIBEIRINHA - ESTOQUE ===
1 - Listar estoque
2 - Cadastrar produto
3 - Registrar venda
4 - Repor estoque
5 - Relatório
0 - Sair
Escolha: 3
Produto: açaí
Quantidade: 5
Venda registrada: 5 x Açaí = R$ 92.50

=== COOPERATIVA RIBEIRINHA - ESTOQUE ===
1 - Listar estoque
2 - Cadastrar produto
3 - Registrar venda
4 - Repor estoque
5 - Relatório
0 - Sair
Escolha: 3
```

## O que entregar

- Arquivo `projeto3_estoque.py` ou notebook `Projeto3_Estoque.ipynb`, com nomes da dupla no topo.
- Quadro de **testes** com, no mínimo, 6 casos e **registro de colaboração** (quem fez cada função).

## Critérios de avaliação

| Critério | O que será observado |
| --- | --- |
| Funcionamento | Todas as opções do menu funcionam com os dados de teste. |
| Modularização | Funções com responsabilidade única, parâmetros e `return` adequados. |
| Estruturas de dados | Dicionário aninhado manipulado corretamente. |
| Regras de negócio | Validações RN01 a RN06 implementadas. |
| Organização e colaboração | Código legível, testes e registro da dupla. |

## Dicas

- Percorra o dicionário com `for nome, dados in estoque.items():`.
- `vender()` deve **retornar** o valor (e `0` quando a venda não ocorrer), para somar à variável `vendido`.
- Funções que apenas alteram o dicionário não precisam de `return`: o dicionário é modificado no lugar.
- Defina a constante `MINIMO = 10` no topo do programa.

## Desafios extras (opcionais)

- **Preço promocional:** vendas de 10 ou mais unidades têm 5% de desconto.
- **Persistência:** salve e carregue o estoque em arquivo `.txt`.
- **Histórico:** guarde as vendas em uma lista e mostre-as no relatório.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto03_estoque.py`](starter/projeto03_estoque.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
