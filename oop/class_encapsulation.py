
class Fruit:
    def __init__(self, name, calories):
        self.__name = name
        self.calories = calories

    def __str__(self):
        return '{} has {} cal per 100 g.'.format(self.__name, self.calories)

if __name__ == '__main__':
    apple = Fruit('Apple', 52)
    print(apple)
    apple.calories = 56
    print(apple)
    apple.__name = 'Pear'  # you can't access 'private' methods or field directly
    print(apple)
    # some advanced information
    apple._Fruit__name = 'Pear' # but in python there are no really 'private' methods neither fields
    print(apple)                # they are rather hidden and if you really need to get access to them out of class
                                # use _ClassName prefix

