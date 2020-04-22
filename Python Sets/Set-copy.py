# create a copy of new set using copy() method - shallow copy
set1 = {10, 20, 30, 1, 2, 3}
print(f'original set set1 is {set1}')
'''
Output:
original set set1 is {10, 20, 30, 1, 2, 3}
'''
new_set = set1.copy()  # shallow copy, any changes made to this set will not affect set1
print(f'copy of set1 is {new_set}')
'''
Output:
copy of set1 is {10, 20, 30, 1, 2, 3}
'''
new_set.add(4)  # add element to new_set using add() method
print(f'original set1 is {set1}')
print(f'new_set after adding element is {new_set}')
'''
Output:
original set1 is {1, 2, 3, 10, 20, 30}
new_set after adding element is {1, 2, 3, 20, 4, 10, 30}
'''

# copy set using = operator
set2 = set1  # any changes done to s1 or s2, changes would be seen on both the sets
print(f'set2 is {set2}')
print(f'set1 is {set1}')
'''
Output:
set2 is {1, 2, 3, 10, 20, 30}
set1 is {1, 2, 3, 10, 20, 30}
'''

set2.add(9)  # add item 9 to set2
print(f'set2 after adding is {set2}')
print(f'set1 after element added to set2 is {set1}')
'''
Output:
set2 after adding is {1, 2, 3, 9, 10, 20, 30}
set1 after element added to set2 is {1, 2, 3, 9, 10, 20, 30}
'''

set1.add(8)  # add item 8 to set1
print(f'set1 after adding is {set1}')
print(f'set2 after element added to set1 is {set2} ')
'''
Output:
set1 after adding is {1, 2, 3, 8, 9, 10, 20, 30}
set2 after element added to set1 is {1, 2, 3, 8, 9, 10, 20, 30}
'''