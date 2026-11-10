"""Projeto 6 – Quiz da Floresta Amazônica: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk, messagebox

import logica
from ui_comum import janela, cabecalho, cartao, botao, seguro, NAVY, BLUE, GREEN, RED, GOLD


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.partidas = 0
        self.melhor = 0
        cabecalho(root, "🌳  Quiz da Floresta Amazônica", "Projeto 6 • perguntas, pontos, bônus de sequência e recorde")
        self.area = ttk.Frame(root, padding=16)
        self.area.pack(fill="both", expand=True)
        self.menu()

    def limpar(self):
        for w in self.area.winfo_children():
            w.destroy()

    def menu(self):
        self.limpar()
        card = cartao(self.area)
        card.pack(fill="x", pady=20, padx=80)
        ttk.Label(card, text="Você conhece a Amazônia?", style="Titulo.TLabel").pack(pady=(10, 4))
        ttk.Label(card, text=f"Partidas: {self.partidas}   •   Melhor pontuação: {self.melhor}", style="Card.TLabel").pack(pady=4)
        botao(card, "▶  Jogar", self.jogar, "Verde").pack(fill="x", padx=60, pady=6)
        botao(card, "📖  Regras", self.regras).pack(fill="x", padx=60, pady=6)
        botao(card, "⎋  Sair", self.sair, "Perigo").pack(fill="x", padx=60, pady=(6, 14))

    def regras(self):
        messagebox.showinfo("Regras", "• 5 perguntas de múltipla escolha.\n• Cada acerto vale 10 pontos.\n"
                            "• A cada 3 acertos seguidos: +5 de bônus.\n• 50+ pontos: Guardião da Floresta | "
                            "30 a 49: Explorador | abaixo de 30: Aprendiz.")

    def sair(self):
        messagebox.showinfo("Até logo!", f"Partidas jogadas: {self.partidas}\nMelhor pontuação: {self.melhor}")
        self.root.destroy()

    # ------------------------------------------------------------------
    @seguro
    def jogar(self):
        self.i = 0
        self.resultados = []
        self.mostrar_pergunta()

    def mostrar_pergunta(self):
        self.limpar()
        p = logica.PERGUNTAS[self.i]
        topo = ttk.Frame(self.area)
        topo.pack(fill="x")
        ttk.Label(topo, text=f"Pergunta {self.i + 1} de {len(logica.PERGUNTAS)}", font=("Segoe UI", 11, "bold")).pack(side="left")
        ttk.Label(topo, text=f"Pontos: {logica.calcular_pontos(self.resultados)}", font=("Segoe UI", 11, "bold"), foreground=BLUE).pack(side="right")
        barra = ttk.Progressbar(self.area, maximum=len(logica.PERGUNTAS), value=self.i)
        barra.pack(fill="x", pady=8)
        card = cartao(self.area)
        card.pack(fill="x", pady=8)
        ttk.Label(card, text=p["texto"], style="Titulo.TLabel", wraplength=780).pack(anchor="w", pady=(4, 12))
        self.botoes = []
        for alt in p["alternativas"]:
            letra = alt[0]
            b = tk.Button(card, text=alt, font=("Segoe UI", 12), anchor="w", bg="#EAF1FA", fg=NAVY, relief="flat",
                          activebackground="#CFE0F5", padx=14, pady=8, cursor="hand2",
                          command=lambda l=letra: self.responder(l))
            b.pack(fill="x", pady=4)
            self.botoes.append((letra, b))
        self.lbl_fb = ttk.Label(card, text="", style="Ok.TLabel", font=("Segoe UI", 12, "bold"))
        self.lbl_fb.pack(anchor="w", pady=(10, 0))
        self.root.bind("<Key>", self.tecla)

    def tecla(self, evento):
        if evento.char and evento.char.upper() in "ABCD" and self.botoes and self.botoes[0][1]["state"] == "normal":
            self.responder(evento.char)

    @seguro
    def responder(self, texto):
        letra = logica.validar_resposta(texto)
        p = logica.PERGUNTAS[self.i]
        acertou = logica.conferir(p, letra)
        self.resultados.append(acertou)
        for l, b in self.botoes:
            b.configure(state="disabled", disabledforeground=NAVY)
            if l == p["correta"]:
                b.configure(bg="#BFE5CE")
            elif l == letra:
                b.configure(bg="#F3C1BD")
        if acertou:
            self.lbl_fb.configure(text="✔ Acertou!", style="Ok.TLabel")
        else:
            self.lbl_fb.configure(text=f"✘ Errou. A correta é a alternativa {p['correta']}.", style="Erro.TLabel")
        ultimo = self.i == len(logica.PERGUNTAS) - 1
        self.root.after(1300, self.fim if ultimo else self.proxima)

    @seguro
    def proxima(self):
        self.i += 1
        self.mostrar_pergunta()

    @seguro
    def fim(self):
        self.root.unbind("<Key>")
        pontos = logica.calcular_pontos(self.resultados)
        self.partidas += 1
        recorde = logica.novo_recorde(pontos, self.melhor)
        if recorde:
            self.melhor = pontos
        self.limpar()
        card = cartao(self.area)
        card.pack(fill="x", pady=20, padx=60)
        ttk.Label(card, text="Fim da partida!", style="Titulo.TLabel").pack(pady=(8, 2))
        ttk.Label(card, text=f"{pontos} pontos", style="Grande.TLabel").pack()
        ttk.Label(card, text=f"Acertos: {sum(self.resultados)} de {len(self.resultados)}", style="Card.TLabel").pack()
        ttk.Label(card, text=f"Título: {logica.titulo(pontos)}", style="Card.TLabel", font=("Segoe UI", 13, "bold")).pack(pady=6)
        if recorde:
            ttk.Label(card, text="🏆 Novo recorde da sessão!", style="Ok.TLabel").pack()
        botao(card, "Jogar de novo", self.jogar, "Verde").pack(fill="x", padx=80, pady=(12, 4))
        botao(card, "Menu", self.menu).pack(fill="x", padx=80, pady=(0, 12))


if __name__ == "__main__":
    raiz = janela("Quiz da Floresta Amazônica", 900, 640)
    QuizApp(raiz)
    raiz.mainloop()
