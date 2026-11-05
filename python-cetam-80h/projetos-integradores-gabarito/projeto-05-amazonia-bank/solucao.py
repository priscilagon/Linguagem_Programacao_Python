# SOLUÇÃO DE REFERÊNCIA – Projeto 5: Amazônia Bank: Mini-Banco Digital
# Projeto 5 - Amazônia Bank: Mini-Banco Digital (valores fictícios)
import os

ARQUIVO = "contas.txt"

class Conta:
    def __init__(self, titular, senha, saldo=0.0):
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.historico = []

    def autenticar(self, senha):
        return self.senha == senha

    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        self.historico.append(f"Depósito: + R$ {valor:.2f}")
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        self.historico.append(f"Saque: - R$ {valor:.2f}")
        return True

    def transferir(self, destino, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        destino.saldo += valor
        self.historico.append(f"Transferência para {destino.titular}: - R$ {valor:.2f}")
        destino.historico.append(f"Transferência de {self.titular}: + R$ {valor:.2f}")
        return True

    def extrato(self):
        print(f"\n--- EXTRATO DE {self.titular} ---")
        if len(self.historico) == 0:
            print("Sem movimentações nesta sessão.")
        for movimento in self.historico:
            print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

def carregar_contas():
    contas = {}
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                titular, senha, saldo = linha.strip().split(";")
                contas[titular] = Conta(titular, senha, float(saldo))
    return contas

def salvar_contas(contas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for conta in contas.values():
            f.write(f"{conta.titular};{conta.senha};{conta.saldo:.2f}\n")

def criar_conta(contas):
    titular = input("Nome do titular: ").strip().title()
    if titular == "" or ";" in titular:
        print("Nome inválido.")
        return
    if titular in contas:
        print("Já existe uma conta para este titular.")
        return
    senha = input("Senha (4 dígitos): ")
    if len(senha) != 4 or not senha.isdigit():
        print("A senha deve ter exatamente 4 dígitos numéricos.")
        return
    contas[titular] = Conta(titular, senha)
    salvar_contas(contas)
    print(f"Conta criada com sucesso para {titular}!")

def menu_conta(conta, contas):
    while True:
        print(f"\n--- Conta de {conta.titular} ---")
        print("1 - Saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Extrato")
        print("0 - Sair da conta")
        opcao = input("Escolha: ")

        if opcao == "1":
            print(f"Saldo: R$ {conta.saldo:.2f}")
        elif opcao == "2":
            valor = float(input("Valor do depósito (R$): "))
            if conta.depositar(valor):
                salvar_contas(contas)
                print("Depósito realizado!")
            else:
                print("Valor inválido.")
        elif opcao == "3":
            valor = float(input("Valor do saque (R$): "))
            if conta.sacar(valor):
                salvar_contas(contas)
                print("Saque realizado!")
            else:
                print("Saque não realizado: valor inválido ou saldo insuficiente.")
        elif opcao == "4":
            nome_destino = input("Titular de destino: ").strip().title()
            if nome_destino not in contas:
                print("Conta de destino não encontrada.")
                continue
            if nome_destino == conta.titular:
                print("Não é possível transferir para a própria conta.")
                continue
            valor = float(input("Valor da transferência (R$): "))
            if conta.transferir(contas[nome_destino], valor):
                salvar_contas(contas)
                print("Transferência realizada!")
            else:
                print("Transferência não realizada: valor inválido ou saldo insuficiente.")
        elif opcao == "5":
            conta.extrato()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def principal():
    contas = carregar_contas()
    while True:
        print("\n=== AMAZÔNIA BANK - MINI-BANCO DIGITAL ===")
        print("1 - Criar conta")
        print("2 - Entrar")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            criar_conta(contas)
        elif opcao == "2":
            titular = input("Titular: ").strip().title()
            senha = input("Senha: ")
            if titular in contas and contas[titular].autenticar(senha):
                print(f"Bem-vindo(a), {titular}!")
                menu_conta(contas[titular], contas)
            else:
                print("Titular ou senha inválidos.")
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

principal()
