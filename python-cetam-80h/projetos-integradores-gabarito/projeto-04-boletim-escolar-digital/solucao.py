# SOLUÇÃO DE REFERÊNCIA – Projeto 4: Boletim Escolar Digital
# Projeto 4 - Boletim Escolar Digital
ARQUIVO = "boletim.txt"
RELATORIO = "relatorio.txt"

def carregar_alunos():
    alunos = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                nome, n1, n2, n3 = linha.strip().split(";")
                alunos.append({"nome": nome, "notas": [float(n1), float(n2), float(n3)]})
    except FileNotFoundError:
        pass
    return alunos

def salvar_alunos(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for aluno in alunos:
            n = aluno["notas"]
            f.write(f"{aluno['nome']};{n[0]};{n[1]};{n[2]}\n")

def calcular_media(aluno):
    return sum(aluno["notas"]) / len(aluno["notas"])

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"

def ler_nota(numero):
    nota = float(input(f"Nota {numero} (0 a 10): "))
    while nota < 0 or nota > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota = float(input(f"Nota {numero} (0 a 10): "))
    return nota

def buscar_aluno(alunos, nome):
    for aluno in alunos:
        if aluno["nome"] == nome:
            return aluno
    return None

def mostrar_aluno(aluno):
    n = aluno["notas"]
    media = calcular_media(aluno)
    print(f"{aluno['nome']} | Notas: {n[0]:.1f} / {n[1]:.1f} / {n[2]:.1f} | Média: {media:.2f} | {situacao(media)}")

def cadastrar_aluno(alunos):
    nome = input("Nome do aluno: ").strip().title()
    if nome == "" or ";" in nome:
        print("Nome inválido.")
        return
    if buscar_aluno(alunos, nome) is not None:
        print("Aluno já cadastrado!")
        return
    notas = [ler_nota(1), ler_nota(2), ler_nota(3)]
    alunos.append({"nome": nome, "notas": notas})
    salvar_alunos(alunos)
    print("Aluno cadastrado e salvo!")

def listar_boletim(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- BOLETIM ---")
    for aluno in alunos:
        mostrar_aluno(aluno)

def estatisticas(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    soma = 0
    melhor = alunos[0]
    contagem = {"Aprovado": 0, "Recuperação": 0, "Reprovado": 0}
    for aluno in alunos:
        media = calcular_media(aluno)
        soma += media
        if media > calcular_media(melhor):
            melhor = aluno
        contagem[situacao(media)] += 1
    print("\n--- ESTATÍSTICAS DA TURMA ---")
    print(f"Média da turma: {soma / len(alunos):.2f}")
    print(f"Maior média: {melhor['nome']} ({calcular_media(melhor):.2f})")
    for sit, qtd in contagem.items():
        print(f"{sit}: {qtd}")

def exportar_relatorio(alunos):
    with open(RELATORIO, "w", encoding="utf-8") as f:
        f.write("RELATÓRIO DA TURMA\n")
        for aluno in alunos:
            media = calcular_media(aluno)
            f.write(f"{aluno['nome']};{media:.2f};{situacao(media)}\n")
    print(f"Relatório gravado em {RELATORIO}.")

alunos = carregar_alunos()

while True:
    print("\n=== BOLETIM ESCOLAR DIGITAL ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar boletim")
    print("3 - Buscar aluno")
    print("4 - Estatísticas da turma")
    print("5 - Exportar relatório")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_aluno(alunos)
    elif opcao == "2":
        listar_boletim(alunos)
    elif opcao == "3":
        nome = input("Nome: ").strip().title()
        aluno = buscar_aluno(alunos, nome)
        if aluno is None:
            print("Aluno não encontrado.")
        else:
            mostrar_aluno(aluno)
    elif opcao == "4":
        estatisticas(alunos)
    elif opcao == "5":
        exportar_relatorio(alunos)
    elif opcao == "0":
        print("Até logo!")
        break
    else:
        print("Opção inválida!")
