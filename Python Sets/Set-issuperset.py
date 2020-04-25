# using issuperset() method
a1 = {1, 2, 3, 4, 5, 8}
a2 = {2, 4, 8}
a3 = {6, 7, 9, 10}
print(f'set a1 is {a1}')
print(f'set a2 is {a2}')
print(f'set a3 is {a3}')
'''
Output:
set a1 is {1, 2, 3, 4, 5, 8}
set a2 is {2, 4, 8}
set a3 is {6, 7, 9, 10}
'''

# issuperset() method
print(f'"(a1.issuperset(a2))" is {a1.issuperset(a2)}')
'''
Output:
"(a1.issuperset(a2))" is True
'''
print(f'"(a2.issuperset(a1))" is {a2.issuperset(a1)}')
'''
Output:
"(a2.issuperset(a1))" is False
'''