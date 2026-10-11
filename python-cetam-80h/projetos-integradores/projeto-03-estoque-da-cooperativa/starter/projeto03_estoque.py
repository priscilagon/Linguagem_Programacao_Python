# Projeto 3 - Estoque da Cooperativa Ribeirinha (dados fictícios)
# Integrantes: ______________________

MINIMO = 10

estoque = {
    "Açaí": {"preco": 18.50, "qtd": 40},
    "Castanha": {"preco": 32.00, "qtd": 15},
    "Tapioca": {"preco": 12.00, "qtd": 8},
    "Cupuaçu": {"preco": 15.00, "qtd": 25},
}


def exibir_menu():
    pass  # TODO RF02: mostrar o menu e devolver a opção


def listar_estoque(estoque):
    pass  # TODO RF03


def valor_total(estoque):
    pass  # TODO RF07: devolver o valor total em estoque


def cadastrar_produto(estoque):
    pass  # TODO RF04 (RN01 a RN03)


def vender(estoque):
    pass  # TODO RF05 (RN04): devolver o valor da venda (ou 0)


def repor(estoque):
    pass  # TODO RF06 (RN05)


def relatorio(estoque, vendido):
    pass  # TODO RF07


# TODO: laço principal com o menu (while True); acumule o total vendido em "vendido"
