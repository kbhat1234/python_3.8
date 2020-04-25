# using issubset() method
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

# issubset() method
print(f'"(a1.issubset(a2))" is {a1.issubset(a2)}')
'''
Output:
"(a1.issubset(a2))" is False
'''
print(f'"(a2.issubset(a1))" is {a2.issubset(a1)}')
'''
Output:
"(a2.issubset(a1))" is True
'''

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print(A.issubset(B))
print(B.issubset(A))
'''
Output:
True
False
'''
print(A.issubset(C))
print(C.issubset(A))
'''
Output:
False
False
'''
print(B.issubset(C))
print(C.issubset(B))
'''
Output:
False
True
'''
