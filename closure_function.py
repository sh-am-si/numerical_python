# decorators

def list_power(lst):
    # enclosing function
    power = 2
    print('enclosing function scope', dir())

    def lst_iteration():
        # nested function
        print('nested function scope', dir())
        return [item ** power for item in lst]

    return lst_iteration


if __name__ == '__main__':
    new_function = list_power([1, 2, 3])
    del list_power
    print(new_function())
