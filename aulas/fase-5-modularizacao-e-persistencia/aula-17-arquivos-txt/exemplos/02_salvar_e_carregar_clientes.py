# Aula 17 | Persistência de registros com separador ;.

def salvar_clientes(clientes, arquivo="clientes.txt"):
    with open(arquivo, "w", encoding="utf-8") as f:
        for cl in clientes:
            f.write(f"{cl['nome']};{cl['destino']};{cl['dias']}\n")

def carregar_clientes(arquivo="clientes.txt"):
    clientes = []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                nome, destino, dias = linha.strip().split(";")
                clientes.append({"nome": nome, "destino": destino, "dias": int(dias)})
    except FileNotFoundError:
        pass            # primeira execução: o arquivo ainda não existe
    return clientes

clientes = [{"nome": "Marina Costa", "destino": "Parintins", "dias": 3}]
salvar_clientes(clientes)
print(carregar_clientes())
