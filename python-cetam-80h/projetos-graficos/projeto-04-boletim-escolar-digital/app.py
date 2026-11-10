"""Projeto 4 – Boletim Escolar Digital: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk, messagebox

import logica
from ui_comum import (janela, cabecalho, cartao, botao, campo, tabela, preencher, seguro, carregar_seguro,
                      ler_float, BLUE, GREEN, GOLD, RED, NAVY)

COR_SIT = {"Aprovado": GREEN, "Recuperação": GOLD, "Reprovado": RED}
TAG_SIT = {"Aprovado": "ok", "Recuperação": "alerta", "Reprovado": "erro"}


class BoletimApp:
    def __init__(self, root):
        self.alunos = carregar_seguro(logica.carregar_alunos, [])          # RF01
        cabecalho(root, "📝  Boletim Escolar Digital", "Projeto 4 • notas, médias, situação e arquivo boletim.txt")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(1, weight=1)
        corpo.rowconfigure(0, weight=1)

        esq = ttk.Frame(corpo)
        esq.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        cad = cartao(esq, "Cadastrar aluno")
        cad.pack(fill="x")
        self.nome = campo(cad, "Nome:", 0, 20)
        self.n = [campo(cad, f"Nota {i + 1}:", i + 1, 20) for i in range(3)]
        botao(cad, "💾 Cadastrar e salvar", self.cadastrar, "Verde").grid(row=4, column=0, columnspan=2, sticky="we", pady=(6, 0))
        bus = cartao(esq, "Buscar aluno")
        bus.pack(fill="x", pady=10)
        self.busca = campo(bus, "Nome:", 0, 20)
        botao(bus, "🔎 Buscar", self.buscar).grid(row=1, column=0, columnspan=2, sticky="we", pady=(6, 0))
        self.lbl_busca = ttk.Label(bus, text="", style="Ok.TLabel", wraplength=240, justify="left")
        self.lbl_busca.grid(row=2, column=0, columnspan=2, sticky="w", pady=(4, 0))
        botao(esq, "📤 Exportar relatorio.txt", self.exportar, "Ouro").pack(fill="x")

        dire = ttk.Frame(corpo)
        dire.grid(row=0, column=1, sticky="nsew")
        lst = cartao(dire, "Boletim da turma")
        lst.pack(fill="both", expand=True)
        self.tv = tabela(lst, ("Aluno", "Nota 1", "Nota 2", "Nota 3", "Média", "Situação"), (170, 60, 60, 60, 70, 110), altura=8)
        est = cartao(dire, "Estatísticas da turma")
        est.pack(fill="x", pady=(10, 0))
        self.lbl_est = ttk.Label(est, text="", style="Card.TLabel", justify="left")
        self.lbl_est.pack(anchor="w")
        self.canvas = tk.Canvas(est, bg="white", height=150, highlightthickness=0)
        self.canvas.pack(fill="x", pady=(6, 0))
        self.atualizar()

    @seguro
    def cadastrar(self):
        notas = [logica.validar_nota(ler_float(v.get(), f"Nota {i + 1}")) for i, v in enumerate(self.n)]
        aluno = logica.cadastrar_aluno(self.alunos, self.nome.get(), notas)
        logica.salvar_alunos(self.alunos)
        self.nome.set("")
        for v in self.n:
            v.set("")
        self.atualizar()
        messagebox.showinfo("Cadastro", f"{aluno['nome']} cadastrado e salvo em {logica.ARQUIVO}.")

    @seguro
    def buscar(self):
        a = logica.buscar_aluno(self.alunos, self.busca.get())
        if a is None:
            self.lbl_busca.configure(text="Aluno não encontrado.", style="Erro.TLabel")
            return
        m = logica.calcular_media(a["notas"])
        self.lbl_busca.configure(text=f"{a['nome']}: média {m:.2f} – {logica.situacao(m)}", style="Ok.TLabel")

    @seguro
    def exportar(self):
        n = logica.exportar_relatorio(self.alunos)
        messagebox.showinfo("Relatório", f"{n} aluno(s) exportado(s) para relatorio.txt")

    @seguro
    def atualizar(self):
        linhas, tags = [], []
        for a in self.alunos:
            m = logica.calcular_media(a["notas"])
            s = logica.situacao(m)
            linhas.append((a["nome"], *[f"{x:g}" for x in a["notas"]], f"{m:.2f}", s))
            tags.append(TAG_SIT[s])
        preencher(self.tv, linhas, tags)
        c = self.canvas
        c.delete("all")
        try:
            e = logica.estatisticas(self.alunos)
        except ValueError as erro:
            self.lbl_est.configure(text=str(erro))
            return
        s = e["situacoes"]
        self.lbl_est.configure(text=(f"Média da turma: {e['media_turma']:.2f}   •   Maior média: {e['melhor_nome']} ({e['melhor_media']:.2f})\n"
                                     f"Aprovados: {s['Aprovado']}   •   Recuperação: {s['Recuperação']}   •   Reprovados: {s['Reprovado']}"))
        c.update_idletasks()
        w = max(c.winfo_width(), 500)
        n = len(self.alunos)
        larg = min(70, (w - 40) / max(n, 1))
        for i, a in enumerate(self.alunos):
            m = logica.calcular_media(a["notas"])
            x0 = 24 + i * larg
            y = 130 - 110 * m / 10
            c.create_rectangle(x0, y, x0 + larg - 10, 130, fill=COR_SIT[logica.situacao(m)], outline="")
            c.create_text(x0 + (larg - 10) / 2, y - 8, text=f"{m:.1f}", font=("Segoe UI", 8, "bold"), fill=NAVY)
            c.create_text(x0 + (larg - 10) / 2, 142, text=a["nome"].split()[0], font=("Segoe UI", 8), fill=NAVY)
        c.create_line(20, 53, w - 10, 53, fill="#C9D3E0", dash=(3, 3))   # linha da média 7


if __name__ == "__main__":
    raiz = janela("Boletim Escolar Digital", 1100, 700)
    BoletimApp(raiz)
    raiz.mainloop()
