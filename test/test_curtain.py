import sys
import unittest
sys.path.append("../")
from models.curtain import Curtain

class TestCurtain(unittest.TestCase):

    def setUp(self):
        self._curtain = Curtain()

    def test_abertura(self):
        self._curtain.abertura = 53
        self.assertEqual(self._curtain.abertura, 53)
        self._curtain.abertura = "67"
        self.assertEqual(self._curtain.abertura, 67)

if __name__ == "__main__":
    unittest.main()