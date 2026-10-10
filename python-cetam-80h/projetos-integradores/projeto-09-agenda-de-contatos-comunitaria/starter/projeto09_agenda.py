# Projeto 9 - Agenda de Contatos Comunitária (dados fictícios)
# Integrantes: ______________________

# Requisitos (veja o README do projeto para os detalhes):
# TODO RF01: Ao iniciar, carregar os contatos de agenda.txt (arquivo inexistente = agenda vazia).
# TODO RF02: Menu: 1 – Cadastrar, 2 – Listar, 3 – Buscar por trecho do nome, 4 – Editar, 5 – Remover, 6 –…
# TODO RF03: Cadastrar contato (nome, telefone, e-mail e bairro) e salvar no arquivo.
# TODO RF04: Listar todos os contatos em ordem alfabética pelo nome.
# TODO RF05: Buscar contatos cujo nome contenha o trecho digitado, sem diferenciar maiúsculas de minúsculas.
# TODO RF06: Editar telefone, e-mail e bairro de um contato: Enter em branco mantém o valor atual. Salvar…
# TODO RF07: Remover um contato após confirmação (s/n) e salvar.
# TODO RF08: Resumo por bairro: quantos contatos há em cada bairro (use um dicionário contador).

ARQUIVO = "agenda.txt"


def carregar_contatos():
    """Lê agenda.txt (se existir) e retorna a lista de dicionários."""
    pass  # TODO


def salvar_contatos(contatos):
    """Grava todos os contatos em agenda.txt (modo "w")."""
    pass  # TODO


def limpar_telefone(texto):
    pass  # TODO


def telefone_valido(telefone):
    pass  # TODO


def email_valido(email):
    pass  # TODO


def cadastrar_contato(contatos):
    pass  # TODO


def listar_contatos(contatos):
    pass  # TODO


def buscar_por_trecho(contatos, trecho):
    pass  # TODO


def editar_contato(contatos):
    pass  # TODO


def remover_contato(contatos):
    pass  # TODO


def resumo_por_bairro(contatos):
    pass  # TODO


def principal():
    contatos = carregar_contatos()
    # TODO: menu com while True
    pass


principal()
