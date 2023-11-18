import unittest
from unittest import TestCase

from main import Polindrom
from main import array_sort
from main import fac
from main import fib
from main import step
from main import prost


'''1'''
class TestSortirovka1(unittest.TestCase):
    def test_sortirovka1(self):
        arr = [1, 3, 2, 4]
        array_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 999999999])
class TestSortirovka2(unittest.TestCase):
    def test_sortirovka2(self):
        arr = [0, 6, -1, 3, 2, 4]
        array_sort(arr)
        self.assertEqual(arr, [-1, 0, 2, 3, 4, 6])


'''2'''
class TestPolindromTrue(TestCase):
    def test_polindrom(self):
        self.assertTrue(Polindrom('malayalam'))

class TestPolindromFalse(unittest.TestCase):
    def test_polindrom(self):
        self.assertFalse(Polindrom("python"))


'''3'''
class TestFactorial1(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(fac(3), 6)

class TestFactorial2(unittest.TestCase):
    def test_factorial(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(fac(-1), 1)

'''4'''
class Testfibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(10), 55)

class Testfibonacci2(unittest.TestCase):
    def test_fibonacci(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(fib(-5), 1)


'''5'''
class Teststepen1(unittest.TestCase):
    def test_stepen(self):
        self.assertEqual(step(0, 5), 0)

class Teststepen2(unittest.TestCase):
    def test_stepen(self):
        a = 4.5
        b = 1.5
        self.assertEqual(step(a, b), 9.545941546018392)

'''6'''
class TestProstoeTrue(unittest.TestCase):
    def test_prostoe(self):
        self.assertTrue(prost(5))
class TestProstoeFalse(unittest.TestCase):
    def test_prostoe(self):
        self.assertFalse(prost(6))

if __name__ == "__main__":
    unittest.main()
