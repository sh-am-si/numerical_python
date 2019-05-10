# decorators
# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

import datetime


def time_it(func):
    t1 = datetime.datetime.now()

    def func_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    t2 = datetime.datetime.now()

    print((t2 - t1).microseconds, 'ms')
    return func_wrapper


if __name__ == '__main__':
    import numpy as np
    import random

    N = 10 ** 7

    array = [random.random() for i in range(N)]
    np_array = np.array(array)


    @time_it
    def python_max(ar):
        return max(ar)


    @time_it
    def numpy_max(ar):
        return np.max(ar)


    print(python_max(array))
    print(numpy_max(np_array))

    # exactly the same code
    print('and once again')

    python_max = time_it(python_max)
    numpy_max = time_it(numpy_max)

    print(python_max(array))
    print(numpy_max(np_array))



