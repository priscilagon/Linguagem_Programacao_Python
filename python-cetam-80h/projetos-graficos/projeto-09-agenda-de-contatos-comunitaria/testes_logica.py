import os
import tempfile
import unittest
import logica as L


def agenda():
    c = []
    L.cadastrar_contato(c, "maria das dores", "(92) 99123-4567", "Maria@Email.com", "centro")
    L.cadastrar_contato(c, "João Silva", "9232345678", "joao@email.com", "")
    L.cadastrar_contato(c, "Ana Lima", "92988887777", "ana@email.com", "Centro")
    return c


class TestAgenda(unittest.TestCase):
    def test_padronizacoes(self):
        self.assertEqual(L.padronizar_nome("  maRIA das dores "), "Maria Das Dores")
        self.assertEqual(L.limpar_telefone("(92) 99123-4567"), "92991234567")
        self.assertEqual(L.padronizar_bairro("  nossa; senhora "), "Nossa Senhora")
        self.assertEqual(L.padronizar_bairro("  ;  "), "Não informado")

    def test_validacoes(self):
        for ok in ("9232345678", "92991234567"):
            self.assertTrue(L.telefone_valido(ok))
        for ruim in ("123", "929912345678", "92a9123456", ""):
            self.assertFalse(L.telefone_valido(ruim))
        self.assertTrue(L.email_valido("a@b.com"))
        for ruim in ("ab.com", "a@bcom", "a b@c.com", "a;b@c.com"):
            self.assertFalse(L.email_valido(ruim))

    def test_cadastro(self):
        c = agenda()
        self.assertEqual(c[0], {"nome": "Maria Das Dores", "telefone": "92991234567",
                                "email": "maria@email.com", "bairro": "Centro"})
        self.assertEqual(c[1]["bairro"], "Não informado")

    def test_cadastro_invalido(self):
        c = agenda()
        for args in (("", "92991234567", "a@b.com", ""), ("A;B", "92991234567", "a@b.com", ""),
                     ("MARIA DAS DORES", "92991234567", "a@b.com", ""), ("Novo", "123", "a@b.com", ""),
                     ("Novo", "92991234567", "sem-arroba", "")):
            with self.assertRaises(ValueError, msg=str(args)):
                L.cadastrar_contato(c, *args)
        self.assertEqual(len(c), 3)

    def test_listar_e_buscar(self):
        c = agenda()
        self.assertEqual([x["nome"] for x in L.listar_ordenado(c)], ["Ana Lima", "João Silva", "Maria Das Dores"])
        self.assertEqual([x["nome"] for x in L.buscar_por_trecho(c, "  MAR ")], ["Maria Das Dores"])
        self.assertEqual(len(L.buscar_por_trecho(c, "a")), 3)
        self.assertEqual(L.buscar_por_trecho(c, "zzz"), [])

    def test_editar(self):
        c = agenda()
        self.assertEqual(L.editar_contato(c, "ana lima", "(92) 98888-0000", "", "Aleixo"), [])
        ana = L.buscar_contato(c, "Ana Lima")
        self.assertEqual((ana["telefone"], ana["email"], ana["bairro"]), ("92988880000", "ana@email.com", "Aleixo"))
        avisos = L.editar_contato(c, "Ana Lima", "123", "semarroba", "")
        self.assertEqual(len(avisos), 2)
        self.assertEqual(ana["telefone"], "92988880000")
        with self.assertRaises(ValueError):
            L.editar_contato(c, "Zé", "", "", "")

    def test_remover(self):
        c = agenda()
        L.remover_contato(c, "joão silva")
        self.assertEqual(len(c), 2)
        with self.assertRaises(ValueError):
            L.remover_contato(c, "Joao")

    def test_resumo(self):
        self.assertEqual(L.resumo_por_bairro(agenda()), {"Centro": 2, "Não informado": 1})

    def test_persistencia(self):
        with tempfile.TemporaryDirectory() as pasta:
            arq = os.path.join(pasta, "agenda.txt")
            self.assertEqual(L.carregar_contatos(arq), [])
            c = agenda()
            L.salvar_contatos(c, arq)
            with open(arq, encoding="utf-8") as f:
                self.assertEqual(f.read().splitlines()[0], "Maria Das Dores;92991234567;maria@email.com;Centro")
            self.assertEqual(L.carregar_contatos(arq), c)
            L.remover_contato(c, "Ana Lima")
            L.salvar_contatos(c, arq)                    # grava de novo SEM duplicar
            self.assertEqual(len(L.carregar_contatos(arq)), 2)


if __name__ == "__main__":
    unittest.main()
