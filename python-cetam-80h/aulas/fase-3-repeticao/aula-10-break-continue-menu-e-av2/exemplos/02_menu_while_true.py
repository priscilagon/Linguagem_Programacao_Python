# Aula 10 | Menu interativo com while True.
# Entradas de teste sugeridas: 2 | 9 | 0

destinos = ["Parintins", "Novo Airão", "Presidente Figueiredo", "Maués"]

while True:
    print("\n=== AGÊNCIA AMAZÔNIA TUR DIGITAL ===")
    print("1 - Calcular viagem")
    print("2 - Ver destinos")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pass    # será implementado depois
    elif opcao == "2":
        for destino in destinos:
            print("-", destino)
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
        continue
