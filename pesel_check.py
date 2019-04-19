"""
pesel consisits of 11 numbers abcdefghjN

where the last 11-th number is verifier of the number

N = (9*a + 7*b + 3*c +1*d +
    9*e + 7*f + 3*g +1*h +
    9*i + 7*j ) mod 10

"""

pesel1 = '44051401358'
pesel2 = '44051401359'


def check_pesel(st):

    assert isinstance(st, str)
    assert len(st) == 11

    pass


if __name__ == '__main__':
    print(check_pesel(pesel1))
    print(check_pesel(pesel2))
