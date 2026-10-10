# Projeto 4 – Boletim Escolar Digital

| Ficha do projeto |  |
| --- | --- |
| **Tema** | Cadastro de alunos e notas com persistência em arquivo |
| **Nível** | ★★★★★ |
| **Conteúdos** | Aulas 1 a 17: listas de dicionários, funções, strings, arquivos `.txt` (leitura e escrita), laços e decisões |
| **Tempo sugerido** | 8 a 12 horas |
| **Organização** | dupla |

## Cenário

Uma escola quer abandonar o boletim em papel. Você foi contratado(a) para criar o **Boletim Escolar Digital**: o professor cadastra alunos e suas três notas, o sistema calcula a média e a situação, e **guarda tudo em arquivo**, para que os dados não se percam ao fechar o programa. Também deve gerar um **relatório** em arquivo de texto.

## Objetivos de aprendizagem

- Combinar **listas e dicionários** (lista de alunos; notas em lista).
- Persistir dados com **leitura e escrita de arquivos .txt**.
- Organizar o sistema em **funções** reutilizáveis.
- Calcular estatísticas e gerar relatório.

## Requisitos funcionais

| Código | O sistema deve... |
| --- | --- |
| RF01 | Ao iniciar, **carregar** os alunos de `boletim.txt` (se o arquivo ainda não existir, começar com a lista vazia). |
| RF02 | **Menu**: 1 – Cadastrar aluno, 2 – Listar boletim, 3 – Buscar aluno, 4 – Estatísticas da turma, 5 – Exportar relatório, 0 – Sair. |
| RF03 | **Cadastrar** aluno com nome e **3 notas** (0 a 10) e **salvar** no arquivo imediatamente. |
| RF04 | **Listar** o boletim: nome, as três notas, **média** e **situação** de cada aluno. |
| RF05 | **Buscar** um aluno pelo nome (sem diferenciar maiúsculas/minúsculas) e mostrar seu boletim. |
| RF06 | **Estatísticas**: média da turma, aluno com a maior média e quantidade de alunos em cada situação. |
| RF07 | **Exportar** um relatório para `relatorio.txt` com uma linha `nome;média;situação` por aluno. |

## Regras de negócio

| Código | Regra |
| --- | --- |
| RN01 | Notas válidas: de **0 a 10**. Fora da faixa, avisar e pedir de novo. |
| RN02 | **Média** = soma das três notas dividida por 3. **≥ 7**: Aprovado; **≥ 5 e < 7**: Recuperação; **< 5**: Reprovado. |
| RN03 | Não cadastrar aluno com **nome repetido**, vazio ou contendo `;` (o ponto e vírgula é o separador do arquivo). |
| RN04 | Nomes são padronizados com `strip()` e `title()`. |
| RN05 | Com a lista vazia, listar e estatísticas devem avisar “Nenhum aluno cadastrado.” sem gerar erro. |
| RN06 | Os dados devem **permanecer** ao fechar e reabrir o programa. |

## Exemplo de execução

Trecho de uma execução (o que o usuário digita aparece após os dois pontos):

```text

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 1
Nome do aluno: ana lima
Nota 1 (0 a 10): 8
Nota 2 (0 a 10): 7
Nota 3 (0 a 10): 9
Aluno cadastrado e salvo!

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
```

## O que entregar

- Arquivo `projeto4_boletim.py` (VS Code) **ou** notebook `Projeto4_Boletim.ipynb` (Colab, com o Drive montado para guardar os arquivos).
- Quadro de **testes** com, no mínimo, 6 casos, incluindo a **prova de persistência** (fechar e reabrir) e o registro de colaboração da dupla.

## Critérios de avaliação

| Critério | O que será observado |
| --- | --- |
| Funcionamento | Cadastro, listagem, busca, estatísticas e exportação funcionando. |
| Persistência | Dados gravados e recarregados corretamente; relatório gerado. |
| Funções e estruturas | Funções coesas; lista de dicionários e notas em lista. |
| Regras de negócio | Validações e situação corretas (RN01 a RN06). |
| Organização e colaboração | Código legível, testes e registro da dupla. |

## Dicas

- Cada linha do arquivo pode ser `nome;nota1;nota2;nota3`. Ao ler, use `linha.strip().split(";")`.
- Guarde as notas em uma **lista** dentro do dicionário: `{"nome": "Ana Lima", "notas": [8.0, 7.0, 9.0]}`.
- No Colab, os arquivos somem ao fim da sessão: monte o Google Drive (Aula 17). No VS Code, abra a **pasta** do projeto.
- Crie funções pequenas: `calcular_media`, `situacao`, `ler_nota`, `buscar_aluno`, `salvar_alunos`, `carregar_alunos`.

## Desafios extras (opcionais)

- **Ranking:** mostre os alunos em ordem decrescente de média.
- **Pesos:** troque a média simples por média ponderada (pesos 2, 3 e 5).
- **Edição:** permita corrigir uma nota ou remover um aluno.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto04_boletim.py`](starter/projeto04_boletim.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
