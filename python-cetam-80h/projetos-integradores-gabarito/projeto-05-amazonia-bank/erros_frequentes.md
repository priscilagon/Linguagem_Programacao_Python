# Erros frequentes – Projeto 5

- **Esquecer o `self`** nos métodos ou escrever `saldo += valor` em vez de `self.saldo += valor`.
- **Salvar o arquivo só ao sair**: se o programa for interrompido, as operações são perdidas.
- **Comparar a senha com `==` sem tratar espaços** ou aceitar senhas de tamanho diferente.
- **Transferir sem atualizar a conta de destino** ou sem passar o **objeto** (e não o nome) como `destino`.
- **Gravar o saldo com `float` sem formatação**, gerando valores como `179.49999999999997`: use `:.2f`.
- **Não verificar `nome_destino in contas`**, causando `KeyError`.
- Mostrar a mensagem “realizado” dentro do método e de novo no menu (duplicidade): o método deve apenas devolver `True`/`False`.
