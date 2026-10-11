# Projeto 5 - Amazônia Bank: Mini-Banco Digital (valores fictícios)
# Integrantes: ______________________
import os

ARQUIVO = "contas.txt"


class Conta:
    def __init__(self, titular, senha, saldo=0.0):
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.historico = []

    def autenticar(self, senha):
        pass  # TODO RF03

    def depositar(self, valor):
        pass  # TODO RF02: devolver True ou False

    def sacar(self, valor):
        pass  # TODO RF02

    def transferir(self, destino, valor):
        pass  # TODO RF02 (RN06): registrar nas duas contas

    def extrato(self):
        pass  # TODO RF03


def carregar_contas():
    pass  # TODO RF06: devolver um dicionário {titular: Conta}


def salvar_contas(contas):
    pass  # TODO RF06


def criar_conta(contas):
    pass  # TODO RN01, RN02


def menu_conta(conta, contas):
    pass  # TODO RF05


def principal():
    pass  # TODO RF04


# principal()  # descomente quando o programa estiver pronto
