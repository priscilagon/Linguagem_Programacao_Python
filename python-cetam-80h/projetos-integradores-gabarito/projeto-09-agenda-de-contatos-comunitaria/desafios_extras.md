# Orientações para os desafios extras – Projeto 9

- **Exportar CSV:** gravar a linha de cabeçalho `nome,telefone,email,bairro` e uma linha por contato com `f.write(f"{c['nome']},...\n")`.
- **Telefone repetido:** percorrer a lista comparando `c["telefone"] == telefone` antes de salvar.
- **Listar por bairro:** `for c in contatos: if c["bairro"] == bairro: print(formatar(c))`.
- **Backup:** ler `agenda.txt` e gravar o mesmo conteúdo em `agenda_backup.txt` (modo `"w"`).
