import sys
import unittest
sys.path.append("../")
from models.curtain_open import CurtainOpen

class TestCurtainOpen(unittest.TestCase):

    def setUp(self):
        self._ca = CurtainOpen()

    def test_is_instance(self):
        self.assertIsInstance(self._ca, CurtainOpen)

    def test_cal(self):
        self._ca.cal = 22.4 
        self.assertEqual(self._ca.cal, 22.4)
        self._ca.cal = "19.25"
        self.assertEqual(self._ca.cal, 19.25)

    def test_cad(self):
        self._ca.cad = 21.4
        self.assertEqual(self._ca.cad, 21.4)
        self._ca.cad = "18.77"
        self.assertEqual(self._ca.cad, 18.77)

    def test_ton(self):
        self._ca.ton = 21
        self.assertEqual(self._ca.ton, 21)
        self._ca.ton = "184"
        self.assertEqual(self._ca.ton, 184)

    def test_toff(self):
        self._ca.toff = 210
        self.assertEqual(self._ca.toff, 210)
        self._ca.toff = "18"
        self.assertEqual(self._ca.toff, 18)

if __name__ == "__main__":
    unittest.main()