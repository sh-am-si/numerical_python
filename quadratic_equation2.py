"""
:author: VB
:created: 17/1/2019
Introduction to Python
Lecture 3, Functions and comprehensions

Function samples 2
"""

import numpy as np
import numbers


def quadratic_formula(*args, **kwargs):
    """

    solution of the equation a*x^2 + b*x + c = 0

    :return:  x1,x2 : a*x_i^2 + b*x_i + c = 0 for i=1,2
    """

    if len(args) > 0:
        print(args)
        assert len(args) == 3

        assert isinstance(args[0], numbers.Number), 'type of the first parameter  is not numerical but {}'.format(
            type(args[0]))
        assert isinstance(args[1], numbers.Number), 'type of the second parameter  is not numerical but {}'.format(
            type(args[1]))
        assert isinstance(args[2], numbers.Number), 'type of the third parameter  is not numerical but {}'.format(
            type(args[2]))
        a, b, c = args
    elif all(kw in kwargs.keys() for kw in ['a', 'b', 'c']):
        a = kwargs['a']
        b = kwargs['b']
        c = kwargs['c']
    elif 'coef' in kwargs.keys():
        a, b, c = kwargs['coef']
    else:
        raise ValueError('Wrong parameter input args={}, kwargs={}'.format(args,kwargs))

    D = b ** 2 - 4 * a * c
    if D >= 0:
        return 0.5 * (-b + np.sqrt(D)) / a, \
               0.5 * (-b - np.sqrt(D)) / a
    else:
        return 0.5 * (-b + 1j * np.sqrt(-D)) / a, \
               0.5 * (-b - 1j * np.sqrt(-D)) / a


if __name__ == '__main__':
    # before using a function let's have a look on its docstrinf
    print('function documentation: ', quadratic_formula.__doc__)

    x1, x2 = quadratic_formula(1, 2, -3)

    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 2, - 3, x1, x2))

    x1, x2 = quadratic_formula(a=1, b=3, c=2)
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 3, 2, x1, x2))

    x1, x2 = quadratic_formula(b=3, a=1, c=2)
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 3, 2, x1, x2))

    coef = [1, 2, -3]
    x1, x2 = quadratic_formula(coef=coef)
    print('default declaration')
    print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(*coef, x1, x2))

    # x1, x2 = quadratic_formula(a=1)
    # print('equation {}x^2+{}x+{}=0 has roots x1={}, x2={}\n'.format(1, 3, 2, x1, x2))
