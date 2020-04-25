# frozenset() method - list, tuple, set, dictionary, string
f1 = frozenset([2, 3, 4, 8, 9])
print(f'type(f1) is {type(f1)}')
'''
Output:
type(f1) is <class 'frozenset'>
'''
for i in f1:
    print(i, end=' ')
print(f'\nf1 is {f1}')
'''
Output:
2 3 4 8 9 
f1 is frozenset({2, 3, 4, 8, 9})
'''
# f1.add(10)  # not possible to add, remove, or modify the frozenset
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-frozenset.py", line 16, in <module>
    f1.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
'''

# list passed to frozenset
list1 = [10, 30, 14, 5, 7, 9]
print(f'\ntype(list1) is {type(list1)}')
f2 = frozenset(list1)
print(f'f2 is {f2}')
print(f'type(f2) is {type(f2)}')
'''
Output:
type(list1) is <class 'list'>

f2 is frozenset({5, 7, 9, 10, 14, 30})
type(f2) is <class 'frozenset'>
'''
# f2.add(100)  # not possible to add, remove, or modify the frozenset

# tuple passed to frozenset
tup = (20, 29, 23, 9)
f3 = frozenset(tup)
print(f'\ntype(f3) is {type(f3)}')
print(f'f3 is {f3}')
'''
Output:
type(f3) is <class 'frozenset'>
f3 is frozenset({9, 20, 29, 23})
'''
# f3.add(10)  # not possible to add, remove, or modify the frozenset

# dictionary passed to frozenset
dic = {1: 'apple', 'orange': 2}
f4 = frozenset(dic)  # only keys will be stored.
print(f'\ntype(f4) is {type(f4)}')
print(f'f4 is {f4}')
'''
Output:
type(f4) is <class 'frozenset'>
f4 is frozenset({1, 'orange'})
'''
# f4.add({5: 'banana'})  # not possible to add, remove, or modify the frozenset
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Sets/Set-frozenset.py", line 62, in <module>
    f1.add({5: 'banana'})  # not possible to add, remove, or modifiy the frozenset
AttributeError: 'frozenset' object has no attribute 'add'
'''

# string passed to frozenset
str1 = 'welcome'
f5 = frozenset(str1)  # each character will be seperately stored
print(f'\ntype(f5) is {type(f5)}')
print(f'f5 is {f5}')
'''
Output:
type(f5) is <class 'frozenset'>
f5 is frozenset({'w', 'o', 'l', 'm', 'e', 'c'})
'''
# f5.add('b')  # not possible to add, remove, or modify the frozenset

# set passed to frozenset
set1 = {20, 30, 40, 50}
f6 = frozenset(set1)
print(f'\ntype(f6) is {type(f6)}')
print(f'f6 is {f6}')
'''
Output:
type(f6) is <class 'frozenset'>
f6 is frozenset({40, 50, 20, 30})
'''
# f6.add(10)  # not possible to add, remove, or modify the frozenset
