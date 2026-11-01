import unittest

from calc import calc


class TestCalc(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(calc(5, 3, "+"), 8)
        
    def test_addition_nega(self):
        self.assertEqual(calc(-5, -3, "+"), -8)

    def test_addition_positive_negative(self):
        self.assertEqual(calc(-5, 3, "+"), -2)

    def test_addition_with_zero(self):
        self.assertEqual(calc(5, 0, "+"), 5)

    def test_addition_decimal_numbers(self):
        self.assertAlmostEqual(calc(1.5, 2.5, "+"), 4.0)

