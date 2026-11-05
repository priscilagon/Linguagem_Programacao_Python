# SOLUÇÃO DE REFERÊNCIA – Projeto 9: Agenda de Contatos Comunitária
# Projeto 9 - Agenda de Contatos Comunitária (dados fictícios)
ARQUIVO = "agenda.txt"


def carregar_contatos():
    contatos = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                nome, telefone, email, bairro = linha.strip().split(";")
                contatos.append({"nome": nome, "telefone": telefone, "email": email, "bairro": bairro})
    except FileNotFoundError:
        pass
    return contatos


def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in contatos:
            f.write(f"{c['nome']};{c['telefone']};{c['email']};{c['bairro']}\n")


def limpar_telefone(texto):
    for simbolo in " -()":
        texto = texto.replace(simbolo, "")
    return texto


def telefone_valido(telefone):
    return telefone.isdigit() and (len(telefone) == 10 or len(telefone) == 11)


def email_valido(email):
    return "@" in email and "." in email and " " not in email and ";" not in email


def buscar_contato(contatos, nome):
    for c in contatos:
        if c["nome"] == nome:
            return c
    return None


def buscar_por_trecho(contatos, trecho):
    encontrados = []
    for c in contatos:
        if trecho.strip().lower() in c["nome"].lower():
            encontrados.append(c)
    return encontrados


def formatar(c):
    return f"{c['nome']} | {c['telefone']} | {c['email']} | {c['bairro']}"


def cadastrar_contato(contatos):
    nome = input("Nome: ").strip().title()
    if nome == "" or ";" in nome:
        print("Nome inválido.")
        return
    if buscar_contato(contatos, nome) is not None:
        print("Já existe um contato com esse nome.")
        return

    telefone = limpar_telefone(input("Telefone (com DDD): "))
    while not telefone_valido(telefone):
        print("Telefone inválido! Use 10 ou 11 dígitos (com DDD).")
        telefone = limpar_telefone(input("Telefone (com DDD): "))

    email = input("E-mail: ").strip().lower()
    while not email_valido(email):
        print("E-mail inválido!")
        email = input("E-mail: ").strip().lower()

    bairro = input("Bairro: ").strip().title().replace(";", "")
    if bairro == "":
        bairro = "Não informado"

    contatos.append({"nome": nome, "telefone": telefone, "email": email, "bairro": bairro})
    salvar_contatos(contatos)
    print("Contato salvo!")


def listar_contatos(contatos):
    if len(contatos) == 0:
        print("Agenda vazia.")
        return
    nomes = []
    for c in contatos:
        nomes.append(c["nome"])
    nomes.sort()
    print(f"\n--- AGENDA ({len(nomes)} contatos) ---")
    for nome in nomes:
        print(formatar(buscar_contato(contatos, nome)))


def editar_contato(contatos):
    nome = input("Nome do contato a editar: ").strip().title()
    contato = buscar_contato(contatos, nome)
    if contato is None:
        print("Contato não encontrado.")
        return
    print("Pressione Enter para manter o valor atual.")

    novo = limpar_telefone(input(f"Telefone [{contato['telefone']}]: "))
    if novo != "":
        if telefone_valido(novo):
            contato["telefone"] = novo
        else:
            print("Telefone inválido: valor anterior mantido.")

    novo = input(f"E-mail [{contato['email']}]: ").strip().lower()
    if novo != "":
        if email_valido(novo):
            contato["email"] = novo
        else:
            print("E-mail inválido: valor anterior mantido.")

    novo = input(f"Bairro [{contato['bairro']}]: ").strip().title().replace(";", "")
    if novo != "":
        contato["bairro"] = novo

    salvar_contatos(contatos)
    print("Contato atualizado!")


def remover_contato(contatos):
    nome = input("Nome do contato a remover: ").strip().title()
    contato = buscar_contato(contatos, nome)
    if contato is None:
        print("Contato não encontrado.")
        return
    confirma = input(f"Remover {nome}? (s/n): ").strip().lower()
    if confirma == "s":
        contatos.remove(contato)
        salvar_contatos(contatos)
        print("Contato removido.")
    else:
        print("Remoção cancelada.")


def resumo_por_bairro(contatos):
    if len(contatos) == 0:
        print("Agenda vazia.")
        return
    contagem = {}
    for c in contatos:
        bairro = c["bairro"]
        if bairro in contagem:
            contagem[bairro] += 1
        else:
            contagem[bairro] = 1
    print("\n--- CONTATOS POR BAIRRO ---")
    for bairro, qtd in contagem.items():
        print(f"{bairro}: {qtd}")


contatos = carregar_contatos()

while True:
    print("\n=== AGENDA COMUNITÁRIA ===")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Buscar por trecho do nome")
    print("4 - Editar")
    print("5 - Remover")
    print("6 - Resumo por bairro")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_contato(contatos)
    elif opcao == "2":
        listar_contatos(contatos)
    elif opcao == "3":
        achados = buscar_por_trecho(contatos, input("Trecho do nome: "))
        if len(achados) == 0:
            print("Nenhum contato encontrado.")
        else:
            for c in achados:
                print(formatar(c))
    elif opcao == "4":
        editar_contato(contatos)
    elif opcao == "5":
        remover_contato(contatos)
    elif opcao == "6":
        resumo_por_bairro(contatos)
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
