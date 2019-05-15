"""
:author: VB
:created: 17/1/2019
Introduction to Python
Lecture 3, Functions and comprehensions

Function samples
"""

import numpy as np
import numbers


def quadratic_formula(a=1, b=2, c=-3):
    """

    solution of the equation a*x^2 + b*x + c = 0

    :param a: coefficient by the term of second degree
    :param b: coefficient by the term of first degree
    :param c: free standing coefficient
    :return:  x1,x2 : a*x_i^2 + b*x_i + c = 0 for i=1,2
    """

    assert isinstance(a, numbers.Number), 'parameter a type is not numerical but {}'.format(type(a))
    assert isinstance(b, numbers.Number), 'parameter b type is not numerical but {}'.format(type(b))
    assert isinstance(c, numbers.Number), 'parameter c type is not numerical but {}'.format(type(c))

    D = b ** 2 - 4 * a * c
    if D >= 0:
        return 0.5 * (-b + np.sqrt(D)) / a, \
               0.5 * (-b - np.sqrt(D)) / a
    else:
        return 0.5 * (-b + 1j * np.sqrt(-D)) / a, \
               0.5 * (-b - 1j * np.sqrt(-D)) / a


if __name__ == '__main__':
    a = 1
    b = -3
    c = 2
    # before using a function let's have a look on its docstrinf
    print('function documentation: ', quadratic_formula.__doc__)

    x1, x2 = quadratic_formula(a, b, c)

    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(a, b, c, x1, x2))

    x1, x2 = quadratic_formula(a=1, b=3, c=2)
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 3, 2, x1, x2))

    x1, x2 = quadratic_formula(b=3, a=1, c=2)
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 3, 2, x1, x2))

    x1, x2 = quadratic_formula()
    print('default declaration')
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 2, -3, x1, x2))

    x1, x2 = quadratic_formula(c=3)
    print('default declaration with partially assigned parameters')
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 2, 3, x1, x2))

    # x1, x2 = quadratic_formula(a='1')
    # print('wrong function call')
    # print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format('1', 2, -3, x1, x2))

    # x1, x2 = quadratic_formula(b='2')
    # print('wrong function call')
    # print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format('1', 2, -3, x1, x2))
