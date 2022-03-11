from functions import *

weight_coefficients = np.array([[1, 1],
                                [0.555555556, 0.888888889, 0.555555556],
                                [0.347854845, 0.652145155, 0.652145155, 0.347854845],
                                [0.236926885, 0.478628670, 0.568888889, 0.478628670, 0.236926885],
                                [0.171324492, 0.360761573, 0.467913935, 0.467913935, 0.360761573, 0.171324492]], dtype=object)
arguments = np.array([[-0.577350269, 0.577350269],
                      [-0.774596669, 0, 0.774596669],
                      [-0.861136312, -0.339981044, 0.339981044, 0.861136312],
                      [-0.906179846, -0.538469310, 0, 0.538469310, 0.906179846],
                      [-0.932469514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.932469514]], dtype=object)


def gaussian_integral(function, a, b, n):
    function_sum = 0
    weight_coefficient = weight_coefficients[n - 2]
    argument = arguments[n - 2]
    for point_ind in range(n):
        xi = (b + a) / 2 + argument[point_ind] * (b - a) / 2
        function_sum += weight_coefficient[point_ind] * function(xi)
    return (b - a) / 2 * function_sum


if __name__ == '__main__':
    a = 1.2155
    b = 3.214
    print("5 * (np.sin(x) - 3) + 1:")
    for point_ind in range(5):
        print("{0} points: {1}".format(point_ind + 2, gaussian_integral(function1, a, b, point_ind + 2)))
    print()

    print("1 / x * (np.cos(x) * x - 3) + np.log(x ** 2 + 2):")
    for point_ind in range(5):
        print("{0} points: {1}".format(point_ind + 2, gaussian_integral(function2, a, b, point_ind + 2)))
    print()

    print("3 ** (2 * x) + np.log(x ** 2):")
    for point_ind in range(5):
        print("{0} points: {1}".format(point_ind + 2, gaussian_integral(function3, a, b, point_ind + 2)))
    print()

    print("np.e ** 1 / x + np.tan(1 / x ** 2) * np.sin(20 * x):")
    for point_ind in range(5):
        print("{0} points: {1}".format(point_ind + 2, gaussian_integral(function4, a, b, point_ind + 2)))
