# https://github.com/calebmammen1/lab11-CM
# Partner 1: Caleb Mammen
# Partner 2: Caleb mammen

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 10), 6)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(10, 20), -10)
        self.assertEqual(sub(0, 7), -7)



    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-4, 5), -20)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        with self.assertRaises(ZeroDivisionError):
            div(0, 7)


    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)
        self.assertAlmostEqual(log(3, 9), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)



    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hyp(3, 4), 5)
        self.assertAlmostEqual(hyp(5, 12), 13)
        self.assertAlmostEqual(hyp(0, 0), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(sqrt(9), 3)
        self.assertAlmostEqual(sqrt(16), 4)
        with self.assertRaises(ValueError):
            sqrt(-1)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
