# empty dictionary
dic1 = {}
print(f'dic1 is {dic1}')
'''
Output:
{}
'''

# Adding elements to empty dictionary using index method
dic1['name'] = 'karthik'
dic1['age'] = 41
dic1['sex'] = 'M'
dic1['profession'] = 'software engineer'
print(f'dic1 is {dic1}')
'''
Output:
dic1 is {'name': 'karthik', 'age': 41, 'sex': 'M', 'profession': 'software engineer'}
'''
print(f'dic1 keys is {dic1.keys()}')
'''
Output:
dic1 keys is dict_keys(['name', 'age', 'sex', 'profession'])
'''
print(f'dic1 values is {dic1.values()}')
'''
Output:
dic1 values is dict_values(['karthik', 41, 'M', 'software engineer'])
'''

# update the existing dictionary using index method (giving key)
dic1['sex'] = 'F'
dic1['profession'] = 'sr.software engineer'

# print the dictionary after updating
print(f'after update dic1 is {dic1}')
'''
Output:
after update dic1 is {'name': 'karthik', 'age': 41, 'sex': 'F', 'profession': 'sr.software engineer'}
'''

# updating the existing dictionary using input method
dic1['name'] = input('update the name ')
dic1['age'] = int(input('update the age '))
print(f'after update dic1 is {dic1}')
'''
Output:
update the name ishani
update the age 10
after update dic1 is {'name': 'ishani', 'age': 10, 'sex': 'F', 'profession': 'sr.software engineer'}
'''

# add the dictionary elements using input() method
dic2 = {}  # empty dictionary
print(f'dic2 is {dic2}')
'''
Output:
{}
'''
dic2['name'] = input('enter name ')
dic2['age'] = int(input('enter age '))
dic2['sex'] = input('enter sex ')
dic2['salary'] = float(input('enter salary '))
dic2['company'] = input('enter company ')

print(f'after adding elements in dic2 is {dic2}')
print(f'dic2 keys is {dic2.keys()}')
print(f'dic2 values is {dic2.values()}')
print(f'length of dic2 is {len(dic2)}')
print(f'length of dic2 keys is {len(dic2.keys())}')
print(f'length of dic2 values is {len(dic2.values())}')
print(f'dic2 items is {dic2.items()}')
print(f'length of dic2 items is {len(dic2.items())}')
