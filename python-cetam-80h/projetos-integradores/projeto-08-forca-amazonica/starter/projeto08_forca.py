# Projeto 8 - Forca Amazônica (dados fictícios)
# Integrantes: ______________________

# Requisitos (veja o README do projeto para os detalhes):
# TODO RF01: Guardar as palavras e dicas em uma tupla de tuplas PALAVRAS (sem acentos, como na tabela).
# TODO RF02: Função escolher_palavra(numero_rodada): devolve a palavra e a dica da rodada (a rodada 7 volta…
# TODO RF03: Função montar_exibicao(palavra, acertadas): devolve o texto da palavra com _ nas letras ainda…
# TODO RF04: Função venceu(palavra, acertadas): devolve True se todas as letras foram descobertas.
# TODO RF05: Função ler_letra(tentadas): lê e valida uma letra, repetindo a pergunta até receber uma…
# TODO RF06: Função jogar_rodada(numero_rodada): executa uma rodada e devolve (ganhou, pontos).
# TODO RF07: Função principal(): controla as rodadas, mantém o placar (pontos e vitórias) e pergunta “Jogar…

PALAVRAS = (
    # TODO: 6 tuplas (palavra, dica) — veja "Dados de partida" no README
)
MAX_ERROS = 6


def escolher_palavra(numero_rodada):
    """Retorna a tupla (palavra, dica) da rodada."""
    pass  # TODO


def montar_exibicao(palavra, acertadas):
    """Retorna a palavra com _ nas letras ainda não descobertas."""
    pass  # TODO


def venceu(palavra, acertadas):
    """Retorna True se todas as letras da palavra já foram acertadas."""
    pass  # TODO


def ler_letra(tentadas):
    """Lê e valida uma letra (1 caractere, alfabético, ainda não tentada)."""
    pass  # TODO


def jogar_rodada(numero_rodada):
    """Joga uma rodada completa e retorna os pontos ganhos."""
    pass  # TODO


def principal():
    # TODO: menu, rodadas e placar final
    pass


principal()
