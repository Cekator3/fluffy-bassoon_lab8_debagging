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
        self.assertEqual(arr, [1, 2, 3, 4])
class TestSortirovka2(unittest.TestCase):
    def test_sortirovka2(self):
        arr = [0, 6, -1, 3, 2, 4]
        array_sort(arr)
        self.assertEqual(arr, [-1, 0, 2, 3, 4, 6])


'''2'''
class TestPolindromTrue(TestCase):
    def test_polindrom(self):
        polindroms = ['malayalam', '121', 'арара']
        for polindrom in polindroms:
            self.assertTrue(Polindrom(polindrom))

class TestPolindromFalse(unittest.TestCase):
    def test_polindrom(self):
        notPolindroms = ['python', '1212', 'базука']
        for notPolindrom in notPolindroms:
            self.assertFalse(Polindrom(notPolindrom))

'''3'''
class TestFactorial1(unittest.TestCase):
    def test_factorial(self):
        inputs = [0, 1, 2, 3, 4]
        expectedOutputs = [1, 1, 2, 6, 24]
        for i in range(len(inputs)):
            self.assertEqual(fac(inputs[i]), expectedOutputs[i])

class TestFactorial2(unittest.TestCase):
    def test_factorial(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(fac(-1), 1)

'''4'''
class Testfibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        inputs = [1, 2, 3, 4]
        expectedOutputs = [1, 1, 2, 3]
        for i in range(len(inputs)):
            self.assertEqual(fib(inputs[i]), expectedOutputs[i])

class Testfibonacci2(unittest.TestCase):
    def test_fibonacci(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(fib(-5), 1)


'''5'''
class TestStepen(unittest.TestCase):
    def test_stepen(self):
        numbers = [0, 1, 2, 3, 4]
        degrees = [0, 9, 2, 2, 2]
        expectedOutputs = [1, 1, 4, 9, 16]
        for i in range(len(numbers)):
            self.assertEqual(step(numbers[i], degrees[i]), expectedOutputs[i])

'''6'''
class TestProstoeTrue(unittest.TestCase):
    def test_prostoe(self):
        primeNumbers = [2, 3, 5, 7, 11]
        for number in primeNumbers:
            self.assertTrue(prost(number))
class TestProstoeFalse(unittest.TestCase):
    def test_prostoe(self):
        notPrimeNumbers = [4, 6, 9, 8, 12]
        for number in notPrimeNumbers:
            self.assertFalse(prost(number))

if __name__ == "__main__":
    unittest.main()
