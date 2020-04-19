d1 = {1: 'apple', 2: 'orange', 3: 'grapes', 4: 'mango', 5: 'banana'}
# person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(f'd1 is {d1}')
'''
Output:
{1: 'apple', 2: 'orange', 3: 'grapes', 4: 'mango', 5: 'banana'}
'''
result = d1.popitem()
print(f'removed element is {result}')
'''
Output:
removed element is (5, 'banana')
'''
print(f'd1 after deleting is {d1}')
