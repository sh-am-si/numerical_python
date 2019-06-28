
def gen3():
    print('first iteration')
    yield 1

    print('second iteration')
    yield 2

    print('third iteration')
    yield 3

print(sum(gen3()))

g3 = gen3()
a = next(g3)
b = next(g3)
c = next(g3)
print(a,b,c)
# next(g3)