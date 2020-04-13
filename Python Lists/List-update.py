# updating the list using slice operator and assignment operator - list[2] = 20
list1 = [28, 56, 22, 12, 10, 78]
list2 = ['apple', 'orange', 'banana', 'pineapple']
list3 = [1, 'karthik', 'raaga', 663673.89]
list4 = []

# adding item to list using index position
print(f'original list1 -> {list1}')
'''
Output:
original list1 -> [28, 56, 22, 12, 10, 78]
'''
list1[3] = 29
print(f'updated list1 is {list1}')
'''
Output:
updated list1 is [28, 56, 22, 29, 10, 78]
'''
list1[-4] = 11
print(f'updated list1 is {list1}')
'''
Output:
updated list1 is [28, 56, 11, 29, 10, 78]
'''
list1[1:3] = [14, 13]
print(f'updated list1 is {list1}')
'''
Output:
updated list1 is [28, 14, 13, 29, 10, 78]
'''
list1[:] = [2, 3, 4]
print(f'updated list1 is {list1}')
'''
Output:
updated list1 is [2, 3, 4]
'''
list1[0:] = [21, 31]
print(f'updated list1 is {list1}')
'''
Output:
updated list4 is [21, 31]
'''

list4[1:3] = ['maths', 'physics']
print(f'updated list4 is {list4}')
'''
Output:
updated list4 is ['maths', 'physics']
'''
list4[0:2] = ['compiler design', 'java programming']
print(f'updated list4 is {list4}')
'''
Output:
updated list4 is ['compiler design', 'java programming']
'''
list4[0] = 'chemistry'
print(f'updated list4 is {list4}')
'''
Output:
updated list4 is ['chemistry', 'java programming']
'''
list4[3:6] = ['computer science', 'operating system', 'logic design']
print(f'updated list4 is {list4}')
'''
Output:
updated list4 is ['chemistry', 'java programming', 'computer science', 'operating system', 'logic design']
'''

# deleting elements in the list using del keyword

del list4[4]
print(f'list4 after deletion is {list4}')
'''
Output:
list4 after deletion is ['chemistry', 'java programming', 'computer science', 'operating system']
'''
del list4[:3]
print(f'list4 after deletion is {list4}')
'''
Output:
list4 after deletion is ['operating system']
'''
del list4[:]
print(f'list4 after deletion is {list4}')
'''
list4 after deletion is []
'''
