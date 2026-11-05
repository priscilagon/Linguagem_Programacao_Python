# Gabarito – Aula 18: Fundamentos de Programação Orientada a Objetos

> **Uso exclusivo do professor.** Há mais de uma solução correta: compare o comportamento, não a forma exata. As saídas abaixo foram obtidas ao executar cada código.

## Atividade 1

> Crie a classe `Pacote` com os atributos `destino`, `preco` e `dias` e o método `descricao()`. Crie dois objetos e mostre suas descrições.

```python
class Pacote:
    def __init__(self, destino, preco, dias):
        self.destino = destino
        self.preco = preco
        self.dias = dias

    def descricao(self):
        return f"{self.destino}: R$ {self.preco:.2f} em {self.dias} dias"

p1 = Pacote("Parintins", 950.00, 3)
p2 = Pacote("Maués", 1350.00, 4)
print(p1.descricao())
print(p2.descricao())
```

**Saída esperada:**

```text
Parintins: R$ 950.00 em 3 dias
Maués: R$ 1350.00 em 4 dias
```

> 📝 **Nota ao professor:** Erros comuns: esquecer o `self` nos métodos ou escrever `nome = nome` em vez de `self.nome = nome` dentro do `__init__`.

## Atividade 2

> Crie a classe `Cliente` com um método `dobrar_dias()` que dobre o atributo `dias`.

```python
class Cliente:
    def __init__(self, nome, dias):
        self.nome = nome
        self.dias = dias

    def dobrar_dias(self):
        self.dias = self.dias * 2

cliente = Cliente("Marina", 3)
print(cliente.dias)
cliente.dobrar_dias()
print(cliente.dias)
```

**Saída esperada:**

```text
3
6
```

## Desafio do projeto – Classe Usuario

> Classe `Usuario` (nome, senha) com os métodos `cadastrar()` e `autenticar()`.

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

# Teste da classe
Usuario("marina", "1234").cadastrar()
print(Usuario("marina", "1234").autenticar())
print(Usuario("marina", "errada").autenticar())
```

**Saída esperada:**

```text
True
False
```

> 📝 **Nota ao professor:** Lembre os alunos de que guardar senha em texto puro é aceitável **apenas para estudo**.

