import collections as c

# empty list
list1 = []
print(f'list1 elements is {list1}')
print(f'"type(list1)" is {type(list1)}')
'''
Output:
list1 elements is []
"type(list1)" is <class 'list'>
'''

# Counter() used for empty list
c1 = c.Counter(list1)
print(f'list1 elements with counter {c1}')
print(f'"type(c1)" is {type(c1)}')
'''
Output:
list1 elements with counter Counter()
"type(c1)" is <class 'collections.Counter'>
'''

# list2 with elements
list2 = [1, 2, 3, 4, 5, 7, 8, 5, 9, 6, 10]
print(f'list2 elements is {list2}')
print(f'"type(list2)" is {type(list2)}')
'''
Output:
list2 elements is [1, 2, 3, 4, 5, 5, 7, 8, 5, 9, 6, 10]
"type(list2)" is <class 'list'>
'''

# list2 with Counter()
c2 = c.Counter(list2)
print(f'list2 elements with counter is {c2}')
print(f'"type(c2)" is {type(c2)}')
print(f'count no. of 1s in list2 is {c2[1]}')
print(f'count no. of 2 in list2 is {c2[2]}')
'''
Output:
list2 elements with counter is Counter({2: 3, 5: 2, 10: 2, 1: 1, 3: 1, 4: 1, 12: 1, 9: 1})
"type(c2)" is <class 'collections.Counter'>
count no. of 1s in list2 is 1
count no. of 2s in list2 is 3
'''

# tuple with elements
tup = ('karthik', 'Karthik', 10, 20, 1, 10, 20, 'karthik')
print(f'tup elements is {tup}')
print(f'"type(tup)" is {type(tup)}')
'''
Output:
tup elements is ('karthik', 'Karthik', 10, 20, 1, 10, 20, 'karthik')
"type(tup)" is <class 'tuple'>
'''

# tuple with Counter()
c3 = c.Counter(tup)
print(f'tup elements with counter is {c3}')
print(f'"type(c3)" is {type(c3)}')
print(f'count no. 10 in tup is {c3[10]}')
print(f"count string 'Karthik' in tup is {c3['Karthik']}")
print(f"count string 'karthik' in tup is {c3['karthik']}")
'''
Output:
tup elements with counter is Counter({'karthik': 2, 10: 2, 20: 2, 'Karthik': 1, 1: 1})
"type(c3)" is <class 'collections.Counter'>
count no. 10 in tup is 2
count string 'Karthik' in tup is 1
count string 'karthik' in tup is 2
'''

# string
str1 = 'welcome to python programming'
print(f'str1 is {str1}')
print(f'"type(str1)" is {str1}')

# str1 with Counter()
c4 = c.Counter(str1)
print(f'str1 with counter is \n{c4}')
print(f'"type(c4)" is {type(c4)}')
print(f"count 'm' in str1 is {c4['m']}")
print(f"count 'g' in str1 is {c4['g']}")
'''
Output:
str1 with counter is 
Counter({'o': 4, 'm': 3, ' ': 3, 'e': 2, 't': 2, 'p': 2, 'n': 2, 'r': 2, 'g': 2, 'w': 1, 'l': 1, 'c': 1, 'y': 1, 'h': 1, 'a': 1, 'i': 1})
"type(c4)" is <class 'collections.Counter'>
count 'm' in str1 is 3
count 'g' in str1 is 2
'''