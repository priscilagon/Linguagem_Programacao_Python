# Casos de teste para correção – Projeto 9

| **Entrada / situação** | **Resultado esperado** |
| --- | --- |
| Cadastrar “maria das dores”, “(92) 99123-4567” | Telefone salvo como 92991234567; nome “Maria Das Dores” |
| Cadastrar “ joão pedro ” com telefone “123” e e-mail “joaoemail.com” | “Telefone inválido!” e “E-mail inválido!”, com novas perguntas; salva com “92 3234-5678” → 9232345678 |
| Cadastrar “MARIA DAS DORES” novamente | “Já existe um contato com esse nome.” |
| Cadastrar “ana lima” sem bairro | Bairro “Não informado” |
| Listar | Ordem alfabética: Ana Lima, João Pedro, Maria Das Dores |
| Buscar “MAR” e “xyz” | Encontra Maria Das Dores; “Nenhum contato encontrado.” |
| Editar João Pedro (Enter, novo e-mail, Enter) | Só o e-mail muda para joao.novo@email.com; “Contato atualizado!” |
| Editar “xingu” | “Contato não encontrado.” |
| Remover Ana Lima com “n” e depois com “s” | “Remoção cancelada.”; depois “Contato removido.” |
| Resumo por bairro | Centro: 1; Compensa: 1 |
| Fechar e reabrir | Maria Das Dores e João Pedro continuam na agenda |
