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
    # >>> SOLUCAO
    return nome.strip().title()
    # <<< SOLUCAO


def limpar_telefone(texto):
    """RN02: remove espaços, hífens e parênteses. '(92) 99123-4567' -> '92991234567'."""
    # >>> SOLUCAO
    for sinal in (" ", "-", "(", ")"):
        texto = texto.replace(sinal, "")
    return texto
    # <<< SOLUCAO


def telefone_valido(telefone):
    """RN02: somente dígitos, com 10 ou 11 caracteres (telefone já limpo)."""
    # >>> SOLUCAO
    return telefone.isdigit() and len(telefone) in (10, 11)
    # <<< SOLUCAO


def email_valido(email):
    """RN03: contém '@' e '.', e não contém espaços nem ';'."""
    # >>> SOLUCAO
    return "@" in email and "." in email and " " not in email and ";" not in email
    # <<< SOLUCAO


def padronizar_bairro(bairro):
    """RN04: title(), remove ';' e usa 'Não informado' se ficar vazio."""
    # >>> SOLUCAO
    bairro = bairro.replace(";", "").strip().title()
    return bairro if bairro else "Não informado"
    # <<< SOLUCAO


def buscar_contato(contatos, nome):
    """Retorna o contato com esse nome exato (após padronizar) ou None."""
    # >>> SOLUCAO
    alvo = padronizar_nome(nome)
    for c in contatos:
        if c["nome"] == alvo:
            return c
    return None
    # <<< SOLUCAO


def cadastrar_contato(contatos, nome, telefone, email, bairro):
    """RF03, RN01–RN04: valida, acrescenta e retorna o contato.

    Erros: nome vazio, com ';' ou repetido; telefone inválido; e-mail inválido.
    """
    # >>> SOLUCAO
    nome = padronizar_nome(nome)
    if nome == "":
        raise ValueError("O nome não pode ser vazio.")
    if ";" in nome:
        raise ValueError("O nome não pode conter ponto e vírgula (;).")
    if buscar_contato(contatos, nome) is not None:
        raise ValueError("Já existe um contato com esse nome.")
    telefone = limpar_telefone(telefone)
    if not telefone_valido(telefone):
        raise ValueError("Telefone inválido: use só dígitos, com DDD (10 ou 11 números).")
    email = email.strip().lower()
    if not email_valido(email):
        raise ValueError("E-mail inválido.")
    contato = {"nome": nome, "telefone": telefone, "email": email, "bairro": padronizar_bairro(bairro)}
    contatos.append(contato)
    return contato
    # <<< SOLUCAO


def listar_ordenado(contatos):
    """RF04: nova lista com os contatos em ordem alfabética pelo nome."""
    # >>> SOLUCAO
    return sorted(contatos, key=lambda c: c["nome"])
    # <<< SOLUCAO


def buscar_por_trecho(contatos, trecho):
    """RF05: contatos cujo nome CONTÉM o trecho, sem diferenciar maiúsculas (em ordem alfabética)."""
    # >>> SOLUCAO
    trecho = trecho.strip().lower()
    return [c for c in listar_ordenado(contatos) if trecho in c["nome"].lower()]
    # <<< SOLUCAO


def editar_contato(contatos, nome, telefone, email, bairro):
    """RF06 e RN02: edita telefone, e-mail e bairro. Campo em branco MANTÉM o valor atual.

    Telefone ou e-mail inválidos mantêm o valor anterior. Retorna a lista de AVISOS (textos)
    sobre o que não foi alterado. Contato inexistente: ValueError("Contato não encontrado.").
    """
    # >>> SOLUCAO
    contato = buscar_contato(contatos, nome)
    if contato is None:
        raise ValueError("Contato não encontrado.")
    avisos = []
    if telefone.strip() != "":
        novo = limpar_telefone(telefone)
        if telefone_valido(novo):
            contato["telefone"] = novo
        else:
            avisos.append("Telefone inválido: mantido o valor anterior.")
    if email.strip() != "":
        novo = email.strip().lower()
        if email_valido(novo):
            contato["email"] = novo
        else:
            avisos.append("E-mail inválido: mantido o valor anterior.")
    if bairro.strip() != "":
        contato["bairro"] = padronizar_bairro(bairro)
    return avisos
    # <<< SOLUCAO


def remover_contato(contatos, nome):
    """RF07 e RN05: remove o contato. Inexistente: ValueError("Contato não encontrado.")."""
    # >>> SOLUCAO
    contato = buscar_contato(contatos, nome)
    if contato is None:
        raise ValueError("Contato não encontrado.")
    contatos.remove(contato)
    # <<< SOLUCAO


def resumo_por_bairro(contatos):
    """RF08: dicionário contador {bairro: quantidade}."""
    # >>> SOLUCAO
    resumo = {}
    for c in contatos:
        resumo[c["bairro"]] = resumo.get(c["bairro"], 0) + 1
    return resumo
    # <<< SOLUCAO


def salvar_contatos(contatos, arquivo=ARQUIVO):
    """RF03 e RN06: grava TODOS os contatos (modo 'w', utf-8): nome;telefone;email;bairro."""
    # >>> SOLUCAO
    with open(arquivo, "w", encoding="utf-8") as f:
        for c in contatos:
            f.write(f"{c['nome']};{c['telefone']};{c['email']};{c['bairro']}\n")
    # <<< SOLUCAO


def carregar_contatos(arquivo=ARQUIVO):
    """RF01: lê o arquivo e retorna a lista de contatos. Inexistente -> lista vazia."""
    # >>> SOLUCAO
    contatos = []
    if not os.path.exists(arquivo):
        return contatos
    with open(arquivo, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                nome, telefone, email, bairro = linha.split(";")
                contatos.append({"nome": nome, "telefone": telefone, "email": email, "bairro": bairro})
    return contatos
    # <<< SOLUCAO
