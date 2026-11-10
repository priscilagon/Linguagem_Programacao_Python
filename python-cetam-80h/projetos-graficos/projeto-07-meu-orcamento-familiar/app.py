"""Projeto 7 – Meu Orçamento Familiar: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk

import logica
from ui_comum import (janela, cabecalho, cartao, botao, campo, tabela, preencher, seguro,
                      moeda, ler_float, NAVY, BLUE, GREEN, GOLD, RED)

CORES = [BLUE, GREEN, GOLD, RED, "#7B4FB5", "#5B6B7F"]


class OrcamentoApp:
    def __init__(self, root):
        self.lancamentos = []
        cabecalho(root, "💰  Meu Orçamento Familiar", "Projeto 7 • receitas, despesas por categoria e situação do mês")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(1, weight=1)
        corpo.rowconfigure(0, weight=1)

        esq = ttk.Frame(corpo)
        esq.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        rec = cartao(esq, "Registrar receita")
        rec.pack(fill="x")
        self.r_desc = campo(rec, "Descrição:", 0, 20)
        self.r_valor = campo(rec, "Valor (R$):", 1, 20)
        botao(rec, "➕ Receita", self.add_receita, "Verde").grid(row=2, column=0, columnspan=2, sticky="we", pady=(6, 0))
        des = cartao(esq, "Registrar despesa")
        des.pack(fill="x", pady=10)
        self.d_desc = campo(des, "Descrição:", 0, 20)
        ttk.Label(des, text="Categoria:", style="Card.TLabel").grid(row=1, column=0, sticky="w", pady=3)
        self.d_cat = ttk.Combobox(des, state="readonly", width=18,
                                  values=[f"{i + 1} – {c}" for i, c in enumerate(logica.CATEGORIAS)])
        self.d_cat.current(0)
        self.d_cat.grid(row=1, column=1, sticky="we")
        self.d_valor = campo(des, "Valor (R$):", 2, 20)
        botao(des, "➖ Despesa", self.add_despesa, "Perigo").grid(row=3, column=0, columnspan=2, sticky="we", pady=(6, 0))

        dir_ = ttk.Frame(corpo)
        dir_.grid(row=0, column=1, sticky="nsew")
        dir_.columnconfigure(0, weight=1)
        dir_.columnconfigure(1, weight=1)
        dir_.rowconfigure(1, weight=1)
        res = cartao(dir_, "Resumo do mês")
        res.grid(row=0, column=0, columnspan=2, sticky="we")
        self.lbl_res = ttk.Label(res, text="", style="Card.TLabel", justify="left")
        self.lbl_res.pack(anchor="w")
        self.medidor = tk.Canvas(res, height=34, bg="white", highlightthickness=0)
        self.medidor.pack(fill="x", pady=(8, 0))
        self.lbl_sit = ttk.Label(res, text="", style="Ok.TLabel", font=("Segoe UI", 11, "bold"))
        self.lbl_sit.pack(anchor="w", pady=(4, 0))

        lan = cartao(dir_, "Lançamentos")
        lan.grid(row=1, column=0, sticky="nsew", padx=(0, 6), pady=(10, 0))
        self.tv = tabela(lan, ("Nº", "Categoria", "Descrição", "Valor"), (35, 100, 130, 100), altura=9)
        cat = cartao(dir_, "Despesas por categoria")
        cat.grid(row=1, column=1, sticky="nsew", padx=(6, 0), pady=(10, 0))
        self.canvas = tk.Canvas(cat, bg="white", highlightthickness=0, width=300, height=250)
        self.canvas.pack(fill="both", expand=True)
        self.atualizar()

    @seguro
    def add_receita(self):
        self.lancamentos.append(logica.novo_lancamento("receita", self.r_desc.get(), ler_float(self.r_valor.get(), "Valor")))
        self.r_desc.set(""); self.r_valor.set("")
        self.atualizar()

    @seguro
    def add_despesa(self):
        numero = int(self.d_cat.get().split(" ")[0])
        self.lancamentos.append(logica.novo_lancamento("despesa", self.d_desc.get(), ler_float(self.d_valor.get(), "Valor"), numero))
        self.d_desc.set(""); self.d_valor.set("")
        self.atualizar()

    @seguro
    def atualizar(self):
        linhas, tags = [], []
        for i, l in enumerate(self.lancamentos, 1):
            sinal = "+" if l["tipo"] == "receita" else "−"
            linhas.append((i, l["categoria"], l["descricao"], f"{sinal} {moeda(l['valor'])}"))
            tags.append("ok" if l["tipo"] == "receita" else "erro")
        preencher(self.tv, linhas, tags)
        rec, desp, saldo = logica.totais(self.lancamentos)
        pct = logica.percentual_comprometido(rec, desp)
        self.lbl_res.configure(text=(f"Receitas: {moeda(rec)}     Despesas: {moeda(desp)}     Saldo: {moeda(saldo)}\n"
                                     f"Renda comprometida: {'—' if pct is None else f'{pct:.1f}%'}"))
        sit = logica.situacao_orcamento(pct)
        cor = "Ok.TLabel" if sit == "Saudável" else "Erro.TLabel"
        self.lbl_sit.configure(text=f"Situação: {sit}", style=cor)
        self.desenhar_medidor(pct)
        self.desenhar_categorias()

    def desenhar_medidor(self, pct):
        c = self.medidor
        c.delete("all")
        c.update_idletasks()
        w = max(c.winfo_width(), 400)
        c.create_rectangle(2, 8, w - 2, 26, fill="#E6ECF4", outline="")
        if pct is not None:
            preenchido = min(pct, 100) / 100 * (w - 4)
            cor = GREEN if pct <= 70 else GOLD if pct <= 100 else RED
            c.create_rectangle(2, 8, 2 + preenchido, 26, fill=cor, outline="")
        c.create_line(2 + 0.7 * (w - 4), 4, 2 + 0.7 * (w - 4), 30, fill=NAVY, dash=(2, 2))
        c.create_text(2 + 0.7 * (w - 4), 31, text="70%", font=("Segoe UI", 7), fill=NAVY, anchor="n")

    def desenhar_categorias(self):
        c = self.canvas
        c.delete("all")
        por = logica.despesas_por_categoria(self.lancamentos)
        if not por:
            c.create_text(150, 110, text="Sem despesas ainda.", fill="#5B6B7F")
            return
        pct = logica.percentuais_por_categoria(por)
        maior, valor = logica.categoria_maior_gasto(por)
        y = 14
        for i, (nome, total) in enumerate(por.items()):
            cor = CORES[logica.CATEGORIAS.index(nome)]
            c.create_text(6, y + 8, text=nome, anchor="w", font=("Segoe UI", 9, "bold" if nome == maior else "normal"), fill=NAVY)
            c.create_rectangle(100, y, 100 + 1.6 * pct[nome], y + 16, fill=cor, outline="")
            c.create_text(104 + 1.6 * pct[nome], y + 8, text=f"{pct[nome]:.0f}%", anchor="w", font=("Segoe UI", 8), fill=NAVY)
            y += 30
        c.create_text(6, y + 10, text=f"Maior gasto: {maior} ({moeda(valor)})", anchor="w", font=("Segoe UI", 9, "bold"), fill=RED)


if __name__ == "__main__":
    raiz = janela("Meu Orçamento Familiar", 1120, 720)
    OrcamentoApp(raiz)
    raiz.mainloop()
