# Aula 15 | Sistema organizado em funções.
# Entradas de teste sugeridas: 1 | 3 | 330 | 2 | marina costa | parintins | 3 | 3 | 0

def exibir_menu():
    print("\n=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===")
    print("1 - Calcular viagem")
    print("2 - Cadastrar cliente")
    print("3 - Listar clientes")
    print("0 - Sair")
    return input("Escolha: ")

def calcular_total(dias, gasto_dia):
    return dias * gasto_dia

def cadastrar_cliente(clientes):
    nome = input("Nome: ").strip().title()
    destino = input("Destino: ").strip().title()
    dias = int(input("Dias: "))
    clientes.append({"nome": nome, "destino": destino, "dias": dias})
    print("Cliente cadastrado!")

clientes = []
while True:
    opcao = exibir_menu()
    if opcao == "1":
        dias = int(input("Dias: "))
        gasto = float(input("Gasto por dia: "))
        print(f"Total: R$ {calcular_total(dias, gasto):.2f}")
    elif opcao == "2":
        cadastrar_cliente(clientes)
    elif opcao == "3":
        for cl in clientes:
            print(f"{cl['nome']} -> {cl['destino']} ({cl['dias']} dias)")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
