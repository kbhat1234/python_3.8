# print all keys of dictionary dic1
dic1 = {'name': 'ishani', 'age': 10, 'gender': 'Female', 'class': '4A'}
for k in dic1:
    print(k, end=', ')
print('\nend of for loop for keys of dictionary dic1')
print('-------------------------------------------------------')
'''
Output:
name, age, gender, class, 
end of for loop for keys of dictionary dic1
-------------------------------------------------------
'''

# print all values of dictionary dic1
for v in dic1:
    print(dic1[v], end=', ')
print('\nend of for lop for values of dictionary dic1')
print('-------------------------------------------------------')
'''
Output:
ishani, 10, Female, 4A, 
end of for lop for values of dictionary dic1
-------------------------------------------------------
'''

# print all keys of dictionary using keys() method
for k in dic1.keys():
    print(k, end=', ')
print('\nend of for loop for keys of dictionary dic1')
print('-------------------------------------------------------')
'''
Output:
name, age, gender, class, 
end of for loop for keys of dictionary dic1
-------------------------------------------------------
'''

# print all values of dictionary using values() method
for v in dic1.values():
    print(v, end=', ')
print('\nend of for loop for values of dictionary dic1')
print('--------------------------------------------------------')
'''
Output:
ishani, 10, Female, 4A, 
end of for loop for values of dictionary dic1
--------------------------------------------------------
'''

# print all items of dictionary using items() method
for i in dic1.items():
    print(i, end=', ')
print('\nend of for loop for items of dictionary dic1')
print('--------------------------------------------------------')
'''
Output:
('name', 'ishani'), ('age', 10), ('gender', 'Female'), ('class', '4A'), 
end of for loop for items of dictionary dic1
--------------------------------------------------------
'''

# print all dictionary items using for loops
for i in dic1:
    print(i, dic1[i])
print('end of for loop')
'''
Output:
name ishani
age 10
gender Female
class 4A
end of for loop
'''