# Erros frequentes – Projeto 10

- **Esquecer o** `self` nos métodos ou nos atributos (`titulo = titulo` em vez de `self.titulo = titulo`).
- **Multar no prazo**: usar `dias >= PRAZO_DIAS` em vez de `dias > PRAZO_DIAS`.
- **Esquecer de limpar o leitor** ao devolver, deixando o livro “emprestado”.
- **Gravar o campo** `leitor` **ausente**: a linha fica com 3 campos e a leitura falha; grave sempre os 4 campos.
- **Criar o acervo inicial a cada execução**, duplicando os livros.
- **Imprimir dentro das classes e de novo no menu** (mensagens duplicadas): os métodos devem **devolver** a mensagem.
- **Contar empréstimos do leitor** com nome diferente por não padronizar (`marina` ≠ `Marina`).
