# Casos de teste para correção – Projeto 5

| Entrada / situação | Resultado esperado |
| --- | --- |
| Criar “marina silva”, senha 1234 | Conta criada para “Marina Silva” |
| Criar “joão pedro”, senha “12ab” | “A senha deve ter exatamente 4 dígitos numéricos.” |
| Criar “JOÃO PEDRO”, senha 4321 | Conta criada para “João Pedro” |
| Criar “marina silva” novamente | “Já existe uma conta para este titular.” |
| Login com senha 0000 | “Titular ou senha inválidos.” |
| Depositar 500; sacar 800; sacar 120,50; depositar −5 | Depósito ok; saque recusado (saldo insuficiente); saque ok; valor inválido |
| Transferir para “xingu”; para si mesma; R$ 200 para João Pedro | Destino não encontrado; recusada; transferência realizada |
| Saldo e extrato de Marina | Saldo R$ 179,50; extrato com depósito, saque e transferência |
| Reiniciar e entrar como João Pedro | Saldo R$ 200,00 (persistido); extrato vazio nesta sessão |
| `contas.txt` ao final | Marina Silva;1234;179.50 e João Pedro;4321;200.00 |
