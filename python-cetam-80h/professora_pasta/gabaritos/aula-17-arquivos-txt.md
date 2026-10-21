# Gabarito – Aula 17: Arquivos .txt

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Grave uma lista de 5 destinos em `destinos.txt` e depois leia e mostre cada um.

```python
destinos = ["Parintins", "Novo Airão", "Maués", "Presidente Figueiredo", "Manaus"]

with open("destinos.txt", "w", encoding="utf-8") as arquivo:
    for destino in destinos:
        arquivo.write(destino + "\n")

with open("destinos.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

**Saída esperada:**

```text
Parintins
Novo Airão
Maués
Presidente Figueiredo
Manaus
```

## Atividade 2

> Leia o arquivo `destinos.txt` e mostre quantas linhas ele possui.

```python
with open("destinos.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(f"O arquivo possui {len(linhas)} linhas.")
```

**Saída esperada:**

```text
O arquivo possui 5 linhas.
```

> 📝 **Nota ao professor:** Pressupõe que o arquivo da Atividade 1 já exista na mesma pasta. No VS Code, confirme que a **pasta** do projeto está aberta; no Colab, o arquivo some se a sessão for encerrada.

## Atividade 3

> Qual a diferença entre os modos `"w"` e `"a"`? O que acontece se usarmos `"w"` por engano em um arquivo com dados?

O modo `"w"` (escrita) cria o arquivo e **apaga todo o conteúdo anterior** se ele já existir; o modo `"a"` (acréscimo) mantém o conteúdo e **adiciona ao final**. Usar `"w"` por engano em um arquivo com dados **apaga esses dados**.

## Desafio do projeto – Persistência de clientes e reservas

> Carregar os dados ao iniciar e salvar a cada cadastro.

```python
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
        pass
    return clientes

clientes = carregar_clientes()

while True:
    print("\n1 - Cadastrar cliente | 2 - Listar clientes | 0 - Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        nome = input("Nome: ").strip().title()
        destino = input("Destino: ").strip().title()
        dias = int(input("Dias: "))
        clientes.append({"nome": nome, "destino": destino, "dias": dias})
        salvar_clientes(clientes)
        print("Cliente cadastrado e salvo!")
    elif opcao == "2":
        for cl in clientes:
            print(f"{cl['nome']} -> {cl['destino']} ({cl['dias']} dias)")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
```

**Saída esperada – 1ª execução (cadastra e sai):**

```text

1 - Cadastrar cliente | 2 - Listar clientes | 0 - Sair
Escolha: 1
Nome: joão pedro
Destino: maués
Dias: 4
Cliente cadastrado e salvo!

1 - Cadastrar cliente | 2 - Listar clientes | 0 - Sair
Escolha: 0
```

**Saída esperada – 2ª execução (os dados foram carregados do arquivo):**

```text

1 - Cadastrar cliente | 2 - Listar clientes | 0 - Sair
Escolha: 2
João Pedro -> Maués (4 dias)

1 - Cadastrar cliente | 2 - Listar clientes | 0 - Sair
Escolha: 0
```

> 📝 **Nota ao professor:** A prova da persistência é fechar o programa e abri-lo de novo: os clientes devem aparecer. Se não aparecerem, verifique o modo de abertura, o nome do arquivo e a pasta de trabalho.

