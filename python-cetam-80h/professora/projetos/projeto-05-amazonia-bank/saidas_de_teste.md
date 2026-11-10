# Saídas de teste – Projeto 5

## 1ª execução: criação de contas, validações, login, operações, extrato

**Entradas:** `1` → `marina silva` → `1234` → `1` → `joão pedro` → `12ab` → `1` → `JOÃO PEDRO` → `4321` → `1` → `marina silva` → `2` → `marina silva` → `0000` → `2` → `marina silva` → `1234` → `2` → `500` → `3` → `800` → `3` → `120.50` → `2` → `-5` → `4` → `xingu` → `4` → `marina silva` → `4` → `joão pedro` → `200` → `1` → `5` → `0` → `0`

```text

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: marina silva
Senha (4 dígitos): 1234
Conta criada com sucesso para Marina Silva!

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: joão pedro
Senha (4 dígitos): 12ab
A senha deve ter exatamente 4 dígitos numéricos.

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: JOÃO PEDRO
Senha (4 dígitos): 4321
Conta criada com sucesso para João Pedro!

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 1
Nome do titular: marina silva
Já existe uma conta para este titular.

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 2
Titular: marina silva
Senha: 0000
Titular ou senha inválidos.

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 2
Titular: marina silva
Senha: 1234
Bem-vindo(a), Marina Silva!

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 2
Valor do depósito (R$): 500
Depósito realizado!

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 3
Valor do saque (R$): 800
Saque não realizado: valor inválido ou saldo insuficiente.

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 3
Valor do saque (R$): 120.50
Saque realizado!

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 2
Valor do depósito (R$): -5
Valor inválido.

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 4
Titular de destino: xingu
Conta de destino não encontrada.

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 4
Titular de destino: marina silva
Não é possível transferir para a própria conta.

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 4
Titular de destino: joão pedro
Valor da transferência (R$): 200
Transferência realizada!

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 1
Saldo: R$ 179.50

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 5

--- EXTRATO DE Marina Silva ---
Depósito: + R$ 500.00
Saque: - R$ 120.50
Transferência para João Pedro: - R$ 200.00
Saldo atual: R$ 179.50

--- Conta de Marina Silva ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 0

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 0
Até logo!
```

## 2ª execução: saldo de João Pedro foi carregado do arquivo (o extrato da sessão anterior não persiste)

**Entradas:** `2` → `joão pedro` → `4321` → `1` → `5` → `0` → `0`

```text

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 2
Titular: joão pedro
Senha: 4321
Bem-vindo(a), João Pedro!

--- Conta de João Pedro ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 1
Saldo: R$ 200.00

--- Conta de João Pedro ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 5

--- EXTRATO DE João Pedro ---
Sem movimentações nesta sessão.
Saldo atual: R$ 200.00

--- Conta de João Pedro ---
1 - Saldo
2 - Depositar
3 - Sacar
4 - Transferir
5 - Extrato
0 - Sair da conta
Escolha: 0

=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===
1 - Criar conta
2 - Entrar
0 - Sair
Escolha: 0
Até logo!
```

## Conteúdo do arquivo contas.txt ao final

```text
Marina Silva;1234;179.50
João Pedro;4321;200.00
```
