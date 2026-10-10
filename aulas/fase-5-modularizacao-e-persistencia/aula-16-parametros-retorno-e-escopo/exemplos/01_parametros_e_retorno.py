# Aula 16 | Parâmetros, argumentos e return.

def calcular_total(dias, gasto_dia):
    return dias * gasto_dia

def eh_par(n):
    return n % 2 == 0

total = calcular_total(3, 330.00)
print(total)
print(eh_par(8))
print(eh_par(7))
