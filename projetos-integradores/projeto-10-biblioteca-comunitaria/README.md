# Projeto 10 – Biblioteca Comunitária

| **Ficha do projeto** |  |
| --- | --- |
| **Tema** | Sistema de empréstimos orientado a objetos |
| **Nível** | ★★★★★ |
| **Tempo sugerido** | 12 a 16 horas |
| **Forma de trabalho** | dupla |
| **Aulas relacionadas** | Aulas 1 a 19 |
| **Conteúdos** | classes e objetos que colaboram entre si, dicionário de objetos, arquivos, validações e regras de negócio |

## Cenário

Uma biblioteca comunitária ribeirinha controla empréstimos em um caderno e vive perdendo livros e prazos. Você vai desenvolver o **sistema da Biblioteca Comunitária**, usando **duas classes que colaboram**: `Livro` (cada exemplar) e `Biblioteca` (o acervo e as operações). O sistema controla **empréstimos, devoluções e multas por atraso**, e guarda o acervo em arquivo.

Este é um projeto de **fechamento do curso**, no nível do Projeto 5. Multas e prazos são **fictícios**.

## Objetivos de aprendizagem

Ao concluir este projeto, você será capaz de:

- Modelar o problema com **duas classes que se relacionam**.
- Guardar objetos em um **dicionário** (`codigo → Livro`).
- Aplicar **regras de negócio** (prazo, multa e limite de empréstimos).
- Persistir o acervo em **arquivo** e recarregá-lo.
- Devolver **tuplas** `(sucesso, mensagem)` para separar a lógica da interface.

## Dados de partida

| **Código** | **Título (acervo inicial)** | **Autor** |
| --- | --- | --- |
| L001 | Dom Casmurro | Machado de Assis |
| L002 | Macunaíma | Mário de Andrade |
| L003 | A Selva | Ferreira de Castro |
| L004 | Memórias Póstumas de Brás Cubas | Machado de Assis |

## Requisitos funcionais

| **Código** | **Requisito** |
| --- | --- |
| RF01 | Classe `Livro` com atributos `codigo`, `titulo`, `autor` e `leitor` (texto vazio = disponível) e métodos `esta_disponivel()`, `emprestar(leitor)`, `devolver(dias)` (devolve a multa) e `descricao()`. |
| RF02 | Classe `Biblioteca` com o dicionário `livros` e os métodos `adicionar(titulo, autor)`, `buscar(codigo)`, `buscar_por_titulo(trecho)`, `emprestar(codigo, leitor)`, `devolver(codigo, dias)`, `salvar()` e `carregar()`. |
| RF03 | Na **primeira execução** (sem arquivo), criar o **acervo inicial** da tabela e salvá-lo em `acervo.txt`; nas seguintes, **carregar** o arquivo. |
| RF04 | **Menu**: 1 – Cadastrar livro, 2 – Listar acervo, 3 – Buscar por título, 4 – Emprestar, 5 – Devolver, 6 – Relatório, 0 – Sair. |
| RF05 | **Emprestar** e **devolver** devolvem uma tupla `(sucesso, mensagem)`, que o menu apenas exibe. |
| RF06 | **Relatório**: total de livros, disponíveis, emprestados e **total de multas** arrecadadas na sessão. |
| RF07 | Salvar o acervo **após cada operação** que o altere (cadastro, empréstimo e devolução). |

## Regras de negócio

| **Código** | **Regra** |
| --- | --- |
| RN01 | O **código** é gerado automaticamente no formato `L001`, `L002`... (sequência do acervo). |
| RN02 | Título e autor **não vazios** e sem “;”; padronize com `strip()` e `title()` no cadastro. |
| RN03 | **Prazo** de empréstimo: **7 dias**. Atraso: **R$ 0,50 por dia** que passar do prazo (devolução em até 7 dias: sem multa). |
| RN04 | Um leitor pode ter **no máximo 3** livros emprestados ao mesmo tempo. |
| RN05 | Não é possível emprestar livro **inexistente** ou **já emprestado** (informar com quem está), nem devolver livro **não emprestado**. |
| RN06 | O nome do leitor é padronizado com `strip()` e `title()` e **não pode ser vazio**. Os dias de uso devem ser **maiores que zero**. |
| RN07 | Busca por título: o trecho **pode estar em qualquer parte** do título, sem diferenciar maiúsculas de minúsculas. |

## Exemplo de execução

Trecho de uma execução do programa (o que o usuário digita aparece depois dos dois-pontos de cada pergunta):

**Saída esperada**

```text

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 2

--- ACERVO ---
L001 | Dom Casmurro | Machado de Assis | Disponível
L002 | Macunaíma | Mário de Andrade | Disponível
L003 | A Selva | Ferreira de Castro | Disponível
L004 | Memórias Póstumas de Brás Cubas | Machado de Assis | Disponível

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 1
Título: vidas secas
Autor: graciliano ramos
```

## O que entregar

- Arquivo `projeto10_biblioteca.py` (VS Code) **ou** notebook `Projeto10_Biblioteca.ipynb` (Colab, com o Drive montado).
- Quadro de **testes** com, no mínimo, 10 casos (incluindo persistência) e **registro de colaboração** da dupla.
- **Apresentação oral** de 5 a 7 minutos: demonstração e explicação da relação entre as duas classes.

## Critérios de avaliação

| **Critério** | **O que será observado** |
| --- | --- |
| Funcionamento | Cadastro, empréstimo, devolução com multa e relatório funcionando. |
| POO | Duas classes coerentes que colaboram; métodos devolvem valores adequados. |
| Persistência | Acervo e empréstimos salvos e recarregados corretamente. |
| Regras de negócio | RN01 a RN07 implementadas. |
| Organização, testes e apresentação | Código legível, testes completos e boa comunicação oral. |

## Dicas

- No `__init__` de `Biblioteca`, use `os.path.exists(arquivo)` para decidir entre carregar e criar o acervo inicial.
- Guarde cada livro em `self.livros[codigo] = livro`; `self.livros.get(codigo)` devolve `None` se não existir.
- Código com zeros à esquerda: `f"L{len(self.livros) + 1:03d}"`.
- Arquivo: `codigo;titulo;autor;leitor` (leitor vazio quando disponível).
- Para contar os empréstimos do leitor, percorra `self.livros.values()`.
- A tupla de retorno: `return False, "Livro indisponível."`, e no menu: `ok, msg = biblioteca.emprestar(codigo, leitor)`.

## Desafios extras (opcionais)

- **Multas em arquivo:** persista o total de multas.
- **Classe** `Leitor`**:** crie uma classe com nome e livros em posse.
- **Reserva:** permita reservar livros emprestados.
- **Mais emprestados:** conte quantas vezes cada livro foi emprestado.

## Por onde começar

1. Leia o enunciado inteiro e planeje em pseudocódigo.
2. Abra o arquivo inicial em [`starter/projeto10_biblioteca.py`](starter/projeto10_biblioteca.py).
3. Implemente um requisito por vez e teste.
4. Preencha o [quadro de testes](testes/quadro_de_testes.md).
