import unittest
from unittest import TestCase
from scipy import integrate
from simple_methods import *

EPSILON = 1e-5


class Test(TestCase):
    def test_rectangle_integral01(self):
        a = 0
        b = math.pi / 6
        n = 100000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(rectangle_integral(function1, a, b, n) - result) < EPSILON)

    def test_rectangle_integral02(self):
        a = -7
        b = -6.9
        n = 100000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(rectangle_integral(function1, a, b, n) - result) < EPSILON)

    def test_trapezoid_integral01(self):
        a = -9
        b = 5.2
        n = 10000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(trapezoid_integral(function1, a, b, n) - result) < EPSILON)

    def test_trapezoid_integral02(self):
        a = 32.1
        b = 41.0545855
        n = 6000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(trapezoid_integral(function1, a, b, n) - result) < EPSILON)

    def test_parabola_integral01(self):
        a = -100
        b = -99
        n = 5000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(parabola_integral(function1, a, b, n) - result) < EPSILON)

    def test_parabola_integral02(self):
        a = -32
        b = 21
        n = 4895
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(parabola_integral(function1, a, b, n) - result) < EPSILON)

    def test_parabola_integral_full_n01(self):
        a = 47.2154
        b = 84.02154
        n = 5000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(parabola_integral_full_n(function1, a, b, n) - result) < EPSILON)

    def test_parabola_integral_full_n02(self):
        a = 89
        b = 3
        n = 7000
        self.assertRaisesRegex(ValueError, "a should be less than b", parabola_integral_full_n, function1, a, b, n)

    def test_cubic_parabola_integral01(self):
        a = 0
        b = 0
        n = 100000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(cubic_parabola_integral(function1, a, b, n) - result) < EPSILON)

    def test_cubic_parabola_integral02(self):
        a = -10
        b = 0
        n = -100000
        self.assertRaisesRegex(ValueError, "n should be > 0", parabola_integral_full_n, function1, a, b, n)

    def test_boole_integral01(self):
        a = 87
        b = 97
        n = 10000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(boole_integral(function1, a, b, n) - result) < EPSILON)

    def test_boole_integral02(self):
        a = 7.2154
        b = 10
        n = 10000
        result, error = integrate.quad(function1, a, b)
        self.assertTrue(abs(boole_integral(function1, a, b, n) - result) < EPSILON)


if __name__ == '__main__':
    unittest.main()
