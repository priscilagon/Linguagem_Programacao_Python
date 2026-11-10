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
    # >>> SOLUCAO
    return PALAVRAS[(numero_rodada - 1) % len(PALAVRAS)]
    # <<< SOLUCAO


def validar_letra(texto, tentadas):
    """RN02 e RN03: retorna a letra em minúscula.

    Erros: não é exatamente UMA letra de a–z; ou a letra já está em 'tentadas'.
    """
    # >>> SOLUCAO
    letra = texto.strip().lower()
    if len(letra) != 1 or not ("a" <= letra <= "z"):
        raise ValueError("Digite uma única letra de A a Z.")
    if letra in tentadas:
        raise ValueError(f"Você já tentou a letra {letra.upper()}.")
    return letra
    # <<< SOLUCAO


def montar_exibicao(palavra, acertadas):
    """RN05: letras acertadas aparecem e as demais viram '_', separadas por espaço.

    Exemplo: montar_exibicao("pirarucu", ["r", "u"]) -> "_ _ r _ r u _ u"
    """
    # >>> SOLUCAO
    return " ".join(letra if letra in acertadas else "_" for letra in palavra)
    # <<< SOLUCAO


def venceu(palavra, acertadas):
    """True quando TODAS as letras da palavra já foram acertadas."""
    # >>> SOLUCAO
    for letra in palavra:
        if letra not in acertadas:
            return False
    return True
    # <<< SOLUCAO


def vidas_restantes(erradas):
    """RN01: MAX_ERROS menos a quantidade de letras erradas."""
    # >>> SOLUCAO
    return MAX_ERROS - len(erradas)
    # <<< SOLUCAO


def pontos_da_rodada(vitoria, vidas):
    """RN04: vitória = 10 + 5 × vidas restantes; derrota = 0."""
    # >>> SOLUCAO
    return 10 + 5 * vidas if vitoria else 0
    # <<< SOLUCAO


def jogar_letra(palavra, letra, acertadas, erradas):
    """Registra a jogada: coloca a letra em 'acertadas' ou em 'erradas'. Retorna True se acertou."""
    # >>> SOLUCAO
    if letra in palavra:
        acertadas.append(letra)
        return True
    erradas.append(letra)
    return False
    # <<< SOLUCAO
