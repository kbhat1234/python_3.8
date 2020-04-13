# count() string method
s1 = 'welcome to python programming'
print(s1.count('m'))
'''
Output:
3
'''

print(s1.count('mm'))
'''
Output:
1
'''

s2 = 'aa bb aa uu 12 23 cd dw ew'
print(s2.count('aa'))
print(s2.count('a'))
print(s2.count('2'))
print(s2.count('x'))
'''
Output:
2
4
2
0
'''

print(s2.count('a', 0, 6))