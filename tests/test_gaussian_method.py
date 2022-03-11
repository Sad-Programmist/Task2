import unittest
from unittest import TestCase
from gaussian_method import gaussian_integral
from simple_methods import parabola_integral_full_n
from functions import *

EPSILON = 1e-5


class Test(TestCase):
    def test_gaussian_integral01(self):
        a = 0
        b = 8
        n = 100000
        n_gaussian = 5
        integral = gaussian_integral(function1, a, b, n_gaussian)
        expected_integral = parabola_integral_full_n(function1, a, b, n)
        self.assertTrue(abs(integral - expected_integral < EPSILON))

    def test_gaussian_integral02(self):
        a = -1.2145
        b = -0.145878
        n = 4000
        n_gaussian = 6
        integral = gaussian_integral(function2, a, b, n_gaussian)
        expected_integral = parabola_integral_full_n(function2, a, b, n)
        self.assertTrue(abs(integral - expected_integral < EPSILON))

    def test_gaussian_integral03(self):
        a = 45
        b = 50
        n = 20000
        n_gaussian = 4
        integral = gaussian_integral(function3, a, b, n_gaussian)
        expected_integral = parabola_integral_full_n(function3, a, b, n)
        self.assertTrue(abs(integral - expected_integral < EPSILON))

    def test_gaussian_integral04(self):
        a = -100
        b = -99.9999
        n = 20000
        n_gaussian = 3
        integral = gaussian_integral(function4, a, b, n_gaussian)
        expected_integral = parabola_integral_full_n(function4, a, b, n)
        self.assertTrue(abs(integral - expected_integral < EPSILON))


if __name__ == '__main__':
    unittest.main()
