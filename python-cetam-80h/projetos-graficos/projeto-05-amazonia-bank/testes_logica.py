import os
import tempfile
import unittest
import logica as L


class TestBanco(unittest.TestCase):
    def setUp(self):
        self.contas = {}
        self.ana = L.criar_conta(self.contas, "  ana lima ", "1234")
        self.bia = L.criar_conta(self.contas, "Bia Souza", "4321")

    def test_formatar(self):
        self.assertEqual(L.formatar(1234.5), "R$ 1.234,50")
        self.assertEqual(L.formatar(0), "R$ 0,00")

    def test_criar_conta(self):
        self.assertEqual(self.ana.titular, "Ana Lima")
        self.assertEqual(self.ana.saldo, 0)
        self.assertIn("Ana Lima", self.contas)

    def test_criar_conta_invalida(self):
        for titular, senha in (("", "1234"), ("A;B", "1234"), ("ana lima", "1234"),
                               ("Novo", "123"), ("Novo", "12345"), ("Novo", "12a4")):
            with self.assertRaises(ValueError, msg=str((titular, senha))):
                L.criar_conta(self.contas, titular, senha)
        self.assertEqual(len(self.contas), 2)

    def test_entrar(self):
        self.assertIs(L.entrar(self.contas, "ANA LIMA", "1234"), self.ana)
        for t, s in (("Ana Lima", "0000"), ("Zé", "1234")):
            with self.assertRaises(ValueError) as ctx:
                L.entrar(self.contas, t, s)
            self.assertEqual(str(ctx.exception), "Titular ou senha inválidos.")

    def test_deposito_e_saque(self):
        self.ana.depositar(100)
        self.ana.sacar(30.5)
        self.assertEqual(self.ana.saldo, 69.5)
        self.assertEqual(self.ana.historico, ["Depósito: +R$ 100,00", "Saque: -R$ 30,50"])
        for f, v in ((self.ana.depositar, 0), (self.ana.depositar, -5), (self.ana.sacar, 0), (self.ana.sacar, 70)):
            with self.assertRaises(ValueError):
                f(v)
        self.assertEqual(self.ana.saldo, 69.5)

    def test_transferencia(self):
        self.ana.depositar(200)
        self.ana.transferir(self.bia, 50)
        self.assertEqual((self.ana.saldo, self.bia.saldo), (150, 50))
        self.assertEqual(self.ana.historico[-1], "Transferência enviada para Bia Souza: -R$ 50,00")
        self.assertEqual(self.bia.historico[-1], "Transferência recebida de Ana Lima: +R$ 50,00")

    def test_transferencia_invalida(self):
        self.ana.depositar(10)
        for destino, valor in ((self.ana, 5), (self.bia, 0), (self.bia, 11)):
            with self.assertRaises(ValueError):
                self.ana.transferir(destino, valor)
        self.assertEqual((self.ana.saldo, self.bia.saldo), (10, 0))

    def test_extrato(self):
        self.ana.depositar(1234.5)
        self.assertEqual(self.ana.extrato(), ["Depósito: +R$ 1.234,50", "Saldo atual: R$ 1.234,50"])
        self.assertEqual(self.bia.extrato(), ["Saldo atual: R$ 0,00"])

    def test_persistencia(self):
        with tempfile.TemporaryDirectory() as pasta:
            arq = os.path.join(pasta, "contas.txt")
            self.assertEqual(L.carregar_contas(arq), {})
            self.ana.depositar(99.9)
            L.salvar_contas(self.contas, arq)
            with open(arq, encoding="utf-8") as f:
                self.assertEqual(f.read().splitlines(), ["Ana Lima;1234;99.90", "Bia Souza;4321;0.00"])
            novas = L.carregar_contas(arq)
            self.assertEqual(novas["Ana Lima"].saldo, 99.9)
            self.assertTrue(novas["Bia Souza"].autenticar("4321"))
            self.assertEqual(novas["Ana Lima"].historico, [])


if __name__ == "__main__":
    unittest.main()
