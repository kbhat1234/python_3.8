# using isdisjoint() method
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

# isdisjoint() method
print(f'"(a1.isdisjoint(a3))" is {a1.isdisjoint(a3)}')
'''
Output:
"(a1.isdisjoint(a3))" is True
'''
print(f'"(a1.isdisjoint(a2))" is {a1.isdisjoint(a2)}')
'''
Output:
"(a1.isdisjoint(a2))" is False
'''
print(f'"(a2.isdisjoint(a3))" is {a2.isdisjoint(a3)}')
'''
Output:
"(a2.isdisjoint(a3))" is True
'''