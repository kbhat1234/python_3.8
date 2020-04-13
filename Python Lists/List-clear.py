# list.clear() will clear the elements of the list
list = [10, 20, 30, 40, 50]
print('\nprinting original list ')
for i in list:
    print(i, end=' ')
list.clear()
print('\nprinting list after clear ')
for i in list:
    print(i)
print(list)
'''
Output:
printing original list 
10 20 30 40 50 
printing list after clear 
[]
'''

# list is already empty
l = []
for i in l:
    print(i)
l.clear()
print('after clearing')
for i in l:
    print(i)
'''
Output:
after clearing
'''