# SOLUÇÃO DE REFERÊNCIA – Sistema modular com dados salvos (Aula 17)
def salvar_clientes(clientes, arquivo="clientes.txt"):
    with open(arquivo, "w", encoding="utf-8") as f:
        for cl in clientes:
            f.write(f"{cl['nome']};{cl['destino']};{cl['dias']}\n")

def carregar_clientes(arquivo="clientes.txt"):
    clientes = []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                nome, destino, dias = linha.strip().split(";")
                clientes.append({"nome": nome, "destino": destino, "dias": int(dias)})
    except FileNotFoundError:
        pass
    return clientes

clientes = carregar_clientes()

while True:
    print("\n1 - Cadastrar cliente | 2 - Listar clientes | 0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        nome = input("Nome: ").strip().title()
        destino = input("Destino: ").strip().title()
        dias = int(input("Dias: "))
        clientes.append({"nome": nome, "destino": destino, "dias": dias})
        salvar_clientes(clientes)
        print("Cliente cadastrado e salvo!")
    elif opcao == "2":
        for cl in clientes:
            print(f"{cl['nome']} -> {cl['destino']} ({cl['dias']} dias)")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
