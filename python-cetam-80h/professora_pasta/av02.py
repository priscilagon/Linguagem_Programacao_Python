clientes = []
 
while True:
    print("\n1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Resumo financeiro")
    print("0 - Sair")
    opcao = input("Opção: ")
 
    if opcao == "1":
        nome = input("Nome: ").strip().title()
        destino = input("Destino: ").strip().title()
        dias = int(input("Dias: "))
        gasto_dia = float(input("Gasto por dia (R$): "))
        cliente = {"nome": nome, "destino": destino, "dias": dias, "gasto_dia": gasto_dia}
        clientes.append(cliente)
        print("Cliente cadastrado!")
    elif opcao == "2":
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                total = c["dias"] * c["gasto_dia"]
                print(c["nome"], "-", c["destino"], "-", c["dias"], "dias - R$", total)
    elif opcao == "3":
        total_geral = 0
        maior = 0
        nome_maior = ""
        for c in clientes:
            total = c["dias"] * c["gasto_dia"]
            total_geral += total
            if total > maior:
                maior = total
                nome_maior = c["nome"]
        print("Total geral: R$", total_geral)
        if nome_maior != "":
            print("Maior gasto:", nome_maior, "- R$", maior)
    elif opcao == "0":
        print("Encerrando.")
        break
    else:
        print("Opção inválida.")
