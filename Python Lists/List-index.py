# list index(x, start, end) - it will be give index of the element.
list = ['a', 'p', 'p', 'l', 'e']
index1 = list.index('p')
print(f'index of "p" is {index1}')
'''
Output:
index of "p" is 1
'''

# if the list is having duplicate elements then 1st occurence element index is returned
index2 = list.index('l')  # index 3 will be returned
index3 = list.index('p')  # alwlays index 1 will be returned
print(f'index of "l" is {index2}')
'''
Output:
index of "l" is 3
'''
print(f'index of "p" is {index3}')
'''
Output:
index of "p" is 1
'''

# if list element is not present in list when we try to put an element which is not in list
index4 = list.index('e')  # index 4 is returned
# index5 = list.index('z')  # 'z' element is not in list, get ValueError

print(f'index of "e" is {index4}')
'''
Output:
index of "e" is 4
'''
# print(f'index of "z" is {index5}')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Python Lists/List-index.py", line 14, in <module>
    index5 = list.index('z')  # 'z' element is not in list
ValueError: 'z' is not in list
'''

# index() method takes optional parameters start and end index. this will make to search indexes within the limit
index6 = list.index('p', 1)  # index 1 will be returned
print(f'index of "p" is {index6}')
'''
output:
index of "p" is 1
'''
index7 = list.index('p', 2)
print(f'index of "P" is {index7}')
'''
Output:
index of "P" is 2
'''
index8 = list.index('p', 0, 3)
print(f'index of "p" is {index8}')
'''
Output:
index of "p" is 1
'''