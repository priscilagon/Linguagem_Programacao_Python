# Erros frequentes – Projeto 9

- **Editar o contato mas esquecer de chamar** `salvar_contatos`: a alteração some ao reabrir.
- **Remover um item da lista dentro de um** `for` **sobre ela mesma** (pula elementos).
- **Comparar o trecho sem padronizar** (`"mar" in "Maria"` é falso por causa da maiúscula).
- **Não limpar o telefone** antes de validar: “(92) 99123-4567” é considerado inválido.
- **Aceitar “;” nos dados**: a leitura do arquivo quebra com `ValueError`.
- **Esquecer o** `.strip()` ao ler o arquivo, deixando o `\n` no último campo.
- **Usar o modo** `"a"` **ao salvar tudo**: duplica todos os contatos a cada gravação.
