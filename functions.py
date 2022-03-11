import numpy as np


def function1(x):
    return 5 * (np.sin(x) - 3) + 1


def function2(x):
    return 1 / x * (np.cos(x) * x - 3) + np.log(x ** 2 + 2)


def function3(x):
    return 3 ** (2 * x) + np.log(x ** 2)


def function4(x):
    return np.e ** 1 / x + np.tan(1 / x ** 2) * np.sin(20 * x)