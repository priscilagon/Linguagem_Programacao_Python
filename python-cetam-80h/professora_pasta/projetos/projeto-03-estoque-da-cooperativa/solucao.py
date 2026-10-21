# SOLUÇÃO DE REFERÊNCIA – Projeto 3: Estoque da Cooperativa Ribeirinha
# Projeto 3 - Estoque da Cooperativa Ribeirinha (dados fictícios)
MINIMO = 10

estoque = {
    "Açaí": {"preco": 18.50, "qtd": 40},
    "Castanha": {"preco": 32.00, "qtd": 15},
    "Tapioca": {"preco": 12.00, "qtd": 8},
    "Cupuaçu": {"preco": 15.00, "qtd": 25},
}

def exibir_menu():
    print("\n=== COOPERATIVA RIBEIRINHA - ESTOQUE ===")
    print("1 - Listar estoque")
    print("2 - Cadastrar produto")
    print("3 - Registrar venda")
    print("4 - Repor estoque")
    print("5 - Relatório")
    print("0 - Sair")
    return input("Escolha: ")

def listar_estoque(estoque):
    print("\n--- ESTOQUE ATUAL ---")
    for nome, dados in estoque.items():
        print(f"{nome}: R$ {dados['preco']:.2f} | {dados['qtd']} un.")

def valor_total(estoque):
    total = 0
    for dados in estoque.values():
        total += dados["preco"] * dados["qtd"]
    return total

def produtos_baixos(estoque, minimo=MINIMO):
    baixos = []
    for nome, dados in estoque.items():
        if dados["qtd"] < minimo:
            baixos.append(nome)
    return baixos

def cadastrar_produto(estoque):
    nome = input("Nome do produto: ").strip().title()
    if nome == "":
        print("Nome inválido.")
        return
    if nome in estoque:
        print("Produto já cadastrado!")
        return
    preco = float(input("Preço (R$): "))
    while preco <= 0:
        print("O preço deve ser maior que zero.")
        preco = float(input("Preço (R$): "))
    qtd = int(input("Quantidade inicial: "))
    while qtd < 0:
        print("A quantidade não pode ser negativa.")
        qtd = int(input("Quantidade inicial: "))
    estoque[nome] = {"preco": preco, "qtd": qtd}
    print(f"Produto {nome} cadastrado!")

def vender(estoque):
    nome = input("Produto: ").strip().title()
    if nome not in estoque:
        print("Produto não encontrado.")
        return 0
    qtd = int(input("Quantidade: "))
    if qtd <= 0:
        print("Quantidade inválida.")
        return 0
    if qtd > estoque[nome]["qtd"]:
        print(f"Estoque insuficiente! Disponível: {estoque[nome]['qtd']} un.")
        return 0
    estoque[nome]["qtd"] -= qtd
    valor = qtd * estoque[nome]["preco"]
    print(f"Venda registrada: {qtd} x {nome} = R$ {valor:.2f}")
    return valor

def repor(estoque):
    nome = input("Produto: ").strip().title()
    if nome not in estoque:
        print("Produto não encontrado.")
        return
    qtd = int(input("Quantidade a repor: "))
    if qtd <= 0:
        print("Quantidade inválida.")
        return
    estoque[nome]["qtd"] += qtd
    print(f"Novo estoque de {nome}: {estoque[nome]['qtd']} un.")

def relatorio(estoque, vendido):
    print("\n=== RELATÓRIO DO ESTOQUE ===")
    print(f"Produtos cadastrados: {len(estoque)}")
    print(f"Valor total em estoque: R$ {valor_total(estoque):.2f}")
    print(f"Total vendido na sessão: R$ {vendido:.2f}")
    mais_caro = ""
    maior_preco = 0
    for nome, dados in estoque.items():
        if dados["preco"] > maior_preco:
            maior_preco = dados["preco"]
            mais_caro = nome
    print(f"Produto mais caro: {mais_caro} (R$ {maior_preco:.2f})")
    baixos = produtos_baixos(estoque)
    if len(baixos) == 0:
        print("Nenhum produto com estoque baixo.")
    else:
        print(f"Estoque baixo (menos de {MINIMO} un.):")
        for nome in baixos:
            print(f"- {nome}: {estoque[nome]['qtd']} un.")

vendido = 0
while True:
    opcao = exibir_menu()
    if opcao == "1":
        listar_estoque(estoque)
    elif opcao == "2":
        cadastrar_produto(estoque)
    elif opcao == "3":
        vendido += vender(estoque)
    elif opcao == "4":
        repor(estoque)
    elif opcao == "5":
        relatorio(estoque, vendido)
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
