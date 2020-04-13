import random

# random.choices(seq, weights=None, cum_weights=None, k=1) using list

list = [10, 20, 30, 25, 21, 67]
print(random.choices(list))
'''
Output:
[21]
'''

# using tuple
tuple = (20, 12, 13, 45, 12)
print(random.choices(tuple))
'''
Output:
[13]
'''

# using string
str1 = 'welcome'
print(random.choices(str1))
'''
Output:
['e']
'''

# using the range
for i in range(5):
    print(random.choices(list), end=' ')
'''
Output:
[30]
[25]
[20]
[30]
[10]
'''

for i in range(5):
    print(random.choices(tuple), end=' ')
print('\n')

for i in range(len(str1)):
    print(random.choices(str1), end=' ')
print('\n')


print(random.choices([29, 30, 40, 50]))
print(random.choices((20, 12, 34, 56, 34)))
print(random.choices('welcome'))

