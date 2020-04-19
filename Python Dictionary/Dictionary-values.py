dic = {1: 100, 2: 200, 'fruit': 'apple'}
print(f'dic is {dic}')
'''
Output:
dic is {1: 100, 2: 200, 'fruit': 'apple'}
'''

# dictionary values using values() method
values = dic.values()
print(f'dic values is {values}')
'''
Output:
dic values is dict_values([100, 200, 'apple'])
'''

# delete the elements in dic
del dic[2]
print(f'dic after delete is {dic}')
'''
Output:
dic after delete is {1: 100, 'fruit': 'apple'}
'''
print(f'dic values after delete is {values}')
'''
Output:
dic values after delete is dict_values([100, 'apple'])
'''
# update the elements in dic

dic.update({3: 3344, 4: 7746})
print(f'dic after update is {dic}')
'''
Output:
dic after update is {1: 100, 'fruit': 'apple', 3: 3344, 4: 7746}
'''
print(f'dic values after update is {values}')
'''
Output:
dic values after update is dict_values([100, 'apple', 3344, 7746])
'''
