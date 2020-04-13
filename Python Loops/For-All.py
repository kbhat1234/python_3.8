list = [1, 2, 3, 4, 5]
tuple = (20, 30, 40, 50)
dic = {1: 'karthik', 2: 'rini', 3: 'ishani', 4: 'kaustubh'}
str = '"welcome to python programming"'
# for loop using list
print(f'original list is as follows ')
for i in list:
    print(i, end=' ')
print(f'\nlist is {list}')
print('\n')
'''
Output:
original list is as follows 
1 2 3 4 5 
list is [1, 2, 3, 4, 5]
'''

# for loop using tuple
print(f'original tuple is as follows ')
for i in tuple:
    print(i, end=' ')
print(f'\ntuple is {tuple}')
print('\n')
'''
Output:
original tuple is as follows 
20 30 40 50 
tuple is (20, 30, 40, 50)
'''

# for loop using dictionary
print(f'original dictionary keys is as follows ')
for i in dic.keys():
    print(i, end=' ')
print(f'\ndictionary is {dic.keys()}')
print('\n')
'''
Output:
original dictionary keys is as follows 
1 2 3 4 
dictionary is dict_keys([1, 2, 3, 4])
'''

print(f'original dictionary values is as follows ')
for i in dic.values():
    print(i, end=' ')
print(f'\ndictionary values is {dic.values()}')
print('\n')
'''
Output:
original dictionary values is as follows 
karthik rini ishani kaustubh 
dictionary values is dict_values(['karthik', 'rini', 'ishani', 'kaustubh'])
'''

# for loop using string
print(f'original string is as follows')
for i in str:
    print(i, end=' ')
print(f'\nstring is {str}')
'''
Output:
original string is as follows
" w e l c o m e   t o   p y t h o n   p r o g r a m m i n g " 
string is "welcome to python programming"
'''