# Aula 06 | Sugestão de destino combinando pacote e dias.
# Entradas de teste sugeridas: 2 | 300

dias = int(input("Dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))
total = dias * gasto_dia

if total <= 800:
    pacote = "Econômico"
elif total <= 1500:
    pacote = "Conforto"
else:
    pacote = "Premium"

if pacote == "Econômico" and dias <= 3:
    sugestao = "Presidente Figueiredo"
elif pacote == "Conforto":
    sugestao = "Novo Airão"
else:
    sugestao = "Parintins"

print(f"Total: R$ {total:.2f} - Pacote {pacote}")
print(f"Sugestão de destino: {sugestao}")
