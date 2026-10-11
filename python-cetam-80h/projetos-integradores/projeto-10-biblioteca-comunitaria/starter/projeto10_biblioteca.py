# Projeto 10 - Biblioteca Comunitária (dados fictícios)
# Integrantes: ______________________

# Requisitos (veja o README do projeto para os detalhes):
# TODO RF01: Classe Livro com atributos codigo, titulo, autor e leitor (texto vazio = disponível) e métodos…
# TODO RF02: Classe Biblioteca com o dicionário livros e os métodos adicionar(titulo, autor),…
# TODO RF03: Na primeira execução (sem arquivo), criar o acervo inicial da tabela e salvá-lo em acervo.txt;…
# TODO RF04: Menu: 1 – Cadastrar livro, 2 – Listar acervo, 3 – Buscar por título, 4 – Emprestar, 5 –…
# TODO RF05: Emprestar e devolver devolvem uma tupla (sucesso, mensagem), que o menu apenas exibe.
# TODO RF06: Relatório: total de livros, disponíveis, emprestados e total de multas arrecadadas na sessão.
# TODO RF07: Salvar o acervo após cada operação que o altere (cadastro, empréstimo e devolução).
import os

ARQUIVO = "acervo.txt"
PRAZO_DIAS = 7
MULTA_POR_DIA = 0.50
LIMITE_EMPRESTIMOS = 3


class Livro:
    def __init__(self, codigo, titulo, autor, leitor=""):
        # TODO: guardar os atributos
        pass

    def esta_disponivel(self):
        pass  # TODO

    def emprestar(self, leitor):
        pass  # TODO

    def devolver(self, dias):
        """Limpa o leitor e devolve o valor da multa."""
        pass  # TODO

    def descricao(self):
        pass  # TODO


class Biblioteca:
    def __init__(self, arquivo=ARQUIVO):
        self.arquivo = arquivo
        self.livros = {}  # codigo -> Livro
        # TODO: carregar() se o arquivo existir; senão, criar o acervo inicial

    def adicionar(self, titulo, autor):
        pass  # TODO

    def buscar(self, codigo):
        pass  # TODO

    def buscar_por_titulo(self, trecho):
        pass  # TODO

    def emprestar(self, codigo, leitor):
        """Retorna a tupla (sucesso, mensagem)."""
        pass  # TODO

    def devolver(self, codigo, dias):
        """Retorna a tupla (sucesso, mensagem)."""
        pass  # TODO

    def salvar(self):
        pass  # TODO

    def carregar(self):
        pass  # TODO


def principal():
    biblioteca = Biblioteca()
    # TODO: menu com while True
    pass


principal()
