# iterating over a list using for loop
l1 = [20, 10, 2, 4, 6]
for i in l1:
    print(i, end=' ')
print('\nend of for loop - list')
'''
Output:
20 10 2 4 6
end of for loop - list
'''

# iterating over a tuple using for loop
t1 = (2, 3, 4, 1, 6)
for i in t1:
    print(i, end=' ')
print('\nend of for loop - tuple')
'''
Output:
2 3 4 1 6
end of for loop - tuple
'''

# iterating over a set using for loop
s1 = {9, 9, 3, 2, 1}
for i in s1:
    print(i, end=' ')
print('\nend of for loop - set')
'''
Output:
9 2 3 1
end of for loop - set
'''

# iterating over a dictionary using for loop
d1 = {1: 'fruits', 2: 'vegetables', 3: 'groceries', 4: 'medicines'}
print('\nprinting the dictionary keys')
for i in d1.keys():
    print(i, end=' ')
print('\nend of for loop - dictionary keys')
'''
Output:
printing the dictionary keys
1 2 3 4
end of for loop dictionary keys
'''

print('\nprinting the dictionary values')
for i in d1.values():
    print(i, end=' ')
print('\nend of for loop - dictionary values')
'''
Output:
fruits vegetables groceries medicines
end of for loop - dictionary values
'''

# iterating over a string using for loop
str1 = 'welcome to python programming'
for i in str1:
    print(i, end=' ')
print('\nend of for loop - string')
'''
Output:
w e l c o m e t o p y t h o n p r o g r a m m i n g
end of for loop string
'''
'''
adding some contents
'''