import numbers

import matplotlib.pylab as plt
import numpy as np


class Polynomial:

    def __init__(self, iterable):
        assert all(isinstance(item, numbers.Number) for item in iterable)
        self.__coef = iterable

    def __len__(self):
        '''

        :return: int the order of polynomial
        '''
        pass

    def __add__(self, other):
        '''
        :param other: Polynomial or numerical values
        :return: sum of two polynomials
        '''
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, t):
        '''
        p(x) = a_n x^n + a_{n-1} x^{n-1} + ... + a_1 x + a_0

        p(x) = (...( a_n x + a_{n-1})x + ... + a_1 ) x + a_0

        :param t: numerical values of and array of it
        :return: value polynomial
        '''

        if isinstance(t, numbers.Number):
            val = self.__coef[0]
            for ind in range(1, len(self.__coef)):
                val *= t
                val += self.__coef[ind]

        return val

    def __getitem__(self, item):
        '''
        returns the polynomail derivative
        e.g. 0  ->  polynomial
             1  ->  first order derivative
             2  ->  second order derivative
             etc
        :param item: int >= 0
        :return:    Polynomail
        '''
        pass

    def integral(self, start, finish):
        pass

    def __str__(self):
        st = '$' + ('' if self.coef[0] > 0 else '-') + (str(abs(self.coef[0])) if abs(self.coef[0]) != 1 else '') + 'x^{}'.format(len(self.coef) - 1)
        for i in range(1, len(self.coef)):
            st += ('+' if self.coef[i] > 0 else '-')
            if self.coef[i] != 0:
                if abs(self.coef[i]) != 1:
                    st += str(abs(self.coef[i]))

                if i < len(self.coef) - 1 :
                    if i < len(self.coef) - 2 :
                        st += 'x^{}'.format(len(self.coef) - i - 1)
                    else:
                        st += 'x'
        st += '$'
        return st

    coef = property(fget=lambda self: self.__coef)


if __name__ == '__main__':
    coef = [1, -6, 11, -6]
    p1 = Polynomial(coef)
    p2 = np.poly1d(coef)

    arg = np.linspace(-1, 5)
    plt.plot(arg, [p1(_arg) for _arg in arg], label=str(p1))
    plt.plot(arg, p2(arg), ls=':', label=str(p2))
    plt.legend()
    plt.show()
