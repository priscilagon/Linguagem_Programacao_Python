# Aula 03 | Gasto por dia e total da viagem.
# Entradas de teste sugeridas: 3 | 200 | 50 | 80

dias = int(input("Quantidade de dias: "))
hospedagem = float(input("Hospedagem por dia (R$): "))
transporte = float(input("Transporte por dia (R$): "))
alimentacao = float(input("Alimentação por dia (R$): "))

gasto_dia = hospedagem + transporte + alimentacao
total = dias * gasto_dia

print(f"Gasto por dia: R$ {gasto_dia:.2f}")
print(f"Total da viagem: R$ {total:.2f}")
