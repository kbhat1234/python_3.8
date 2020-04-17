# create a dictionary with keys immutable (duplicate keys)
dic1 = {1: 'apple', 1: 'orange', 1:'pineapple', 1: 'watermelon', 1: 'litchi'}
print(f'dic1 items is {dic1.items()}')
'''
Output:
dic1 items is dict_items([(1, 'litchi')])
'''
print(f'dic1 is {dic1}')
'''
Output:
{1: 'litchi'}
'''
print(f'dic1 keys is {dic1.keys()}')
'''
Output:
dict_keys is dict_keys([1])
'''
print(f'dic1 values is {dic1.values()}')
'''
Output:
dic1 values is dict_values(['litchi'])
'''

# duplicate keys in different order defined
dic2 = {1: 'karthik', 2: 'rini', 3: 'ishani', 2: 'kaustubh'}
print(f'dic2 is {dic2}')
'''
Output:
dic2 is {{1: 'karthik', 2: 'kaustubh', 3: 'ishani'}
'''
print(f'dic2 items is {dic2.items()}')
'''
Output:
dic2 items is dict_items([(1, 'karthik'), (2, 'kaustubh'), (3, 'ishani')])
'''
print(f'dic2 keys is {dic2.keys()}')
'''
Output:
dic2 keys is dict_keys([1, 2, 3])
'''
print(f'dic2 values is {dic2.values()}')
'''
Output:
dic2 values is dict_values(['karthik', 'kasutubh', 'ishani'])
'''

# dictionary key is tuple of values
dic3 = {(1, 2, 3): 'karthik', (4, 5, 6): 'karthik', (7, 8, 9): 'ishani', (10, 11, 12): 'kaustubh', (13, 14, 15): 'ishani'}
print(f'dic3 items is {dic3.items()}')
'''
Output:
dic3 items is dict_items([((1, 2, 3), 'karthik'), ((4, 5, 6), 'karthik'), ((7, 8, 9), 'ishani'), ((10, 11, 12), 'kaustubh'), ((13, 14, 15), 'ishani')])
'''
print(f'dic3 is {dic3}')
'''
Output:
dic3 is {(1, 2, 3): 'karthik', (4, 5, 6): 'karthik', (7, 8, 9): 'ishani', (10, 11, 12): 'kaustubh', (13, 14, 15): 'ishani'}
'''
print(f'dic3 keys is {dic3.keys()}')
'''
Output:
dic3 keys is dict_keys([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)])
'''
print(f'dic3 values is {dic3.values()}')
'''
Output:
dic3 values is dict_values(['karthik', 'karthik', 'ishani', 'kaustubh', 'ishani'])
'''
print(f'dic3[({1}, {2}, {3})]) is {dic3[(1, 2, 3)]}')
'''
Output:
dic3[(1, 2, 3)] is karthik
'''

d = dic3.copy()
print(d)
print(dic3.get((7, 8, 9)))
dic3.popitem()
dic3.popitem()
print(dic3)
dic3.pop((1, 2, 3))
print(dic3)
print(len(dic3))

# dic3.clear()
# print(dic3)

dic4 = {1: 'karthik', 'name': 'bhat', 1: 55454, 1: (2, 3, 4)}
print(dic4)