from __future__ import annotations
import unittest

from src.calculate_gini import calculate_gini

class TestCalculateGini(unittest.TestCase):

    def test_calculate_gini_zero(self):
        income = [0, 0, 0]
        self.assertEqual(calculate_gini(income), 0.0)

    def test_calculate_gini_all_Same(self):
        income = [1, 1, 1]
        self.assertEqual(calculate_gini(income), 0.0)

    def test_calculate_gini_values(self):
        income = [10, 20, 30]
        gini_value = calculate_gini(income)
        self.assertTrue(gini_value >= 0 or gini_value <= 1.0)
    


if __name__ == '__main__':
    unittest.main()