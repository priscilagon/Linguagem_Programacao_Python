"""Projeto 5 – Amazônia Bank: Mini-Banco Digital (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Os métodos da classe Conta gerem ValueError("mensagem") quando uma regra for violada
(versão gráfica: a tela mostra a mensagem em uma janela de aviso).
No arquivo contas.txt cada linha é:  titular;senha;saldo

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""
import os

ARQUIVO = "contas.txt"


def formatar(valor):
    """RN07: 1234.5 -> 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


class Conta:
    def __init__(self, titular, senha, saldo=0.0):
        self.titular = titular
        self.senha = senha
        self.saldo = saldo
        self.historico = []          # movimentações da sessão (textos)

    def autenticar(self, senha):
        """RF03: True se a senha estiver correta."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def depositar(self, valor):
        """RF02, RN04: valor > 0. Soma ao saldo e registra 'Depósito: +R$ ...' no histórico."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def sacar(self, valor):
        """RF02, RN04 e RN05: valor > 0 e não maior que o saldo. Registra 'Saque: -R$ ...'."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def transferir(self, destino, valor):
        """RF02 e RN06: transfere para outra Conta. Registra nas DUAS contas.

        Erros: destino igual à origem, valor <= 0, saldo insuficiente.
        Textos: 'Transferência enviada para X: -R$ ...' e 'Transferência recebida de Y: +R$ ...'.
        """
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def extrato(self):
        """RF03: lista de textos — movimentações da sessão e, por último, 'Saldo atual: R$ ...'."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")


def criar_conta(contas, titular, senha):
    """RF04, RN01 e RN02: cria e retorna a Conta (guarda em contas[titular]).

    titular: strip() + title(); não vazio, sem ';' e sem repetir.
    senha: exatamente 4 dígitos numéricos.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def entrar(contas, titular, senha):
    """RN03: retorna a Conta se titular existir e a senha estiver correta.

    Caso contrário: ValueError("Titular ou senha inválidos.").
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def salvar_contas(contas, arquivo=ARQUIVO):
    """RF06: grava  titular;senha;saldo  (saldo com 2 casas) — modo 'w', utf-8."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def carregar_contas(arquivo=ARQUIVO):
    """RF06: lê o arquivo e retorna {titular: Conta}. Arquivo inexistente -> {}."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")
