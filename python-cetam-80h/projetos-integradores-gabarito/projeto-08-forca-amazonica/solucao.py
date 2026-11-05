# SOLUÇÃO DE REFERÊNCIA – Projeto 8: Forca Amazônica
# Projeto 8 - Forca Amazônica
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
    posicao = (numero_rodada - 1) % len(PALAVRAS)
    return PALAVRAS[posicao]


def montar_exibicao(palavra, acertadas):
    exibicao = ""
    for letra in palavra:
        if letra in acertadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()


def venceu(palavra, acertadas):
    for letra in palavra:
        if letra not in acertadas:
            return False
    return True


def ler_letra(tentadas):
    while True:
        entrada = input("Digite uma letra: ").strip().lower()
        if len(entrada) != 1 or not entrada.isalpha():
            print("Digite apenas UMA letra (de a a z).")
        elif entrada in tentadas:
            print("Você já tentou essa letra!")
        else:
            return entrada


def jogar_rodada(numero_rodada):
    palavra, dica = escolher_palavra(numero_rodada)
    acertadas = []
    erradas = []
    print(f"\n=== RODADA {numero_rodada} ===")
    print(f"Dica: {dica}")

    while len(erradas) < MAX_ERROS and not venceu(palavra, acertadas):
        vidas = MAX_ERROS - len(erradas)
        print(f"\nPalavra: {montar_exibicao(palavra, acertadas)}")
        print("Vidas: " + "O " * vidas + "X " * len(erradas))
        if len(erradas) > 0:
            print(f"Letras erradas: {erradas}")
        letra = ler_letra(acertadas + erradas)
        if letra in palavra:
            acertadas.append(letra)
            print("Acertou!")
        else:
            erradas.append(letra)
            print("Errou!")

    if venceu(palavra, acertadas):
        vidas = MAX_ERROS - len(erradas)
        pontos = 10 + vidas * 5
        print(f"\nParabéns! A palavra era {palavra.upper()}. +{pontos} pontos.")
        return True, pontos
    print(f"\nFim de jogo! A palavra era {palavra.upper()}.")
    return False, 0


def principal():
    rodada = 1
    total = 0
    vitorias = 0
    continuar = "s"
    while continuar == "s":
        ganhou, pontos = jogar_rodada(rodada)
        total += pontos
        if ganhou:
            vitorias += 1
        print(f"Placar: {total} pontos | Vitórias: {vitorias} de {rodada} rodada(s)")
        rodada += 1
        continuar = input("Jogar outra rodada? (s/n): ").strip().lower()

    print("\n=== FIM DA SESSÃO ===")
    print(f"Rodadas: {rodada - 1}")
    print(f"Vitórias: {vitorias}")
    print(f"Pontuação total: {total}")


principal()
