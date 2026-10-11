# Aula 18 | Classe Usuario com persistência em arquivo.

import os

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def cadastrar(self, arquivo="usuarios.txt"):
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(f"{self.nome};{self.senha}\n")

    def autenticar(self, arquivo="usuarios.txt"):
        if not os.path.exists(arquivo):
            return False
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                nome, senha = linha.strip().split(";")
                if nome == self.nome and senha == self.senha:
                    return True
        return False

Usuario("marina", "1234").cadastrar()
print(Usuario("marina", "1234").autenticar())
print(Usuario("marina", "errada").autenticar())
