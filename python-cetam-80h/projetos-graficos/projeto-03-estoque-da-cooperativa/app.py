"""Projeto 3 – Estoque da Cooperativa Ribeirinha: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk

import logica
from ui_comum import (janela, cabecalho, cartao, botao, campo, tabela, preencher, seguro,
                      moeda, ler_float, ler_int)


class EstoqueApp:
    def __init__(self, root):
        self.root = root
        self.estoque = logica.estoque_inicial()
        self.total_vendido = 0.0
        cabecalho(root, "📦  Estoque da Cooperativa Ribeirinha", "Projeto 3 • cadastro, venda, reposição e relatório")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(0, weight=3)
        corpo.columnconfigure(1, weight=2)
        corpo.rowconfigure(0, weight=1)

        esq = cartao(corpo, "Estoque atual (linhas vermelhas = estoque baixo)")
        esq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.tv = tabela(esq, ("Produto", "Preço", "Qtd", "Valor em estoque"), (180, 90, 70, 130), altura=14)
        self.tv.bind("<<TreeviewSelect>>", self.selecionar)
        self.lbl_rel = ttk.Label(esq, text="", style="Card.TLabel", justify="left")
        self.lbl_rel.pack(anchor="w", pady=(8, 0))

        dire = ttk.Frame(corpo)
        dire.grid(row=0, column=1, sticky="nsew")
        cad = cartao(dire, "Cadastrar produto")
        cad.pack(fill="x")
        self.c_nome = campo(cad, "Nome:", 0, 18)
        self.c_preco = campo(cad, "Preço (R$):", 1, 18)
        self.c_qtd = campo(cad, "Qtd inicial:", 2, 18, "0")
        botao(cad, "➕ Cadastrar", self.cadastrar, "Verde").grid(row=3, column=0, columnspan=2, sticky="we", pady=(6, 0))

        mov = cartao(dire, "Vender / repor (selecione na tabela)")
        mov.pack(fill="x", pady=10)
        self.m_nome = campo(mov, "Produto:", 0, 18)
        self.m_qtd = campo(mov, "Quantidade:", 1, 18, "1")
        botao(mov, "💰 Vender", self.vender).grid(row=2, column=0, sticky="we", pady=(6, 0), padx=(0, 4))
        botao(mov, "⬆ Repor", self.repor, "Ouro").grid(row=2, column=1, sticky="we", pady=(6, 0))
        self.lbl_msg = ttk.Label(dire, text="", style="Ok.TLabel", wraplength=300, justify="left")
        self.lbl_msg.pack(anchor="w", padx=4)
        self.atualizar()

    def selecionar(self, _evento=None):
        sel = self.tv.selection()
        if sel:
            self.m_nome.set(self.tv.item(sel[0], "values")[0])

    def msg(self, texto, erro=False):
        self.lbl_msg.configure(text=texto, style="Erro.TLabel" if erro else "Ok.TLabel")

    @seguro
    def atualizar(self):
        baixos = set(logica.estoque_baixo(self.estoque))
        linhas, tags = [], []
        for nome, d in self.estoque.items():
            linhas.append((nome, moeda(d["preco"]), d["qtd"], moeda(d["preco"] * d["qtd"])))
            tags.append("erro" if nome in baixos else None)
        preencher(self.tv, linhas, tags)
        r = logica.relatorio(self.estoque, self.total_vendido)
        baixo = ", ".join(r["baixo"]) or "nenhum"
        self.lbl_rel.configure(text=(
            f"Produtos: {r['produtos']}   •   Valor em estoque: {moeda(r['valor_estoque'])}\n"
            f"Total vendido na sessão: {moeda(r['total_vendido'])}   •   Mais caro: {r['mais_caro'] or '—'}\n"
            f"Estoque baixo (< {logica.MINIMO}): {baixo}"))

    @seguro
    def cadastrar(self):
        nome = logica.cadastrar_produto(self.estoque, self.c_nome.get(),
                                        ler_float(self.c_preco.get(), "Preço"),
                                        ler_int(self.c_qtd.get(), "Quantidade"))
        self.msg(f"{nome} cadastrado com sucesso.")
        self.c_nome.set(""); self.c_preco.set(""); self.c_qtd.set("0")
        self.atualizar()

    @seguro
    def vender(self):
        valor = logica.vender(self.estoque, self.m_nome.get(), ler_int(self.m_qtd.get(), "Quantidade"))
        self.total_vendido += valor
        self.msg(f"Venda registrada: {moeda(valor)}.")
        self.atualizar()

    @seguro
    def repor(self):
        logica.repor(self.estoque, self.m_nome.get(), ler_int(self.m_qtd.get(), "Quantidade"))
        self.msg("Estoque reposto.")
        self.atualizar()


if __name__ == "__main__":
    raiz = janela("Estoque da Cooperativa Ribeirinha", 1050, 640)
    EstoqueApp(raiz)
    raiz.mainloop()
