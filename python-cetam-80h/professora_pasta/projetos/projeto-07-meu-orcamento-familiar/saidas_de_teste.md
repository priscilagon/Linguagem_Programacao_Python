# Saídas de teste – Projeto 7

> Saídas geradas por execução real da `solucao.py`.

**Teste 1:** cenário completo: sem dados, entradas inválidas, resumo, categorias e listagem.

**Saída obtida**

```text

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 3

--- RESUMO DO MÊS ---
Receitas: R$ 0.00
Despesas: R$ 0.00
Saldo: R$ 0.00
Registre ao menos uma receita para analisar o orçamento.

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 4
Nenhuma despesa registrada.

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 5
Nenhum lançamento registrado.

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 1
Descrição:   salário
Valor (R$): 3000
Lançamento registrado: Salário - R$ 3000.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 1
Descrição:
A descrição não pode ficar vazia.
Descrição: extra feira
Valor (R$): 450.5
Lançamento registrado: Extra feira - R$ 450.50

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 2
Descrição: aluguel
Categorias:
1 - Moradia
2 - Alimentação
3 - Transporte
4 - Saúde
5 - Lazer
6 - Outros
Categoria (número): 1
Valor (R$): 1200
Lançamento registrado: Aluguel - R$ 1200.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 2
Descrição: feira da semana
Categorias:
1 - Moradia
2 - Alimentação
3 - Transporte
4 - Saúde
5 - Lazer
6 - Outros
Categoria (número): 2
Valor (R$): 0
O valor deve ser maior que zero.
Valor (R$): 650.75
Lançamento registrado: Feira da semana - R$ 650.75

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 2
Descrição: barco para o interior
Categorias:
1 - Moradia
2 - Alimentação
3 - Transporte
4 - Saúde
5 - Lazer
6 - Outros
Categoria (número): 9
Categoria inválida!
Categoria (número): 3
Valor (R$): 380
Lançamento registrado: Barco para o interior - R$ 380.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 2
Descrição: cinema
Categorias:
1 - Moradia
2 - Alimentação
3 - Transporte
4 - Saúde
5 - Lazer
6 - Outros
Categoria (número): 5
Valor (R$): 120
Lançamento registrado: Cinema - R$ 120.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 3

--- RESUMO DO MÊS ---
Receitas: R$ 3450.50
Despesas: R$ 2350.75
Saldo: R$ 1099.75
Comprometimento da renda: 68.1%
Situação: Saudável

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 4

--- DESPESAS POR CATEGORIA ---
Moradia: R$ 1200.00 (51.0%)
Alimentação: R$ 650.75 (27.7%)
Transporte: R$ 380.00 (16.2%)
Lazer: R$ 120.00 (5.1%)
Maior gasto: Moradia (R$ 1200.00)

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 5

--- LANÇAMENTOS ---
1. [Receita] Salário: + R$ 3000.00
2. [Receita] Extra feira: + R$ 450.50
3. [Moradia] Aluguel: - R$ 1200.00
4. [Alimentação] Feira da semana: - R$ 650.75
5. [Transporte] Barco para o interior: - R$ 380.00
6. [Lazer] Cinema: - R$ 120.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 0
Até logo!
```

**Teste 2:** despesas maiores que a receita (120%).

**Saída obtida**

```text

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 1
Descrição: renda
Valor (R$): 1000
Lançamento registrado: Renda - R$ 1000.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 2
Descrição: dívida
Categorias:
1 - Moradia
2 - Alimentação
3 - Transporte
4 - Saúde
5 - Lazer
6 - Outros
Categoria (número): 6
Valor (R$): 1200
Lançamento registrado: Dívida - R$ 1200.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 3

--- RESUMO DO MÊS ---
Receitas: R$ 1000.00
Despesas: R$ 1200.00
Saldo: R$ -200.00
Comprometimento da renda: 120.0%
Situação: Alerta - despesas maiores que a receita

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 0
Até logo!
```

**Teste 3:** despesas altas (90%).

**Saída obtida**

```text

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 1
Descrição: renda
Valor (R$): 1000
Lançamento registrado: Renda - R$ 1000.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 2
Descrição: conta de luz
Categorias:
1 - Moradia
2 - Alimentação
3 - Transporte
4 - Saúde
5 - Lazer
6 - Outros
Categoria (número): 1
Valor (R$): 900
Lançamento registrado: Conta de luz - R$ 900.00

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 3

--- RESUMO DO MÊS ---
Receitas: R$ 1000.00
Despesas: R$ 900.00
Saldo: R$ 100.00
Comprometimento da renda: 90.0%
Situação: Atenção - despesas altas

=== MEU ORÇAMENTO FAMILIAR ===
1 - Registrar receita
2 - Registrar despesa
3 - Resumo do mês
4 - Despesas por categoria
5 - Listar lançamentos
0 - Sair
Escolha: 0
Até logo!
```
