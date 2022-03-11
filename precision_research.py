from simple_methods import *
import matplotlib.pyplot as plt
import numpy as np


def error_function(function, a, b, n):
    result = []
    true_value = function(a, b, 10000)
    for index in n:
        result.append(np.abs(function(a, b, index) - true_value))
    return result


def draw_function(a, b, n, step):
    list_n = np.arange(1, n, step)
    h = (b-a)/list_n

    fig, ax = plt.subplots()
    ax.plot(h, error_function(boole_integral, a, b, list_n), c="deepskyblue", label="boole")
    ax.plot(h, error_function(cubic_parabola_integral, a, b, list_n), c="lawngreen", label="cubic_parabola")
    ax.plot(h, error_function(rectangle_integral, a, b, list_n), c="r", label="rectangle")
    ax.plot(h, error_function(trapezoid_integral, a, b, list_n), c="darkorange", label="trapezoid")
    ax.plot(h, error_function(parabola_integral, a, b, list_n), c="darkviolet", label="parabola")

    ax.set(xlabel='h', ylabel='error', title='Precision research')
    plt.xlim(0, 0.15)
    plt.ylim(0, 0.5)
    ax.grid()
    ax.legend()

    plt.show()


if __name__ == '__main__':
    a = 0
    b = math.pi / 6
    n = 1000
    step = 5
    draw_function(a, b, n, step)