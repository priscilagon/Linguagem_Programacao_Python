import unittest
import logica as L


class TestEstoque(unittest.TestCase):
    def setUp(self):
        self.e = L.estoque_inicial()

    def test_estoque_inicial_novo_a_cada_chamada(self):
        self.e["Açaí"]["qtd"] = 0
        self.assertEqual(L.estoque_inicial()["Açaí"]["qtd"], 40)

    def test_padronizar(self):
        self.assertEqual(L.padronizar_nome("  AÇAÍ "), "Açaí")

    def test_cadastrar(self):
        nome = L.cadastrar_produto(self.e, "  guaraná ", 20.0, 5)
        self.assertEqual(nome, "Guaraná")
        self.assertEqual(self.e["Guaraná"], {"preco": 20.0, "qtd": 5})
        L.cadastrar_produto(self.e, "Pupunha", 7.5, 0)  # quantidade 0 é permitida

    def test_cadastrar_invalidos(self):
        casos = [("  ", 5, 1), ("AÇAÍ", 5, 1), ("Novo", 0, 1), ("Novo", -3, 1), ("Novo", 5, -1)]
        for nome, preco, qtd in casos:
            with self.assertRaises(ValueError, msg=str((nome, preco, qtd))):
                L.cadastrar_produto(self.e, nome, preco, qtd)
        self.assertEqual(len(self.e), 4)

    def test_vender(self):
        self.assertEqual(L.vender(self.e, "açaí", 10), 185.00)
        self.assertEqual(self.e["Açaí"]["qtd"], 30)

    def test_vender_invalidos(self):
        for nome, qtd in (("Banana", 1), ("Açaí", 0), ("Açaí", -2), ("Açaí", 41)):
            with self.assertRaises(ValueError, msg=str((nome, qtd))):
                L.vender(self.e, nome, qtd)
        self.assertEqual(self.e["Açaí"]["qtd"], 40)
        self.assertEqual(L.vender(self.e, "Açaí", 40), 740.00)   # vende tudo

    def test_repor(self):
        L.repor(self.e, "tapioca", 12)
        self.assertEqual(self.e["Tapioca"]["qtd"], 20)
        for nome, qtd in (("Banana", 5), ("Tapioca", 0)):
            with self.assertRaises(ValueError):
                L.repor(self.e, nome, qtd)

    def test_valor_total_e_baixo(self):
        self.assertEqual(L.valor_total(self.e), 18.5 * 40 + 32 * 15 + 12 * 8 + 15 * 25)
        self.assertEqual(L.estoque_baixo(self.e), ["Tapioca"])
        L.vender(self.e, "Castanha", 6)           # sobra 9
        self.assertEqual(L.estoque_baixo(self.e), ["Castanha", "Tapioca"])
        L.repor(self.e, "Tapioca", 2)             # exatamente 10: não é baixo
        self.assertEqual(L.estoque_baixo(self.e), ["Castanha"])

    def test_relatorio(self):
        r = L.relatorio(self.e, 185.0)
        self.assertEqual(r["produtos"], 4)
        self.assertEqual(r["valor_estoque"], 1691.0)
        self.assertEqual(r["total_vendido"], 185.0)
        self.assertEqual(r["mais_caro"], "Castanha")
        self.assertEqual(r["baixo"], ["Tapioca"])
        self.assertEqual(L.relatorio({}, 0)["mais_caro"], "")


if __name__ == "__main__":
    unittest.main()
