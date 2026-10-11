# Aula 14 | Cadastro de clientes em memória.
# Entradas de teste sugeridas:  marina costa  | parintins | 3 | s | joão pedro | maués | 4 | n

clientes = []

continuar = "s"
while continuar == "s":
    cliente = {
        "nome": input("Nome: ").strip().title(),
        "destino": input("Destino: ").strip().title(),
        "dias": int(input("Dias: "))
    }
    clientes.append(cliente)
    continuar = input("Cadastrar outro? (s/n): ").lower()

print()
for cl in clientes:
    print(f"{cl['nome']} -> {cl['destino']} ({cl['dias']} dias)")
print(f"Total de clientes: {len(clientes)}")
