
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        return '{} has {} cal per 100 g.'.format(self.name, self.calories)


if __name__ == '__main__':
    apple = Fruit('Apple', 52)
    apricot = Fruit('Apricot', 48)
    avocado = Fruit('Avocado', 160)

    fruit_list = [apple, apricot, avocado]

    for fruit in fruit_list:
        print(fruit)
