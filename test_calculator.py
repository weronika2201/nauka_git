import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_dodwanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)
