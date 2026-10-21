# Saídas de teste – Projeto 10

> Saídas geradas por execução real da `solucao.py`.

**Teste 1:** 1ª execução: acervo inicial, cadastro, busca, empréstimos (limite), devoluções (multa) e relatório.

**Saída obtida**

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
Livro cadastrado com o código L005.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 1
Título:
Título inválido.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 3
Trecho do título: casmurro
L001 | Dom Casmurro | Machado de Assis | Disponível

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 3
Trecho do título: xyz
Nenhum livro encontrado.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 4
Código do livro: L001
Nome do leitor: marina
Empréstimo registrado: Dom Casmurro para Marina. Prazo: 7 dias.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 4
Código do livro: L001
Nome do leitor: joão
Livro indisponível (com Marina).

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 4
Código do livro: L099
Nome do leitor: fulano
Código não encontrado.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 4
Código do livro: L002
Nome do leitor: marina
Empréstimo registrado: Macunaíma para Marina. Prazo: 7 dias.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 4
Código do livro: L003
Nome do leitor: marina
Empréstimo registrado: A Selva para Marina. Prazo: 7 dias.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 4
Código do livro: L004
Nome do leitor: marina
Limite de 3 empréstimos atingido.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 5
Código do livro: L001
Dias com o livro: 10
Devolvido com atraso de 3 dia(s). Multa: R$ 1.50.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 5
Código do livro: L001
Dias com o livro: 3
Este livro não está emprestado.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 5
Código do livro: L002
Dias com o livro: 5
Devolução registrada sem multa.

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 6

--- RELATÓRIO ---
Livros no acervo: 5
Disponíveis: 4
Emprestados: 1
Multas arrecadadas na sessão: R$ 1.50

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 9
Opção inválida!

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 0
Até logo!
```

**Teste 2:** 2ª execução: o acervo e os empréstimos foram carregados do arquivo (persistência).

**Saída obtida**

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
L003 | A Selva | Ferreira de Castro | Emprestado a Marina
L004 | Memórias Póstumas de Brás Cubas | Machado de Assis | Disponível
L005 | Vidas Secas | Graciliano Ramos | Disponível

=== BIBLIOTECA COMUNITÁRIA ===
1 - Cadastrar livro
2 - Listar acervo
3 - Buscar por título
4 - Emprestar
5 - Devolver
6 - Relatório
0 - Sair
Escolha: 0
Até logo!
```

**Conteúdo do arquivo** `acervo.txt` **ao final**

**Arquivo gerado**

```text
L001;Dom Casmurro;Machado de Assis;
L002;Macunaíma;Mário de Andrade;
L003;A Selva;Ferreira de Castro;Marina
L004;Memórias Póstumas de Brás Cubas;Machado de Assis;
L005;Vidas Secas;Graciliano Ramos;
```
