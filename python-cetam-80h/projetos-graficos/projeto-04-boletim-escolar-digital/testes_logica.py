import os
import tempfile
import unittest
import logica as L


class TestBoletim(unittest.TestCase):
    def test_media_e_situacao(self):
        self.assertEqual(L.calcular_media([8, 7, 6]), 7)
        self.assertEqual(L.situacao(7.0), "Aprovado")
        self.assertEqual(L.situacao(6.99), "Recuperação")
        self.assertEqual(L.situacao(5.0), "Recuperação")
        self.assertEqual(L.situacao(4.99), "Reprovado")

    def test_validar_nota(self):
        self.assertEqual(L.validar_nota(0), 0)
        self.assertEqual(L.validar_nota(10), 10)
        for ruim in (-1, 10.1):
            with self.assertRaises(ValueError):
                L.validar_nota(ruim)

    def test_cadastro(self):
        alunos = []
        a = L.cadastrar_aluno(alunos, "  maria das dores ", [8, 7, 9])
        self.assertEqual(a, {"nome": "Maria Das Dores", "notas": [8, 7, 9]})
        self.assertEqual(len(alunos), 1)

    def test_cadastro_invalidos(self):
        alunos = [{"nome": "Maria", "notas": [8, 8, 8]}]
        for nome, notas in (("", [1, 2, 3]), ("   ", [1, 2, 3]), ("Jo;ão", [1, 2, 3]),
                            ("MARIA", [1, 2, 3]), ("Pedro", [11, 5, 5]), ("Pedro", [5, -1, 5])):
            with self.assertRaises(ValueError, msg=str(nome)):
                L.cadastrar_aluno(alunos, nome, notas)
        self.assertEqual(len(alunos), 1)

    def test_buscar(self):
        alunos = [{"nome": "Ana Lima", "notas": [7, 7, 7]}]
        self.assertEqual(L.buscar_aluno(alunos, "  ANA lima ")["nome"], "Ana Lima")
        self.assertIsNone(L.buscar_aluno(alunos, "Zé"))

    def test_estatisticas(self):
        alunos = [{"nome": "Ana", "notas": [9, 8, 10]},      # 9.0 Aprovado
                  {"nome": "Bia", "notas": [6, 5, 7]},       # 6.0 Recuperação
                  {"nome": "Caio", "notas": [3, 4, 2]}]      # 3.0 Reprovado
        e = L.estatisticas(alunos)
        self.assertAlmostEqual(e["media_turma"], 6.0)
        self.assertEqual((e["melhor_nome"], round(e["melhor_media"], 2)), ("Ana", 9.0))
        self.assertEqual(e["situacoes"], {"Aprovado": 1, "Recuperação": 1, "Reprovado": 1})
        with self.assertRaises(ValueError):
            L.estatisticas([])

    def test_persistencia_e_relatorio(self):
        with tempfile.TemporaryDirectory() as pasta:
            arq = os.path.join(pasta, "boletim.txt")
            self.assertEqual(L.carregar_alunos(arq), [])           # arquivo inexistente
            alunos = []
            L.cadastrar_aluno(alunos, "Ana Lima", [9, 8, 10])
            L.cadastrar_aluno(alunos, "Bia Souza", [6.5, 5, 7])
            L.salvar_alunos(alunos, arq)
            with open(arq, encoding="utf-8") as f:
                self.assertEqual(f.read().splitlines()[0], "Ana Lima;9;8;10")
            self.assertEqual(L.carregar_alunos(arq), alunos)         # dados permanecem
            rel = os.path.join(pasta, "relatorio.txt")
            self.assertEqual(L.exportar_relatorio(alunos, rel), 2)
            with open(rel, encoding="utf-8") as f:
                self.assertEqual(f.read().splitlines(), ["Ana Lima;9.00;Aprovado", "Bia Souza;6.17;Recuperação"])


if __name__ == "__main__":
    unittest.main()
