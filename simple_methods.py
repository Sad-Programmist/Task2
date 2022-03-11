import math
from functions import *


def rectangle_integral(function, a, b, n):
    check_abn(a, b, n)
    if a == b:
        return 0
    h = (b - a) / n
    function_sum = 0
    for rectangle_ind in range(n):
        function_sum += function(a + rectangle_ind * h)
    return h * function_sum


def trapezoid_integral(function, a, b, n):
    check_abn(a, b, n)
    if a == b:
        return 0
    h = (b - a) / n
    function_sum = 0
    for trapezoid_ind in range(1, n):
        function_sum += function(a + trapezoid_ind * h)
    return h / 2 * (function(a) + function(b) + 2 * function_sum)


def parabola_integral(function, a, b, n):
    check_abn(a, b, n)
    if a == b:
        return 0
    h = (b - a) / (2 * n)
    function_odd_sum = 0
    function_even_sum = 0
    for x_index in range(1, 2 * n):
        if x_index % 2 != 0:
            function_odd_sum += function(a + x_index * h)
        else:
            function_even_sum += function(a + x_index * h)
    return h / 3 * (function(a) + function(b) + 4 * function_odd_sum + 2 * function_even_sum)


def parabola_integral_full_n(function, a, b, n):
    check_abn(a, b, n)
    if a == b:
        return 0
    h = (b - a) / n
    function_odd_sum = 0
    function_even_sum = 0
    for x_index in range(1, n):
        if x_index % 2 != 0:
            function_odd_sum += function(a + x_index * h)
        else:
            function_even_sum += function(a + x_index * h)
    return h / 3 * (function(a) + function(b) + 4 * function_odd_sum + 2 * function_even_sum)


def cubic_parabola_integral(function, a, b, n):
    check_abn(a, b, n)
    if a == b:
        return 0
    h = (b - a) / n
    function_sum_for_3 = 0
    function_sum_for_2 = 0
    for x_index in range(1, n):
        if x_index % 3 != 0:
            function_sum_for_3 += function(a + x_index * h)
        else:
            function_sum_for_2 += function(a + x_index * h)
    return 3 * h / 8 * (function(a) + function(b) + 3 * function_sum_for_3 + 2 * function_sum_for_2)


def boole_integral(function, a, b, n):
    check_abn(a, b, n)
    if a == b:
        return 0
    h = (b - a) / n
    function_sum_for_32 = 0
    function_sum_for_12 = 0
    function_sum_for_14 = 0
    for x_index in range(1, n):
        if x_index % 2 != 0:
            function_sum_for_32 += function(a + x_index * h)
        elif x_index % 2 == 0 and x_index % 4 != 0:
            function_sum_for_12 += function(a + x_index * h)
        elif x_index % 4 == 0:
            function_sum_for_14 += function(a + x_index * h)
    return 2 * h / 45 * (7 * (function(a) + function(b)) + 32 * function_sum_for_32 +
                         12 * function_sum_for_12 + 14 * function_sum_for_14)


def check_abn(a, b, n):
    if a > b:
        raise ValueError("a should be less than b")
    if n <= 0:
        raise ValueError("n should be > 0")


if __name__ == '__main__':
    a = 0
    b = math.pi / 6
    n = 5000
    print("Rectangle integral: {}".format(rectangle_integral(function1, a, b, n)))
    print("Trapezoid integral: {}".format(trapezoid_integral(function1, a, b, n)))
    print("Parabola integral: {}".format(parabola_integral(function1, a, b, n // 2)))
    print("Parabola integral full n: {}".format(parabola_integral_full_n(function1, a, b, n)))
    print("Cubic parabola integral: {}".format(cubic_parabola_integral(function1, a, b, n)))
    print("Boole's integral: {}".format(boole_integral(function1, a, b, n)))
