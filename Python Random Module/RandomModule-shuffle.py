import random

# shuffle using the list
list1 = [10, 29, 11, 8, 9, 2]
print(f'original list is {list1}')
random.shuffle(list1)
print(f'shuffled list is {list1}')
'''
Output:
[9, 8, 11, 2, 10, 29]
'''

# shuffle using the tuple - using list(seq) built in function
tuple = (3, 1, 9, 6, 4)
print(f'original tuple is {tuple}')
t = list(tuple)  # convert tuple to list
random.shuffle(t)
print(f'shuffled list after list(tuple) is {t}')
'''
Output:
[3, 6, 9, 4, 1]
'''

# shuffle using the string - using list(seq) built in function
str1 = 'welcome'
s = list(str1)  # convert string to list
random.shuffle(s)
print(f'shuffled list after list(str1) is {s}')
'''
Output:
['e', 'e', 'm', 'c', 'o', 'l', 'w']
'''

# shuffle usig the dictionary - using list(seq) built in function
dic1 = {1: 'a', 2: 'b', 3: 'c'}
print(f'original dictionary is {dic1}')
dk = list(dic1.keys())  # convert dictionary keys to list
dv = list(dic1.values())  # convert dictionary values to list

random.shuffle(dk)
print(f'shuffled list after list(dic1.keys()) is {dk}')
'''
Output:
[1, 2, 3]
'''

random.shuffle(dv)
print(f'shuffled list after list(dic1.values()) is {dv}')

