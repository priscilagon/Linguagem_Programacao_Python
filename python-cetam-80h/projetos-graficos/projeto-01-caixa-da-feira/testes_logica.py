import unittest
import logica as L


class TestCaixa(unittest.TestCase):
    def test_quantidade_valida_e_invalida(self):
        self.assertEqual(L.validar_quantidade(2.5), 2.5)
        for ruim in (0, -1):
            with self.assertRaises(ValueError):
                L.validar_quantidade(ruim)

    def test_valor_item(self):
        self.assertEqual(L.valor_item(28.00, 2), 56.00)
        self.assertEqual(L.valor_item(45.00, 1.5), 67.50)

    def test_faixas_de_desconto(self):
        self.assertEqual(L.percentual_desconto(99.99), 0)
        self.assertEqual(L.percentual_desconto(100.00), 5)
        self.assertEqual(L.percentual_desconto(199.99), 5)
        self.assertEqual(L.percentual_desconto(200.00), 10)

    def test_resumo_sem_desconto(self):
        r = L.calcular_resumo([("Tambaqui", 2, 28.00)])
        self.assertEqual(r["itens"], 1)
        self.assertEqual(r["subtotal"], 56.00)
        self.assertEqual(r["percentual"], 0)
        self.assertEqual(r["desconto"], 0)
        self.assertEqual(r["total"], 56.00)

    def test_resumo_com_5_por_cento(self):
        r = L.calcular_resumo([("Tambaqui", 2, 28.00), ("Pirarucu", 1, 45.00)])
        self.assertEqual(r["subtotal"], 101.00)
        self.assertEqual(r["percentual"], 5)
        self.assertEqual(r["desconto"], 5.05)
        self.assertEqual(r["total"], 95.95)

    def test_resumo_com_10_por_cento(self):
        r = L.calcular_resumo([("Pirarucu", 4, 45.00), ("Farinha de mandioca", 2, 9.00)])
        self.assertEqual(r["subtotal"], 198.00)
        self.assertEqual(r["percentual"], 5)
        r = L.calcular_resumo([("Pirarucu", 5, 45.00)])
        self.assertEqual(r["subtotal"], 225.00)
        self.assertEqual(r["percentual"], 10)
        self.assertEqual(r["desconto"], 22.50)
        self.assertEqual(r["total"], 202.50)

    def test_resumo_sem_itens(self):
        with self.assertRaises(ValueError):
            L.calcular_resumo([])

    def test_troco(self):
        self.assertEqual(L.calcular_troco(95.95, 100.00), 4.05)
        self.assertEqual(L.calcular_troco(50.00, 50.00), 0.0)

    def test_troco_insuficiente(self):
        with self.assertRaises(ValueError) as ctx:
            L.calcular_troco(95.95, 90.00)
        self.assertIn("5.95", str(ctx.exception))

    def test_fechamento(self):
        self.assertEqual(L.fechamento([95.95, 56.00]), (2, 151.95))
        self.assertEqual(L.fechamento([]), (0, 0))


if __name__ == "__main__":
    unittest.main()
