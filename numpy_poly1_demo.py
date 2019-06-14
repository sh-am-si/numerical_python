'''
examples of Numpy Poly1 uses

https://docs.scipy.org/doc/numpy/reference/generated/numpy.poly1d.html

This is a vary basic implementation of polynomials in Numpy

More advance tool is here
https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.polynomials.html
'''

import matplotlib.pylab as plt
import numpy as np

p = np.poly1d([1, -3, 2])  # p(x) = x^2 - 3x + 2
p2 = np.poly1d([1, -3])  # p2(x) = x - 3


def f(x):
    '''
    $x^3 - 6x^2 + 11x - 6$
    '''
    return x ** 3 - 6 * x ** 2 + 11 * x - 6


arg = np.linspace(-1, 5)
plt.plot(arg, p(arg), label=str(p))
plt.plot(arg, (p * p2)(arg), ls='-', label=str(p * p2))
plt.plot(arg, f(arg), ls='--', label=f.__doc__)
plt.axhline(y=0, c='k', lw=0.5)
plt.axvline(x=0, c='k', lw=0.5)
plt.legend()
plt.show()
