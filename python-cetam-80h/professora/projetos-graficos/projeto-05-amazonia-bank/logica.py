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
        # >>> SOLUCAO
        return self.senha == senha
        # <<< SOLUCAO

    def depositar(self, valor):
        """RF02, RN04: valor > 0. Soma ao saldo e registra 'Depósito: +R$ ...' no histórico."""
        # >>> SOLUCAO
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        self.saldo = round(self.saldo + valor, 2)
        self.historico.append(f"Depósito: +{formatar(valor)}")
        # <<< SOLUCAO

    def sacar(self, valor):
        """RF02, RN04 e RN05: valor > 0 e não maior que o saldo. Registra 'Saque: -R$ ...'."""
        # >>> SOLUCAO
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo = round(self.saldo - valor, 2)
        self.historico.append(f"Saque: -{formatar(valor)}")
        # <<< SOLUCAO

    def transferir(self, destino, valor):
        """RF02 e RN06: transfere para outra Conta. Registra nas DUAS contas.

        Erros: destino igual à origem, valor <= 0, saldo insuficiente.
        Textos: 'Transferência enviada para X: -R$ ...' e 'Transferência recebida de Y: +R$ ...'.
        """
        # >>> SOLUCAO
        if destino is self or destino.titular == self.titular:
            raise ValueError("A conta de destino deve ser diferente da conta de origem.")
        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo = round(self.saldo - valor, 2)
        destino.saldo = round(destino.saldo + valor, 2)
        self.historico.append(f"Transferência enviada para {destino.titular}: -{formatar(valor)}")
        destino.historico.append(f"Transferência recebida de {self.titular}: +{formatar(valor)}")
        # <<< SOLUCAO

    def extrato(self):
        """RF03: lista de textos — movimentações da sessão e, por último, 'Saldo atual: R$ ...'."""
        # >>> SOLUCAO
        return list(self.historico) + [f"Saldo atual: {formatar(self.saldo)}"]
        # <<< SOLUCAO


def criar_conta(contas, titular, senha):
    """RF04, RN01 e RN02: cria e retorna a Conta (guarda em contas[titular]).

    titular: strip() + title(); não vazio, sem ';' e sem repetir.
    senha: exatamente 4 dígitos numéricos.
    """
    # >>> SOLUCAO
    titular = titular.strip().title()
    if titular == "":
        raise ValueError("O titular não pode ser vazio.")
    if ";" in titular:
        raise ValueError("O titular não pode conter ponto e vírgula (;).")
    if titular in contas:
        raise ValueError("Já existe uma conta com esse titular.")
    if len(senha) != 4 or not senha.isdigit():
        raise ValueError("A senha deve ter exatamente 4 dígitos numéricos.")
    contas[titular] = Conta(titular, senha)
    return contas[titular]
    # <<< SOLUCAO


def entrar(contas, titular, senha):
    """RN03: retorna a Conta se titular existir e a senha estiver correta.

    Caso contrário: ValueError("Titular ou senha inválidos.").
    """
    # >>> SOLUCAO
    conta = contas.get(titular.strip().title())
    if conta is None or not conta.autenticar(senha):
        raise ValueError("Titular ou senha inválidos.")
    return conta
    # <<< SOLUCAO


def salvar_contas(contas, arquivo=ARQUIVO):
    """RF06: grava  titular;senha;saldo  (saldo com 2 casas) — modo 'w', utf-8."""
    # >>> SOLUCAO
    with open(arquivo, "w", encoding="utf-8") as f:
        for c in contas.values():
            f.write(f"{c.titular};{c.senha};{c.saldo:.2f}\n")
    # <<< SOLUCAO


def carregar_contas(arquivo=ARQUIVO):
    """RF06: lê o arquivo e retorna {titular: Conta}. Arquivo inexistente -> {}."""
    # >>> SOLUCAO
    contas = {}
    if not os.path.exists(arquivo):
        return contas
    with open(arquivo, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                titular, senha, saldo = linha.split(";")
                contas[titular] = Conta(titular, senha, float(saldo))
    return contas
    # <<< SOLUCAO
