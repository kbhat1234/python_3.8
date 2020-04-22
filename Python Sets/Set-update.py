# updating the existing set using update(0 method
set1 = {'fname', 'lname', 2334, 23.76, 'karthik', 'bhat'}
print(f'original set items is {set1}')
print(f'type(set1) is {type(set1)}')
print(f'length of set1 is {len(set1)}')
'''
Output:
original set items is {'fname', 'bhat', 'lname', 'karthik', 23.76, 2334}
type(set1) is <class 'set'>
length of set1 is 6
'''
# adding items to set using update() method
set1.update({2, 'rini', 34, 'kaustubh', 'karthik'})
print(f'set1 after update is {set1}')
print(f'length of set1 after update is {len(set1)}')
'''
Output:
set1 after update is {'fname', 'rini', 2, 34, 'bhat', 'kaustubh', 'lname', 'karthik', 23.76, 2334}
length of set1 after update is 10
'''

# updating the set using iterable - set
set2 = set()
set3 = {10, 20, 30, 40}
set2.update(set3)
print(f'set2 after updating with set3 is {set2}')
print(f'length of set2 is {len(set2)}')
print(f'length of set3 is {len(set3)}')
'''
Output:
set2 after updating with set3 is {40, 10, 20, 30}
length of set2 is 4
length of set3 is 4
'''

# updating the set using iterable - list
list = ['karthik', 'bhat', 'manoj', 'abhijheet', 10, 30]
print(f'list items is {list}')
print(f'type(list) is {type(list)}')
'''
Output:
list items is ['karthik', 'bhat', 'manoj', 'abhijheet', 10, 30]
type(list) is <class 'list'>
'''
set3.update(list)
print(f'set3 after updating with list is {set3}')
print(f'length of set3 is {len(set3)}')
print(f'length of list is {len(list)}')
'''
Output:
set3 after updating with list is {40, 10, 'karthik', 'manoj', 'abhijheet', 20, 'bhat', 30}
length of set3 is 8
length of list is 6
'''

# updating the set using iterable - tuple
tup = ('karthik', 'manoj', 'manusi')
set3.update(tup)  # only 'manusi will be added to set
print(f'set3 after update using tup is {set3}')
print(f'length of set3 after update is {len(set3)}')
print(f'type(set3) is {type(set3)}')
'''
Output:
set3 after update using tup is {'bhat', 'manusi', 40, 10, 'manoj', 20, 'karthik', 'abhijheet', 30}
length of set3 after update is 9
type(set3) is <class 'set'>
'''

# updating the set using iterable - dictionary
dic = {1: 'ashish', 2: 'karthik', 3: 'manoj', 4: 'anika', 'guava': 5}
set3.update(dic)  # only keys of dic is added to set
print(f'set3 after update with dic is {set3}')
print(f'length of set3 after update is {len(set3)}')
print(f'type(set3) is {type(set3)}')
'''
Output:
set3 after update with dic is {'bhat', 1, 2, 'manusi', 3, 4, 40, 10, 'manoj', 'guava', 20, 'karthik', 'abhijheet', 30}
length of set3 after update is 14
type(set3) is <class 'set'>
'''

# updating the set using iterable - string
str1 = 'welcome'
set3.update(str1)  # 'w', 'e', 'l', 'c', 'o', 'm', 'e' is added to set
print(f'set3 after update is {set3}')
print(f'length of set3 is {len(set3)}')
'''
Output:
set3 after update is {'w', 1, 2, 3, 4, 'l', 'guava', 10, 20, 30, 40, 'manusi', 'bhat', 'c', 'o', 'karthik', 'm', 'manoj', 'abhijheet', 'e'}
length of set3 is 20
'''