# extend(iterable) is list method for extending the list from the iterable. Iterable can be list, tuple or set
list = [10, 20, 30, 40]
'''
Output:
original list is [10, 20, 30, 40]
'''

print(f'original list is {list}')
for i in list:
    print(i, end=' ')
'''
Output:
10 20 30 40
'''

list.extend('50')
print(f'\nextended list is {list}')
'''
Output:
extended list is [10, 20, 30, 40, '5', '0']
'''

# extend the list by adding list as elements - list
list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
list1.extend(list2)
list1.sort()
print(f'updated list1 after extending list2 is {list1}')
'''
Output:
updated list1 after extending list2 is [10, 20, 30, 40, 50, 60, 70, 80]
'''

# extend the list by adding tuple as elements - tuple
list3 = [10, 20, 30, 40]
list4 = [50, 60, 70, 80]
tuple = (1, 2, 3, 4, 5)

list3.extend(list4)
print(f'updated list is {list3}')
'''
Output:
updated list is [10, 20, 30, 40, 50, 60, 70, 80]
'''

list3.extend(tuple)
list3.sort(reverse=False)
print(f'updated list after extending tuple is {list3}')
'''
Output:
updated list after extending tuple is [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 60, 70, 80]
'''

# extend the list by extending set as elements - set
set1 = {11, 12, 13, 14}

list3.extend(set1)
list3.sort()
print(f'updated list a1 after extending the set is {list3}')
'''
Output:
updated list a1 after extending the set is [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 20, 30, 40, 50, 60, 70, 80]
'''