# decorators
# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

import datetime


def time_it(func):

    def func_wrapper(*args, **kwargs):
        t1 = datetime.datetime.now()
        result = func(*args, **kwargs)
        t2 = datetime.datetime.now()
        print((t2 - t1).microseconds, 'ms')

        return result

    return func_wrapper


if __name__ == '__main__':
    import numpy as np
    import random

    N = 10 ** 7

    array = [random.random() for i in range(N)]
    np_array = np.array(array)

    @time_it
    def python_sum(ar):
        return sum(ar)


    @time_it
    def numpy_sum(ar):
        return np.sum(ar)

    print('Python sum', python_sum(array))
    print('Numpy sum', numpy_sum(np_array))

    # exactly the same code
    print('and once again')

    def python_sum2(ar):
        return sum(ar)

    def numpy_sum2(ar):
        return np.sum(ar)

    python_sum3 = time_it(python_sum2)
    numpy_sum3 = time_it(numpy_sum2)

    print('Python sum', python_sum3(array))
    print('Numpy sum', numpy_sum3(np_array))



