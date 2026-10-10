# Aula 09 | Gasto dia a dia com acumulador.
# Entradas de teste sugeridas: 3 | 330

dias = int(input("Dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))
acumulado = 0

for dia in range(1, dias + 1):
    acumulado += gasto_dia
    print(f"Dia {dia}: R$ {gasto_dia:.2f} | Acumulado: R$ {acumulado:.2f}")
