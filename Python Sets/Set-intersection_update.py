a1 = {1, 2, 3, 4, 5}
a2 = {2, 3, 5, 6, 7}
a3 = {3, 8, 7, 9}

# a3 elements  with a2 and a1 (common elements in a3 is retained, rest removed), a2 and a1 will not have any changes
result = a3.intersection_update(a2, a1)
print(f'--------------a3.intersection_update(a1, a2)------------------')
print(f'a1 is {a1}')
print(f'a2 is {a2}')
print(f'a3 is {a3}')
print(result)
'''
Output:
--------------a3.intersection_update(a1, a2)------------------
a1 is {1, 2, 3, 4, 5}
a2 is {2, 3, 5, 6, 7}
a3 is {3}
'''

# a1 elements with a2 and a3 (common elements in a1 is retained, rest removed), a2 and a3 will not have any changes
result = a1.intersection_update(a2, a3)
print(f'--------------a1.intersection_update(a2, a3)------------------')
print(f'a1 is {a1}')
print(f'a2 is {a2}')
print(f'a3 is {a3}')
print(result)
'''
Output:
--------------a1.intersection_update(a2, a3)------------------
a1 is {3}
a2 is {2, 3, 5, 6, 7}
a3 is {3}
'''

# a2 elements with a1 and a3 (common elements in a2 is retained, rest removed), a1 and a3 will not have any changes
result = a2.intersection_update(a1, a3)
print(f'--------------a2.intersection_update(a1, a3)------------------')
print(f'a1 is {a1}')
print(f'a2 is {a2}')
print(f'a3 is {a3}')
print(result)
'''
Output:
--------------a2.intersection_update(a1, a3)------------------
a1 is {3}
a2 is {3}
a3 is {3}
'''

a = {'ayush', 'bob', 'castle'}
b = {'castle', 'dude', 'emyway'}
c = {'fuson', 'gaurav', 'castle'}

print('------------------------------------------------')
a.intersection_update(b, c)
print(f'a is {a}')
print(f'b is {b}')
print(f'c is {c}')
'''
Output:
a is {'castle'}
b is {'castle', 'dude', 'emyway'}
c is {'fuson', 'gaurav', 'castle'}
'''

print('--------------------------------------')
b.intersection_update(c, a)
print(f'a is {a}')
print(f'b is {b}')
print(f'c is {c}')
'''
Output:
a is {'castle'}
b is {'castle'}
c is {'fuson', 'gaurav', 'castle'}
'''

print('------------------------------------------------')
c.intersection_update(a, b)
print(f'a is {a}')
print(f'b is {b}')
print(f'c is {c}')
'''
Output:
a is {'castle'}
b is {'castle'}
c is {'castle'}
'''

s1 = {'apple', 'karthik', 23, 'a', 'b'}
s2 = {'orange', 'ishani', 'apple', 'b', 24}
print('----------------------------------------------------')
s1.intersection_update(s2)
print(f's1 is {s1}')
print(f's2 is {s2}')
'''
Output:
s1 is {'apple', 'b'}
s2 is {'orange', 'ishani', 'apple', 'b', 24}
'''
print('------------------------------------------------------')
s2.intersection_update(s1)
print(f's1 is {s1}')
print(f's2 is {s2}')
'''
Output:
s1 is {'apple', 'b'}
s2 is {'apple', 'b'}
'''