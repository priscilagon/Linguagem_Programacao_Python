# SOLUÇÃO DE REFERÊNCIA – Projeto 2: Monitor Fluvial: Nível do Rio Negro
# Projeto 2 - Monitor Fluvial: Nível do Rio Negro (dados fictícios)
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
niveis = []

print("=== MONITOR FLUVIAL - RIO NEGRO ===")
for mes in meses:
    nivel = float(input(f"Nível em {mes} (m): "))
    while nivel < 0 or nivel > 40:
        print("Valor inválido! Digite entre 0 e 40 metros.")
        nivel = float(input(f"Nível em {mes} (m): "))
    niveis.append(nivel)

# ----- Estatísticas -----
media = sum(niveis) / len(niveis)
maior = max(niveis)
menor = min(niveis)
mes_maior = meses[niveis.index(maior)]
mes_menor = meses[niveis.index(menor)]

print("\n--- ESTATÍSTICAS DO ANO ---")
print(f"Média anual: {media:.2f} m")
print(f"Maior nível: {maior:.1f} m em {mes_maior}")
print(f"Menor nível: {menor:.1f} m em {mes_menor}")

# ----- Relatório e contagem por classificação -----
contagem = {"Cheia": 0, "Enchente/Vazante": 0, "Seca": 0}
situacoes = []

print("\n--- RELATÓRIO MENSAL ---")
for i in range(len(meses)):
    nivel = niveis[i]
    if nivel >= 29:
        situacao = "Cheia"
    elif nivel >= 26:
        situacao = "Enchente/Vazante"
    else:
        situacao = "Seca"
    situacoes.append(situacao)
    contagem[situacao] += 1
    print(f"{meses[i]} | {nivel:.1f} m | {situacao} | {'#' * int(nivel)}")

print("\n--- MESES POR CLASSIFICAÇÃO ---")
for classe, qtd in contagem.items():
    print(f"{classe}: {qtd}")

# ----- Maior subida -----
maior_subida = 0
mes_subida = ""
for i in range(1, len(niveis)):
    variacao = niveis[i] - niveis[i - 1]
    if variacao > maior_subida:
        maior_subida = variacao
        mes_subida = meses[i]
print(f"\nMaior subida: +{maior_subida:.1f} m em {mes_subida}")

# ----- Consulta por mês -----
while True:
    busca = input("\nConsultar mês (ou 'fim'): ").strip().title()
    if busca == "Fim":
        break
    if busca in meses:
        i = meses.index(busca)
        print(f"{busca}: {niveis[i]:.1f} m - {situacoes[i]}")
    else:
        print("Mês não encontrado.")
print("Monitoramento encerrado.")
