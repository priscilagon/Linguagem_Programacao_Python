"""Projeto 8 – Forca Amazônica (regras de negócio).

PARTE LÓGICA: sem print() nem input(). A tela (app.py) já está pronta.
Regra violada  ->  raise ValueError("mensagem para o usuário").

Teste:  python -m unittest -v testes_logica.py      Tela:  python app.py
"""

PALAVRAS = (
    ("tambaqui", "Peixe de escamas, famoso na culinária do Amazonas"),
    ("pirarucu", "Um dos maiores peixes de água doce, pode passar de 2 metros"),
    ("tucunare", "Peixe de rios e lagos, muito procurado na pesca esportiva"),
    ("castanha", "Semente de árvore gigante, também chamada castanha-do-pará"),
    ("cupuacu", "Fruta de polpa cremosa, usada em sucos e doces"),
    ("jaraqui", "Peixe pequeno e muito consumido pelos manauaras"),
)
MAX_ERROS = 6


def escolher_palavra(numero_rodada):
    """Retorna a tupla (palavra, dica) da rodada (1, 2, 3...). Depois da última, volta à primeira."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def validar_letra(texto, tentadas):
    """RN02 e RN03: retorna a letra em minúscula.

    Erros: não é exatamente UMA letra de a–z; ou a letra já está em 'tentadas'.
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def montar_exibicao(palavra, acertadas):
    """RN05: letras acertadas aparecem e as demais viram '_', separadas por espaço.

    Exemplo: montar_exibicao("pirarucu", ["r", "u"]) -> "_ _ r _ r u _ u"
    """
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def venceu(palavra, acertadas):
    """True quando TODAS as letras da palavra já foram acertadas."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def vidas_restantes(erradas):
    """RN01: MAX_ERROS menos a quantidade de letras erradas."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def pontos_da_rodada(vitoria, vidas):
    """RN04: vitória = 10 + 5 × vidas restantes; derrota = 0."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")


def jogar_letra(palavra, letra, acertadas, erradas):
    """Registra a jogada: coloca a letra em 'acertadas' ou em 'erradas'. Retorna True se acertou."""
    raise NotImplementedError("TODO: implemente esta função em logica.py")
