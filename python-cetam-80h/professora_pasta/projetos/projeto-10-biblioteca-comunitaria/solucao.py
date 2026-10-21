# SOLUÇÃO DE REFERÊNCIA – Projeto 10: Biblioteca Comunitária
# Projeto 10 - Biblioteca Comunitária (valores fictícios)
import os

ARQUIVO = "acervo.txt"
PRAZO_DIAS = 7
MULTA_POR_DIA = 0.50
LIMITE_EMPRESTIMOS = 3


class Livro:
    def __init__(self, codigo, titulo, autor, leitor=""):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.leitor = leitor

    def esta_disponivel(self):
        return self.leitor == ""

    def emprestar(self, leitor):
        if not self.esta_disponivel():
            return False
        self.leitor = leitor
        return True

    def devolver(self, dias):
        multa = 0.0
        if dias > PRAZO_DIAS:
            multa = (dias - PRAZO_DIAS) * MULTA_POR_DIA
        self.leitor = ""
        return multa

    def descricao(self):
        if self.esta_disponivel():
            situacao = "Disponível"
        else:
            situacao = f"Emprestado a {self.leitor}"
        return f"{self.codigo} | {self.titulo} | {self.autor} | {situacao}"


class Biblioteca:
    def __init__(self, arquivo=ARQUIVO):
        self.arquivo = arquivo
        self.livros = {}
        self.multas = 0.0
        if os.path.exists(self.arquivo):
            self.carregar()
        else:
            self.criar_acervo_inicial()

    def criar_acervo_inicial(self):
        iniciais = [
            ("Dom Casmurro", "Machado de Assis"),
            ("Macunaíma", "Mário de Andrade"),
            ("A Selva", "Ferreira de Castro"),
            ("Memórias Póstumas de Brás Cubas", "Machado de Assis"),
        ]
        for titulo, autor in iniciais:
            self.adicionar(titulo, autor)

    def adicionar(self, titulo, autor):
        codigo = f"L{len(self.livros) + 1:03d}"
        livro = Livro(codigo, titulo, autor)
        self.livros[codigo] = livro
        self.salvar()
        return livro

    def salvar(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            for livro in self.livros.values():
                f.write(f"{livro.codigo};{livro.titulo};{livro.autor};{livro.leitor}\n")

    def carregar(self):
        with open(self.arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                codigo, titulo, autor, leitor = linha.strip().split(";")
                self.livros[codigo] = Livro(codigo, titulo, autor, leitor)

    def buscar(self, codigo):
        return self.livros.get(codigo)

    def buscar_por_titulo(self, trecho):
        achados = []
        for livro in self.livros.values():
            if trecho.strip().lower() in livro.titulo.lower():
                achados.append(livro)
        return achados

    def emprestimos_do_leitor(self, leitor):
        total = 0
        for livro in self.livros.values():
            if livro.leitor == leitor:
                total += 1
        return total

    def emprestar(self, codigo, leitor):
        livro = self.buscar(codigo)
        if livro is None:
            return False, "Código não encontrado."
        if not livro.esta_disponivel():
            return False, f"Livro indisponível (com {livro.leitor})."
        if self.emprestimos_do_leitor(leitor) >= LIMITE_EMPRESTIMOS:
            return False, f"Limite de {LIMITE_EMPRESTIMOS} empréstimos atingido."
        livro.emprestar(leitor)
        self.salvar()
        return True, f"Empréstimo registrado: {livro.titulo} para {leitor}. Prazo: {PRAZO_DIAS} dias."

    def devolver(self, codigo, dias):
        livro = self.buscar(codigo)
        if livro is None:
            return False, "Código não encontrado."
        if livro.esta_disponivel():
            return False, "Este livro não está emprestado."
        multa = livro.devolver(dias)
        self.multas += multa
        self.salvar()
        if multa > 0:
            return True, f"Devolvido com atraso de {dias - PRAZO_DIAS} dia(s). Multa: R$ {multa:.2f}."
        return True, "Devolução registrada sem multa."

    def relatorio(self):
        total = len(self.livros)
        emprestados = 0
        for livro in self.livros.values():
            if not livro.esta_disponivel():
                emprestados += 1
        print("\n--- RELATÓRIO ---")
        print(f"Livros no acervo: {total}")
        print(f"Disponíveis: {total - emprestados}")
        print(f"Emprestados: {emprestados}")
        print(f"Multas arrecadadas na sessão: R$ {self.multas:.2f}")


def principal():
    biblioteca = Biblioteca()
    while True:
        print("\n=== BIBLIOTECA COMUNITÁRIA ===")
        print("1 - Cadastrar livro")
        print("2 - Listar acervo")
        print("3 - Buscar por título")
        print("4 - Emprestar")
        print("5 - Devolver")
        print("6 - Relatório")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ").strip().title()
            if titulo == "" or ";" in titulo:
                print("Título inválido.")
                continue
            autor = input("Autor: ").strip().title()
            if autor == "" or ";" in autor:
                print("Autor inválido.")
                continue
            livro = biblioteca.adicionar(titulo, autor)
            print(f"Livro cadastrado com o código {livro.codigo}.")
        elif opcao == "2":
            print("\n--- ACERVO ---")
            for livro in biblioteca.livros.values():
                print(livro.descricao())
        elif opcao == "3":
            achados = biblioteca.buscar_por_titulo(input("Trecho do título: "))
            if len(achados) == 0:
                print("Nenhum livro encontrado.")
            for livro in achados:
                print(livro.descricao())
        elif opcao == "4":
            codigo = input("Código do livro: ").strip().upper()
            leitor = input("Nome do leitor: ").strip().title()
            if leitor == "":
                print("O nome do leitor é obrigatório.")
                continue
            ok, mensagem = biblioteca.emprestar(codigo, leitor)
            print(mensagem)
        elif opcao == "5":
            codigo = input("Código do livro: ").strip().upper()
            dias = int(input("Dias com o livro: "))
            while dias <= 0:
                print("Informe um número de dias maior que zero.")
                dias = int(input("Dias com o livro: "))
            ok, mensagem = biblioteca.devolver(codigo, dias)
            print(mensagem)
        elif opcao == "6":
            biblioteca.relatorio()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")


principal()
