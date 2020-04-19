# delete all the dictionary elements
dic = {'name': 'karthik', 'age': 41, 'gender': 'male'}
print(f'original dic elements is\n{dic}')
'''
Output:
original dic elements is
{'name': 'karthik', 'age': 41, 'gender': 'male'}
'''
dic['salary'] = 326363.33
dic['profession'] = 'QA Manager'
print(f'dic elements after update is\n{dic}')
'''
Output:
dic elements after update is
{'name': 'karthik', 'age': 41, 'gender': 'male', 'salary': 326363.33, 'profession': 'QA Manager'}
'''
dic.clear()
# del dic -> will actual delete the elements and structure
print(f'dic after clear is {dic}')
'''
Output:
dic after clear is {}
'''

# example
d1 = {1: 156, 2: 256, 3: 356, 4: 456}
print(f'd1 is {d1}')
'''
Output:
{1: 156, 2: 256, 3: 356, 4: 456}
'''
d2 = d1  # d2 will have d1 copied but any changes to d1 will affect d2
print(f'd2 is {d2}')
'''
Output:
{1: 156, 2: 256, 3: 356, 4: 456}
'''
d3 = d1.copy()  # d3 will have shallow copy (own copy), changes to d1 or d2 will not affect d3
print(f'd3 is {d3}')
'''
Output:
{1: 156, 2: 256, 3: 356, 4: 456}
'''
d1.clear()  # clear the dictionary items
print(f'after clear d1 is {d1}')
'''
Output:
after clear d1 is {}
'''
print(f'after clear d2 is {d2}')
'''
Output:
after clear d1 is {}
'''
print(f'after clear d3 is {d3}')
'''
Output:
after clear d3 is {1: 156, 2: 256, 3: 356, 4: 456}
'''