# Projeto 8 – Forca Amazônica

| **Ficha do projeto** |  |
| --- | --- |
| **Tema** | Jogo da forca com palavras da fauna e da flora regionais |
| **Nível** | ★★★☆☆ |
| **Tempo sugerido** | 8 a 10 horas |
| **Forma de trabalho** | dupla |
| **Aulas relacionadas** | Aulas 1 a 16 |
| **Conteúdos** | funções com parâmetros e retorno, tuplas, listas, strings, laços e decisões |

## Cenário

Uma escola quer um **jogo da forca** para treinar o vocabulário sobre a **fauna e a flora da Amazônia**. O jogador tem **6 vidas**, tenta descobrir a palavra letra por letra e acumula pontos ao longo das rodadas.

O código deve ser organizado em **funções**, cada uma com uma responsabilidade clara.

## Objetivos de aprendizagem

Ao concluir este projeto, você será capaz de:

- Criar e combinar **funções** com parâmetros e retorno (inclusive retornando mais de um valor).
- Usar **tuplas** (palavra e dica) e **listas** (letras acertadas e erradas).
- Manipular **strings** (`lower`, `strip`, `isalpha`, percorrer letras).
- Controlar rodadas com `while` e pontuação acumulada.

## Dados de partida

| **Rodada** | **Palavra** | **Dica** |
| --- | --- | --- |
| 1 | tambaqui | Peixe de escamas, famoso na culinária do Amazonas |
| 2 | pirarucu | Um dos maiores peixes de água doce, pode passar de 2 metros |
| 3 | tucunare | Peixe de rios e lagos, muito procurado na pesca esportiva |
| 4 | castanha | Semente de árvore gigante, também chamada castanha-do-pará |
| 5 | cupuacu | Fruta de polpa cremosa, usada em sucos e doces |
| 6 | jaraqui | Peixe pequeno e muito consumido pelos manauaras |

## Requisitos funcionais

| **Código** | **Requisito** |
| --- | --- |
| RF01 | Guardar as palavras e dicas em uma **tupla de tuplas** `PALAVRAS` (sem acentos, como na tabela). |
| RF02 | Função `escolher_palavra(numero_rodada)`: devolve a palavra e a dica da rodada (a rodada 7 volta à palavra da rodada 1). |
| RF03 | Função `montar_exibicao(palavra, acertadas)`: devolve o texto da palavra com `_` nas letras ainda não descobertas (ex.: `t a _ b _ q _ i`). |
| RF04 | Função `venceu(palavra, acertadas)`: devolve `True` se todas as letras foram descobertas. |
| RF05 | Função `ler_letra(tentadas)`: lê e valida uma letra, repetindo a pergunta até receber uma entrada válida. |
| RF06 | Função `jogar_rodada(numero_rodada)`: executa uma rodada e devolve `(ganhou, pontos)`. |
| RF07 | Função `principal()`: controla as rodadas, mantém o **placar** (pontos e vitórias) e pergunta “Jogar outra rodada? (s/n)”. |

## Regras de negócio

| **Código** | **Regra** |
| --- | --- |
| RN01 | O jogador começa cada rodada com **6 vidas**; cada letra errada tira uma vida. Com 0 vidas, a rodada termina em derrota. |
| RN02 | A letra digitada é padronizada com `strip()` e `lower()`. Só vale **uma letra** de “a” a “z”. |
| RN03 | Letra **já tentada** (certa ou errada): avisar e pedir outra, **sem perder vida**. |
| RN04 | Vitória: pontos da rodada = **10 + 5 × vidas restantes**. Derrota: **0 ponto**. |
| RN05 | A cada rodada, mostrar a dica, a palavra parcial, as vidas e as letras erradas. |
| RN06 | Ao encerrar, mostrar o número de rodadas, vitórias e pontuação total. |

## Exemplo de execução

Trecho de uma execução do programa (o que o usuário digita aparece depois dos dois-pontos de cada pergunta):

**Saída esperada**

```text

=== RODADA 1 ===
Dica: Peixe de escamas, famoso na culinária do Amazonas

Palavra: _ _ _ _ _ _ _ _
Vidas: O O O O O O
Digite uma letra: t
Acertou!

Palavra: t _ _ _ _ _ _ _
Vidas: O O O O O O
Digite uma letra: x
Errou!

Palavra: t _ _ _ _ _ _ _
Vidas: O O O O O X
Letras erradas: ['x']
Digite uma letra: t
Você já tentou essa letra!
Digite uma letra: 12
Digite apenas UMA letra (de a a z).
Digite uma letra: ab
Digite apenas UMA letra (de a a z).
Digite uma letra: a
Acertou!

Palavra: t a _ _ a _ _ _
Vidas: O O O O O X
Letras erradas: ['x']
Digite uma letra: m
```

## O que entregar

- Arquivo `projeto08_forca.py` ou notebook `Projeto08_Forca.ipynb`, com nomes da dupla no topo.
- Quadro de **testes** com, no mínimo, 6 casos e **registro de colaboração** (quem fez cada função).

## Critérios de avaliação

| **Critério** | **O que será observado** |
| --- | --- |
| Funcionamento | Rodadas completas (vitória e derrota) e placar corretos. |
| Modularização | Funções com responsabilidade única, parâmetros e `return` adequados. |
| Strings e listas | Letras certas/erradas controladas; exibição correta. |
| Regras de negócio | RN01 a RN06 implementadas. |
| Organização e colaboração | Código legível, testes e registro da dupla. |

## Dicas

- `for letra in palavra:` percorre as letras de um texto.
- Mantenha duas listas: `acertadas` e `erradas`. A lista de **tentadas** é `acertadas + erradas`.
- Uma função pode devolver dois valores: `return True, pontos` — e quem chama recebe com `ganhou, pontos = jogar_rodada(1)`.
- Para mostrar as vidas: `"O " * vidas + "X " * len(erradas)`.
- Com a tupla `(palavra, dica)`, use `palavra, dica = escolher_palavra(numero)`.

## Desafios extras (opcionais)

- **Desenho da forca:** crie uma tupla com 7 desenhos em ASCII e mostre o estágio de acordo com os erros.
- **Palavras sorteadas:** use `import random` e `random.choice(PALAVRAS)`.
- **Placar em arquivo:** grave o recorde de pontos em `placar.txt`.
- **Mais categorias:** organize palavras por tema em um dicionário.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto08_forca.py`](starter/projeto08_forca.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
