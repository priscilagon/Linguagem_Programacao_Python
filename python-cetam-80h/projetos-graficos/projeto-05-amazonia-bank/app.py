"""Projeto 5 – Amazônia Bank: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

import logica
from ui_comum import (janela, cabecalho, cartao, botao, campo, tabela, preencher, seguro, carregar_seguro,
                      ler_float, NAVY, BLUE, GREEN, RED, GOLD, BG)


class BancoApp:
    def __init__(self, root):
        self.root = root
        self.contas = carregar_seguro(logica.carregar_contas, {})          # RF06
        self.conta = None
        cabecalho(root, "🏦  Amazônia Bank", "Projeto 5 • mini-banco digital com contas salvas em contas.txt")
        self.area = ttk.Frame(root, padding=16)
        self.area.pack(fill="both", expand=True)
        self.tela_inicial()

    def limpar(self):
        for w in self.area.winfo_children():
            w.destroy()

    # ------------------------------------------------------------------ login
    def tela_inicial(self):
        self.conta = None
        self.limpar()
        self.area.columnconfigure(0, weight=1)
        self.area.columnconfigure(1, weight=1)
        ent = cartao(self.area, "Entrar na conta")
        ent.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=10)
        self.l_titular = campo(ent, "Titular:", 0, 22)
        self.l_senha = campo(ent, "Senha (4 dígitos):", 1, 22)
        ent.winfo_children()[-1].configure(show="•")
        botao(ent, "🔐 Entrar", self.entrar).grid(row=2, column=0, columnspan=2, sticky="we", pady=(8, 0))
        novo = cartao(self.area, "Abrir nova conta")
        novo.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=10)
        self.n_titular = campo(novo, "Titular:", 0, 22)
        self.n_senha = campo(novo, "Senha (4 dígitos):", 1, 22)
        novo.winfo_children()[-1].configure(show="•")
        botao(novo, "✨ Criar conta", self.criar, "Verde").grid(row=2, column=0, columnspan=2, sticky="we", pady=(8, 0))
        self.lbl_contas = ttk.Label(self.area, text=f"Contas cadastradas: {len(self.contas)}", foreground="#5B6B7F")
        self.lbl_contas.grid(row=1, column=0, columnspan=2, sticky="w")

    @seguro
    def criar(self):
        conta = logica.criar_conta(self.contas, self.n_titular.get(), self.n_senha.get())
        logica.salvar_contas(self.contas)
        messagebox.showinfo("Conta criada", f"Bem-vindo(a), {conta.titular}! Agora faça o login.")
        self.tela_inicial()

    @seguro
    def entrar(self):
        self.conta = logica.entrar(self.contas, self.l_titular.get(), self.l_senha.get())
        self.tela_conta()

    # ------------------------------------------------------------------ conta
    def tela_conta(self):
        self.limpar()
        self.area.columnconfigure(0, weight=1)
        self.area.columnconfigure(1, weight=2)
        self.area.rowconfigure(0, weight=1)
        esq = cartao(self.area)
        esq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        ttk.Label(esq, text=f"Olá, {self.conta.titular}", style="Titulo.TLabel").pack(anchor="w")
        ttk.Label(esq, text="Saldo disponível", style="Card.TLabel").pack(anchor="w", pady=(12, 0))
        self.lbl_saldo = ttk.Label(esq, text="", style="Grande.TLabel")
        self.lbl_saldo.pack(anchor="w", pady=(0, 14))
        botao(esq, "⬇ Depositar", lambda: self.operar("Depositar")).pack(fill="x", pady=3)
        botao(esq, "⬆ Sacar", lambda: self.operar("Sacar"), "Ouro").pack(fill="x", pady=3)
        botao(esq, "⇄ Transferir", self.transferir, "Verde").pack(fill="x", pady=3)
        botao(esq, "⎋ Sair da conta", self.tela_inicial, "Perigo").pack(fill="x", pady=(18, 0))
        dir_ = cartao(self.area, "Extrato da sessão")
        dir_.grid(row=0, column=1, sticky="nsew")
        self.tv = tabela(dir_, ("Movimentação",), (520,), altura=14)
        self.atualizar()

    def atualizar(self):
        self.lbl_saldo.configure(text=logica.formatar(self.conta.saldo))
        linhas = self.conta.extrato()
        tags = []
        for t in linhas:
            tags.append("ok" if "+R$" in t else "erro" if "-R$" in t else None)
        preencher(self.tv, [(t,) for t in linhas], tags)

    @seguro
    def operar(self, nome):
        texto = simpledialog.askstring(nome, "Valor (R$):", parent=self.root)
        if texto is None:
            return
        valor = ler_float(texto, "Valor")
        (self.conta.depositar if nome == "Depositar" else self.conta.sacar)(valor)
        logica.salvar_contas(self.contas)
        self.atualizar()

    @seguro
    def transferir(self):
        titular = simpledialog.askstring("Transferir", "Titular da conta de destino:", parent=self.root)
        if titular is None:
            return
        destino = self.contas.get(titular.strip().title())
        if destino is None:
            raise ValueError("Conta de destino inexistente.")
        texto = simpledialog.askstring("Transferir", f"Valor para {destino.titular} (R$):", parent=self.root)
        if texto is None:
            return
        self.conta.transferir(destino, ler_float(texto, "Valor"))
        logica.salvar_contas(self.contas)
        self.atualizar()


if __name__ == "__main__":
    raiz = janela("Amazônia Bank", 900, 620)
    BancoApp(raiz)
    raiz.mainloop()
