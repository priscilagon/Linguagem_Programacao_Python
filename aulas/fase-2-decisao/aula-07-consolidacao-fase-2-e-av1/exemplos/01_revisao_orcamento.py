# Aula 07 | Revisão: decisão sobre o orçamento (exemplo diferente da AV1).
# Entradas de teste sugeridas: Marina | 3 | 330

LIMITE = 1000.00

nome = input("Nome do cliente: ")
dias = int(input("Dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))
total = dias * gasto_dia

print(f"Cliente: {nome} | Total: R$ {total:.2f}")
if total <= LIMITE:
    print("Dentro do orçamento.")
else:
    print(f"Fora do orçamento por R$ {total - LIMITE:.2f}.")
