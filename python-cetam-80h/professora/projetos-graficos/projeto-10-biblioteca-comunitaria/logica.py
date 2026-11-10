"""Projeto 10 – Biblioteca Comunitária (regras de negócio, orientado a objetos).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Duas classes colaboram: Livro e Biblioteca.
Emprestar e devolver na Biblioteca devolvem a tupla (sucesso, mensagem), que a tela só exibe.
No arquivo acervo.txt cada linha é:  codigo;titulo;autor;leitor   (leitor vazio = disponível)

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""
import os

ARQUIVO = "acervo.txt"
PRAZO_DIAS = 7
MULTA_POR_DIA = 0.50
LIMITE_EMPRESTIMOS = 3


class Livro:
    def __init__(self, codigo, titulo, autor, leitor=""):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.leitor = leitor

    def esta_disponivel(self):
        """True quando ninguém está com o livro (leitor vazio)."""
        # >>> SOLUCAO
        return self.leitor == ""
        # <<< SOLUCAO

    def emprestar(self, leitor):
        """Registra o leitor que levou o livro."""
        # >>> SOLUCAO
        self.leitor = leitor
        # <<< SOLUCAO

    def devolver(self, dias):
        """RN03: limpa o leitor e devolve a multa (R$ 0,50 por dia além de 7; até 7 dias = 0)."""
        # >>> SOLUCAO
        self.leitor = ""
        atraso = max(0, dias - PRAZO_DIAS)
        return round(atraso * MULTA_POR_DIA, 2)
        # <<< SOLUCAO

    def descricao(self):
        """Texto 'L001 | Título | Autor | Disponível' (ou 'Emprestado a Fulano')."""
        # >>> SOLUCAO
        situacao = "Disponível" if self.esta_disponivel() else f"Emprestado a {self.leitor}"
        return f"{self.codigo} | {self.titulo} | {self.autor} | {situacao}"
        # <<< SOLUCAO


class Biblioteca:
    def __init__(self, arquivo=ARQUIVO):
        self.arquivo = arquivo
        self.livros = {}            # codigo -> Livro
        self.total_multas = 0.0     # multas arrecadadas na sessão
        try:
            if os.path.exists(arquivo):
                self.carregar()
            else:
                self.criar_acervo_inicial()
        except NotImplementedError:
            pass    # só para a tela abrir enquanto você ainda está implementando salvar()/carregar()

    def criar_acervo_inicial(self):
        """RF03: cria os 4 livros iniciais (tabela do enunciado) e salva o arquivo."""
        for codigo, titulo, autor in (("L001", "Dom Casmurro", "Machado de Assis"),
                                      ("L002", "Macunaíma", "Mário de Andrade"),
                                      ("L003", "A Selva", "Ferreira de Castro"),
                                      ("L004", "Memórias Póstumas de Brás Cubas", "Machado de Assis")):
            self.livros[codigo] = Livro(codigo, titulo, autor)
        self.salvar()

    def adicionar(self, titulo, autor):
        """RF02, RN01 e RN02: cadastra o livro com código automático (L001, L002...) e salva.

        titulo/autor: strip() + title(); não vazios e sem ';'. Retorna o Livro criado.
        """
        # >>> SOLUCAO
        titulo = titulo.strip().title()
        autor = autor.strip().title()
        if titulo == "" or autor == "":
            raise ValueError("Título e autor não podem ser vazios.")
        if ";" in titulo or ";" in autor:
            raise ValueError("Título e autor não podem conter ponto e vírgula (;).")
        codigo = f"L{len(self.livros) + 1:03d}"
        livro = Livro(codigo, titulo, autor)
        self.livros[codigo] = livro
        self.salvar()
        return livro
        # <<< SOLUCAO

    def buscar(self, codigo):
        """Retorna o Livro do código (qualquer caixa) ou None."""
        # >>> SOLUCAO
        return self.livros.get(codigo.strip().upper())
        # <<< SOLUCAO

    def buscar_por_titulo(self, trecho):
        """RN07: livros cujo título CONTÉM o trecho (sem diferenciar maiúsculas), na ordem do acervo."""
        # >>> SOLUCAO
        trecho = trecho.strip().lower()
        return [l for l in self.livros.values() if trecho in l.titulo.lower()]
        # <<< SOLUCAO

    def emprestimos_do_leitor(self, leitor):
        """Quantidade de livros que o leitor (nome já padronizado) está com ele agora."""
        # >>> SOLUCAO
        return sum(1 for l in self.livros.values() if l.leitor == leitor)
        # <<< SOLUCAO

    def emprestar(self, codigo, leitor):
        """RF05, RN04, RN05 e RN06: retorna (sucesso, mensagem). Salva se der certo.

        Falhas (sem levantar erro): livro inexistente, livro já emprestado (diga com quem),
        leitor vazio, leitor com 3 livros.
        """
        # >>> SOLUCAO
        livro = self.buscar(codigo)
        leitor = leitor.strip().title()
        if livro is None:
            return False, "Livro inexistente."
        if leitor == "":
            return False, "Informe o nome do leitor."
        if not livro.esta_disponivel():
            return False, f"Livro indisponível: está com {livro.leitor}."
        if self.emprestimos_do_leitor(leitor) >= LIMITE_EMPRESTIMOS:
            return False, f"{leitor} já está com {LIMITE_EMPRESTIMOS} livros (limite atingido)."
        livro.emprestar(leitor)
        self.salvar()
        return True, f"“{livro.titulo}” emprestado a {leitor}. Prazo: {PRAZO_DIAS} dias."
        # <<< SOLUCAO

    def devolver(self, codigo, dias):
        """RF05, RN03, RN05 e RN06: retorna (sucesso, mensagem). Soma a multa em total_multas.

        Falhas: livro inexistente, livro não emprestado, dias <= 0.
        """
        # >>> SOLUCAO
        livro = self.buscar(codigo)
        if livro is None:
            return False, "Livro inexistente."
        if livro.esta_disponivel():
            return False, "Este livro não está emprestado."
        if dias <= 0:
            return False, "Os dias de uso devem ser maiores que zero."
        multa = livro.devolver(dias)
        self.total_multas = round(self.total_multas + multa, 2)
        self.salvar()
        if multa > 0:
            return True, f"“{livro.titulo}” devolvido com {dias - PRAZO_DIAS} dia(s) de atraso. Multa: R$ {multa:.2f}."
        return True, f"“{livro.titulo}” devolvido no prazo. Sem multa."
        # <<< SOLUCAO

    def relatorio(self):
        """RF06: dicionário com 'total', 'disponiveis', 'emprestados' e 'multas'."""
        # >>> SOLUCAO
        total = len(self.livros)
        disponiveis = sum(1 for l in self.livros.values() if l.esta_disponivel())
        return {"total": total, "disponiveis": disponiveis,
                "emprestados": total - disponiveis, "multas": self.total_multas}
        # <<< SOLUCAO

    def salvar(self):
        """RF07: grava uma linha  codigo;titulo;autor;leitor  por livro (leitor vazio = disponível)."""
        # >>> SOLUCAO
        with open(self.arquivo, "w", encoding="utf-8") as f:
            for l in self.livros.values():
                f.write(f"{l.codigo};{l.titulo};{l.autor};{l.leitor}\n")
        # <<< SOLUCAO

    def carregar(self):
        """RF03: lê o arquivo e recria os objetos Livro em self.livros."""
        # >>> SOLUCAO
        self.livros = {}
        with open(self.arquivo, encoding="utf-8") as f:
            for linha in f:
                linha = linha.rstrip("\n")
                if linha.strip():
                    codigo, titulo, autor, leitor = linha.split(";")
                    self.livros[codigo] = Livro(codigo, titulo, autor, leitor)
        # <<< SOLUCAO
