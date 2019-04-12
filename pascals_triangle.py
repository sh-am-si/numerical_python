'''
Introduction to python
Lecture 2: Sequences and Comprehensions

Pascal's triangle
'''

triangle = [[1]]

num = 100

for i in range(num):
    last = triangle[-1]
    triangle.append([1 if i == 0 else last[i - 1] + last[i] for i in range(len(last))] + [1])

for i, tri in enumerate(triangle):
    print(i, ':', tri)
