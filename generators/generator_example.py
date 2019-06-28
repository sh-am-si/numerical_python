gen = (i for i in range(10))

for i in gen:
    print(i, end=' ')
print()


def gen2(final):
    counter = 0
    while counter < final:
        yield counter
        counter += 1


for i in gen2(final=12):
    print(i, end=' ')
print()

gen = (i for i in range(10))
_range = range(10)

print('generator sum 1 :', sum(_range))
print('range sum 1 :', sum(gen))
print('generator sum 2 :', sum(_range))
print('range sum 2 :', sum(gen))
