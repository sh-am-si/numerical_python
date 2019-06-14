
class Fruit:
    def __init__(self, name, calories, type='Berry'):
        self.__name = name
        self.calories = calories
        self.type = type

    def __str__(self):
        return '{} has {} cal per 100 g.'.format(self.__name, self.calories)


class Berry(Fruit):
    def __init__(self, name, calories):
        Fruit.__init__(self, name, calories, type='Berry')


class Pomes(Fruit):
    def __init__(self, name, calories):
        Fruit.__init__(self, name, calories, type='Pomes')


if __name__ == '__main__':
    apple = Pomes('Apple', 52)
    print(apple)
    raspberry = Berry('Raspberry', 64)
    print(raspberry)
    print(issubclass(Pomes, Fruit))
    print(issubclass(Pomes, Berry))
    print(issubclass(Fruit, Berry))
    import numbers
    print(issubclass(complex, numbers.Number))
    print(issubclass(numbers.Complex, numbers.Number))
    print(issubclass(numbers.Real, numbers.Complex))
    print(issubclass(float, complex))
