# using the & operator for intersection
a1 = {1, 2, 3, 4, 5}
a2 = { 2, 6, 7, 3, 8}
print(f'a1 set is {a1}')
print(f'a2 set is {a2}')
'''
Output:
a1 set is {1, 2, 3, 4, 5}
a2 set is {2, 3, 6, 7, 8
'''
i1 = a1 & a2
print(f'intersection of "a1 & a2" is {i1}')
'''
Output:
intersection of "a1 & a2" is {2, 3}
'''
# using the intersection() method for intersection
i2 = a1.intersection(a2)
print(f'intersection of "a1.intersection(a2)" is {i2}')
'''
Output:
intersection of "a1.intersection(a2)" is {2, 3}
'''