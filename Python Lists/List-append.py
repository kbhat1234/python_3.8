# append() method used to add elements/items in list - this will add element to end of list
list1 = [20, 30, 40, 11]
list2 = []
print(list1)
'''
Output:
[20, 30, 40, 11]
'''
list1.append(21)
print(list1)
'''
Output:
[20, 30, 40, 11, 21]
'''
list1.append(22)
print(list1)
'''
Output:
[20, 30, 40, 11, 21, 22]
'''

list2.append('karthik')
list2.append(23)
list2.append('ishani')
list2.append('kaustubh')
print(list2)
'''
Output:
['karthik', 23, 'ishani', 'kaustubh']
'''

for i in list2:
    print(i, end=' ')
'''
Output:
karthik 23 ishani kaustubh
'''

l = []
n = int(input('\nenter the no. of elements in list '))
for i in range(0, n):
    l.append(input('enter the item '))
print('printing the list contents ')
for i in l:
    print(i, end=' ')
print(f'\nprinting the list after appending is {l}')
'''
Output:
karthik 23 ishani kaustubh 
enter the no. of elements in list3
enter the item 1
enter the item karthik
enter the item 4774.44
printing the list contents
1 karthik 4774.44 
printing the list after appending is ['1', 'karthik', '4774.44']
'''

# appending item/element to the existing list
l1 = [10, 20, 49, 12, 44]
print(f'original list is {l1}')
'''
Output:
original list is [10, 20, 49, 12, 44]
'''

for i in l1:
    print(i, end=' ')
'''
Output:
10 20 49 12 44
'''

l1.append(23)  # appending item 23 to existing list l1, will append to end of the list
print('\nafter apppending the list')
for i in l1:
    print(i, end=' ')
'''
Output:
10 20 49 12 44
'''

print(f'\nupdated list after append is {l1}')
'''
Output:
updated list after append is [10, 20, 49, 12, 44, 23]
'''

# appending list to the existing list
list1 = [10, 20, 30, 40]
for i in list1:
    print(i, end=' ')
'''
Output:
10 20 30 40
'''

list1.append(34)
print(f'\nupdated list after append is {list1}')
'''
Output:
updated list after append is [10, 20, 30, 40, 34]
'''

list2 = [50, 60, 70, 80]
list1.append(list2)  # appending the list2 elements to list1
print(f'\nupdated list {list1}')
'''
Output:
updated list [10, 20, 30, 40, 34, [50, 60, 70, 80]]
'''
print(f'updated list {list2}')
'''
Output:
updated list [50, 60, 70, 80]
'''

# appending multiple list element within a list creating nested list
list3 = [10, 20, 30, 40]
list4 = [50, 60, 70, 80]
list5 = [90, 100, 110, 120]
print(f'list3 is {list3}')
print(f'list4 is {list4}')
print(f'list5 is {list5}')
'''
Output:
list3 is [10, 20, 30, 40]
list4 is [50, 60, 70, 80]
list5 is [90, 100, 110, 120]
'''

list3.append(list4)
print(f'\nlist3 after appending list4 is {list3}')
'''
Output:
list3 after appending list4 is [10, 20, 30, 40, [50, 60, 70, 80]]
'''
list3.append(list5)
print(f'\nlist3 after appending list5 is {list3}')
'''
Output:
list3 after appending list5 is [10, 20, 30, 40, [50, 60, 70, 80], [90, 100, 110, 120]]
'''

# appending a tuple as an element to the list
tuple = (22, 4, 3, 5, 8)
li1 = [3, 2, 9, 0, 7]
li2 = [23, 56, 65, 34]

print(f'original contents of tuple is {tuple}')
print(f'original contents of li1 is {li1}')
print(f'original contents of li2 is {li2}')

print('printing the tuple contents ')
for i in tuple:
    print(i, end=' ')
print('\n')

print('printing the li1 contents ')
for i in li1:
    print(i, end=' ')
print('\n')

print('printing the li2 contents ')
for i in li2:
    print(i, end=' ')
print('\n')

li1.append(li2)
print(f'li1 list after appending a list is {li1}')

li1.append(tuple)
print(f'li1 list after appending tuple to list is {li1} ')

# appending a dictionary elements to list
li3 = [3, 2, 9, 0, 7]
li4 = [23, 56, 65, 34]
dic = {1: 'karthik', 2: 'rini', 3: 'ishani'}

li3.append(li4)
print(f'updated list is {li3}')
li3.append(dic)
print(f'updated list is {li3}')

print(li3[6][3])