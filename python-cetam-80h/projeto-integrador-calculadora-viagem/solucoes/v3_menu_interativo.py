# SOLUÇÃO DE REFERÊNCIA – Menu interativo (Aula 10)
LIMITE = 1000.00
destinos = ["Parintins", "Novo Airão", "Presidente Figueiredo", "Maués"]

while True:
    print("\n=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===")
    print("1 - Calcular viagem")
    print("2 - Ver destinos")
    print("3 - Ver orçamento limite")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        dias = int(input("Dias: "))
        gasto_dia = float(input("Gasto por dia: "))
        print(f"Total: R$ {dias * gasto_dia:.2f}")
    elif opcao == "2":
        for destino in destinos:
            print("-", destino)
    elif opcao == "3":
        print(f"Orçamento limite: R$ {LIMITE:.2f}")
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
        continue
