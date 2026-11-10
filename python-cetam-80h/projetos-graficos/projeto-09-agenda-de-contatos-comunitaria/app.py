"""Projeto 9 – Agenda de Contatos Comunitária: TELA (já pronta).  Execute:  python app.py"""
import tkinter as tk
from tkinter import ttk, messagebox

import logica
from ui_comum import janela, cabecalho, cartao, botao, campo, tabela, preencher, seguro, carregar_seguro, NAVY, BLUE, GREEN


class AgendaApp:
    def __init__(self, root):
        self.contatos = carregar_seguro(logica.carregar_contatos, [])          # RF01
        cabecalho(root, "📒  Agenda de Contatos Comunitária", "Projeto 9 • cadastro, busca, edição, remoção e arquivo agenda.txt")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(1, weight=1)
        corpo.rowconfigure(0, weight=1)

        esq = ttk.Frame(corpo)
        esq.grid(row=0, column=0, sticky="ns", padx=(0, 10))
        form = cartao(esq, "Dados do contato")
        form.pack(fill="x")
        self.nome = campo(form, "Nome:", 0, 22)
        self.tel = campo(form, "Telefone:", 1, 22)
        self.email = campo(form, "E-mail:", 2, 22)
        self.bairro = campo(form, "Bairro:", 3, 22)
        botao(form, "💾 Cadastrar", self.cadastrar, "Verde").grid(row=4, column=0, columnspan=2, sticky="we", pady=(8, 2))
        botao(form, "✏ Editar (campo vazio mantém)", self.editar).grid(row=5, column=0, columnspan=2, sticky="we", pady=2)
        botao(form, "🗑 Remover", self.remover, "Perigo").grid(row=6, column=0, columnspan=2, sticky="we", pady=2)
        botao(form, "🧹 Limpar campos", self.limpar_campos, "Ouro").grid(row=7, column=0, columnspan=2, sticky="we", pady=2)
        self.lbl_msg = ttk.Label(esq, text="", style="Ok.TLabel", wraplength=300, justify="left")
        self.lbl_msg.pack(anchor="w", pady=8)

        dir_ = ttk.Frame(corpo)
        dir_.grid(row=0, column=1, sticky="nsew")
        dir_.columnconfigure(0, weight=1)
        dir_.rowconfigure(0, weight=1)
        lst = cartao(dir_, "Contatos (clique para preencher o formulário)")
        lst.grid(row=0, column=0, sticky="nsew")
        topo = ttk.Frame(lst, style="Card.TFrame")
        topo.pack(fill="x", pady=(0, 6))
        ttk.Label(topo, text="🔎 Buscar:", style="Card.TLabel").pack(side="left")
        self.busca = tk.StringVar()
        self.busca.trace_add("write", lambda *_: self.atualizar())
        ttk.Entry(topo, textvariable=self.busca, width=28).pack(side="left", padx=6)
        self.lbl_total = ttk.Label(topo, text="", style="Card.TLabel")
        self.lbl_total.pack(side="right")
        self.tv = tabela(lst, ("Nome", "Telefone", "E-mail", "Bairro"), (170, 110, 190, 110), altura=10)
        self.tv.bind("<<TreeviewSelect>>", self.selecionar)
        res = cartao(dir_, "Resumo por bairro")
        res.grid(row=1, column=0, sticky="we", pady=(10, 0))
        self.canvas = tk.Canvas(res, bg="white", height=110, highlightthickness=0)
        self.canvas.pack(fill="x")
        self.atualizar()

    def msg(self, texto, erro=False):
        self.lbl_msg.configure(text=texto, style="Erro.TLabel" if erro else "Ok.TLabel")

    def limpar_campos(self):
        for v in (self.nome, self.tel, self.email, self.bairro):
            v.set("")

    def selecionar(self, _e=None):
        sel = self.tv.selection()
        if sel:
            nome, tel, email, bairro = self.tv.item(sel[0], "values")
            self.nome.set(nome); self.tel.set(tel); self.email.set(email); self.bairro.set(bairro)

    @seguro
    def cadastrar(self):
        c = logica.cadastrar_contato(self.contatos, self.nome.get(), self.tel.get(), self.email.get(), self.bairro.get())
        logica.salvar_contatos(self.contatos)
        self.msg(f"{c['nome']} cadastrado e salvo.")
        self.limpar_campos()
        self.atualizar()

    @seguro
    def editar(self):
        avisos = logica.editar_contato(self.contatos, self.nome.get(), self.tel.get(), self.email.get(), self.bairro.get())
        logica.salvar_contatos(self.contatos)
        self.msg("Contato atualizado." + ("\n" + "\n".join(avisos) if avisos else ""), erro=bool(avisos))
        self.atualizar()

    @seguro
    def remover(self):
        nome = self.nome.get()
        if logica.buscar_contato(self.contatos, nome) is None:
            raise ValueError("Contato não encontrado.")
        if messagebox.askyesno("Remover", f"Remover {nome.strip().title()}?"):
            logica.remover_contato(self.contatos, nome)
            logica.salvar_contatos(self.contatos)
            self.msg("Contato removido.")
            self.limpar_campos()
            self.atualizar()

    @seguro
    def atualizar(self):
        lista = logica.buscar_por_trecho(self.contatos, self.busca.get()) if self.busca.get().strip() else logica.listar_ordenado(self.contatos)
        preencher(self.tv, [(c["nome"], c["telefone"], c["email"], c["bairro"]) for c in lista])
        self.lbl_total.configure(text=f"{len(lista)} de {len(self.contatos)} contato(s)")
        c = self.canvas
        c.delete("all")
        resumo = logica.resumo_por_bairro(self.contatos)
        if not resumo:
            c.create_text(10, 20, text="Nenhum contato cadastrado.", anchor="w", fill="#5B6B7F")
            return
        maior = max(resumo.values())
        for i, (bairro, qtd) in enumerate(sorted(resumo.items())):
            col, lin = i // 3, i % 3
            x0, y0 = 10 + col * 330, 8 + lin * 32
            c.create_text(x0, y0 + 10, text=bairro, anchor="w", font=("Segoe UI", 9), fill=NAVY)
            c.create_rectangle(x0 + 120, y0, x0 + 120 + 150 * qtd / maior, y0 + 20, fill=BLUE, outline="")
            c.create_text(x0 + 126 + 150 * qtd / maior, y0 + 10, text=str(qtd), anchor="w", font=("Segoe UI", 9, "bold"), fill=NAVY)


if __name__ == "__main__":
    raiz = janela("Agenda de Contatos Comunitária", 1120, 700)
    AgendaApp(raiz)
    raiz.mainloop()
