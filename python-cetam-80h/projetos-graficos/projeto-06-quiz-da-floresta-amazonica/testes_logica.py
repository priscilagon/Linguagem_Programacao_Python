import unittest
import logica as L


class TestQuiz(unittest.TestCase):
    def test_banco_de_perguntas(self):
        self.assertEqual(len(L.PERGUNTAS), 5)
        for p in L.PERGUNTAS:
            self.assertEqual(len(p["alternativas"]), 4)
            self.assertIn(p["correta"], "ABCD")

    def test_validar_resposta(self):
        self.assertEqual(L.validar_resposta("b"), "B")
        self.assertEqual(L.validar_resposta("  c "), "C")
        for ruim in ("", "x", "AB", "1"):
            with self.assertRaises(ValueError, msg=repr(ruim)):
                L.validar_resposta(ruim)

    def test_conferir(self):
        self.assertTrue(L.conferir(L.PERGUNTAS[0], "B"))
        self.assertFalse(L.conferir(L.PERGUNTAS[0], "A"))

    def test_pontos_partida_45(self):
        # acerta, acerta, acerta (bônus), erra, acerta = 30 + 5 + 10
        self.assertEqual(L.calcular_pontos([True, True, True, False, True]), 45)

    def test_pontos_zero(self):
        self.assertEqual(L.calcular_pontos([False] * 5), 0)

    def test_pontos_55(self):
        # 5 acertos: bônus no 3º e a contagem recomeça (4º e 5º não dão novo bônus)
        self.assertEqual(L.calcular_pontos([True] * 5), 55)

    def test_erro_zera_sequencia(self):
        self.assertEqual(L.calcular_pontos([True, True, False, True, True]), 40)
        self.assertEqual(L.calcular_pontos([True, True, True, True, True, True]), 70)  # dois bônus
        self.assertEqual(L.calcular_pontos([]), 0)

    def test_titulos(self):
        self.assertEqual(L.titulo(50), "Guardião da Floresta")
        self.assertEqual(L.titulo(49), "Explorador")
        self.assertEqual(L.titulo(30), "Explorador")
        self.assertEqual(L.titulo(29), "Aprendiz")

    def test_recorde(self):
        self.assertTrue(L.novo_recorde(45, 0))
        self.assertFalse(L.novo_recorde(45, 45))
        self.assertFalse(L.novo_recorde(0, 45))


if __name__ == "__main__":
    unittest.main()
