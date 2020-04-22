# clear the set using clear() method
set1 = {10, 20, 30, 'karthik', 'apple', 'lion', 35, 373.8787, 'a'}
print(f'set1 before clear is {set1}')
'''
Output:
set1 before clear is {35, 'a', 'apple', 10, 'karthik', 20, 373.8787, 'lion', 30}
'''
set1.clear()  # removes all elements from set
print(f'set1 after clear is {set1}')
'''
Output:
set1 after clear is set()
'''
set1.update([10, 20, 30, 40])
print(f'set1 after update is {set1}')
'''
Output:
set1 after update is {40, 10, 20, 30}
'''
set1.clear()
print(f'set1 after clear is {set1}')
'''
Output:
set1 after clear is set()
'''