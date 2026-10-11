# Aula 10 | Pular e interromper repetições.

for numero in range(1, 11):
    if numero == 4:
        continue        # pula o 4
    if numero == 8:
        break           # encerra no 8
    print(numero)
