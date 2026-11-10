"""Roda os testes automáticos em uma pasta de projeto de aluno e resume o resultado.

Uso:  python corrigir.py caminho/da/pasta/do/projeto
A pasta precisa ter logica.py (do aluno) e testes_logica.py.
"""
import re
import subprocess
import sys

if len(sys.argv) != 2:
    sys.exit("Uso: python corrigir.py <pasta-do-projeto>")
r = subprocess.run([sys.executable, "-m", "unittest", "-v", "testes_logica"], cwd=sys.argv[1], capture_output=True, text=True)
saida = r.stderr + r.stdout
for linha in saida.splitlines():
    if re.search(r"\.\.\. (ok|FAIL|ERROR)", linha):
        print(("✔ " if linha.endswith("ok") else "✘ ") + linha.split(" (")[0])
print("-" * 50)
print(saida.strip().splitlines()[-1] if saida.strip() else "Sem saída")
sys.exit(r.returncode)
