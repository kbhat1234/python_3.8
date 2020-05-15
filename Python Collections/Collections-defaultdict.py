import collections as c

dic = c.defaultdict(int)

print(dic)
'''
Output:
defaultdict(<class 'int'>, {})
'''

dic['one'] = 1
dic['two'] = 2
dic['three'] = 3
print(dic)
'''
Output:
defaultdict(<class 'int'>, {'one': 1, 'two': 2, 'three': 3})
'''

print(dic['one'])
print(dic['four'])
print(dic['five'])
'''
Output:
1
0
0
'''
