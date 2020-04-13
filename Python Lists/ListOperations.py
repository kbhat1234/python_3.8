from filecmp import cmp

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l3 = [10]
# repetition (*) python operation
print(f'l1 * {2} is {l1 * 2}')
'''
l1 * 2 is [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
'''
# print(f'l1 * l2 is {l1 * l2}') -> this is not possible
'''
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Lists/ListOperations.py", line 6, in <module>
    print(f'l1 * l2 is {l1 * l2}')
TypeError: can't multiply sequence by non-int of type 'list'
'''

# concatenation (+) python operation
print(f'l1+l2 is {l1 + l2}')
'''
Output:
l1+l2 is [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
print(f'l1+l2+l3 is {l1 + l2 + l3}')
'''
Output:
l1+l2+l3 is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

# membership (in or not in) python operation
if 3 in l1:
    print('element present in l1')
else:
    print('element not present in l1')
'''
Output:
element present in l1
'''

if -3 not in l1:
    print('element not present in l1')
else:
    print('element present in l1')
'''
Output:
element not present in l1
'''

print(6 in l1)
'''
Output:
False
'''
print(7 in l2)
'''
Output:
True
'''
print(9 in l3)
'''
Output:
False
'''

# iteration operations - for loop
for i in l1:
    print(i, end=' ') # end=' ' gives a space after each number print
print("\n")
'''
Output:
1
2
3
4
'''

# length of list using len() method
print(f'length of l1 is {len(l1)}')
'''
Output:
length of l1 is 5
'''
print(f'length of l2 is {len(l2)}')
'''
Output:
length of l2 is 4
'''
print(f'length of l3 is {len(l3)}')
'''
Output:
length of l3 is 1
'''
print(f'length of len(l1*2) is {len(l1*2)}')
'''
Output:
length of len(l1*2) is 10
'''
print(f'length of len(l1+l2) is {len(l1+l2)}')
'''
Output:
length of len(l1+l2) is 9
'''