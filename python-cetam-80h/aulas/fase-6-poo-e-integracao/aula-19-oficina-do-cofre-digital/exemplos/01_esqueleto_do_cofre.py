# Aula 19 | Esqueleto para a dupla completar (os TODO são a sua tarefa).

# Cofre digital - Agência Amazônia Tur
# Dupla: ______________________ e ______________________
import os


class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def cadastrar(self, arquivo="usuarios.txt"):
        pass  # TODO: gravar "nome;senha" no arquivo (modo "a")

    def autenticar(self, arquivo="usuarios.txt"):
        pass  # TODO: devolver True se nome e senha existirem no arquivo


def exibir_menu():
    pass  # TODO: mostrar 1 - Cadastrar | 2 - Entrar | 0 - Sair e devolver a opção


def principal():
    pass  # TODO: laço do menu, validações e mensagem personalizada após o login


principal()
