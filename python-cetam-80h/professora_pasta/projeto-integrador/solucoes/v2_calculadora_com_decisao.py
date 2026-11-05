# SOLUÇÃO DE REFERÊNCIA – Calculadora de viagem v2 (Aula 07)
# Agência Amazônia Tur Digital - Calculadora de viagem v2
LIMITE = 1000.00

nome = input("Nome do cliente: ")
dias = int(input("Quantidade de dias: "))
gasto_dia = float(input("Gasto por dia (R$): "))

total = dias * gasto_dia

if total <= 800:
    pacote = "Econômico"
elif total <= 1500:
    pacote = "Conforto"
else:
    pacote = "Premium"

print(f"\nCliente: {nome}")
print(f"Total: R$ {total:.2f} - Pacote {pacote}")

if total <= LIMITE:
    print("Dentro do orçamento de R$ 1000,00.")
else:
    print(f"Fora do orçamento! Excede em R$ {total - LIMITE:.2f}.")
