import unittest
import logica as L


class TestForca(unittest.TestCase):
    def test_escolher_palavra(self):
        self.assertEqual(L.escolher_palavra(1)[0], "tambaqui")
        self.assertEqual(L.escolher_palavra(6)[0], "jaraqui")
        self.assertEqual(L.escolher_palavra(7)[0], "tambaqui")      # volta ao início
        self.assertEqual(len(L.escolher_palavra(2)), 2)

    def test_validar_letra(self):
        self.assertEqual(L.validar_letra("  A ", []), "a")
        for ruim, tent in (("", []), ("ab", []), ("1", []), ("ç", []), ("!", []), ("a", ["a"]), ("A", ["a"])):
            with self.assertRaises(ValueError, msg=repr((ruim, tent))):
                L.validar_letra(ruim, tent)

    def test_exibicao(self):
        self.assertEqual(L.montar_exibicao("pirarucu", []), "_ _ _ _ _ _ _ _")
        self.assertEqual(L.montar_exibicao("pirarucu", ["r", "u"]), "_ _ r _ r u _ u")

    def test_venceu(self):
        self.assertFalse(L.venceu("cupuacu", ["c", "u"]))
        self.assertTrue(L.venceu("cupuacu", ["c", "u", "p", "a"]))
        self.assertFalse(L.venceu("cupuacu", []))

    def test_vidas_e_pontos(self):
        self.assertEqual(L.vidas_restantes([]), 6)
        self.assertEqual(L.vidas_restantes(["x", "z"]), 4)
        self.assertEqual(L.pontos_da_rodada(True, 5), 35)      # vitória com 1 erro
        self.assertEqual(L.pontos_da_rodada(True, 6), 40)      # sem erros
        self.assertEqual(L.pontos_da_rodada(False, 0), 0)

    def test_jogar_letra(self):
        ac, er = [], []
        self.assertTrue(L.jogar_letra("jaraqui", "a", ac, er))
        self.assertFalse(L.jogar_letra("jaraqui", "z", ac, er))
        self.assertEqual((ac, er), (["a"], ["z"]))

    def test_rodada_completa_vitoria_com_um_erro(self):
        palavra = L.escolher_palavra(1)[0]
        ac, er = [], []
        for letra in "xtambqui":
            letra = L.validar_letra(letra, ac + er)
            L.jogar_letra(palavra, letra, ac, er)
        self.assertTrue(L.venceu(palavra, ac))
        self.assertEqual(L.pontos_da_rodada(True, L.vidas_restantes(er)), 35)


if __name__ == "__main__":
    unittest.main()
