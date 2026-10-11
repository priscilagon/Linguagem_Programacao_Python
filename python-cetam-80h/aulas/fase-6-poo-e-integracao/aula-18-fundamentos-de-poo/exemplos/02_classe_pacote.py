# Aula 18 | Classe com três atributos e um método.

class Pacote:
    def __init__(self, destino, preco, dias):
        self.destino = destino
        self.preco = preco
        self.dias = dias

    def descricao(self):
        return f"{self.destino}: R$ {self.preco:.2f} em {self.dias} dias"

pacote = Pacote("Novo Airão", 1200.00, 4)
print(pacote.descricao())
