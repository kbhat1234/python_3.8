# insert(i, x) - will insert an element to the specified position
list = ['apple', 'orange', 'bannana', 'pineapple']
for i in list:
    print(i, end=' ')
'''
Output:
apple orange bannana pineapple
'''

list.insert(2, 'mango')
print(f'\nlist after inserting')
for i in list:
    print(i, end=' ')
'''
Output:
list after inserting
apple orange mango bannana pineapple
'''

print(f'\nupdated list after insertion is {list}')
'''
Output:
updated list after insertion is ['apple', 'orange', 'mango', 'bannana', 'pineapple']
'''

l = ['1', '2', '3']
for i in l:
    print(i, end=' ')
'''
Output:
1 2 3
'''

l.insert(3, '4')
print('\nlist after insertion ')
for i in l:
    print(i, end=' ')
'''
Output:
list after insertion 
1 2 3 4
'''
print(f'\nupadated list is {l}')
'''
Output:
upadated list is ['1', '2', '3', '4']
'''

# inserting a list as an element to the existing list
l.insert(2, ['3', '4', '5', '6'])
print('after inserting')
for i in l:
    print(i, end=' ')
print(f'\nupdated list is {l}')
'''
Output:
after inserting
1 2 ['3', '4', '5', '6'] 3 4 
updated list is ['1', '2', ['3', '4', '5', '6'], '3', '4']
'''

# inserting a tuple as an element to the existing list
l.insert(2, ('3', '4', '5', '6'))
print('after inserting ')
for i in l:
    print(i, end= ' ')
print(f'\nupdated list is {l}')
'''
Output:
after inserting 
1 2 ('3', '4', '5', '6') ['3', '4', '5', '6'] 3 4 
updated list is ['1', '2', ('3', '4', '5', '6'), ['3', '4', '5', '6'], '3', '4']
'''

# inserting a set as an element to the existing list
l.insert(4, {'1', '2', '3', '4'})
print('after inserting ')
for i in l:
    print(i, end=' ')
print(f'\nupdated list is {l}')
'''
Output:
after inserting 
1 2 ('3', '4', '5', '6') ['3', '4', '5', '6'] {'4', '3', '1', '2'} 3 4 
updated list is ['1', '2', ('3', '4', '5', '6'), ['3', '4', '5', '6'], {'4', '3', '1', '2'}, '3', '4']
'''

print(l[0])
print(l[2][2])
print(l[3][1])
print(l[4])
