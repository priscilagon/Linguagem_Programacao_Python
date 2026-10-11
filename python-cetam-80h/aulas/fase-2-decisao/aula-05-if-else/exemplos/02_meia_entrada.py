# Aula 05 | Condição composta com or.
# Entradas de teste sugeridas: 65 | n

idade = int(input("Idade: "))
estudante = input("É estudante? (s/n): ").lower()
valor = 150.00

if idade >= 60 or estudante == "s":
    valor = valor * 0.5
    print("Meia entrada aplicada.")
else:
    print("Valor integral.")

print(f"Valor do passeio: R$ {valor:.2f}")
