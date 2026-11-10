"""Projeto 8 – Forca Amazônica: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk, messagebox

import logica
from ui_comum import janela, cabecalho, cartao, botao, seguro, NAVY, BLUE, GREEN, RED, GOLD

LETRAS = "abcdefghijklmnopqrstuvwxyz"


class ForcaApp:
    def __init__(self, root):
        self.root = root
        self.rodada = 0
        self.palavra, self.dica = "", ""
        self.acertadas, self.erradas = [], []
        self.terminou = True
        self.vitorias = 0
        self.total = 0
        cabecalho(root, "🪢  Forca Amazônica", "Projeto 8 • palavras da fauna e da flora do Amazonas")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(1, weight=1)
        corpo.rowconfigure(0, weight=1)
        esq = cartao(corpo, "Forca")
        esq.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        self.canvas = tk.Canvas(esq, width=250, height=290, bg="white", highlightthickness=0)
        self.canvas.pack()
        self.lbl_placar = ttk.Label(esq, text="", style="Card.TLabel", justify="left")
        self.lbl_placar.pack(anchor="w", pady=(8, 0))

        dir_ = cartao(corpo)
        dir_.grid(row=0, column=1, sticky="nsew")
        self.lbl_rodada = ttk.Label(dir_, text="", style="Titulo.TLabel")
        self.lbl_rodada.pack(anchor="w")
        self.lbl_dica = ttk.Label(dir_, text="", style="Card.TLabel", wraplength=560, font=("Segoe UI", 11, "italic"))
        self.lbl_dica.pack(anchor="w", pady=(4, 10))
        self.lbl_palavra = ttk.Label(dir_, text="", style="Grande.TLabel", font=("Consolas", 28, "bold"))
        self.lbl_palavra.pack(anchor="w", pady=6)
        self.lbl_vidas = ttk.Label(dir_, text="", style="Card.TLabel", font=("Segoe UI", 12, "bold"))
        self.lbl_vidas.pack(anchor="w")
        self.lbl_erradas = ttk.Label(dir_, text="", style="Erro.TLabel")
        self.lbl_erradas.pack(anchor="w", pady=(0, 8))
        teclado = ttk.Frame(dir_, style="Card.TFrame")
        teclado.pack(anchor="w", pady=6)
        self.teclas = {}
        for i, letra in enumerate(LETRAS):
            b = tk.Button(teclado, text=letra.upper(), width=3, font=("Segoe UI", 11, "bold"), bg="#EAF1FA", fg=NAVY,
                          relief="flat", cursor="hand2", command=lambda l=letra: self.jogar(l))
            b.grid(row=i // 9, column=i % 9, padx=2, pady=2)
            self.teclas[letra] = b
        self.lbl_fim = ttk.Label(dir_, text="", style="Ok.TLabel", font=("Segoe UI", 12, "bold"), wraplength=560)
        self.lbl_fim.pack(anchor="w", pady=(10, 4))
        self.btn_prox = botao(dir_, "▶ Próxima rodada", self.nova_rodada, "Verde")
        self.btn_prox.pack(anchor="w")
        root.bind("<Key>", self.tecla)
        self.nova_rodada()

    def tecla(self, evento):
        if evento.char and evento.char.lower() in LETRAS and not self.terminou:
            self.jogar(evento.char)

    @seguro
    def nova_rodada(self):
        self.rodada += 1
        self.palavra, self.dica = logica.escolher_palavra(self.rodada)
        self.acertadas, self.erradas = [], []
        self.terminou = False
        for b in self.teclas.values():
            b.configure(state="normal", bg="#EAF1FA")
        self.lbl_fim.configure(text="")
        self.btn_prox.state(["disabled"])
        self.atualizar()

    @seguro
    def jogar(self, texto):
        letra = logica.validar_letra(texto, self.acertadas + self.erradas)
        acertou = logica.jogar_letra(self.palavra, letra, self.acertadas, self.erradas)
        self.teclas[letra].configure(state="disabled", bg="#BFE5CE" if acertou else "#F3C1BD")
        self.atualizar()
        if logica.venceu(self.palavra, self.acertadas):
            self.encerrar(True)
        elif logica.vidas_restantes(self.erradas) <= 0:
            self.encerrar(False)

    @seguro
    def encerrar(self, vitoria):
        self.terminou = True
        pontos = logica.pontos_da_rodada(vitoria, logica.vidas_restantes(self.erradas))
        self.total += pontos
        if vitoria:
            self.vitorias += 1
            self.lbl_fim.configure(text=f"🎉 Parabéns! A palavra era {self.palavra.upper()}. +{pontos} pontos.", style="Ok.TLabel")
        else:
            self.lbl_fim.configure(text=f"Fim de jogo! A palavra era {self.palavra.upper()}.", style="Erro.TLabel")
        for b in self.teclas.values():
            b.configure(state="disabled")
        self.btn_prox.state(["!disabled"])
        self.atualizar()

    @seguro
    def atualizar(self):
        vidas = logica.vidas_restantes(self.erradas)
        self.lbl_rodada.configure(text=f"Rodada {self.rodada}")
        self.lbl_dica.configure(text=f"Dica: {self.dica}")
        exib = logica.montar_exibicao(self.palavra, self.acertadas)
        self.lbl_palavra.configure(text=exib)
        self.lbl_vidas.configure(text="Vidas: " + "♥ " * vidas + "♡ " * (logica.MAX_ERROS - vidas))
        self.lbl_erradas.configure(text="Erradas: " + (" ".join(l.upper() for l in self.erradas) or "—"))
        self.lbl_placar.configure(text=f"Rodadas: {self.rodada}\nVitórias: {self.vitorias}\nPontuação total: {self.total}")
        self.desenhar(len(self.erradas))

    def desenhar(self, erros):
        c = self.canvas
        c.delete("all")
        c.create_line(20, 270, 230, 270, width=5, fill="#6B4F2A")      # chão
        c.create_line(60, 270, 60, 25, width=5, fill="#6B4F2A")        # poste
        c.create_line(60, 25, 170, 25, width=5, fill="#6B4F2A")        # topo
        c.create_line(170, 25, 170, 60, width=3, fill="#6B4F2A")       # corda
        partes = [
            lambda: c.create_oval(150, 60, 190, 100, width=3, outline=NAVY),            # cabeça
            lambda: c.create_line(170, 100, 170, 175, width=3, fill=NAVY),             # tronco
            lambda: c.create_line(170, 115, 140, 150, width=3, fill=NAVY),             # braço esq.
            lambda: c.create_line(170, 115, 200, 150, width=3, fill=NAVY),             # braço dir.
            lambda: c.create_line(170, 175, 145, 220, width=3, fill=NAVY),             # perna esq.
            lambda: c.create_line(170, 175, 195, 220, width=3, fill=NAVY),             # perna dir.
        ]
        for i in range(min(erros, len(partes))):
            partes[i]()
        if erros >= logica.MAX_ERROS:
            c.create_text(160, 76, text="x x", fill=RED, font=("Segoe UI", 9, "bold"))


if __name__ == "__main__":
    raiz = janela("Forca Amazônica", 1000, 640)
    ForcaApp(raiz)
    raiz.mainloop()
