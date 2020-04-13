# max(list) - returns max element in the list
l1 = [10, 2, 4, 9, 5, 7]
m1 = max(l1)
print(f'max number in l1 is {m1}')
'''
Output:
max number in l1 is 10
'''

# min(list) - returns min element in the list
m2 = min(l1)
print(f'min number in l1 is {m2}')
'''
Output:
min number in l1 is 2
'''

# len(list) - calculates the length of the list
m3 = len(l1)
print(f'length of list l1 is {m3}')
'''
Output:
length of list l1 is 6
'''

# list(seq) - list(seq) method takes sequence types and converts them to list. this is used to convert given tuple to list
tuple = (10, 20, 30, 40, 50)
# tuple[0] = 99
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Lists/ListBuiltinFunctions.py", line 16, in <module>
    tuple[0] = 99
TypeError: 'tuple' object does not support item assignment
'''
print(f'tuple is {tuple}')
'''
Output:
(10, 20, 30, 40, 50)
'''
m4 = list(tuple)
print(f'list sequence elements is {m4}')
'''
Output:
list sequence elements is [10, 20, 30, 40, 50]
'''
m4[0] = 90
print(m4)
'''
[90, 20, 30, 40, 50]
'''