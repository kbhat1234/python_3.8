s1 = {2, 4, 1, 5, 8, 9}
s2 = {5, 7, 9, 10, 2, 7}

print(f's1 is {s1}')
print(f's2 is {s2}')
'''
Output:
s1 is {2, 4, 1, 5, 8, 9}
s2 is {5, 7, 9, 10, 2, 7}
'''

s1.difference_update(s2)
print(f's1 is {s1}')
print(f's2 is {s2}')
print(f'"s1.difference_update(s2)" is {s1}')
'''
Output:
s1 is {1, 4, 8}
s2 is {2, 5, 7, 9, 10}
"s1.difference_update(s2)" is {4, 1, 8}
'''

s2.difference_update(s1)
print(f's1 is {s1}')
print(f's2 is {s2}')
print(f'"s2.difference_update(s1)" is {s2}')
'''
Output:
s1 is {1, 4, 8}
s2 is {2, 5, 7, 9, 10}
"s2.difference_update(s1)" is {5, 7, 9, 10, 2, 7}
'''