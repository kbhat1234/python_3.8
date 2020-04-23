# union of 2 sets using or | operator
a1 = {1, 2, 3, 4}
a2 = {2, 1, 3, 5, 6}
print(f'a1 set is {a1}')
print(f'a2 set is {a2}')
'''
Output:
a1 set is {1, 2, 3, 4}
a2 set is {2, 1, 3, 5, 6}
'''

u1 = a1 | a2  # perform union of a1 and a2 using | operator
print(f'union of "a1 | a2" is {u1}')
'''
Output:
union of "a1 | a2" is {1, 2, 3, 4, 5, 6}
'''

# union of 2 sets using union() method
u2 = a1.union(a2)
print(f'union of "a1.union(a2)" is {u2}')