# SOLUÇÃO DE REFERÊNCIA – Cadastro em memória (Aula 14)
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
