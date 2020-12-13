import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodwanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)

    def test_odejmowanie(self):
        r = calculate(5, 3, '-')
        self.assertEqual(r, 2)

    def test_mnozenie(self):
        r = calculate(2, 2, '*')
        self.assertEqual(r, 4)

    def test_dzielenie(self):
        r = calculate(20, 2, '/')
        self.assertEqual(r, 10)

    def test_reszta(self):
        r = calculate(4, 3, '/')
        self.assertEqual(r, 1)
