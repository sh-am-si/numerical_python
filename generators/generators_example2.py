'''
tuple, generators and range comparison
'''

_range = range(8)
_tuple1 = (0, 1, 2, 3, 4, 5, 6, 7)
_tuple2 = tuple(i for i in range(8))
gen1 = (i for i in range(8))

print('range example', _range)
print('tuple example 1', _tuple1)
print('tuple example 2', _tuple2)
print('generator example, first go', gen1)
print('generator example, second go', [i for i in gen1])
print('generator example, third go', [i for i in gen1])
print('generator example, forth go', gen1)


def gen2(n=8):
    i = 0
    while i < n:
        yield i
        i += 1


class Gen3:

    def __init__(self, max=8):
        self.max = max

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        if self.n >= self.max - 1:
            raise StopIteration
        self.n += 1
        return self.n


gen1 = (i for i in range(8))
_gen2 = gen2(8)
gen3 = Gen3(8)

print([i for i in gen1])
print([i for i in _gen2])
print([i for i in gen3])

print([i for i in gen1])
print([i for i in _gen2])
print([i for i in gen3])
print([i for i in gen3])
