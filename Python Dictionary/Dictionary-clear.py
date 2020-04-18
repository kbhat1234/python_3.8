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