def gen():
    yield from [1, 3, 6, 9, 12]


g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
