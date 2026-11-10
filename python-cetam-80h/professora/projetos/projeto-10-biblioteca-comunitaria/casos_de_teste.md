# Casos de teste para correção – Projeto 10

| **Entrada / situação** | **Resultado esperado** |
| --- | --- |
| Primeira execução, opção 2 | Acervo inicial com 4 livros (L001 a L004), todos disponíveis |
| Cadastrar “vidas secas”, “graciliano ramos” | Cadastrado como L005 (“Vidas Secas”, “Graciliano Ramos”) |
| Cadastrar com título vazio | “Título inválido.” (nada é cadastrado) |
| Buscar “casmurro” e “xyz” | Encontra o L001; “Nenhum livro encontrado.” |
| Emprestar L001 para “marina”; depois L001 para “joão” | Registrado; “Livro indisponível (com Marina).” |
| Emprestar L099 | “Código não encontrado.” |
| Marina pega L002 e L003; depois tenta L004 | Os dois primeiros ok; “Limite de 3 empréstimos atingido.” |
| Devolver L001 com 10 dias | Atraso de 3 dias; multa R$ 1,50 |
| Devolver L001 de novo (3 dias) | “Este livro não está emprestado.” |
| Devolver L002 com 5 dias | “Devolução registrada sem multa.” |
| Relatório | 5 livros; 4 disponíveis; 1 emprestado (L003); multas R$ 1,50 |
| Fechar e reabrir | L003 continua “Emprestado a Marina”; L005 continua no acervo |
