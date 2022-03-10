import unittest
import math
from unittest import TestCase
from scipy import integrate
from simple_methods import function, rectangle_integral, trapezoid_integral, parabola_integral, parabola_integral_full_n, \
    cubic_parabola_integral, boole_integral

EPSILON = 1e-4


class Test(TestCase):
    def test_rectangle_integral(self):
        a = 0
        b = math.pi / 6
        n = 10000
        result, error = integrate.quad(function, a, b)
        self.assertTrue(abs(rectangle_integral(a, b, n) - result) < EPSILON)

    def test_trapezoid_integral(self):
        a = 0
        b = math.pi / 6
        n = 5000
        result, error = integrate.quad(function, a, b)
        self.assertTrue(abs(trapezoid_integral(a, b, n) - result) < EPSILON)

    def test_parabola_integral(self):
        a = 0
        b = math.pi / 6
        n = 5000
        result, error = integrate.quad(function, a, b)
        self.assertTrue(abs(parabola_integral(a, b, n) - result) < EPSILON)

    def test_parabola_integral_full_n(self):
        a = 0
        b = math.pi / 6
        n = 5000
        result, error = integrate.quad(function, a, b)
        self.assertTrue(abs(parabola_integral_full_n(a, b, n) - result) < EPSILON)

    def test_cubic_parabola_integral(self):
        a = 0
        b = math.pi / 6
        n = 100000
        result, error = integrate.quad(function, a, b)
        self.assertTrue(abs(cubic_parabola_integral(a, b, n) - result) < EPSILON)

    def test_boole_integral(self):
        a = 0
        b = math.pi / 6
        n = 10000
        result, error = integrate.quad(function, a, b)
        self.assertTrue(abs(boole_integral(a, b, n) - result) < EPSILON)


if __name__ == '__main__':
    unittest.main()
