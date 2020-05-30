import sys
import unittest
sys.path.append("../")
from minimum_ventilation import MinimunVentilation

class TestMinimunVentilation(unittest.TestCase):

    def setUp(self):
        self._vm = MinimunVentilation()

    def test_is_instance(self):
        self.assertIsInstance(self._vm, MinimunVentilation)

    def test_abrefecha(self):
        self._vm.abrefecha = 22
        self.assertEqual(self._vm.abrefecha, 22)
        self._vm.abrefecha = "19"
        self.assertEqual(self._vm.abrefecha, 19)

    def test_aberto(self):
        self._vm.aberto = 21
        self.assertEqual(self._vm.aberto, 21)
        self._vm.aberto = "18"
        self.assertEqual(self._vm.aberto, 18)

    def test_fechado(self):
        self._vm.fechado = 21
        self.assertEqual(self._vm.fechado, 21)
        self._vm.fechado = "184"
        self.assertEqual(self._vm.fechado, 184)

    def test_limite(self):
        self._vm.limite = 99
        self.assertEqual(self._vm.limite, 99)
        self._vm.limite = "18"
        self.assertEqual(self._vm.limite, 18)

if __name__ == "__main__":
    unittest.main()