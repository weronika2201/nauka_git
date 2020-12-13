import unittest

from str_calculator import str_calculator

class TestSringCalculator(unittest.TestCase):
    def test_concat(self):
        r = str_calculator("a", "b", 'concat')
        self.assertEqual(r, 'ab')

    def test_contain_when_true(self):
        r = str_calculator("ala", "ala ma kota", 'contains')
        self.assertEqual(r, True)

    def test_contain_when_false(self):
        r = str_calculator("xxx", "ala ma kota", 'contains')
        self.assertEqual(r, False)

    def test_endsWith(self):
        r = str_calculator()
        r = str_calculator("a", "hhhhhha", 'endsWith')
        self.assertEqual(r, True)
