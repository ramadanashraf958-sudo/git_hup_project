import unittest

from calc import calc


class TestCalc(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(calc(5, 3, "+"), 8)
        
    def test_addition_nega(self):
        self.assertEqual(calc(-5, -3, "+"), -8)
