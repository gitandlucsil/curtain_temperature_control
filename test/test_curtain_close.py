import sys
import unittest
sys.path.append("../")
from models.curtain_close import CurtainClose

class TestCurtainClose(unittest.TestCase):

    def setUp(self):
        self._cf = CurtainClose()

    def test_is_instance(self):
        self.assertIsInstance(self._cf, CurtainClose)

    def test_cfl(self):
        self._cf.cfl = 15.0
        self.assertEqual(self._cf.cfl, 15.0)
        self._cf.cfl = "17.22"
        self.assertEqual(self._cf.cfl, 17.22)

    def test_cfd(self):
        self._cf.cfd = 21.4
        self.assertEqual(self._cf.cfd, 21.4)
        self._cf.cfd = "18.77"
        self.assertEqual(self._cf.cfd, 18.77)

    def test_ton(self):
        self._cf.ton = 21
        self.assertEqual(self._cf.ton, 21)
        self._cf.ton = "184"
        self.assertEqual(self._cf.ton, 184)

    def test_toff(self):
        self._cf.toff = 210
        self.assertEqual(self._cf.toff, 210)
        self._cf.toff = "18"
        self.assertEqual(self._cf.toff, 18)

if __name__ == "__main__":
    unittest.main()