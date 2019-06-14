
class UniqueList(list):


    def append(self, object) -> None:
        if object not in self:
            super().append(object)

    def extend(self, iterable) -> None:
        for item in iterable:
            self.append(item)

    def __add__(self, other):
        self.extend(other)
        return self

    def __mul__(self, other):
        return self

    def __iadd__(self, other):
        self = self + other
        return self

if __name__ == '__main__':
    ul = UniqueList()
    print(ul)
    ul.append(1)
    ul.append(2)
    ul.append(1)
    print(ul)
    ul.extend([1, 2, 3, 4, 5])
    print(ul)
    ul = ul + [4, 5, 6, 7, 8]
    print(ul)
    ul += [7, 8, 9, 10]
    print(ul)