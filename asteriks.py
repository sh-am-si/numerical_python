'''
:author: Włodek
:created: 16/12/2019
Introduction to Python
Lecture 3, Functions and comprehensions

Asteriks
'''

lst = [1, 2, 3]
print('calling without asteriks', lst)
print('calling with asteriks', *lst)


def my_sum(a, b, c):
    return a + b + c

lst = [1, 2, 3]
print(my_sum(*lst))

dic = {'a': 1, 'b': 2, 'c': 3}
print(my_sum(**dic))

lst = [1, 2, 3, 4]
print(my_sum(*lst)) # error

dic = {'a': 10, 'b': 20, 'c': 30, 'd': 4}
print(my_sum(**dic))  # error


