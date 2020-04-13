import random

# return a random element from a list
list = [20, 30, 40, 50]
print(f'random element from list is {random.choice(list)}')
'''
Output:
random element from list is 40
'''
# return a random element from a tuple
tuple = (2, 5, 3, 7, 6)
print(f'random element from tuple is {random.choice(tuple)}')
'''
Output:
random element from tuple is 2
'''

# return a random element from a string str
str1 = 'welcome'
print(f'random element from string is {random.choice(str1)}')
'''
Output:
random element from string is m
'''

# return a random number from a range
for i in range(2):
    print(random.choice(list))
'''
Output:
20
20
'''
print('\n')
print(random.choice(['apple', 'orange', 'pineapple', 'jackfruit', 'mango']))
'''
Output:
orange
'''
print(random.choice((2, 1, 4, 3, 5, 6, 5)))
'''
Output:
4
'''
print(random.choice('abcdef'))
'''
Output:
b
'''
print(random.choice(list))
'''
Output:
20
'''
print(random.choice(tuple))
'''
Output:
5
'''
print(random.choice(str1))
'''
Output:
m
'''
