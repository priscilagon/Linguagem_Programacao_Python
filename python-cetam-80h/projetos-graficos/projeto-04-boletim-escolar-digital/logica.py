"""Projeto 4 – Boletim Escolar Digital (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Cada aluno é um dicionário  {"nome": str, "notas": [n1, n2, n3]}.
No arquivo boletim.txt cada linha é:  nome;nota1;nota2;nota3
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""
import os

ARQUIVO = "boletim.txt"


def calcular_media(notas):
    """RN02: média = soma das notas / quantidade de notas."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def situacao(media):
    """RN02: 'Aprovado' (>= 7), 'Recuperação' (>= 5 e < 7) ou 'Reprovado' (< 5)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def validar_nota(nota):
    """RN01: a nota deve estar entre 0 e 10 (inclusive). Retorna a nota."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def cadastrar_aluno(alunos, nome, notas):
    """RF03, RN01, RN03 e RN04: valida e acrescenta o aluno à lista. Retorna o aluno.

    Erros: nome vazio, nome com ';', nome repetido (ignore maiúsculas/minúsculas
    — o nome é padronizado com strip() e title()) ou nota fora de 0 a 10.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def buscar_aluno(alunos, nome):
    """RF05: retorna o aluno com esse nome (sem diferenciar maiúsculas) ou None."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def estatisticas(alunos):
    """RF06 e RN05: retorna {'media_turma', 'melhor_nome', 'melhor_media', 'situacoes'}.

    'situacoes' é um dicionário contador {'Aprovado': n, 'Recuperação': n, 'Reprovado': n}.
    Lista vazia: ValueError("Nenhum aluno cadastrado.").
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def salvar_alunos(alunos, arquivo=ARQUIVO):
    """RF03 e RN06: grava uma linha  nome;n1;n2;n3  por aluno (modo 'w', encoding utf-8)."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def carregar_alunos(arquivo=ARQUIVO):
    """RF01: lê o arquivo e retorna a lista de alunos. Arquivo inexistente -> lista vazia."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def exportar_relatorio(alunos, arquivo="relatorio.txt"):
    """RF07: grava  nome;média;situação  por aluno (média com 2 casas). Retorna nº de linhas."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")
