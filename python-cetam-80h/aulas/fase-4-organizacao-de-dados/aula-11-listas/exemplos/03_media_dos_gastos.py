# Aula 11 | Maior, menor e média de uma lista numérica.

gastos = [990.00, 1250.50, 780.00]

for gasto in gastos:
    print(f"R$ {gasto:.2f}")

print(f"Maior: {max(gastos)} | Menor: {min(gastos)}")
print(f"Média: {sum(gastos) / len(gastos):.2f}")
