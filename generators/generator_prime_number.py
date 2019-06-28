import numpy as np

def is_prime(number):
    if number == 2:
        return True
    else:
        for j in range(3, number//2 + 1, 2):
            if number % j == 0:
                return False
        return True


def prime_number_generator():
    yield 2
    number = 3
    while True:
        if is_prime(number):
            yield number
        number += 2


for i in prime_number_generator():
    print(i, end=' ')
    if i > 1000:
        break
