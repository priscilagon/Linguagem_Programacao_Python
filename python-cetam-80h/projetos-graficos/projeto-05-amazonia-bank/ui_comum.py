"""Utilitários de interface compartilhados pelos projetos gráficos (tkinter).

Você NÃO precisa alterar este arquivo. Ele reúne o tema de cores do CETAM,
funções para montar telas e a leitura segura de números digitados.
"""
import tkinter as tk
from tkinter import ttk, messagebox

NAVY = "#0B2545"
BLUE = "#1F6FB2"
GREEN = "#1B7F4B"
GOLD = "#C9A227"
RED = "#B3261E"
BG = "#F4F7FB"
CARD = "#FFFFFF"
GRAY = "#5B6B7F"


def moeda(valor):
    """Formata 1234.5 como 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


def ler_float(texto, campo="Valor"):
    """Converte texto em float (aceita vírgula). Gera ValueError com mensagem clara."""
    try:
        return float(str(texto).strip().replace(",", "."))
    except ValueError:
        raise ValueError(f"{campo} inválido: digite um número.")


def ler_int(texto, campo="Valor"):
    """Converte texto em inteiro. Gera ValueError com mensagem clara."""
    try:
        return int(str(texto).strip())
    except ValueError:
        raise ValueError(f"{campo} inválido: digite um número inteiro.")


def configurar_estilo(root):
    """Aplica o tema do CETAM aos widgets ttk."""
    root.configure(bg=BG)
    est = ttk.Style(root)
    est.theme_use("clam")
    est.configure(".", font=("Segoe UI", 10), background=BG, foreground=NAVY)
    est.configure("TFrame", background=BG)
    est.configure("Card.TFrame", background=CARD, relief="flat")
    est.configure("TLabel", background=BG, foreground=NAVY)
    est.configure("Card.TLabel", background=CARD, foreground=NAVY)
    est.configure("Titulo.TLabel", font=("Segoe UI", 15, "bold"), background=CARD)
    est.configure("Grande.TLabel", font=("Segoe UI", 22, "bold"), background=CARD, foreground=BLUE)
    est.configure("Ok.TLabel", background=CARD, foreground=GREEN, font=("Segoe UI", 10, "bold"))
    est.configure("Erro.TLabel", background=CARD, foreground=RED, font=("Segoe UI", 10, "bold"))
    est.configure("TLabelframe", background=CARD, bordercolor="#C9D3E0")
    est.configure("TLabelframe.Label", background=CARD, foreground=BLUE, font=("Segoe UI", 10, "bold"))
    est.configure("TEntry", padding=4)
    est.configure("TNotebook", background=BG)
    est.configure("TNotebook.Tab", padding=(14, 6), font=("Segoe UI", 10, "bold"))
    est.map("TNotebook.Tab", background=[("selected", CARD)], foreground=[("selected", BLUE)])
    for nome, cor, hover in (("Primario", BLUE, "#175A93"), ("Verde", GREEN, "#146038"),
                             ("Perigo", RED, "#8E1D17"), ("Ouro", GOLD, "#A98A1D")):
        est.configure(f"{nome}.TButton", background=cor, foreground="white",
                      font=("Segoe UI", 10, "bold"), padding=(12, 6), borderwidth=0)
        est.map(f"{nome}.TButton", background=[("active", hover), ("disabled", "#9AA5B1")])
    est.configure("Treeview", rowheight=26, background="white", fieldbackground="white")
    est.configure("Treeview.Heading", background=NAVY, foreground="white",
                  font=("Segoe UI", 10, "bold"), padding=5)
    est.map("Treeview.Heading", background=[("active", BLUE)])
    est.configure("Horizontal.TProgressbar", troughcolor="#DDE5EF", background=GREEN)


def cabecalho(root, titulo, subtitulo=""):
    """Faixa azul-marinho no topo da janela."""
    faixa = tk.Frame(root, bg=NAVY)
    faixa.pack(fill="x")
    tk.Label(faixa, text=titulo, bg=NAVY, fg="white", font=("Segoe UI", 16, "bold"),
             anchor="w").pack(fill="x", padx=18, pady=(12, 0))
    tk.Label(faixa, text=subtitulo or "CETAM • Linguagem de Programação Python • dados fictícios",
             bg=NAVY, fg="#B9C7DA", font=("Segoe UI", 9), anchor="w").pack(fill="x", padx=18, pady=(0, 10))
    tk.Frame(root, bg=GOLD, height=3).pack(fill="x")


def cartao(parent, titulo=None, **opcoes):
    """Quadro branco (Labelframe se tiver título)."""
    if titulo:
        quadro = ttk.Labelframe(parent, text=f" {titulo} ", padding=10)
    else:
        quadro = ttk.Frame(parent, style="Card.TFrame", padding=10)
    return quadro


def botao(parent, texto, comando, estilo="Primario"):
    return ttk.Button(parent, text=texto, command=comando, style=f"{estilo}.TButton", cursor="hand2")


def campo(parent, rotulo, linha, largura=22, valor="", coluna=0):
    """Rótulo + Entry em grade. Retorna a StringVar."""
    var = tk.StringVar(value=valor)
    ttk.Label(parent, text=rotulo, style="Card.TLabel").grid(row=linha, column=coluna, sticky="w", pady=3, padx=(0, 8))
    ttk.Entry(parent, textvariable=var, width=largura).grid(row=linha, column=coluna + 1, sticky="we", pady=3)
    return var


def tabela(parent, colunas, larguras=None, altura=8):
    """Treeview com barra de rolagem. Retorna a Treeview."""
    moldura = ttk.Frame(parent)
    moldura.pack(fill="both", expand=True)
    tv = ttk.Treeview(moldura, columns=colunas, show="headings", height=altura)
    barra = ttk.Scrollbar(moldura, orient="vertical", command=tv.yview)
    tv.configure(yscrollcommand=barra.set)
    for i, col in enumerate(colunas):
        tv.heading(col, text=col)
        tv.column(col, width=(larguras[i] if larguras else 100), anchor="w")
    tv.pack(side="left", fill="both", expand=True)
    barra.pack(side="right", fill="y")
    tv.tag_configure("par", background="#F1F5FA")
    tv.tag_configure("ok", foreground=GREEN)
    tv.tag_configure("alerta", foreground="#B26A00")
    tv.tag_configure("erro", foreground=RED)
    return tv


def preencher(tv, linhas, tags=None):
    """Limpa a tabela e insere as linhas (listas). tags = lista de tags por linha."""
    tv.delete(*tv.get_children())
    for i, linha in enumerate(linhas):
        marca = (tags[i],) if tags and tags[i] else (("par",) if i % 2 else ())
        tv.insert("", "end", values=linha, tags=marca)


def seguro(funcao):
    """Decorador: mostra erros de validação (ValueError) e funções ainda não implementadas."""
    def envelope(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except NotImplementedError as erro:
            messagebox.showinfo("Falta implementar",
                                f"{erro}\n\nAbra o arquivo logica.py e complete a função indicada.")
        except ValueError as erro:
            messagebox.showwarning("Atenção", str(erro))
    envelope.__name__ = funcao.__name__
    return envelope


def carregar_seguro(funcao, padrao):
    """Executa funcao() para carregar dados ao abrir a tela.

    Se a função de logica.py ainda não foi implementada, avisa e usa o valor padrão,
    para a janela abrir mesmo assim enquanto você faz o projeto aos poucos.
    """
    try:
        return funcao()
    except NotImplementedError as erro:
        messagebox.showinfo("Falta implementar", f"{erro}\n\nA tela vai abrir sem os dados salvos.")
        return padrao


def janela(titulo, largura=980, altura=640):
    """Cria a janela principal já estilizada e centralizada."""
    root = tk.Tk()
    root.title(titulo)
    x = max((root.winfo_screenwidth() - largura) // 2, 0)
    y = max((root.winfo_screenheight() - altura) // 3, 0)
    root.geometry(f"{largura}x{altura}+{x}+{y}")
    root.minsize(780, 520)
    configurar_estilo(root)
    return root
