# Projeto 1 – Caixa da Feira do Produtor

| Ficha do projeto |  |
| --- | --- |
| **Tema** | Ponto de venda de uma feira regional |
| **Nível** | ★☆☆☆☆ |
| **Conteúdos** | Aulas 1 a 10: variáveis, tipos, `input()`, operadores, `if/elif/else`, `while`, `break`, `continue` |
| **Tempo sugerido** | 4 a 6 horas |
| **Organização** | individual ou dupla |

## Cenário

Na feira do produtor de um bairro de Manaus, o caixa ainda é feito na calculadora e na caderneta. Os feirantes querem um **programa de caixa digital** que registre os produtos comprados por cada cliente, aplique descontos por volume, receba o pagamento e calcule o troco, e que ao fim do dia informe quanto foi vendido.

Os preços são **fictícios** e servem apenas para o exercício.

## Objetivos de aprendizagem

- Aplicar entrada e saída de dados com conversão de tipos.
- Tomar decisões com `if/elif/else` e condições compostas.
- Usar laços `while` para repetir atendimentos e validar entradas.
- Controlar o fluxo com `break` e `continue`.

## Dados de partida

| Código | Produto | Preço por kg (fictício) |
| --- | --- | --- |
| 1 | Tambaqui | R$ 28,00 |
| 2 | Pirarucu | R$ 45,00 |
| 3 | Tucunaré | R$ 32,00 |
| 4 | Farinha de mandioca | R$ 9,00 |

## Requisitos funcionais

| Código | O sistema deve... |
| --- | --- |
| RF01 | Exibir um **menu de produtos** (códigos 1 a 4) e a opção **0 – Finalizar compra**, repetindo o menu até o cliente finalizar. |
| RF02 | Para cada produto escolhido, pedir a **quantidade em kg** e mostrar a linha: produto, quantidade, preço por kg e valor. |
| RF03 | Acumular o **subtotal** da compra e a **quantidade de itens** registrados. |
| RF04 | Aplicar **desconto por volume** sobre o subtotal (regras RN02 e RN03). |
| RF05 | Mostrar o **resumo da compra**: itens, subtotal, desconto (com a porcentagem) e total a pagar. |
| RF06 | Perguntar a **forma de pagamento** (1 – Dinheiro, 2 – Cartão). No dinheiro, ler o valor recebido e **calcular o troco**. |
| RF07 | Perguntar **“Atender novo cliente? (s/n)”** e repetir o atendimento completo enquanto a resposta for “s”. |
| RF08 | Ao encerrar, mostrar o **fechamento do caixa**: clientes atendidos e total vendido no dia. |

## Regras de negócio

| Código | Regra |
| --- | --- |
| RN01 | A quantidade deve ser **maior que zero**; caso contrário, avisar e perguntar de novo. |
| RN02 | Subtotal **a partir de R$ 100,00** e menor que R$ 200,00: **5%** de desconto. |
| RN03 | Subtotal **a partir de R$ 200,00**: **10%** de desconto. Abaixo de R$ 100,00: sem desconto. |
| RN04 | Opção de menu inexistente: avisar “Opção inválida!” e mostrar o menu novamente. |
| RN05 | Não é possível finalizar uma compra **sem nenhum item** registrado. |
| RN06 | No pagamento em dinheiro, o valor recebido não pode ser **menor que o total**: informar quanto falta e pedir de novo. |
| RN07 | A forma de pagamento só aceita 1 ou 2; repetir a pergunta se for outro valor. |

## Exemplo de execução

Trecho de uma execução (o que o usuário digita aparece após os dois pontos):

```text
=== FEIRA DO PRODUTOR - CAIXA DIGITAL ===
(preços fictícios, apenas para o exercício)

--- Novo atendimento ---

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 1
Quantidade de Tambaqui (kg): 5
Tambaqui: 5.00 kg x R$ 28.00 = R$ 140.00

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 4
Quantidade de Farinha de mandioca (kg): 2
Farinha de mandioca: 2.00 kg x R$ 9.00 = R$ 18.00

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
```

## O que entregar

- Arquivo `projeto1_caixa.py` (VS Code) **ou** notebook `Projeto1_Caixa.ipynb` (Colab), com os nomes dos integrantes em comentário no topo.
- Quadro de **testes** preenchido (veja o modelo na Apresentação) com, no mínimo, 5 casos.

## Critérios de avaliação

| Critério | O que será observado |
| --- | --- |
| Funcionamento | O caixa roda do início ao fechamento sem travar e com resultados corretos. |
| Regras de negócio | Descontos, troco e validações (RN01 a RN07) corretos. |
| Uso dos conteúdos | `input()` com conversão, `if/elif/else`, `while`, `break` e `continue`. |
| Organização | Nomes claros, indentação, comentários e saída legível. |
| Testes | Quadro de testes coerente com o comportamento do programa. |

## Dicas

- Use **dois laços `while`**: um interno (itens da compra) e outro externo (clientes).
- Zere `subtotal` e `itens` **no início de cada atendimento**.
- Use `continue` para voltar ao menu quando a opção for inválida.
- Para mostrar a porcentagem, use `taxa * 100` e `:.0f`.

## Desafios extras (opcionais)

- **Nota detalhada:** guarde os itens da compra em uma lista e imprima a nota com todos eles.
- **Cupom:** peça um código; “FEIRA10” dá mais 10% sobre o total.
- **Fechamento em arquivo:** grave o resumo do dia em `fechamento.txt`.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto01_caixa.py`](starter/projeto01_caixa.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
