import os
import tempfile
import unittest
import logica as L


class TestLivro(unittest.TestCase):
    def test_livro(self):
        l = L.Livro("L001", "Dom Casmurro", "Machado de Assis")
        self.assertTrue(l.esta_disponivel())
        l.emprestar("Ana Lima")
        self.assertFalse(l.esta_disponivel())
        self.assertIn("Emprestado a Ana Lima", l.descricao())
        self.assertEqual(l.devolver(7), 0)           # no prazo
        self.assertTrue(l.esta_disponivel())
        l.emprestar("Ana Lima")
        self.assertEqual(l.devolver(10), 1.5)        # 3 dias de atraso
        self.assertEqual(l.descricao(), "L001 | Dom Casmurro | Machado de Assis | Disponível")
        self.assertEqual(l.devolver(8), 0.5)


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.pasta = tempfile.TemporaryDirectory()
        self.arq = os.path.join(self.pasta.name, "acervo.txt")
        self.b = L.Biblioteca(self.arq)

    def tearDown(self):
        self.pasta.cleanup()

    def test_acervo_inicial_criado_e_salvo(self):
        self.assertEqual(list(self.b.livros), ["L001", "L002", "L003", "L004"])
        self.assertTrue(os.path.exists(self.arq))

    def test_adicionar(self):
        livro = self.b.adicionar("  vidas secas ", "graciliano ramos")
        self.assertEqual((livro.codigo, livro.titulo, livro.autor), ("L005", "Vidas Secas", "Graciliano Ramos"))
        for t, a in (("", "x"), ("x", "  "), ("a;b", "x"), ("x", "a;b")):
            with self.assertRaises(ValueError):
                self.b.adicionar(t, a)
        self.assertEqual(len(self.b.livros), 5)

    def test_buscas(self):
        self.assertEqual(self.b.buscar("l002").titulo, "Macunaíma")
        self.assertIsNone(self.b.buscar("L999"))
        achados = self.b.buscar_por_titulo("  CASMU")
        self.assertEqual([l.codigo for l in achados], ["L001"])
        self.assertEqual([l.codigo for l in self.b.buscar_por_titulo("a")], ["L001", "L002", "L003", "L004"])

    def test_emprestar_ok_e_falhas(self):
        ok, msg = self.b.emprestar("L001", "  ana lima ")
        self.assertTrue(ok)
        self.assertEqual(self.b.livros["L001"].leitor, "Ana Lima")
        ok, msg = self.b.emprestar("L001", "Bia")
        self.assertFalse(ok)
        self.assertIn("Ana Lima", msg)
        self.assertFalse(self.b.emprestar("L999", "Ana")[0])
        self.assertFalse(self.b.emprestar("L002", "   ")[0])

    def test_limite_de_tres(self):
        for codigo in ("L001", "L002", "L003"):
            self.assertTrue(self.b.emprestar(codigo, "Ana Lima")[0])
        ok, msg = self.b.emprestar("L004", "ana LIMA")
        self.assertFalse(ok)
        self.assertEqual(self.b.emprestimos_do_leitor("Ana Lima"), 3)
        self.assertTrue(self.b.emprestar("L004", "Bia Souza")[0])

    def test_devolver_e_multa(self):
        self.b.emprestar("L001", "Ana Lima")
        self.b.emprestar("L002", "Ana Lima")
        ok, msg = self.b.devolver("L001", 10)
        self.assertTrue(ok)
        self.assertIn("1.50", msg)
        self.assertEqual(self.b.total_multas, 1.5)
        self.assertTrue(self.b.devolver("L002", 7)[0])
        self.assertEqual(self.b.total_multas, 1.5)

    def test_devolver_falhas(self):
        self.assertFalse(self.b.devolver("L001", 3)[0])         # não emprestado
        self.assertFalse(self.b.devolver("L999", 3)[0])         # inexistente
        self.b.emprestar("L001", "Ana")
        self.assertFalse(self.b.devolver("L001", 0)[0])         # dias inválidos
        self.assertFalse(self.b.livros["L001"].esta_disponivel())

    def test_relatorio(self):
        self.b.emprestar("L001", "Ana")
        self.b.devolver("L001", 9)
        self.b.emprestar("L002", "Bia")
        self.assertEqual(self.b.relatorio(), {"total": 4, "disponiveis": 3, "emprestados": 1, "multas": 1.0})

    def test_persistencia_entre_execucoes(self):
        self.b.emprestar("L003", "Ana Lima")
        self.b.adicionar("Vidas Secas", "Graciliano Ramos")
        nova = L.Biblioteca(self.arq)                          # "reabre o programa"
        self.assertEqual(len(nova.livros), 5)                  # não duplicou o acervo
        self.assertEqual(nova.livros["L003"].leitor, "Ana Lima")
        self.assertTrue(nova.livros["L001"].esta_disponivel())
        with open(self.arq, encoding="utf-8") as f:
            self.assertEqual(f.read().splitlines()[0], "L001;Dom Casmurro;Machado de Assis;")


if __name__ == "__main__":
    unittest.main()
