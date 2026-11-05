# SOLUÇÃO DE REFERÊNCIA – Projeto 7: Meu Orçamento Familiar
# Projeto 7 - Meu Orçamento Familiar (dados fictícios)
categorias = ["Moradia", "Alimentação", "Transporte", "Saúde", "Lazer", "Outros"]
lancamentos = []

while True:
    print("\n=== MEU ORÇAMENTO FAMILIAR ===")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Resumo do mês")
    print("4 - Despesas por categoria")
    print("5 - Listar lançamentos")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1" or opcao == "2":
        descricao = input("Descrição: ").strip().capitalize()
        while descricao == "":
            print("A descrição não pode ficar vazia.")
            descricao = input("Descrição: ").strip().capitalize()

        categoria = "Receita"
        if opcao == "2":
            print("Categorias:")
            for i in range(len(categorias)):
                print(f"{i + 1} - {categorias[i]}")
            numero = int(input("Categoria (número): "))
            while numero < 1 or numero > len(categorias):
                print("Categoria inválida!")
                numero = int(input("Categoria (número): "))
            categoria = categorias[numero - 1]

        valor = float(input("Valor (R$): "))
        while valor <= 0:
            print("O valor deve ser maior que zero.")
            valor = float(input("Valor (R$): "))

        if opcao == "1":
            tipo = "receita"
        else:
            tipo = "despesa"
        lancamentos.append({"tipo": tipo, "descricao": descricao, "categoria": categoria, "valor": valor})
        print(f"Lançamento registrado: {descricao} - R$ {valor:.2f}")

    elif opcao == "3":
        receitas = 0
        despesas = 0
        for item in lancamentos:
            if item["tipo"] == "receita":
                receitas += item["valor"]
            else:
                despesas += item["valor"]
        saldo = receitas - despesas

        print("\n--- RESUMO DO MÊS ---")
        print(f"Receitas: R$ {receitas:.2f}")
        print(f"Despesas: R$ {despesas:.2f}")
        print(f"Saldo: R$ {saldo:.2f}")
        if receitas == 0:
            print("Registre ao menos uma receita para analisar o orçamento.")
        else:
            percentual = despesas / receitas * 100
            print(f"Comprometimento da renda: {percentual:.1f}%")
            if percentual <= 70:
                print("Situação: Saudável")
            elif percentual <= 100:
                print("Situação: Atenção - despesas altas")
            else:
                print("Situação: Alerta - despesas maiores que a receita")

    elif opcao == "4":
        totais = {}
        for nome in categorias:
            totais[nome] = 0
        total_despesas = 0
        for item in lancamentos:
            if item["tipo"] == "despesa":
                totais[item["categoria"]] += item["valor"]
                total_despesas += item["valor"]

        if total_despesas == 0:
            print("Nenhuma despesa registrada.")
        else:
            print("\n--- DESPESAS POR CATEGORIA ---")
            maior_categoria = ""
            maior_valor = 0
            for nome, total_cat in totais.items():
                if total_cat > 0:
                    print(f"{nome}: R$ {total_cat:.2f} ({total_cat / total_despesas * 100:.1f}%)")
                if total_cat > maior_valor:
                    maior_valor = total_cat
                    maior_categoria = nome
            print(f"Maior gasto: {maior_categoria} (R$ {maior_valor:.2f})")

    elif opcao == "5":
        if len(lancamentos) == 0:
            print("Nenhum lançamento registrado.")
        else:
            print("\n--- LANÇAMENTOS ---")
            for i in range(len(lancamentos)):
                item = lancamentos[i]
                if item["tipo"] == "receita":
                    sinal = "+"
                else:
                    sinal = "-"
                print(f"{i + 1}. [{item['categoria']}] {item['descricao']}: {sinal} R$ {item['valor']:.2f}")

    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
