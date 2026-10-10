# Aula 06 | Classificação do pacote por faixa de valor.
# Entradas de teste sugeridas: 1200

total = float(input("Total da viagem (R$): "))

if total <= 800:
    pacote = "Econômico"
elif total <= 1500:
    pacote = "Conforto"
else:
    pacote = "Premium"

print(f"Pacote: {pacote}")
