# Projeto 9 – Agenda de Contatos Comunitária

| **Ficha do projeto** |  |
| --- | --- |
| **Tema** | Cadastro com busca, edição, remoção e persistência |
| **Nível** | ★★★★☆ |
| **Tempo sugerido** | 10 a 12 horas |
| **Forma de trabalho** | dupla |
| **Aulas relacionadas** | Aulas 1 a 17 |
| **Conteúdos** | funções, listas de dicionários, strings, validações, arquivos `.txt`, busca, edição e remoção |

## Cenário

A associação de moradores de um bairro de Manaus quer uma **agenda de contatos** digital para localizar rapidamente vizinhos, comerciantes e serviços. O sistema deve permitir **cadastrar, listar em ordem alfabética, buscar por parte do nome, editar e remover** contatos, e **guardar tudo em arquivo**.

Use apenas dados **fictícios** nos testes.

## Objetivos de aprendizagem

Ao concluir este projeto, você será capaz de:

- Implementar as operações de um **CRUD** (criar, ler, atualizar e remover).
- Persistir uma lista de dicionários em **arquivo** `.txt`.
- Validar telefone e e-mail com funções de **string**.
- Organizar o sistema em **funções**.

## Dados de partida

| **Campo** | **Exemplo** | **Regra** |
| --- | --- | --- |
| nome | Maria Das Dores | obrigatório, único, padronizado com `title()` |
| telefone | 92991234567 | só dígitos, 10 ou 11 (com DDD) |
| email | maria@email.com | contém “@” e “.” e não tem espaços |
| bairro | Centro | opcional; se vazio, “Não informado” |

## Requisitos funcionais

| **Código** | **Requisito** |
| --- | --- |
| RF01 | Ao iniciar, **carregar** os contatos de `agenda.txt` (arquivo inexistente = agenda vazia). |
| RF02 | **Menu**: 1 – Cadastrar, 2 – Listar, 3 – Buscar por trecho do nome, 4 – Editar, 5 – Remover, 6 – Resumo por bairro, 0 – Sair. |
| RF03 | **Cadastrar** contato (nome, telefone, e-mail e bairro) e salvar no arquivo. |
| RF04 | **Listar** todos os contatos em **ordem alfabética** pelo nome. |
| RF05 | **Buscar** contatos cujo nome **contenha** o trecho digitado, sem diferenciar maiúsculas de minúsculas. |
| RF06 | **Editar** telefone, e-mail e bairro de um contato: **Enter em branco mantém** o valor atual. Salvar após a edição. |
| RF07 | **Remover** um contato após **confirmação** (s/n) e salvar. |
| RF08 | **Resumo por bairro**: quantos contatos há em cada bairro (use um dicionário contador). |

## Regras de negócio

| **Código** | **Regra** |
| --- | --- |
| RN01 | Nome padronizado com `strip()` e `title()`; **não vazio, sem “;” e sem repetição** na agenda. |
| RN02 | Telefone: remover espaços, hífens e parênteses; aceitar **somente dígitos com 10 ou 11 caracteres**. Inválido: pedir de novo (no cadastro) ou **manter o valor anterior** (na edição). |
| RN03 | E-mail: converter para minúsculas; deve conter “@” e “.”, **não** conter espaços nem “;”. |
| RN04 | Bairro: padronizar com `title()`, remover “;” e usar “Não informado” se vazio. |
| RN05 | Busca, edição e remoção por nome inexistente: avisar “Contato não encontrado.” sem erro. |
| RN06 | Os dados devem **permanecer** ao fechar e reabrir o programa. |

## Exemplo de execução

Trecho de uma execução do programa (o que o usuário digita aparece depois dos dois-pontos de cada pergunta):

**Saída esperada**

```text

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 1
Nome: maria das dores
Telefone (com DDD): (92) 99123-4567
E-mail: maria@email.com
Bairro: centro
Contato salvo!

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 1
Nome:  joão pedro
Telefone (com DDD): 123
Telefone inválido! Use 10 ou 11 dígitos (com DDD).
```

## O que entregar

- Arquivo `projeto09_agenda.py` (VS Code) **ou** notebook `Projeto09_Agenda.ipynb` (Colab, com o Drive montado).
- Quadro de **testes** com, no mínimo, 8 casos (incluindo persistência) e **registro de colaboração** da dupla.

## Critérios de avaliação

| **Critério** | **O que será observado** |
| --- | --- |
| Funcionamento | Cadastro, listagem, busca, edição, remoção e resumo funcionando. |
| Persistência | Dados gravados e recarregados; alterações refletidas no arquivo. |
| Validações | Telefone, e-mail, nome e bairro tratados conforme as regras. |
| Funções e estruturas | Funções coesas; lista de dicionários bem usada. |
| Organização e colaboração | Código legível, testes e registro da dupla. |

## Dicas

- Cada linha do arquivo: `nome;telefone;email;bairro`. Ao ler, use `linha.strip().split(";")`.
- Para limpar o telefone: `for simbolo in " -()": texto = texto.replace(simbolo, "")`.
- Para listar em ordem: monte uma lista só com os nomes, use `.sort()` e busque cada contato pelo nome.
- Crie `buscar_contato(contatos, nome)` e reutilize em cadastro, edição e remoção.
- Para remover: `contatos.remove(contato)` e depois `salvar_contatos(contatos)`.
- Telefone (`isdigit()` e `len()`) e e-mail (`in`) são validações de **formato**.

## Desafios extras (opcionais)

- **Exportar CSV:** grave `agenda.csv` com cabeçalho.
- **Telefone repetido:** impeça dois contatos com o mesmo telefone.
- **Listar por bairro:** peça um bairro e mostre só os contatos dele.
- **Backup:** copie a agenda para `agenda_backup.txt` antes de cada remoção.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto09_agenda.py`](starter/projeto09_agenda.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
