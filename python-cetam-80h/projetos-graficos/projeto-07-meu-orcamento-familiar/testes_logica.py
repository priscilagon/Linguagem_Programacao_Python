import unittest
import logica as L


def exemplo():
    return [
        L.novo_lancamento("receita", "salário", 2500.00),
        L.novo_lancamento("despesa", "aluguel", 700.00, 1),
        L.novo_lancamento("despesa", "feira", 450.00, 2),
        L.novo_lancamento("despesa", "barco", 300.00, 3),
        L.novo_lancamento("despesa", "cinema", 252.50, 5),
    ]


class TestOrcamento(unittest.TestCase):
    def test_novo_lancamento(self):
        r = L.novo_lancamento("receita", "  salário  ", 2500)
        self.assertEqual(r, {"tipo": "receita", "descricao": "Salário", "categoria": "Receita", "valor": 2500})
        d = L.novo_lancamento("despesa", "AÇAÍ da feira", 35.5, 2)
        self.assertEqual((d["descricao"], d["categoria"]), ("Açaí da feira", "Alimentação"))

    def test_lancamento_invalido(self):
        casos = [("receita", "  ", 10, None), ("receita", "x", 0, None), ("receita", "x", -5, None),
                 ("despesa", "x", 10, 0), ("despesa", "x", 10, 7), ("despesa", "x", 10, None)]
        for tipo, desc, valor, cat in casos:
            with self.assertRaises(ValueError, msg=str((tipo, desc, valor, cat))):
                L.novo_lancamento(tipo, desc, valor, cat)

    def test_totais(self):
        self.assertEqual(L.totais(exemplo()), (2500.0, 1702.5, 797.5))
        self.assertEqual(L.totais([]), (0, 0, 0))

    def test_percentual_e_situacao(self):
        self.assertAlmostEqual(L.percentual_comprometido(2500, 1702.5), 68.1)
        self.assertIsNone(L.percentual_comprometido(0, 100))
        self.assertEqual(L.situacao_orcamento(68.1), "Saudável")
        self.assertEqual(L.situacao_orcamento(70), "Saudável")
        self.assertEqual(L.situacao_orcamento(70.01), "Atenção – despesas altas")
        self.assertEqual(L.situacao_orcamento(90), "Atenção – despesas altas")
        self.assertEqual(L.situacao_orcamento(100), "Atenção – despesas altas")
        self.assertEqual(L.situacao_orcamento(120), "Alerta – despesas maiores que a receita")
        self.assertIn("Registre ao menos uma receita", L.situacao_orcamento(None))

    def test_categorias(self):
        por = L.despesas_por_categoria(exemplo())
        self.assertEqual(por, {"Moradia": 700.0, "Alimentação": 450.0, "Transporte": 300.0, "Lazer": 252.5})
        self.assertEqual(L.categoria_maior_gasto(por), ("Moradia", 700.0))
        self.assertEqual(L.categoria_maior_gasto({}), ("", 0.0))
        pct = L.percentuais_por_categoria(por)
        self.assertAlmostEqual(pct["Moradia"], 700 / 1702.5 * 100)
        self.assertAlmostEqual(sum(pct.values()), 100)
        self.assertEqual(L.percentuais_por_categoria({}), {})

    def test_despesas_nao_incluem_receitas(self):
        self.assertEqual(L.despesas_por_categoria([L.novo_lancamento("receita", "bolsa", 100)]), {})


if __name__ == "__main__":
    unittest.main()
