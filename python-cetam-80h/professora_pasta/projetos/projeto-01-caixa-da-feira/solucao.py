# SOLUÇÃO DE REFERÊNCIA – Projeto 1: Caixa da Feira do Produtor
# Projeto 1 - Caixa da Feira do Produtor
print("=== FEIRA DO PRODUTOR - CAIXA DIGITAL ===")
print("(preços fictícios, apenas para o exercício)")

total_dia = 0
clientes = 0
novo_cliente = "s"

while novo_cliente == "s":
    subtotal = 0
    itens = 0
    print("\n--- Novo atendimento ---")

    while True:
        print("\n1 - Tambaqui (R$ 28,00/kg)")
        print("2 - Pirarucu (R$ 45,00/kg)")
        print("3 - Tucunaré (R$ 32,00/kg)")
        print("4 - Farinha de mandioca (R$ 9,00/kg)")
        print("0 - Finalizar compra")
        opcao = input("Produto: ")

        if opcao == "0":
            if itens == 0:
                print("Nenhum item registrado ainda.")
                continue
            break
        elif opcao == "1":
            nome = "Tambaqui"
            preco = 28.00
        elif opcao == "2":
            nome = "Pirarucu"
            preco = 45.00
        elif opcao == "3":
            nome = "Tucunaré"
            preco = 32.00
        elif opcao == "4":
            nome = "Farinha de mandioca"
            preco = 9.00
        else:
            print("Opção inválida!")
            continue

        quantidade = float(input(f"Quantidade de {nome} (kg): "))
        while quantidade <= 0:
            print("Quantidade inválida! Digite um valor maior que zero.")
            quantidade = float(input(f"Quantidade de {nome} (kg): "))

        valor = preco * quantidade
        subtotal += valor
        itens += 1
        print(f"{nome}: {quantidade:.2f} kg x R$ {preco:.2f} = R$ {valor:.2f}")

    if subtotal >= 200:
        taxa = 0.10
    elif subtotal >= 100:
        taxa = 0.05
    else:
        taxa = 0

    desconto = subtotal * taxa
    total = subtotal - desconto

    print("\n=== RESUMO DA COMPRA ===")
    print(f"Itens registrados: {itens}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Desconto ({taxa * 100:.0f}%): R$ {desconto:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")

    forma = input("Pagamento (1 - Dinheiro, 2 - Cartão): ")
    while forma != "1" and forma != "2":
        print("Forma de pagamento inválida!")
        forma = input("Pagamento (1 - Dinheiro, 2 - Cartão): ")

    if forma == "1":
        recebido = float(input("Valor recebido (R$): "))
        while recebido < total:
            print(f"Valor insuficiente! Faltam R$ {total - recebido:.2f}.")
            recebido = float(input("Valor recebido (R$): "))
        print(f"Troco: R$ {recebido - total:.2f}")
    else:
        print("Pagamento no cartão aprovado.")

    total_dia += total
    clientes += 1
    novo_cliente = input("Atender novo cliente? (s/n): ").lower()

print("\n=== FECHAMENTO DO CAIXA ===")
print(f"Clientes atendidos: {clientes}")
print(f"Total vendido no dia: R$ {total_dia:.2f}")
