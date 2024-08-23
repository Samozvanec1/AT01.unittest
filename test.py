import unittest
from main import *

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertNotEqual(add(2, 3), 6)

    def test_sub(self):
        self.assertEqual(sub(1, 2), -1)
        self.assertNotEqual(sub(2, 3), 1)

    def test_mul(self):
        self.assertEqual(mul(1, 2), 2)
        self.assertNotEqual(mul(2, 3), 7)

    def test_div(self):
        self.assertEqual(div(1, 2), 0.5)
        self.assertNotEqual(div(2, 3), 0.7)

    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(4))
        self.assertFalse(check(1))
        self.assertFalse(check(3))
    def test_divide_zero(self):
        self.assertEqual(divide_zero(1, 2), 0.5) # AssertEqual это метод для сравнения двух значений
        self.assertRaises(TypeError, divide_zero, 1, 0) # AssertRaises это метод для проверки исключений


if __name__ == '__main__':
    unittest.main()
