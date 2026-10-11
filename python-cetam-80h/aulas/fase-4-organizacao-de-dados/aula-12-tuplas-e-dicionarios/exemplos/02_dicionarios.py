# Aula 12 | Criar, alterar, incluir e percorrer.

destino = {"nome": "Parintins", "preco": 950.00, "dias": 3}

print(destino["nome"])
destino["preco"] = 990.00          # altera
destino["transporte"] = "barco"    # inclui

for chave, valor in destino.items():
    print(f"{chave}: {valor}")
