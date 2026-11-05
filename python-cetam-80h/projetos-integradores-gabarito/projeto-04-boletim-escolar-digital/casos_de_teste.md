# Casos de teste para correção – Projeto 4

| Entrada / situação | Resultado esperado |
| --- | --- |
| Cadastrar Ana Lima (8, 7, 9) | Média 8,00 – Aprovado |
| Cadastrar Bruno Souza (4, “11”, 5, 3,5) | “Nota inválida!” para 11; média 4,17 – Reprovado |
| Cadastrar Carla Dias (6, 5, 7) | Média 6,00 – Recuperação |
| Cadastrar “ANA LIMA” novamente | “Aluno já cadastrado!” (nome padronizado) |
| Buscar “ana lima” e “xyz” | Mostra o boletim de Ana; “Aluno não encontrado.” |
| Estatísticas | Média da turma 6,06; maior média Ana Lima (8,00); 1 Aprovado, 1 Recuperação, 1 Reprovado |
| Exportar relatório | `relatorio.txt` com 3 linhas `nome;média;situação` |
| Fechar e reabrir o programa | Os 3 alunos continuam na listagem |
| Listar com `boletim.txt` inexistente | “Nenhum aluno cadastrado.” (sem erro) |
