import sys
import unittest
sys.path.append("../")
from curtain_open import CurtainOpen

class TestCurtainOpen(unittest.TestCase):

    def setUp(self):
        self._ca = CurtainOpen()

    def test_is_instance(self):
        self.assertIsInstance(self._ca, CurtainOpen)

    def test_cal(self):
        self._ca.cal =22.4 
        self.assertEqual(self._ca.cal, 22.4)

if __name__ == "__main__":
    unittest.main()