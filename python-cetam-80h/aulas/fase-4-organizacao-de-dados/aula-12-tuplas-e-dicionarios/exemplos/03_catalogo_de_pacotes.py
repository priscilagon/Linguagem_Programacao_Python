# Aula 12 | Dicionário de dicionários (valores fictícios).

catalogo = {
    "Parintins": {"preco": 950.00, "dias": 3},
    "Novo Airão": {"preco": 1200.00, "dias": 4},
    "Presidente Figueiredo": {"preco": 780.00, "dias": 2},
    "Maués": {"preco": 1350.00, "dias": 4},
}

for nome, dados in catalogo.items():
    print(f"{nome}: R$ {dados['preco']:.2f} em {dados['dias']} dias")
