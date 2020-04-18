dic1 = {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male'}
print(f'dic1 is {dic1}')
'''
Output:
dic1 is {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male'}
'''
print(type(dic1))
'''
Output:
<class 'dict'>
'''

# shallow copy of dic1, if we do any operation to dic1, dic2 is not affected
dic2 = dic1.copy()
print(f'dic2 is {dic2}')
'''
Output:
dic2 is {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male'}
'''

# dic3 is assigned to dic1, means if we do any operation to dic1, dic3 will be affected.
dic3 = dic1
print(f'dic3 is {dic3}')
'''
Output:
dic3 is {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male'}
'''
dic3['school'] = 'dps'
print(f'dic3 after update is {dic3}')
print(f'dic1 is {dic1}')
'''
Output:
dic3 after update is {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male', 'school': 'dps'}
dic1 is {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male', 'school': 'dps'}
'''

# clear the dic1 elements, dic2 is not affected, but dic3 is affected.
dic1.clear()
print(f'dic1 is {dic1}')
print(f'dic2 is {dic2}')
print(f'dic3 is {dic3}')
'''
Output:
dic1 is {}
dic2 is {'name': 'karthik', 'age': 42, 'salary': 343553.33, 'gender': 'Male'}
dic3 is {}
'''
