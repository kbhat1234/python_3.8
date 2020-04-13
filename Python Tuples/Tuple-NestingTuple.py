# nested tuple within the list
list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(f'original list is {list1}')
'''
Output:
original list is [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
'''

print('printing the list')
for i in list1:
    print(i, end=' ')
'''
Output:
(1, 2, 3) (4, 5, 6) (7, 8, 9)
'''

list1[0] = (2, 3, 4)  # updating the list for particular index
print(f'\nlist modified is {list1}')
'''
Output:
list modified is [(2, 3, 4), (4, 5, 6), (7, 8, 9)]
'''

print('\nprinting the list after modification')
for i in list1:
    print(i, end=' ')
'''
Output:
printing the list after modification
(2, 3, 4) (4, 5, 6) (7, 8, 9)
'''

# nested list within the tuple
tuple1 = ([10, 20, 30], [40, 50, 60], [70, 80, 90])
print(f'\noriginal tuple is {tuple1}')
print('printing the tuple')
for i in tuple1:
    print(i, end=' ')

'''
tuple1[0] = [11, 21, 31]
print('f\ntuple modified is {tuple1}')
print('\nprinting the tuple after modification')
for i in tuple1:
    print(i, end=' ')
'''

# nesting of tuples
tuple1 = (20, 30, 40, 10)
tuple2 = ('java', 'python', 'c', 'javascript')
tuple3 = (tuple1, tuple2)  # ((20, 30, 40, 10), ('java', 'python', 'c', 'javascript'))
print(tuple3)
'''
Output:
((20, 30, 40, 10), ('java', 'python', 'c', 'javascript'))
'''