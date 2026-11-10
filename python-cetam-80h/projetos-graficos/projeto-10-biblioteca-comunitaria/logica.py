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
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def emprestar(self, leitor):
        """Registra o leitor que levou o livro."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def devolver(self, dias):
        """RN03: limpa o leitor e devolve a multa (R$ 0,50 por dia além de 7; até 7 dias = 0)."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def descricao(self):
        """Texto 'L001 | Título | Autor | Disponível' (ou 'Emprestado a Fulano')."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")


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
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def buscar(self, codigo):
        """Retorna o Livro do código (qualquer caixa) ou None."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def buscar_por_titulo(self, trecho):
        """RN07: livros cujo título CONTÉM o trecho (sem diferenciar maiúsculas), na ordem do acervo."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def emprestimos_do_leitor(self, leitor):
        """Quantidade de livros que o leitor (nome já padronizado) está com ele agora."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def emprestar(self, codigo, leitor):
        """RF05, RN04, RN05 e RN06: retorna (sucesso, mensagem). Salva se der certo.

        Falhas (sem levantar erro): livro inexistente, livro já emprestado (diga com quem),
        leitor vazio, leitor com 3 livros.
        """
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def devolver(self, codigo, dias):
        """RF05, RN03, RN05 e RN06: retorna (sucesso, mensagem). Soma a multa em total_multas.

        Falhas: livro inexistente, livro não emprestado, dias <= 0.
        """
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def relatorio(self):
        """RF06: dicionário com 'total', 'disponiveis', 'emprestados' e 'multas'."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def salvar(self):
        """RF07: grava uma linha  codigo;titulo;autor;leitor  por livro (leitor vazio = disponível)."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")

    def carregar(self):
        """RF03: lê o arquivo e recria os objetos Livro em self.livros."""
        raise NotImplementedError("TODO: implemente esta função em logica.py")
