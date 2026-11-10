"""Projeto 10 – Biblioteca Comunitária: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk

import logica
from ui_comum import (janela, cabecalho, cartao, botao, campo, tabela, preencher, seguro,
                      ler_int, moeda, NAVY, BLUE, GREEN, GOLD, RED)


class BibliotecaApp:
    def __init__(self, root):
        self.bib = logica.Biblioteca()
        cabecalho(root, "📚  Biblioteca Comunitária", "Projeto 10 • empréstimos, multas e arquivo acervo.txt (orientação a objetos)")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(1, weight=1)
        corpo.rowconfigure(0, weight=1)

        esq = ttk.Frame(corpo)
        esq.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        cad = cartao(esq, "Cadastrar livro")
        cad.pack(fill="x")
        self.c_tit = campo(cad, "Título:", 0, 22)
        self.c_aut = campo(cad, "Autor:", 1, 22)
        botao(cad, "➕ Cadastrar", self.cadastrar, "Verde").grid(row=2, column=0, columnspan=2, sticky="we", pady=(6, 0))
        emp = cartao(esq, "Emprestar / devolver")
        emp.pack(fill="x", pady=10)
        self.m_cod = campo(emp, "Código:", 0, 22)
        self.m_leitor = campo(emp, "Leitor:", 1, 22)
        self.m_dias = campo(emp, "Dias de uso:", 2, 22, "7")
        botao(emp, "📤 Emprestar", self.emprestar).grid(row=3, column=0, columnspan=2, sticky="we", pady=(6, 2))
        botao(emp, "📥 Devolver", self.devolver, "Ouro").grid(row=4, column=0, columnspan=2, sticky="we", pady=2)
        self.lbl_msg = ttk.Label(esq, text="Regras: prazo de 7 dias, multa de R$ 0,50 por dia de atraso, máximo de 3 livros por leitor.",
                                 style="Ok.TLabel", wraplength=290, justify="left")
        self.lbl_msg.pack(anchor="w", pady=4)

        dir_ = ttk.Frame(corpo)
        dir_.grid(row=0, column=1, sticky="nsew")
        dir_.columnconfigure(0, weight=1)
        dir_.rowconfigure(1, weight=1)
        self.lbl_rel = ttk.Label(dir_, text="", style="Card.TLabel", padding=10, font=("Segoe UI", 10, "bold"))
        self.lbl_rel.grid(row=0, column=0, sticky="we")
        lst = cartao(dir_, "Acervo (verde = disponível, vermelho = emprestado)")
        lst.grid(row=1, column=0, sticky="nsew", pady=(8, 0))
        topo = ttk.Frame(lst, style="Card.TFrame")
        topo.pack(fill="x", pady=(0, 6))
        ttk.Label(topo, text="🔎 Buscar por título:", style="Card.TLabel").pack(side="left")
        self.busca = tk.StringVar()
        self.busca.trace_add("write", lambda *_: self.atualizar())
        ttk.Entry(topo, textvariable=self.busca, width=26).pack(side="left", padx=6)
        self.tv = tabela(lst, ("Código", "Título", "Autor", "Situação"), (70, 250, 160, 160), altura=11)
        self.tv.bind("<<TreeviewSelect>>", self.selecionar)
        self.atualizar()

    def selecionar(self, _e=None):
        sel = self.tv.selection()
        if sel:
            self.m_cod.set(self.tv.item(sel[0], "values")[0])

    def resultado(self, ok, msg):
        self.lbl_msg.configure(text=msg, style="Ok.TLabel" if ok else "Erro.TLabel")
        self.atualizar()

    @seguro
    def cadastrar(self):
        livro = self.bib.adicionar(self.c_tit.get(), self.c_aut.get())
        self.c_tit.set(""); self.c_aut.set("")
        self.resultado(True, f"{livro.codigo} – {livro.titulo} cadastrado.")

    @seguro
    def emprestar(self):
        self.resultado(*self.bib.emprestar(self.m_cod.get(), self.m_leitor.get()))

    @seguro
    def devolver(self):
        self.resultado(*self.bib.devolver(self.m_cod.get(), ler_int(self.m_dias.get(), "Dias de uso")))

    @seguro
    def atualizar(self):
        achados = self.bib.buscar_por_titulo(self.busca.get()) if self.busca.get().strip() else list(self.bib.livros.values())
        linhas, tags = [], []
        for l in achados:
            linhas.append((l.codigo, l.titulo, l.autor, "Disponível" if l.esta_disponivel() else f"Com {l.leitor}"))
            tags.append("ok" if l.esta_disponivel() else "erro")
        preencher(self.tv, linhas, tags)
        r = self.bib.relatorio()
        self.lbl_rel.configure(text=(f"Total: {r['total']}   •   Disponíveis: {r['disponiveis']}   •   "
                                     f"Emprestados: {r['emprestados']}   •   Multas na sessão: {moeda(r['multas'])}"))


if __name__ == "__main__":
    raiz = janela("Biblioteca Comunitária", 1120, 700)
    BibliotecaApp(raiz)
    raiz.mainloop()
