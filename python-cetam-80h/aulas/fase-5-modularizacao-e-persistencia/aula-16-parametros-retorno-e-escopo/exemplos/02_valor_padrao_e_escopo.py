# Aula 16 | Valor padrão, busca em dicionário e escopo local.

def validar_orcamento(total, limite=1000.00):
    return total <= limite

print(validar_orcamento(990))
print(validar_orcamento(1200))
print(validar_orcamento(1200, 1500))

catalogo = {"Parintins": {"preco": 950.00, "dias": 3}, "Maués": {"preco": 1350.00, "dias": 4}}

def buscar_destino(nome, catalogo):
    return catalogo.get(nome.strip().title())

print(buscar_destino("maués", catalogo))
print(buscar_destino("Xingu", catalogo))

def exemplo():
    mensagem = "variável local"
    print(mensagem)

exemplo()
# print(mensagem)   # NameError: a variável não existe fora da função
