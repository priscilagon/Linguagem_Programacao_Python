# Linguagem de Programação Python – CETAM (80h)

![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?logo=python&logoColor=white)
![Carga horária](https://img.shields.io/badge/carga%20hor%C3%A1ria-80h-1F6FB2)
![Aulas](https://img.shields.io/badge/aulas-20-1B7F4B)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-C9A227)
[![Começar no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/priscilagon/python-cetam-80h/blob/main/aulas/fase-1-fundamentos/aula-01-abertura-e-conceituacao/aula-01.ipynb)

Material didático do curso de **Qualificação Profissional em Linguagem de Programação Python** do **CETAM – Centro de Educação Tecnológica do Amazonas** (PPC versão 001/DAC-2026), para quem **nunca programou**.

Você vai aprender **Python do zero**, usando o **Google Colab** e o **Visual Studio Code**, e construir, ao longo de 20 aulas, o sistema de uma agência de turismo fictícia do Amazonas: a **Agência Amazônia Tur Digital**.

---

## Sumário

- [O que você vai aprender](#-o-que-você-vai-aprender)
- [Como usar este repositório](#-como-usar-este-repositório)
- [Estrutura do repositório](#-estrutura-do-repositório)
- [Mapa das 20 aulas](#-mapa-das-20-aulas)
- [Projeto integrador](#-projeto-integrador-agência-amazônia-tur-digital)
- [Projetos integradores para praticar](#-projetos-integradores-para-praticar)
- [Avaliações](#-avaliações)
- [Para professores](#-para-professores)
- [Contribuindo](#-contribuindo)
- [Licença e autoria](#-licença-e-autoria)

---

## O que você vai aprender

- Preparar o ambiente de programação no **Colab** e no **VS Code**.
- Usar **variáveis, tipos de dados, entrada e saída** (`print`, `input`).
- Fazer cálculos com **operadores** aritméticos, relacionais e lógicos.
- Tomar decisões com **`if`, `elif` e `else`**.
- Repetir tarefas com **`while` e `for`**, controlando o fluxo com `break`, `continue` e `pass`.
- Organizar dados em **listas, tuplas, dicionários** e manipular **strings**.
- Dividir o programa em **funções** (parâmetros, retorno e escopo).
- Gravar e ler dados em **arquivos `.txt`**.
- Dar os primeiros passos em **Programação Orientada a Objetos** (classes e objetos).

**Pré-requisitos:** nenhum conhecimento prévio de programação. Basta um computador (ou celular/tablet com navegador, para o Colab) e conta Google.

---

## Como usar este repositório

### Opção 1 – Google Colab (sem instalar nada)

Abra o notebook da aula pelo botão **Abrir no Colab** no `README.md` de cada aula. Exemplo: [Aula 01 no Colab](https://colab.research.google.com/drive/1hIcf39hufCkqK2u99UL5RyjCSHeQ4H-u?usp=sharing).

### Opção 2 – VS Code (no seu computador)

```bash
git clone https://github.com/priscilagon/python-cetam-80h.git
cd python-cetam-80h
code .
```

Execute um exemplo:

```bash
python aulas/fase-1-fundamentos/aula-01-abertura-e-conceituacao/exemplos/01_ola_amazonas.py
```

Guia completo de instalação: **[docs/SETUP.md](docs/SETUP.md)**.

### Dica: repetir testes sem digitar tudo de novo

```bash
python tools/simular_entrada.py aulas/fase-1-fundamentos/aula-02-tipos-variaveis-entrada-saida/exemplos/02_entrada_de_dados.py aulas/fase-1-fundamentos/aula-02-tipos-variaveis-entrada-saida/exemplos/entradas/02_entrada_de_dados.txt
```

### Rotina de estudo sugerida

1. Leia o `README.md` da aula.
2. **Digite** (não copie!) e execute os exemplos; depois altere valores e observe.
3. Resolva `exercicios/enunciados.md`.
4. Avance o **projeto integrador** com o desafio da aula.

---

## Estrutura do repositório

```text
python-cetam-80h/
├── README.md                          ← você está aqui
├── LICENSE                            ← licença MIT
├── CONTRIBUTING.md                    ← como contribuir
├── requirements.txt                   ← dependências (apenas opcionais)
├── .gitignore
├── .github/
│   └── workflows/
│       └── verificar-codigo.yml       ← verifica a sintaxe dos .py a cada push
├── docs/                              ← guias de apoio
│   ├── SETUP.md                       ← Colab e VS Code passo a passo
│   ├── CRONOGRAMA.md                  ← as 20 aulas
│   ├── AVALIACOES.md                  ← AV1 a AV4
│   ├── GIT_BASICO.md                  ← Git e GitHub para o portfólio
│   ├── GLOSSARIO.md
│   └── REFERENCIAS.md
├── material/
│   └── Apostila_Python_CETAM_80h.pdf ← apostila do aluno
├── aulas/                             ← 6 fases, 20 aulas
│   ├── fase-1-fundamentos/            ← aulas 01 a 04
│   ├── fase-2-decisao/                ← aulas 05 a 07
│   ├── fase-3-repeticao/              ← aulas 08 a 10
│   ├── fase-4-organizacao-de-dados/   ← aulas 11 a 14
│   ├── fase-5-modularizacao-e-persistencia/  ← aulas 15 a 17
│   └── fase-6-poo-e-integracao/       ← aulas 18 a 20
│       └── aula-NN-tema/
│           ├── README.md              ← resumo e links
│           ├── aula-NN.ipynb          ← notebook para o Colab
│           ├── exemplos/              ← códigos testados (.py)
│           │   └── entradas/          ← entradas de teste (.txt)
│           └── exercicios/
│               └── enunciados.md
├── projeto-integrador-agencia-tur/    ← projeto construído ao longo do curso
│   ├── README.md
│   └── starter/                       ← v1 a v6 (com TODO)
├── projetos-integradores/             ← 10 projetos para praticar (1 a 5 e 6 a 10)
│   ├── README.md
│   └── projeto-NN-tema/
│       ├── README.md                  ← enunciado
│       ├── starter/                   ← esqueleto do código
│       └── testes/quadro_de_testes.md
├── tools/
│   └── simular_entrada.py             ← simula o teclado nos testes
└── _professor/                        ← NÃO publicado (está no .gitignore)
```

---

## Mapa das 20 aulas

| Fase | Aula | Tema | Avaliação |
| --- | --- | --- | --- |
| 1 | [01](aulas/fase-1-fundamentos/aula-01-abertura-e-conceituacao/) | Abertura e conceituação | diagnóstica (sem nota) e participação |
| 1 | [02](aulas/fase-1-fundamentos/aula-02-tipos-variaveis-entrada-saida/) | Tipos de dados, variáveis, entrada e saída | formativa, pelo checklist da prática |
| 1 | [03](aulas/fase-1-fundamentos/aula-03-operadores-aritmeticos/) | Operadores aritméticos | formativa, pela entrega da lista de exercícios |
| 1 | [04](aulas/fase-1-fundamentos/aula-04-operadores-relacionais-e-logicos/) | Operadores relacionais e lógicos; estrutura de um algoritmo | formativa; Calculadora v1 com devolutiva qualitativa |
| 2 | [05](aulas/fase-2-decisao/aula-05-if-else/) | Estrutura condicional if / else | formativa |
| 2 | [06](aulas/fase-2-decisao/aula-06-elif-e-condicoes-compostas/) | elif, condições encadeadas e compostas | formativa |
| 2 | [07](aulas/fase-2-decisao/aula-07-consolidacao-fase-2-e-av1/) | Consolidação da Fase 2 e AV1 | AV1 – prática individual em laboratório |
| 3 | [08](aulas/fase-3-repeticao/aula-08-laco-while/) | Laço while | formativa |
| 3 | [09](aulas/fase-3-repeticao/aula-09-laco-for-e-range/) | Laço for e range() | formativa |
| 3 | [10](aulas/fase-3-repeticao/aula-10-break-continue-menu-e-av2/) | break, continue, pass, menu interativo e AV2 | AV2 – prática em duplas, com registro de colaboração |
| 4 | [11](aulas/fase-4-organizacao-de-dados/aula-11-listas/) | Listas | formativa |
| 4 | [12](aulas/fase-4-organizacao-de-dados/aula-12-tuplas-e-dicionarios/) | Tuplas e dicionários | formativa |
| 4 | [13](aulas/fase-4-organizacao-de-dados/aula-13-manipulacao-de-strings/) | Manipulação de strings | formativa |
| 4 | [14](aulas/fase-4-organizacao-de-dados/aula-14-consolidacao-fase-4-e-av3/) | Consolidação da Fase 4 e AV3 | AV3 – prova prática e teórica individual |
| 5 | [15](aulas/fase-5-modularizacao-e-persistencia/aula-15-funcoes-com-def/) | Funções com def | formativa |
| 5 | [16](aulas/fase-5-modularizacao-e-persistencia/aula-16-parametros-retorno-e-escopo/) | Parâmetros, argumentos, retorno e escopo | formativa, com checklist de code review |
| 5 | [17](aulas/fase-5-modularizacao-e-persistencia/aula-17-arquivos-txt/) | Arquivos .txt | formativa |
| 6 | [18](aulas/fase-6-poo-e-integracao/aula-18-fundamentos-de-poo/) | Fundamentos de Programação Orientada a Objetos | formativa |
| 6 | [19](aulas/fase-6-poo-e-integracao/aula-19-oficina-do-cofre-digital/) | Desenvolvimento do cofre digital (oficina de projeto) | formativa, com acompanhamento do docente e registro do progresso |
| 6 | [20](aulas/fase-6-poo-e-integracao/aula-20-apresentacao-final-e-av4/) | Apresentação final, AV4 e encerramento | AV4 – avaliação somativa final |

Cada fase termina com uma entrega do projeto integrador:

| Fase | Foco | Entrega |
| --- | --- | --- |
| [1](aulas/fase-1-fundamentos/) | Descoberta e Fundamentos | Calculadora de viagem v1 |
| [2](aulas/fase-2-decisao/) | Decisão | Calculadora de viagem v2 |
| [3](aulas/fase-3-repeticao/) | Repetição | Menu interativo |
| [4](aulas/fase-4-organizacao-de-dados/) | Organização de Dados | Cadastro em memória |
| [5](aulas/fase-5-modularizacao-e-persistencia/) | Modularização e Persistência | Sistema modular com dados salvos |
| [6](aulas/fase-6-poo-e-integracao/) | POO e Integração | Cofre digital (sistema final) |

---

## Projeto integrador: Agência Amazônia Tur Digital

Você constrói, aula após aula, o sistema de uma agência de turismo fictícia — de uma simples calculadora de viagem até um **cofre digital** com cadastro, login e dados salvos em arquivo.

| Versão | Entrega | Fase |
| --- | --- | --- |
| v1 | Calculadora de viagem v1 | 1 |
| v2 | Calculadora de viagem v2 | 2 |
| v3 | Menu interativo | 3 |
| v4 | Cadastro em memória | 4 |
| v5 | Sistema modular com dados salvos | 5 |
| v6 | Cofre digital (sistema final) | 6 |

 Veja os arquivos iniciais e as regras em **[projeto-integrador-agencia-tur/](projeto-integrador-agencia-tur/)**.

---

## Projetos integradores para praticar

Dez projetos em **dificuldade crescente** (dois ciclos de cinco), com enunciado, requisitos, regras de negócio, esqueleto de código e quadro de testes.

| Projeto | Nível | Conteúdos |
| --- | --- | --- |
| [1 – Caixa da Feira do Produtor](projetos-integradores/projeto-01-caixa-da-feira/) | ★★★★★ | variáveis, tipos, `input()`, operadores, `if/elif/else`, `while`, `break`, `continue` |
| [2 – Monitor Fluvial: Nível do Rio Negro](projetos-integradores/projeto-02-monitor-fluvial/) | ★★★★★ | listas, dicionários, strings, `for`/`range`, decisões, métodos de listas e funções internas |
| [3 – Estoque da Cooperativa Ribeirinha](projetos-integradores/projeto-03-estoque-da-cooperativa/) | ★★★★★ | dicionários aninhados, funções com parâmetros e retorno, menu com `while`, validações, strings |
| [4 – Boletim Escolar Digital](projetos-integradores/projeto-04-boletim-escolar-digital/) | ★★★★★ | listas de dicionários, funções, strings, arquivos `.txt` (leitura e escrita), laços e decisões |
| [5 – Amazônia Bank: Mini-Banco Digital](projetos-integradores/projeto-05-amazonia-bank/) | ★★★★★ | classes e objetos, métodos, atributos, dicionário de objetos, arquivos, funções, menus aninhados e validações |
| [6 – Quiz da Floresta Amazônica](projetos-integradores/projeto-06-quiz-da-floresta-amazonica/) | ★★★★★ | variáveis, `input()`, operadores, `if/elif/else`, `while`, `for`/`range`, contadores e acumuladores |
| [7 – Meu Orçamento Familiar](projetos-integradores/projeto-07-meu-orcamento-familiar/) | ★★★★★ | listas, dicionários, listas de dicionários, strings, `for`/`range`, decisões e validações |
| [8 – Forca Amazônica](projetos-integradores/projeto-08-forca-amazonica/) | ★★★★★ | funções com parâmetros e retorno, tuplas, listas, strings, laços e decisões |
| [9 – Agenda de Contatos Comunitária](projetos-integradores/projeto-09-agenda-de-contatos-comunitaria/) | ★★★★★ | funções, listas de dicionários, strings, validações, arquivos `.txt`, busca, edição e remoção |
| [10 – Biblioteca Comunitária](projetos-integradores/projeto-10-biblioteca-comunitaria/) | ★★★★★ | classes e objetos que colaboram entre si, dicionário de objetos, arquivos, validações e regras de negócio |

---

## Avaliações

O curso tem avaliação diagnóstica, avaliações formativas e quatro atividades avaliativas (**AV1 a AV4**). Detalhes em **[docs/AVALIACOES.md](docs/AVALIACOES.md)**.

---

## Para professores

A pasta `_professor/` (gabaritos, soluções de referência e matrizes de correção) está no `.gitignore` e **não é publicada**. Se este repositório for público, **não remova** essa linha. Veja `_professor/README.md` na sua cópia local.

---

## Contribuindo

Encontrou um erro ou tem uma sugestão? Abra uma **Issue** ou um **Pull Request**. Veja **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## Licença e autoria

Distribuído sob a licença **MIT** — veja [LICENSE](LICENSE).

**Autoria:** Profa. Priscila Gonçalves • CETAM • Manaus – Amazonas
GitHub: [@priscilagon](https://github.com/priscilagon)

> Todos os dados e valores usados nos exemplos e projetos são **fictícios**, criados apenas para fins didáticos.
