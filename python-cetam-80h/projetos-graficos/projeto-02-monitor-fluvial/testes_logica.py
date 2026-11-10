import unittest
import logica as L

DADOS = [26.1, 27.4, 28.3, 29.0, 29.6, 29.8, 29.2, 27.9, 25.7, 23.8, 23.1, 24.0]


class TestMonitor(unittest.TestCase):
    def test_validar_nivel(self):
        self.assertEqual(L.validar_nivel(0), 0)
        self.assertEqual(L.validar_nivel(40), 40)
        for ruim in (-0.1, 40.1, 45):
            with self.assertRaises(ValueError):
                L.validar_nivel(ruim)

    def test_classificar_limites(self):
        self.assertEqual(L.classificar(29.0), "Cheia")
        self.assertEqual(L.classificar(28.99), "Enchente/Vazante")
        self.assertEqual(L.classificar(26.0), "Enchente/Vazante")
        self.assertEqual(L.classificar(25.99), "Seca")

    def test_barra(self):
        self.assertEqual(L.barra(5.9), "#####")
        self.assertEqual(L.barra(0.4), "")

    def test_estatisticas(self):
        e = L.estatisticas(DADOS)
        self.assertAlmostEqual(e["media"], 26.99, places=2)
        self.assertEqual((e["maior"], e["mes_maior"]), (29.8, "Jun"))
        self.assertEqual((e["menor"], e["mes_menor"]), (23.1, "Nov"))

    def test_contagem(self):
        self.assertEqual(L.contar_classificacoes(DADOS),
                         {"Cheia": 4, "Enchente/Vazante": 4, "Seca": 4})

    def test_maior_subida(self):
        self.assertEqual(L.maior_subida(DADOS), (1.3, "Fev"))
        self.assertEqual(L.maior_subida([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19]), (0.0, ""))

    def test_consulta(self):
        self.assertEqual(L.consultar_mes("  jun ", DADOS), ("Jun", 29.8, "Cheia"))
        self.assertEqual(L.consultar_mes("ABR", DADOS)[2], "Cheia")
        with self.assertRaises(ValueError) as ctx:
            L.consultar_mes("xyz", DADOS)
        self.assertEqual(str(ctx.exception), "Mês não encontrado.")


if __name__ == "__main__":
    unittest.main()
