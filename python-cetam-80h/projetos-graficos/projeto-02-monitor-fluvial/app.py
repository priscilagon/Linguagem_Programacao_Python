"""Projeto 2 – Monitor Fluvial: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk

import logica
from ui_comum import (janela, cabecalho, cartao, botao, tabela, preencher, seguro,
                      ler_float, BLUE, GREEN, GOLD, RED, NAVY)

SUGESTAO = [26.1, 27.4, 28.3, 29.0, 29.6, 29.8, 29.2, 27.9, 25.7, 23.8, 23.1, 24.0]
COR = {"Cheia": BLUE, "Enchente/Vazante": GOLD, "Seca": RED}


class MonitorApp:
    def __init__(self, root):
        cabecalho(root, "🌊  Monitor Fluvial – Rio Negro", "Projeto 2 • nível mensal, classificação e gráfico")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(1, weight=1)
        corpo.rowconfigure(0, weight=1)

        ent = cartao(corpo, "1. Nível em metros (0 a 40)")
        ent.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        self.vars = []
        for i, mes in enumerate(logica.MESES):
            ttk.Label(ent, text=mes, style="Card.TLabel").grid(row=i % 6, column=(i // 6) * 2, sticky="e", padx=(8, 4), pady=3)
            v = tk.StringVar()
            ttk.Entry(ent, textvariable=v, width=7, justify="right").grid(row=i % 6, column=(i // 6) * 2 + 1, pady=3)
            self.vars.append(v)
        botao(ent, "📥 Usar dados de exemplo", self.exemplo, "Ouro").grid(row=6, column=0, columnspan=4, sticky="we", pady=(10, 3))
        botao(ent, "📊 Analisar o ano", self.analisar).grid(row=7, column=0, columnspan=4, sticky="we", pady=3)
        ttk.Label(ent, text="Consultar mês:", style="Card.TLabel").grid(row=8, column=0, columnspan=2, sticky="w", pady=(14, 0))
        self.busca = tk.StringVar()
        e = ttk.Entry(ent, textvariable=self.busca, width=10)
        e.grid(row=8, column=2, columnspan=2, sticky="we", pady=(14, 0))
        e.bind("<Return>", lambda _: self.consultar())
        botao(ent, "🔎 Consultar", self.consultar, "Verde").grid(row=9, column=0, columnspan=4, sticky="we", pady=3)
        self.lbl_consulta = ttk.Label(ent, text="", style="Ok.TLabel", wraplength=230)
        self.lbl_consulta.grid(row=10, column=0, columnspan=4, sticky="w")

        dir_ = ttk.Frame(corpo)
        dir_.grid(row=0, column=1, sticky="nsew")
        dir_.rowconfigure(1, weight=1)
        dir_.columnconfigure(0, weight=1)
        self.lbl_stats = ttk.Label(dir_, text="Digite os 12 níveis e clique em “Analisar o ano”.", style="Card.TLabel", padding=10, wraplength=620)
        self.lbl_stats.grid(row=0, column=0, sticky="we")
        graf = cartao(dir_, "2. Gráfico do ano")
        graf.grid(row=1, column=0, sticky="nsew", pady=8)
        self.canvas = tk.Canvas(graf, bg="white", height=230, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        rel = cartao(dir_, "3. Relatório mensal")
        rel.grid(row=2, column=0, sticky="nsew")
        self.tv = tabela(rel, ("Mês", "Nível (m)", "Classificação", "Barra"), (60, 90, 150, 300), altura=5)
        self.niveis = []

    def exemplo(self):
        for v, n in zip(self.vars, SUGESTAO):
            v.set(str(n))

    @seguro
    def ler_niveis(self):
        niveis = []
        for mes, v in zip(logica.MESES, self.vars):
            niveis.append(logica.validar_nivel(ler_float(v.get(), f"Nível de {mes}")))
        return niveis

    @seguro
    def analisar(self):
        niveis = self.ler_niveis()
        if niveis is None:
            return
        self.niveis = niveis
        e = logica.estatisticas(niveis)
        c = logica.contar_classificacoes(niveis)
        valor, mes = logica.maior_subida(niveis)
        self.lbl_stats.configure(text=(
            f"Média anual: {e['media']:.2f} m   •   Maior: {e['maior']:.1f} m ({e['mes_maior']})   •   "
            f"Menor: {e['menor']:.1f} m ({e['mes_menor']})\n"
            f"Cheia: {c['Cheia']}   •   Enchente/Vazante: {c['Enchente/Vazante']}   •   Seca: {c['Seca']}   •   "
            f"Maior subida: +{valor:.1f} m em {mes or '—'}"))
        linhas, tags = [], []
        for m, n in zip(logica.MESES, niveis):
            cl = logica.classificar(n)
            linhas.append((m, f"{n:.1f}", cl, logica.barra(n)))
            tags.append({"Cheia": "ok", "Enchente/Vazante": "alerta", "Seca": "erro"}[cl])
        preencher(self.tv, linhas, tags)
        self.desenhar()

    def desenhar(self):
        c = self.canvas
        c.delete("all")
        c.update_idletasks()
        w, h = max(c.winfo_width(), 560), max(c.winfo_height(), 200)
        base, topo, esq = h - 28, 16, 38
        largura = (w - esq - 14) / 12
        for marco in (0, 10, 20, 30, 40):
            y = base - (base - topo) * marco / 40
            c.create_line(esq, y, w - 8, y, fill="#E1E7EF")
            c.create_text(esq - 6, y, text=str(marco), anchor="e", fill="#5B6B7F", font=("Segoe UI", 8))
        for i, (m, n) in enumerate(zip(logica.MESES, self.niveis)):
            x0 = esq + i * largura + 6
            y = base - (base - topo) * n / 40
            cor = COR[logica.classificar(n)]
            c.create_rectangle(x0, y, x0 + largura - 12, base, fill=cor, outline="")
            c.create_text(x0 + (largura - 12) / 2, y - 8, text=f"{n:.1f}", fill=NAVY, font=("Segoe UI", 8, "bold"))
            c.create_text(x0 + (largura - 12) / 2, base + 12, text=m, fill=NAVY, font=("Segoe UI", 9))
        for nome, cor, x in (("Cheia", BLUE, 50), ("Enchente/Vazante", GOLD, 120), ("Seca", RED, 260)):
            c.create_rectangle(x + 150, 4, x + 162, 14, fill=cor, outline="")
            c.create_text(x + 168, 9, text=nome, anchor="w", font=("Segoe UI", 8), fill=NAVY)

    @seguro
    def consultar(self):
        if not self.niveis:
            raise ValueError("Analise o ano primeiro (clique em “Analisar o ano”).")
        mes, nivel, classe = logica.consultar_mes(self.busca.get(), self.niveis)
        self.lbl_consulta.configure(text=f"{mes}: {nivel:.1f} m – {classe}")


if __name__ == "__main__":
    raiz = janela("Monitor Fluvial – Rio Negro", 1100, 720)
    MonitorApp(raiz)
    raiz.mainloop()
