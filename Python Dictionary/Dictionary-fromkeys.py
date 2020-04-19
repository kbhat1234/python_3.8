# fromkeys() method creates new dictionary from the given sequence of elements with a value provided by the user
# sequence is a set
keys = {'apple', 'orange', 'pineapple', 'grapes', 'papaya', 'guava'}
print(type(keys))
'''
Output:
<class 'set'>
'''
value = 'fruits'  # value is a string
print(type(value))
'''
Output:
<class 'str'>
'''
fruits = dict.fromkeys(keys, value)
print(type(fruits))
'''
Output:
<class 'dict'>
'''
print(f'dictionary is {fruits}')
'''
Output:
dictionary is {'orange': 'fruits', 'papaya': 'fruits', 'grapes': 'fruits', 'pineapple': 'fruits', 'guava': 'fruits', 'apple': 'fruits'}
'''
print(type(fruits['pineapple']))
'''
Output:
<class 'str'>
'''

# sequence is string
str1 = 'welcome'
print(type(str1))
'''
Output:
<class 'str'>
'''
value = ['india']  # value is a list
print(type(value))
'''
Output:
<class 'list'>
'''
str2 = dict.fromkeys(str1, value)
print(type(str2))
'''
Output:
<class 'dict'>
'''
print(str2)
'''
Output:
{'w': 'india', 'e': 'india', 'l': 'india', 'c': 'india', 'o': 'india', 'm': 'india'}
'''
value.append('usa')
print(str2)
'''
Output:
{'w': ['india', 'usa'], 'e': ['india', 'usa'], 'l': ['india', 'usa'], 'c': ['india', 'usa'], 'o': ['india', 'usa'], 'm': ['india', 'usa']}
'''

# sequence as list
list = ['name', 'age', 'gender']
print(type(list))
'''
<class 'list'>
'''
value = 'employee'
l1 = dict.fromkeys(list, value)
print(type(l1))
'''
Output:
<class 'dict'>
'''
print(l1)
'''
Output:
{'name': 'employee', 'age': 'employee', 'gender': 'employee'}
'''
# value.append('a') -> cannot append string

# sequence as tuple
tup = ('sex', 'profession')
print(type(tup))
'''
Output:
<class 'tuple'>
'''
value = ('a', 'b')
t1 = dict.fromkeys(tup, value)
print(type(t1))
'''
Output:
<class 'dict'>
'''
print(t1)
'''
Output:
{'sex': 'a', 'profession': 'a'}
'''
# value.append('c') -> cannot append a tuple
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Dictionary/Dictionary-fromkeys.py", line 101, in <module>
    value.append('c')
AttributeError: 'tuple' object has no attribute 'append'
'''
