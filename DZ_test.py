import unittest
from DZ import ost

class TestMath(unittest.TestCase):

    def test_ost(self):
        self.assertEqual(ost(10, 5 ), 0 )
        self.assertEqual(ost(17, 4), 1)
        self.assertEqual(ost(43, 4), 3)
        self.assertRaises(TypeError, ost, 12, 0)
