# Aula 18 | Primeira classe.

class Cliente:
    def __init__(self, nome, destino):
        self.nome = nome
        self.destino = destino

    def resumo(self):
        return f"{self.nome} viajará para {self.destino}"

cliente1 = Cliente("Marina", "Parintins")
cliente2 = Cliente("João", "Maués")
print(cliente1.resumo())
print(cliente2.resumo())
