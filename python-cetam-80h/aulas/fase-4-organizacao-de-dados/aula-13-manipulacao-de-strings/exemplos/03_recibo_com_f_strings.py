# Aula 13 | Recibo e código de reserva.

nome = "marina costa"
destino = "Parintins"
dias = 3
total = 990.00

codigo = f"{destino[:3].upper()}-{dias:02d}-{nome[:2].upper()}"

print("=" * 34)
print("     RECIBO - AMAZÔNIA TUR DIGITAL")
print("=" * 34)
print(f"Cliente: {nome.title()}")
print(f"Destino: {destino}")
print(f"Duração: {dias} dias")
print(f"Total:   R$ {total:.2f}")
print(f"Reserva: {codigo}")
