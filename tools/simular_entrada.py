"""Executa um programa Python simulando as entradas do teclado.

Uso:
    python tools/simular_entrada.py programa.py entradas.txt

Cada linha de entradas.txt responde a um input(), na ordem em que eles aparecem.
"""
import builtins
import sys


def main():
    if len(sys.argv) != 3:
        print("Uso: python simular_entrada.py programa.py entradas.txt")
        sys.exit(1)

    programa, arquivo_entradas = sys.argv[1], sys.argv[2]

    with open(arquivo_entradas, encoding="utf-8") as f:
        linhas = iter(f.read().split("\n"))

    def entrada_simulada(prompt=""):
        try:
            valor = next(linhas)
        except StopIteration:
            print(prompt)
            raise SystemExit("[simular_entrada] As entradas acabaram antes do fim do programa.")
        print(prompt + valor)
        return valor

    builtins.input = entrada_simulada

    with open(programa, encoding="utf-8") as f:
        codigo = f.read()
    exec(compile(codigo, programa, "exec"), {"__name__": "__main__"})


if __name__ == "__main__":
    main()
