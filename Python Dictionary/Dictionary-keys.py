dic = {1: 100, 2: 200, 'fruit': 'apple'}
print(f'dic is {dic}')
'''
Output:
dic is {1: 100, 2: 200, 'fruit': 'apple'}
'''

# keys of dictionary dic with elements
keys = dic.keys()
print(f'keys of dic is {keys}')
'''
Output:
keys of dic is dict_keys([1, 2, 'fruit'])
'''

# keys of empty dictionary
dic1 = {}
empty_dic = dic1.keys()
print(f'keys of empty dic1 is {empty_dic}')
'''
Output:
keys of empty dic1 is dict_keys([])
'''

# update the dictionary dic using update() method
dic.update({'vegetable': 'green leaves'})
print(f'dic keys after update is {keys}')
'''
Output:
dic keys after update is dict_keys([1, 2, 'fruit', 'vegetable'])
'''