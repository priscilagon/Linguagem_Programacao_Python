# SOLUÇÃO DE REFERÊNCIA – Projeto 6: Quiz da Floresta Amazônica
# Projeto 6 - Quiz da Floresta Amazônica
melhor_pontuacao = 0
partidas = 0

while True:
    print("\n=== QUIZ DA FLORESTA AMAZÔNICA ===")
    print("1 - Jogar")
    print("2 - Regras")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        pontos = 0
        acertos = 0
        seguidos = 0

        for numero in range(1, 6):
            if numero == 1:
                pergunta = "Quais rios formam o Encontro das Águas, em Manaus?"
                a = "Madeira e Purus"
                b = "Negro e Solimões"
                c = "Tapajós e Xingu"
                d = "Juruá e Japurá"
                correta = "B"
            elif numero == 2:
                pergunta = "Qual peixe amazônico pode ultrapassar 2 metros de comprimento?"
                a = "Tambaqui"
                b = "Pirarucu"
                c = "Jaraqui"
                d = "Matrinxã"
                correta = "B"
            elif numero == 3:
                pergunta = "O Festival Folclórico de Parintins reúne quais bois-bumbás?"
                a = "Garantido e Caprichoso"
                b = "Mimoso e Caprichoso"
                c = "Garantido e Mimoso"
                d = "Faceiro e Caprichoso"
                correta = "A"
            elif numero == 4:
                pergunta = "Em qual cidade fica o Teatro Amazonas?"
                a = "Belém"
                b = "Manaus"
                c = "Parintins"
                d = "Santarém"
                correta = "B"
            else:
                pergunta = "Qual é o rio de maior volume de água do mundo?"
                a = "Nilo"
                b = "Mississippi"
                c = "Amazonas"
                d = "Yangtzé"
                correta = "C"

            print(f"\nPergunta {numero} de 5")
            print(pergunta)
            print(f"A) {a}")
            print(f"B) {b}")
            print(f"C) {c}")
            print(f"D) {d}")

            resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
            while resposta != "A" and resposta != "B" and resposta != "C" and resposta != "D":
                print("Resposta inválida! Digite A, B, C ou D.")
                resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()

            if resposta == correta:
                pontos += 10
                acertos += 1
                seguidos += 1
                print("Correto! +10 pontos.")
                if seguidos == 3:
                    pontos += 5
                    seguidos = 0
                    print("Bônus de sequência! +5 pontos.")
            else:
                seguidos = 0
                print(f"Errou! A resposta correta era {correta}.")

        print("\n=== RESULTADO ===")
        print(f"Acertos: {acertos} de 5")
        print(f"Pontuação: {pontos}")
        if pontos >= 50:
            titulo = "Guardião da Floresta"
        elif pontos >= 30:
            titulo = "Explorador"
        else:
            titulo = "Aprendiz"
        print(f"Título: {titulo}")

        partidas += 1
        if pontos > melhor_pontuacao:
            melhor_pontuacao = pontos
            print("Novo recorde da sessão!")

    elif opcao == "2":
        print("\n--- REGRAS ---")
        print("São 5 perguntas de múltipla escolha.")
        print("Cada acerto vale 10 pontos.")
        print("A cada 3 acertos seguidos, você ganha 5 pontos de bônus.")
        print("50+ pontos: Guardião da Floresta | 30 a 49: Explorador | abaixo de 30: Aprendiz.")
    elif opcao == "0":
        print(f"\nPartidas jogadas: {partidas}")
        print(f"Melhor pontuação: {melhor_pontuacao}")
        print("Até a próxima!")
        break
    else:
        print("Opção inválida!")
