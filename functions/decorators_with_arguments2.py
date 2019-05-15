# decorators
# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

import datetime


def time_it(repeats=100):
    def inner_function(func):
        t1 = datetime.datetime.now()

        def func_wrapper(*args, **kwargs):
            for i in range(repeats-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)

        t2 = datetime.datetime.now()

        print(f'Execution time of {repeats} repeats', (t2 - t1).microseconds, 'ms')
        return func_wrapper
    return inner_function


if __name__ == '__main__':
    import numpy as np
    import random

    N = 10 ** 4

    array = [random.random() for i in range(N)]
    np_array = np.array(array)


    @time_it(200)
    def python_max(ar):
        return max(ar)


    @time_it(200)
    def numpy_max(ar):
        return np.max(ar)


    print(python_max(array))
    print(numpy_max(np_array))
