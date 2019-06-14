
class Fruit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} is a fruit'.format(self.name)


class Berry(Fruit):
    def __init__(self, name):
        Fruit.__init__(self, name)

    def __str__(self):
        return '{} has many seed'.format(self.name)


class Drupe(Fruit):
    def __init__(self, name):
        Fruit.__init__(self, name)

    def __str__(self):
        return '{} has one seed'.format(self.name)


if __name__ == '__main__':
    raspberry = Berry('Raspberry')
    print(raspberry)
    peach = Drupe('Peach')
    print(peach)
    peach2 = Fruit('Peach')
    print(peach2)
