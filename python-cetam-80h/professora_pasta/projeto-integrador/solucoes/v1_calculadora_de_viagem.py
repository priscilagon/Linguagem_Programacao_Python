# SOLUÇÃO DE REFERÊNCIA – Calculadora de viagem v1 (Aula 04)
# Agência Amazônia Tur Digital - Calculadora de viagem v1

# ----- ENTRADA -----
print("=== Agência Amazônia Tur Digital ===")
nome = input("Nome do cliente: ")
destino = input("Destino: ")
dias = int(input("Quantidade de dias: "))
hospedagem = float(input("Hospedagem por dia (R$): "))
transporte = float(input("Transporte por dia (R$): "))
alimentacao = float(input("Alimentação por dia (R$): "))

# ----- PROCESSAMENTO -----
gasto_dia = hospedagem + transporte + alimentacao
total = dias * gasto_dia

# ----- SAÍDA -----
print()
print(f"Cliente: {nome}")
print(f"Destino: {destino}")
print(f"Gasto por dia: R$ {gasto_dia:.2f}")
print(f"Total da viagem ({dias} dias): R$ {total:.2f}")
