# Projeto 6 – Quiz da Floresta Amazônica

| **Ficha do projeto** |  |
| --- | --- |
| **Tema** | Jogo de perguntas e respostas com pontuação |
| **Nível** | ★★★★★ |
| **Tempo sugerido** | 2 a 4 horas |
| **Forma de trabalho** | individual ou dupla |
| **Aulas relacionadas** | Aulas 1 a 10 |
| **Conteúdos** | variáveis, `input()`, operadores, `if/elif/else`, `while`, `for/range`, contadores e acumuladores |

## Cenário

A secretaria de educação de um município do Amazonas quer um **jogo de perguntas sobre a Amazônia** para usar nas escolas. Você vai criar o **Quiz da Floresta Amazônica**: o jogador responde a 5 perguntas de múltipla escolha, ganha pontos por acerto e **bônus por sequência de acertos**, recebe um título ao final e pode jogar várias partidas, disputando o recorde da sessão.

## Objetivos de aprendizagem

Ao concluir este projeto, você será capaz de:

- Usar `for` com `range()` para percorrer as perguntas.
- Aplicar `if/elif/else` para escolher a pergunta e avaliar a resposta.
- Validar entradas com `while`.
- Usar **contadores e acumuladores** (acertos, pontos e sequência).
- Controlar um menu com repetição e `break`.

## Dados de partida

| **Nº** | **Pergunta** | **Alternativas** | **Correta** |
| --- | --- | --- | --- |
| 1 | Quais rios formam o Encontro das Águas, em Manaus? | A) Madeira e Purus  B) Negro e Solimões  C) Tapajós e Xingu  D) Juruá e Japurá | B |
| 2 | Qual peixe amazônico pode ultrapassar 2 metros de comprimento? | A) Tambaqui  B) Pirarucu  C) Jaraqui  D) Matrinxã | B |
| 3 | O Festival Folclórico de Parintins reúne quais bois-bumbás? | A) Garantido e Caprichoso  B) Mimoso e Caprichoso  C) Garantido e Mimoso  D) Faceiro e Caprichoso | A |
| 4 | Em qual cidade fica o Teatro Amazonas? | A) Belém  B) Manaus  C) Parintins  D) Santarém | B |
| 5 | Qual é o rio de maior volume de água do mundo? | A) Nilo  B) Mississippi  C) Amazonas  D) Yangtzé | C |

## Requisitos funcionais

| **Código** | **Requisito** |
| --- | --- |
| RF01 | **Menu principal**: 1 – Jogar, 2 – Regras, 0 – Sair, repetido até o jogador escolher sair. |
| RF02 | Em cada partida, apresentar **5 perguntas** (use `for numero in range(1, 6)` e `if/elif` para definir texto, alternativas e resposta correta). |
| RF03 | Ler a resposta do jogador, **validar** (A, B, C ou D) e dizer se acertou; se errou, informar a alternativa correta. |
| RF04 | Calcular a **pontuação** com o bônus de sequência (regras RN02 e RN03). |
| RF05 | Ao fim da partida, mostrar **acertos, pontuação e título** do jogador. |
| RF06 | Guardar o **recorde da sessão** e a **quantidade de partidas**; avisar quando houver novo recorde. |
| RF07 | Ao sair, mostrar o total de partidas e a melhor pontuação. |

## Regras de negócio

| **Código** | **Regra** |
| --- | --- |
| RN01 | A resposta é aceita em **maiúscula ou minúscula**, com ou sem espaços ao redor. Resposta fora de A–D: avisar e **perguntar de novo**, sem penalidade. |
| RN02 | Cada acerto vale **10 pontos**; erro vale 0. |
| RN03 | **Bônus de +5 pontos a cada 3 acertos seguidos**. Depois do bônus, a contagem de acertos seguidos **recomeça do zero**. Qualquer erro também zera a contagem. |
| RN04 | Título: **50 pontos ou mais**, “Guardião da Floresta”; **de 30 a 49**, “Explorador”; **abaixo de 30**, “Aprendiz”. |
| RN05 | Há **novo recorde** quando a pontuação da partida é **maior** que a melhor da sessão. |
| RN06 | Opção de menu inexistente: “Opção inválida!”. |

## Exemplo de execução

Trecho de uma execução do programa (o que o usuário digita aparece depois dos dois-pontos de cada pergunta):

**Saída esperada**

```text

=== QUIZ DA FLORESTA AMAZÔNICA ===
1 - Jogar
2 - Regras
0 - Sair
Escolha: 2

--- REGRAS ---
São 5 perguntas de múltipla escolha.
Cada acerto vale 10 pontos.
A cada 3 acertos seguidos, você ganha 5 pontos de bônus.
50+ pontos: Guardião da Floresta | 30 a 49: Explorador | abaixo de 30: Aprendiz.

=== QUIZ DA FLORESTA AMAZÔNICA ===
1 - Jogar
2 - Regras
0 - Sair
Escolha: 1

Pergunta 1 de 5
Quais rios formam o Encontro das Águas, em Manaus?
A) Madeira e Purus
B) Negro e Solimões
C) Tapajós e Xingu
D) Juruá e Japurá
Sua resposta (A, B, C ou D): B
Correto! +10 pontos.

Pergunta 2 de 5
Qual peixe amazônico pode ultrapassar 2 metros de comprimento?
```

## O que entregar

- Arquivo `projeto06_quiz.py` (VS Code) **ou** notebook `Projeto06_Quiz.ipynb` (Colab), com os nomes dos integrantes em comentário no topo.
- Quadro de **testes** com, no mínimo, 5 casos (inclua resposta inválida, sequência de 3 acertos e partida sem acertos).

## Critérios de avaliação

| **Critério** | **O que será observado** |
| --- | --- |
| Funcionamento | O jogo roda do menu ao encerramento, com várias partidas, sem travar. |
| Regras de pontuação | Pontos, bônus de sequência, títulos e recorde corretos. |
| Uso dos conteúdos | `for/range`, `if/elif/else`, `while`, contadores e acumuladores. |
| Validação | Respostas e opções inválidas tratadas conforme as regras. |
| Organização e testes | Código legível, comentado e quadro de testes coerente. |

## Dicas

- Zere `pontos`, `acertos` e `seguidos` **no início de cada partida**.
- Para aceitar “b”, “ B ” ou “B”, use `.strip().upper()` na resposta.
- Valide com `while resposta != "A" and resposta != "B" and ...` (cuidado: com `or` a condição seria sempre verdadeira).
- Quando `seguidos == 3`, some o bônus e **volte** `seguidos` **para 0**.
- Atualize o recorde **depois** de calcular a pontuação final.

## Desafios extras (opcionais)

- **Mais perguntas:** quando estudar listas, guarde as perguntas em uma lista de dicionários.
- **Dificuldade:** crie um multiplicador de pontos (fácil ×1, difícil ×2).
- **Ajuda:** uma vez por partida, elimine duas alternativas erradas (e perca 5 pontos).

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto06_quiz.py`](starter/projeto06_quiz.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
