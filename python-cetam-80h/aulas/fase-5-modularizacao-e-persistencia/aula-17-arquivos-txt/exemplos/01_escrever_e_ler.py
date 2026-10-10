# Aula 17 | Gravar uma lista e ler de volta.

destinos = ["Parintins", "Novo Airão", "Maués"]

with open("destinos.txt", "w", encoding="utf-8") as arquivo:
    for destino in destinos:
        arquivo.write(destino + "\n")

with open("destinos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
