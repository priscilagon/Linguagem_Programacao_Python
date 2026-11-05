# Saídas de teste – Projeto 4

## 1ª execução: cadastros, duplicidade, nota inválida, listagem, busca, estatísticas e exportação

**Entradas:** `1` → `ana lima` → `8` → `7` → `9` → `1` → `bruno souza` → `4` → `11` → `5` → `3.5` → `1` → `carla dias` → `6` → `5` → `7` → `1` → `ANA LIMA` → `2` → `3` → `ana lima` → `3` → `xyz` → `4` → `5` → `9` → `0`

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
Escolha: 1
Nome do aluno: bruno souza
Nota 1 (0 a 10): 4
Nota 2 (0 a 10): 11
Nota inválida! Digite um valor entre 0 e 10.
Nota 2 (0 a 10): 5
Nota 3 (0 a 10): 3.5
Aluno cadastrado e salvo!

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 1
Nome do aluno: carla dias
Nota 1 (0 a 10): 6
Nota 2 (0 a 10): 5
Nota 3 (0 a 10): 7
Aluno cadastrado e salvo!

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 1
Nome do aluno: ANA LIMA
Aluno já cadastrado!

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 2

--- BOLETIM ---
Ana Lima | Notas: 8.0 / 7.0 / 9.0 | Média: 8.00 | Aprovado
Bruno Souza | Notas: 4.0 / 5.0 / 3.5 | Média: 4.17 | Reprovado
Carla Dias | Notas: 6.0 / 5.0 / 7.0 | Média: 6.00 | Recuperação

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 3
Nome: ana lima
Ana Lima | Notas: 8.0 / 7.0 / 9.0 | Média: 8.00 | Aprovado

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 3
Nome: xyz
Aluno não encontrado.

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 4

--- ESTATÍSTICAS DA TURMA ---
Média da turma: 6.06
Maior média: Ana Lima (8.00)
Aprovado: 1
Recuperação: 1
Reprovado: 1

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 5
Relatório gravado em relatorio.txt.

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 9
Opção inválida!

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 0
Até logo!
```

## 2ª execução: os alunos foram carregados do arquivo (persistência)

**Entradas:** `2` → `0`

```text

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 2

--- BOLETIM ---
Ana Lima | Notas: 8.0 / 7.0 / 9.0 | Média: 8.00 | Aprovado
Bruno Souza | Notas: 4.0 / 5.0 / 3.5 | Média: 4.17 | Reprovado
Carla Dias | Notas: 6.0 / 5.0 / 7.0 | Média: 6.00 | Recuperação

=== BOLETIM ESCOLAR DIGITAL ===
1 - Cadastrar aluno
2 - Listar boletim
3 - Buscar aluno
4 - Estatísticas da turma
5 - Exportar relatório
0 - Sair
Escolha: 0
Até logo!
```

## Conteúdo do arquivo relatorio.txt gerado

```text
RELATÓRIO DA TURMA
Ana Lima;8.00;Aprovado
Bruno Souza;4.17;Reprovado
Carla Dias;6.00;Recuperação
```
