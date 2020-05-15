import collections as c

dic = {
    'a': 10,
    'e': 20,
    'f': 30,
    'b': 40,
    'c': 50,
    'a': 60,
    'a': 70
}
print(f'dic items is {dic}')
print(f'dic items is {dic.items()}')
print(f'"type(dic)" is {type(dic)}')
print(f'"type(dic)" is {type(dic)}')
'''
Output:
{'a': 70, 'e': 20, 'f': 30, 'b': 40, 'c': 50}
dict_items([('a', 70), ('e', 20), ('f', 30), ('b', 40), ('c', 50)])
<class 'dict'>
'''

# OrderedDict()
d1 = c.OrderedDict()
d1['A'] = 10
d1['D'] = 40
d1['E'] = 50
d1['B'] = 20
d1['C'] = 30
d1['B'] = 90

for k, v in d1.items():
    print(k, v)
'''
Output:
A 10
D 40
E 50
B 90
C 30
'''

print(d1)
print(type(d1))
print(d1.items())
''''
Output:
OrderedDict([('A', 10), ('D', 40), ('E', 50), ('B', 90), ('C', 30)])
<class 'collections.OrderedDict'>
odict_items([('A', 10), ('D', 40), ('E', 50), ('B', 90), ('C', 30)])
'''