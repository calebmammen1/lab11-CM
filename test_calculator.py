import unittest
from calculator import *

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):


    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)     # 10 / 2 = 5
        self.assertEqual(divide(5, 20), 4)     # 20 / 5 = 4
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)  # a == 0 should raise error

    def test_log_invalid_argument(self):
        # invalid because base <= 0, base == 1, or b <= 0
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()