# decorators

def list_power(lst):
    # enclosing function
    power = 2
    print('enclosing function scope', dir())

    def lst_iteration():
        # nested function
        print('nested function scope', dir())
        nonlocal power
        power += 1
        print([item ** power for item in lst])

    lst_iteration()


if __name__ == '__main__':
    print(dir())
    list_power([1, 2, 3])
