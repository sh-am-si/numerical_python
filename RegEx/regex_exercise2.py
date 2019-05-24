'''
useful video
https://www.youtube.com/watch?v=abrcJ9MpF60

more exercises
https://pycon2016.regex.training/exercises
'''

# Task 1 water tank: CISxxxx
# Task 2 pastry: xxxTE
# Task 3 temporary: xxAxSxExx
# Task 4 Find all words that have a consecutive repeated letter two times with only one other letter between them
# e.g. voodoo, assessed
# Task 5 Find all words that consist of the same letters repeated two times
# e.g. mama, tutu

import re


def trim(string):
    ltrim = re.compile('^\W*')
    rtrim = re.compile('\W*$')
    return rtrim.sub('', ltrim.sub('', string))


dictionary = []
with open('dictionary.txt', 'r+') as f:
    for word in f.readlines():
        dictionary.append(trim(word))

print(dictionary)

print(len(dictionary))

for word in dictionary:
    if re.search(r'(.)\1\w\1\1', word):
        print('task4: ', word)

    if re.search(r'^(\w+)\1$', word):
        print('task5: ', word)


