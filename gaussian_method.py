import math

import numpy as np

m_i = np.array([[1, 1],
                [0.555555556, 0.888888889, 0.555555556],
                [0.347854845, 0.652145155, 0.652145155, 0.347854845],
                [0.236926885, 0.478628670, 0.568888889, 0.478628670, 0.236926885],
                [0.171324492, 0.360761573, 0.467913935, 0.467913935, 0.360761573, 0.171324492]], dtype=object)
x_i = np.array([[-0.577350269, 0.577350269],
                [-0.774596669, 0, 0.774596669],
                [-0.861136312, -0.339981044, 0.339981044, 0.861136312],
                [-0.906179846, -0.538469310, 0, 0.538469310, 0.906179846],
                [-0.932469514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.932469514]], dtype=object)


def function(x):
    return 5 * (np.sin(x) - 3) + 1


def gaussian_integral(a, b, n):
    function_sum = 0
    m = m_i[n - 2]
    x = x_i[n - 2]
    for point_ind in range(n):
        xi = (b + a) / 2 + x[point_ind] * (b - a) / 2
        function_sum += m[point_ind] * function(xi)
    return (b - a) / 2 * function_sum


if __name__ == '__main__':
    a = 0
    b = math.pi / 6
    for point_ind in range(5):
        print("{0} point: {1}".format(point_ind + 2, gaussian_integral(a, b, point_ind + 2)))