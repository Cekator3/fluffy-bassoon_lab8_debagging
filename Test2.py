import unittest
from math import inf
from unittest import TestCase
from main2 import abs
from main2 import factorial
from main2 import cos
from main2 import sin
from main2 import ln
from main2 import func

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(1), 1)

    def test_abs2(self):
        self.assertEqual(abs(-1), 1)

class TestFactorial(unittest.TestCase):
    def test_factorial1(self):
        self.assertEqual(factorial(1), 1)

class TestCos(unittest.TestCase):
    def test_cos1(self):
        self.assertEqual(cos(0.5), 0.8775825621589781)

class TestCos2(unittest.TestCase):
    def test_cos2(self):
        self.assertEqual(round(cos(3.14/2)), 0)

class TestSin(unittest.TestCase):
    def test_sin1(self):
        self.assertEqual(sin(0.5), 0.4794255386164159)

class TestSin2(unittest.TestCase):
    def test_sin2(self):
        self.assertEqual(round(sin(3.14/2)), 1)

class TestLn(unittest.TestCase):
    def test_ln1(self):
        self.assertEqual(ln(0.5), -0.6931471795482411)

class TestLn2(unittest.TestCase):
    def test_ln2(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual((ln(-0.5)), 1)

class TestIntegrLnCos(unittest.TestCase):
    def test_ln2(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual((ln(5)), 1)


class Testfunc(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func(-0.5), -1.9577488602923039)
class Testfunc2(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func(0), inf)

if __name__ == "__main__":
    unittest.main()
