"""Projeto 9 – Agenda de Contatos Comunitária (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Cada contato é um dicionário {"nome", "telefone", "email", "bairro"}.
No arquivo agenda.txt cada linha é:  nome;telefone;email;bairro
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""
import os

ARQUIVO = "agenda.txt"


def padronizar_nome(nome):
    """RN01: strip() + title()."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def limpar_telefone(texto):
    """RN02: remove espaços, hífens e parênteses. '(92) 99123-4567' -> '92991234567'."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def telefone_valido(telefone):
    """RN02: somente dígitos, com 10 ou 11 caracteres (telefone já limpo)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def email_valido(email):
    """RN03: contém '@' e '.', e não contém espaços nem ';'."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def padronizar_bairro(bairro):
    """RN04: title(), remove ';' e usa 'Não informado' se ficar vazio."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def buscar_contato(contatos, nome):
    """Retorna o contato com esse nome exato (após padronizar) ou None."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def cadastrar_contato(contatos, nome, telefone, email, bairro):
    """RF03, RN01–RN04: valida, acrescenta e retorna o contato.

    Erros: nome vazio, com ';' ou repetido; telefone inválido; e-mail inválido.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def listar_ordenado(contatos):
    """RF04: nova lista com os contatos em ordem alfabética pelo nome."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def buscar_por_trecho(contatos, trecho):
    """RF05: contatos cujo nome CONTÉM o trecho, sem diferenciar maiúsculas (em ordem alfabética)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def editar_contato(contatos, nome, telefone, email, bairro):
    """RF06 e RN02: edita telefone, e-mail e bairro. Campo em branco MANTÉM o valor atual.

    Telefone ou e-mail inválidos mantêm o valor anterior. Retorna a lista de AVISOS (textos)
    sobre o que não foi alterado. Contato inexistente: ValueError("Contato não encontrado.").
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def remover_contato(contatos, nome):
    """RF07 e RN05: remove o contato. Inexistente: ValueError("Contato não encontrado.")."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def resumo_por_bairro(contatos):
    """RF08: dicionário contador {bairro: quantidade}."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def salvar_contatos(contatos, arquivo=ARQUIVO):
    """RF03 e RN06: grava TODOS os contatos (modo 'w', utf-8): nome;telefone;email;bairro."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def carregar_contatos(arquivo=ARQUIVO):
    """RF01: lê o arquivo e retorna a lista de contatos. Inexistente -> lista vazia."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")
