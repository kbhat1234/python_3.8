dic = {'name': 'karthik', 'age': 42, 'profession': 'software engineer', 'aadhaarid': 'ajppb4129b'}
print(f'dic is {dic}')
print(type(dic))
'''
Output:
dic is {'name': 'karthik', 'age': 42, 'profession': 'software engineer', 'aadhaarid': 'ajppb4129b'}
<class 'dict'>
'''
# items() method
print(f'dic items is {dic.items()}')
print(type(dic.items()))
'''
Output:
dic items is dict_items([('name', 'karthik'), ('age', 42), ('profession', 'software engineer'), ('aadhaarid', ajppb4129b')])
<class 'dict_items'>
'''

# delting dictionary item using del keyword
del dic['name']

# printing the dic after delete of item
print(f'dic after updating is {dic}')
'''
Output:
dic after updating is {'age': 42, 'profession': 'software engineer', 'aadhaarid': 'ajppb4129b'}
'''

# printing the dic_items after delete of item
print(f'dic_items after updating is {dic.items()}')
'''
Output:
dic_items after updating is dict_items([('age', 42), ('profession', 'software engineer'), ('aadhaarid', 'ajppb4129b')])
'''