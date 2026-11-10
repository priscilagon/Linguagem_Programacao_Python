# Saídas de teste – Projeto 9

> Saídas geradas por execução real da `solucao.py`.

**Teste 1:** 1ª execução: cadastros e validações, listagem, busca, edição, remoção e resumo.

**Saída obtida**

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
Telefone (com DDD): 92 3234-5678
E-mail: joaoemail.com
E-mail inválido!
E-mail: joao@email.com
Bairro: compensa
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
Nome: MARIA DAS DORES
Já existe um contato com esse nome.

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 1
Nome: ana lima
Telefone (com DDD): 92988887777
E-mail: ana@email.com
Bairro:
Contato salvo!

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 2

--- AGENDA (3 contatos) ---
Ana Lima | 92988887777 | ana@email.com | Não informado
João Pedro | 9232345678 | joao@email.com | Compensa
Maria Das Dores | 92991234567 | maria@email.com | Centro

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 3
Trecho do nome: MAR
Maria Das Dores | 92991234567 | maria@email.com | Centro

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 3
Trecho do nome: xyz
Nenhum contato encontrado.

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 4
Nome do contato a editar: joão pedro
Pressione Enter para manter o valor atual.
Telefone [9232345678]:
E-mail [joao@email.com]: joao.novo@email.com
Bairro [Compensa]:
Contato atualizado!

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 4
Nome do contato a editar: xingu
Contato não encontrado.

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 5
Nome do contato a remover: ana lima
Remover Ana Lima? (s/n): n
Remoção cancelada.

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 5
Nome do contato a remover: ana lima
Remover Ana Lima? (s/n): s
Contato removido.

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 6

--- CONTATOS POR BAIRRO ---
Centro: 1
Compensa: 1

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 9
Opção inválida!

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 0
Até logo!
```

**Teste 2:** 2ª execução: os contatos foram carregados do arquivo (persistência).

**Saída obtida**

```text

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 2

--- AGENDA (2 contatos) ---
João Pedro | 9232345678 | joao.novo@email.com | Compensa
Maria Das Dores | 92991234567 | maria@email.com | Centro

=== AGENDA COMUNITÁRIA ===
1 - Cadastrar
2 - Listar
3 - Buscar por trecho do nome
4 - Editar
5 - Remover
6 - Resumo por bairro
0 - Sair
Escolha: 0
Até logo!
```

**Conteúdo do arquivo** `agenda.txt` **ao final**

**Arquivo gerado**

```text
Maria Das Dores;92991234567;maria@email.com;Centro
João Pedro;9232345678;joao.novo@email.com;Compensa
```
