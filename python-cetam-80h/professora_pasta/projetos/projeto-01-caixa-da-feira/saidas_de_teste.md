# Saídas de teste – Projeto 1

## dois atendimentos (dinheiro com erro de valor; cartão com entradas inválidas)

**Entradas:** `1` → `5` → `4` → `2` → `0` → `1` → `100` → `200` → `s` → `9` → `2` → `-1` → `1.5` → `0` → `3` → `2` → `n`

```text
=== FEIRA DO PRODUTOR - CAIXA DIGITAL ===
(preços fictícios, apenas para o exercício)

--- Novo atendimento ---

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 1
Quantidade de Tambaqui (kg): 5
Tambaqui: 5.00 kg x R$ 28.00 = R$ 140.00

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 4
Quantidade de Farinha de mandioca (kg): 2
Farinha de mandioca: 2.00 kg x R$ 9.00 = R$ 18.00

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 0

=== RESUMO DA COMPRA ===
Itens registrados: 2
Subtotal: R$ 158.00
Desconto (5%): R$ 7.90
Total a pagar: R$ 150.10
Pagamento (1 - Dinheiro, 2 - Cartão): 1
Valor recebido (R$): 100
Valor insuficiente! Faltam R$ 50.10.
Valor recebido (R$): 200
Troco: R$ 49.90
Atender novo cliente? (s/n): s

--- Novo atendimento ---

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 9
Opção inválida!

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 2
Quantidade de Pirarucu (kg): -1
Quantidade inválida! Digite um valor maior que zero.
Quantidade de Pirarucu (kg): 1.5
Pirarucu: 1.50 kg x R$ 45.00 = R$ 67.50

1 - Tambaqui (R$ 28,00/kg)
2 - Pirarucu (R$ 45,00/kg)
3 - Tucunaré (R$ 32,00/kg)
4 - Farinha de mandioca (R$ 9,00/kg)
0 - Finalizar compra
Produto: 0

=== RESUMO DA COMPRA ===
Itens registrados: 1
Subtotal: R$ 67.50
Desconto (0%): R$ 0.00
Total a pagar: R$ 67.50
Pagamento (1 - Dinheiro, 2 - Cartão): 3
Forma de pagamento inválida!
Pagamento (1 - Dinheiro, 2 - Cartão): 2
Pagamento no cartão aprovado.
Atender novo cliente? (s/n): n

=== FECHAMENTO DO CAIXA ===
Clientes atendidos: 2
Total vendido no dia: R$ 217.60
```
