# pop(index) list method removes an element from the given index.
list = [10, 20, 12, 11, 9, 8, 3]
print(f'orginal list is {list}')

for i in list:
    print(i, end=' ')
list.pop(3)  # at index 3 the value is 11 which is been poppped (removed) from the list
print(f'\nAfter poping ')
for i in list:
    print(i, end=' ')
'''
Output:
orginal list is [10, 20, 12, 11, 9, 8, 3]
10 20 12 11 9 8 3 
After poping 
10 20 12 9 8 3 
'''

print(f'\nlist is {list}')
# poping element from list when no index is provided in pop()
list.pop()  # pop element without providing the index position, last index is popped
print('After poping')
for i in list:
    print(i, end=' ')
'''
Output:
list is [10, 20, 12, 9, 8, 3]
After poping
10 20 12 9 8 
'''

# popping element from list with negative index
print(f'\nlist is {list}')
list.pop(-2)  # -2 index will pop element 9 from the list
print('After poping ')
for i in list:
    print(i, end=' ')
'''
Output:
list is [10, 20, 12, 9, 8]
After poping 
10 20 12 8 
'''

# popping element from list when index number is invalid
# list.pop(8)
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Lists/List-pop.py", line 46, in <module>
    list.pop(8)
IndexError: pop index out of range
'''
print('After poping ')
for i in list:
    print(i, end=' ')
