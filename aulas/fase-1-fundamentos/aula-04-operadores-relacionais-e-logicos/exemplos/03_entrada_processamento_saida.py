# Aula 04 | Estrutura de um algoritmo em três blocos.
# Entradas de teste sugeridas: Parintins | 3 | 330

# ----- ENTRADA -----
destino = input("Destino: ")
dias = int(input("Dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))

# ----- PROCESSAMENTO -----
total = dias * gasto_dia

# ----- SAÍDA -----
print(f"Destino: {destino}")
print(f"Total: R$ {total:.2f}")
