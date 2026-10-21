# Casos de teste para correção – Projeto 7

| **Entrada / situação** | **Resultado esperado** |
| --- | --- |
| Opções 3, 4 e 5 sem nenhum lançamento | Resumo com R$ 0,00 e aviso “Registre ao menos uma receita…”; “Nenhuma despesa registrada.”; “Nenhum lançamento registrado.” |
| Descrição vazia na receita “extra feira” | “A descrição não pode ficar vazia.” e nova pergunta; salva como “Extra feira” |
| Valor 0 na feira; categoria 9 no barco | “O valor deve ser maior que zero.”; “Categoria inválida!” e novas perguntas |
| Receitas 3000 + 450,50; despesas 1200 + 650,75 + 380 + 120 | Receitas R$ 3450,50; despesas R$ 2350,75; saldo R$ 1099,75; comprometimento 68,1%; “Saudável” |
| Despesas por categoria do cenário | Moradia 51,0%; Alimentação 27,7%; Transporte 16,2%; Lazer 5,1%; maior gasto: Moradia (R$ 1200,00) |
| Renda 1000 e despesa 900 | 90,0% – “Atenção – despesas altas” |
| Renda 1000 e despesa 1200 | 120,0% – “Alerta – despesas maiores que a receita” |
| Listagem final | 6 lançamentos numerados, com sinal + nas receitas e − nas despesas |
