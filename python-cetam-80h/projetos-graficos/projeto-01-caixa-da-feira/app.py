"""Projeto 1 – Caixa da Feira do Produtor: TELA (já pronta).
Execute:  python app.py     (precisa de logica.py completo para funcionar)
"""
import tkinter as tk
from tkinter import ttk, messagebox

import logica
from ui_comum import (janela, cabecalho, cartao, botao, tabela, preencher, seguro,
                      moeda, ler_float, BLUE, GREEN, RED)


class CaixaApp:
    def __init__(self, root):
        self.root = root
        self.itens = []          # [(produto, qtd, preco)]
        self.vendas = []         # totais pagos no dia
        cabecalho(root, "🐟  Caixa da Feira do Produtor", "Projeto 1 • atendimento de clientes e fechamento do caixa")
        corpo = ttk.Frame(root, padding=12)
        corpo.pack(fill="both", expand=True)
        corpo.columnconfigure(0, weight=3)
        corpo.columnconfigure(1, weight=2)
        corpo.rowconfigure(0, weight=1)

        # ---- coluna esquerda: produtos e carrinho
        esq = ttk.Frame(corpo)
        esq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        prod = cartao(esq, "1. Escolha o produto")
        prod.pack(fill="x")
        nomes = [f"{cod} – {nome}  ({moeda(preco)}/kg)" for cod, (nome, preco) in logica.PRODUTOS.items()]
        self.combo = ttk.Combobox(prod, values=nomes, state="readonly", width=40)
        self.combo.current(0)
        self.combo.grid(row=0, column=0, columnspan=3, sticky="we", pady=4)
        ttk.Label(prod, text="Quantidade (kg):", style="Card.TLabel").grid(row=1, column=0, sticky="w")
        self.qtd = tk.StringVar(value="1")
        ttk.Spinbox(prod, from_=0, to=100, increment=0.5, textvariable=self.qtd, width=8).grid(row=1, column=1, sticky="w")
        botao(prod, "➕ Adicionar", self.adicionar).grid(row=1, column=2, padx=8, pady=6)

        carrinho = cartao(esq, "2. Carrinho do cliente")
        carrinho.pack(fill="both", expand=True, pady=(10, 0))
        self.tv = tabela(carrinho, ("Produto", "Kg", "Preço/kg", "Valor"), (190, 60, 90, 90), altura=9)
        botao(carrinho, "🗑 Limpar carrinho", self.limpar, "Perigo").pack(anchor="e", pady=(6, 0))

        # ---- coluna direita: resumo e pagamento
        dire = ttk.Frame(corpo)
        dire.grid(row=0, column=1, sticky="nsew")
        res = cartao(dire, "3. Resumo da compra")
        res.pack(fill="x")
        self.lbl_itens = ttk.Label(res, text="Itens: 0", style="Card.TLabel")
        self.lbl_sub = ttk.Label(res, text="Subtotal: R$ 0,00", style="Card.TLabel")
        self.lbl_desc = ttk.Label(res, text="Desconto: R$ 0,00 (0%)", style="Card.TLabel")
        self.lbl_total = ttk.Label(res, text="R$ 0,00", style="Grande.TLabel")
        for w in (self.lbl_itens, self.lbl_sub, self.lbl_desc):
            w.pack(anchor="w")
        ttk.Label(res, text="Total a pagar", style="Card.TLabel").pack(anchor="w", pady=(8, 0))
        self.lbl_total.pack(anchor="w")

        pag = cartao(dire, "4. Pagamento")
        pag.pack(fill="x", pady=10)
        self.forma = tk.IntVar(value=1)
        ttk.Radiobutton(pag, text="Dinheiro", variable=self.forma, value=1, command=self.trocar_forma).grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(pag, text="Cartão", variable=self.forma, value=2, command=self.trocar_forma).grid(row=0, column=1, sticky="w")
        ttk.Label(pag, text="Valor recebido (R$):", style="Card.TLabel").grid(row=1, column=0, sticky="w", pady=6)
        self.recebido = tk.StringVar()
        self.ent_rec = ttk.Entry(pag, textvariable=self.recebido, width=12)
        self.ent_rec.grid(row=1, column=1, sticky="w")
        self.lbl_troco = ttk.Label(pag, text="", style="Ok.TLabel")
        self.lbl_troco.grid(row=2, column=0, columnspan=2, sticky="w")
        botao(pag, "✔ Finalizar compra", self.finalizar, "Verde").grid(row=3, column=0, columnspan=2, sticky="we", pady=(8, 0))

        cx = cartao(dire, "Caixa do dia")
        cx.pack(fill="x")
        self.lbl_caixa = ttk.Label(cx, text="Clientes: 0   •   Vendido: R$ 0,00", style="Card.TLabel")
        self.lbl_caixa.pack(anchor="w")
        botao(cx, "📋 Fechar o caixa", self.fechar_caixa, "Ouro").pack(anchor="e", pady=(6, 0))

    # ------------------------------------------------------------------
    def produto_escolhido(self):
        codigo = int(self.combo.get().split(" ")[0])
        return logica.PRODUTOS[codigo]

    @seguro
    def adicionar(self):
        qtd = logica.validar_quantidade(ler_float(self.qtd.get(), "Quantidade"))
        nome, preco = self.produto_escolhido()
        self.itens.append((nome, qtd, preco))
        self.atualizar()

    def limpar(self):
        self.itens.clear()
        self.atualizar()

    def trocar_forma(self):
        self.ent_rec.configure(state="normal" if self.forma.get() == 1 else "disabled")
        self.lbl_troco.configure(text="")

    @seguro
    def atualizar(self):
        linhas = [(n, f"{q:g}", moeda(p), moeda(logica.valor_item(p, q))) for n, q, p in self.itens]
        preencher(self.tv, linhas)
        if not self.itens:
            self.lbl_itens.configure(text="Itens: 0")
            self.lbl_sub.configure(text="Subtotal: R$ 0,00")
            self.lbl_desc.configure(text="Desconto: R$ 0,00 (0%)")
            self.lbl_total.configure(text="R$ 0,00")
            return
        r = logica.calcular_resumo(self.itens)
        self.lbl_itens.configure(text=f"Itens: {r['itens']}")
        self.lbl_sub.configure(text=f"Subtotal: {moeda(r['subtotal'])}")
        self.lbl_desc.configure(text=f"Desconto: {moeda(r['desconto'])} ({r['percentual']}%)")
        self.lbl_total.configure(text=moeda(r["total"]))

    @seguro
    def finalizar(self):
        r = logica.calcular_resumo(self.itens)          # RN05: levanta erro se vazio
        if self.forma.get() == 1:
            recebido = ler_float(self.recebido.get(), "Valor recebido")
            troco = logica.calcular_troco(r["total"], recebido)
            self.lbl_troco.configure(text=f"Troco: {moeda(troco)}")
            msg = f"Compra de {moeda(r['total'])} paga em dinheiro.\nTroco: {moeda(troco)}"
        else:
            msg = f"Compra de {moeda(r['total'])} paga no cartão."
        self.vendas.append(r["total"])
        messagebox.showinfo("Compra finalizada", msg + "\n\nObrigado pela preferência!")
        self.itens.clear()
        self.recebido.set("")
        self.atualizar()
        clientes, total = logica.fechamento(self.vendas)
        self.lbl_caixa.configure(text=f"Clientes: {clientes}   •   Vendido: {moeda(total)}")

    @seguro
    def fechar_caixa(self):
        clientes, total = logica.fechamento(self.vendas)
        messagebox.showinfo("Fechamento do caixa", f"Clientes atendidos: {clientes}\nTotal vendido no dia: {moeda(total)}")


if __name__ == "__main__":
    raiz = janela("Caixa da Feira do Produtor", 1000, 660)
    CaixaApp(raiz)
    raiz.mainloop()
