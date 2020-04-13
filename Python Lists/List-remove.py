l = [20, 23, 36, 99, 56, 44]
print('printing original list')
for i in l:
    print(i, end=' ')
l.remove(36)
print('\nprinting the list after removal')
for i in l:
    print(i, end=' ')
print("\n")
'''
Output:
printing original list
20 23 36 99 56 44 
printing the list after removal
20 23 99 56 44 
'''

l2 = [10, 20, 30]
l3 = [10, 20, 30, 40]
print(l2)
print(l3)

if l2 == l3:
    print('\nboth lists are equal')
else:
    print('\nlists are not equal')

# removing an element from the list
list = [10, 8, 3, 4, 5, 6, 1, 2, 9]
print(f'\noriginal list is {list}')

for i in list:
    print(i, end=' ')
list.remove(5)

print('\nafter removing')
for i in list:
    print(i, end=' ')
'''
Output:
original list is [10, 8, 3, 4, 5, 6, 1, 2, 9]
10 8 3 4 5 6 1 2 9 
after removing
10 8 3 4 6 1 2 9
'''

# removing element from list when we have duplicate elements in the list
list1 = [10, 13, 4, 13, 19, 34, 22]
print(f'\noriginal list is {list1}')

for i in list1:
    print(i, end=' ')
list1.remove(13)

print(f'\nAfter removing')
for i in list1:
    print(i, end=' ')
'''
Output:
original list is [10, 13, 4, 13, 19, 34, 22]
10 13 4 13 19 34 22 
After removing
10 4 13 19 34 22
'''

# removing an element from the list when element is not in list
list2 = [10, 20, 30, 40, 60]
print(f'\noriginal list is {list2}')

for i in list2:
    print(i, end=' ')
list2.remove(50)
print('\nAfter removing')
for i in list2:
    print(i, end=' ')
'''
Output:
original list is [10, 20, 30, 40, 60]
10 20 30 40 60 
'''