dic1 = {}

print(f'empty dictionary is {dic1}')
"""
Output:
empty dictionary is {}
"""

# adding elements one at a time to dictionary
dic1['name'] = 'karthik'
dic1['roll no'] = 2376
dic1['address'] = 'Jp nagar bangalore'
dic1['salary'] = 234432.223

print(f'after adding elements to dictionary {dic1}')
"""
Output:
after adding elements to dictionary {'name': 'karthik', 'roll no': 2376, 'address': 'Jp nagar bangalore', 'salary': 234432.223}
"""

print(type(dic1))
print(type(dic1['name']))
print(type(dic1['roll no']))
print(type(dic1['address']))
print(type(dic1['salary']))
"""
Output:
<class 'dict'>
<class 'str'>
<class 'int'>
<class 'str'>
<class 'float'>
"""

# adding set of values to a single key to dictionary
dic1['gender'] = 'male', 'female'
print(f'Adding set of values {dic1}')
"""
Output:
{'name': 'karthik', 'roll no': 2376, 'address': 'Jp nagar bangalore', 'salary': 234432.223, 'gender': ('male', 'female')}
"""

print(dic1['gender'][0])
print(dic1['gender'][1])
"""
Output:
male
female
"""

# updating the key's values
dic1['name'] = 'ashish'
dic1['roll no'] = 7632

print(dic1)
"""
Output:
{'name': 'ashish', 'roll no': 7632, 'address': 'Jp nagar bangalore', 'salary': 234432.223, 'gender': ('male', 'female')}
"""

# adding nested key value to dictionary
dic1['profession'] = {'select': {1: 'software engineer', 2: 'surgeon', 3: 'charted accountant'}}

print(dic1)
"""
Output:
{'name': 'ashish', 'roll no': 7632, 'address': 'Jp nagar bangalore', 'salary': 234432.223, 'gender': ('male', 'female'), 'profession': {'select': {1: 'software engineer', 2: 'surgeon', 3: 'charted accountant'}}}
"""

print(dic1['profession']['select'][1])
print(dic1['profession']['select'][2])
print(dic1['profession']['select'][3])

"""
Output:
software engineer
surgeon
charted accountant
"""

print(dic1.get('profession'))
"""
Output:
{'select': {1: 'software engineer', 2: 'surgeon', 3: 'charted accountant'}}
"""