# Gabarito – Aula 19: Desenvolvimento do cofre digital (oficina de projeto)

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Solução de referência do cofre digital

> Cadastro de usuário com senha, login e mensagem personalizada, tudo persistido em arquivo.

```python
import os

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def cadastrar(self, arquivo="usuarios.txt"):
        with open(arquivo, "a", encoding="utf-8") as f:
            f.write(f"{self.nome};{self.senha}\n")

    def autenticar(self, arquivo="usuarios.txt"):
        if not os.path.exists(arquivo):
            return False
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                nome, senha = linha.strip().split(";")
                if nome == self.nome and senha == self.senha:
                    return True
        return False

def exibir_menu():
    print("\n=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===")
    print("1 - Cadastrar usuário")
    print("2 - Entrar")
    print("0 - Sair")
    return input("Escolha: ")

def principal():
    while True:
        opcao = exibir_menu()
        if opcao == "1":
            nome = input("Nome de usuário: ").strip()
            senha = input("Senha: ")
            if nome == "" or senha == "":
                print("Nome e senha são obrigatórios.")
                continue
            if ";" in nome or ";" in senha:
                print("O caractere ; não é permitido.")
                continue
            Usuario(nome, senha).cadastrar()
            print("Usuário cadastrado com sucesso!")
        elif opcao == "2":
            nome = input("Nome de usuário: ").strip()
            senha = input("Senha: ")
            if Usuario(nome, senha).autenticar():
                print(f"Bem-vindo(a) ao cofre digital, {nome}!")
            else:
                print("Usuário ou senha incorretos.")
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

principal()
```

**Saída esperada – 1ª execução: cadastro, login correto e incorreto, validações e opção inválida:**

```text

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 1
Nome de usuário: marina
Senha: 1234
Usuário cadastrado com sucesso!

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 2
Nome de usuário: marina
Senha: 1234
Bem-vindo(a) ao cofre digital, marina!

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 2
Nome de usuário: marina
Senha: errada
Usuário ou senha incorretos.

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 1
Nome de usuário: 
Senha: 123
Nome e senha são obrigatórios.

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 1
Nome de usuário: ana;x
Senha: abc
O caractere ; não é permitido.

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 9
Opção inválida.

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 0
Até logo!
```

**Saída esperada – 2ª execução: o usuário continua cadastrado (persistência):**

```text

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 2
Nome de usuário: marina
Senha: 1234
Bem-vindo(a) ao cofre digital, marina!

=== COFRE DIGITAL - AGÊNCIA AMAZÔNIA TUR ===
1 - Cadastrar usuário
2 - Entrar
0 - Sair
Escolha: 0
Até logo!
```

> 📝 **Nota ao professor:** A solução acima é um **ponto de partida**; aceite versões com recursos adicionais (impedir usuário repetido, limitar tentativas, guardar reservas). Durante a depuração coletiva, os bugs mais comuns são: nomes vazios cadastrados, uso do separador `;` nos dados e `split` quebrando por linha em branco no arquivo.

