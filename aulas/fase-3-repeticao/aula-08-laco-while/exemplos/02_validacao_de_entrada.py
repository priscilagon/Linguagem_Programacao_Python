# Aula 08 | Repete a pergunta até o valor ser válido.
# Entradas de teste sugeridas: 40 | 3

dias = int(input("Dias de viagem (1 a 30): "))
while dias < 1 or dias > 30:
    print("Valor inválido! Digite de 1 a 30.")
    dias = int(input("Dias de viagem (1 a 30): "))
print(f"Dias registrados: {dias}")
