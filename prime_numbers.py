'''

'''
import datetime

counter = 1
num = 10000

t1 = datetime.datetime.now()
for i in range(3, num, 2):
    for j in range(3, i // 2, 2):
        if i % j == 0:
            break
    else:
        print(i, end=' ')
        counter += 1
t2 = datetime.datetime.now()

print(counter, (t2-t1).microseconds)
