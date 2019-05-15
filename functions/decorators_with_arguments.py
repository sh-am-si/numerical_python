# decorators
# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

import datetime


def time_it(name):
    def named_function(func):
        t1 = datetime.datetime.now()

        def func_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        t2 = datetime.datetime.now()

        print(name, (t2 - t1).microseconds, 'ms')
        return func_wrapper
    return named_function


if __name__ == '__main__':
    import numpy as np
    import random

    N = 10 ** 5

    array = [random.random() for i in range(N)]
    np_array = np.array(array)


    @time_it('Python execution time')
    def python_max(ar):
        return max(ar)


    @time_it('Numpy execution time')
    def numpy_max(ar):
        return np.max(ar)


    print(python_max(array))
    print(numpy_max(np_array))
