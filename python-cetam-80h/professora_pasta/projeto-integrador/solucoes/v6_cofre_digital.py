# SOLUÇÃO DE REFERÊNCIA – Cofre digital (sistema final) (Aula 19)
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

def exibir_menu():
    print("\n=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===")
    print("1 - Cadastrar usuário")
    print("2 - Entrar")
    print("0 - Sair")
    return input("Escolha: ")

def principal():
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            nome = input("Nome de usuário: ").strip()
            senha = input("Senha: ")
            if nome == "" or senha == "":
                print("Nome e senha são obrigatórios.")
                continue
            if ";" in nome or ";" in senha:
                print("O caractere ; não é permitido.")
                continue
            Usuario(nome, senha).cadastrar()
            print("Usuário cadastrado com sucesso!")
        elif opcao == "2":
            nome = input("Nome de usuário: ").strip()
            senha = input("Senha: ")
            if Usuario(nome, senha).autenticar():
                print(f"Bem-vindo(a) ao cofre digital, {nome}!")
            else:
                print("Usuário ou senha incorretos.")
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

principal()
