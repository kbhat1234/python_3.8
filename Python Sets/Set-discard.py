# if x element present in set, discard() item from set
set1 = {10, 2, 'karthik', 'apple', 377.99}
print(f'set1 before discard is {set1}')
'''
Output:
set1 before discard is {2, 10, 'apple', 377.99, 'karthik'}
'''
# print(set1.discard(2))
set1.discard(2)  # 2 is present in the set, element removed from set
print(f'set1 is {set1}')
'''
Output:
set1 is {10, 'apple', 377.99, 'karthik'}
'''

# if x element is not present in set, nothing will be performed ignoring the error
# print(set1.discard(200))  # 200 is not present in the set, element not removed without any error.
print(f'set1 is {set1}')
'''
Output:
set1 is {10, 'apple', 377.99, 'karthik'}
'''