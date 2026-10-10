# Aula 08 | Várias viagens em sequência.
# Entradas de teste sugeridas: 3 | 330 | s | 2 | 200 | n

continuar = "s"
while continuar == "s":
    dias = int(input("Dias: "))
    gasto_dia = float(input("Gasto por dia: "))
    print(f"Total: R$ {dias * gasto_dia:.2f}")
    continuar = input("Deseja continuar? (s/n): ").lower()
print("Obrigado por usar a calculadora!")
