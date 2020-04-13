t1 = (10, 2, 4, 67, 43, 56, 3, 9, 87)

# len(tuple) function gives the length of tuple
l = len(t1)

print(f'length of l is {l}')
'''
Output:
length if 1 is 9
'''

# printing elemens of tuple using index
print('tuple elements with index is ')
count = 0
for i in t1:
    print(f't1[{count}] = {i}')
    count += 1
'''
Output:
tuple elements with index is 
t1[0] = 10
t1[1] = 2
t1[2] = 4
t1[3] = 67
t1[4] = 43
t1[5] = 56
t1[6] = 3
t1[7] = 9
t1[8] = 87
'''

# max element in the given tuple
m1 = max(t1)
print(f'maximum element in tuple is {m1}')
'''
Output:
maximum element in tuple is 87
'''

# min element in the given tuple
m2 = min(t1)
print(f'minimum element in tuple is {m2}')
'''
Output:
minimum element in tuple is 2
'''

# convert list to tuple using tuple(seq) function
l1 = [10, 6, 3, 4, 0, 1]
t = tuple(l1)
print(f'converted list to tuple is {t}')
'''
Output:
converted list to tuple is (10, 6, 3, 4, 0, 1)
'''

# convert set to tuple using tuple(seq) function
s1 = {4, 2, 3, 9, 0}
s = tuple(s1)
print(f'converted set to tuple is {s}')
'''
Output:
converted set to tuple is {0, 2, 3, 4, 9}
'''

# convert string to tuple using tuple(seq) function
str1 = 'welcome'
st1 = tuple(str1)
print(f'converted string to tuple is {st1}')
'''
Output:
converted string to tuple is ('w', 'e', 'l', 'c', 'o', 'm', 'e')
'''

# convert dictionary keys and values to tuple using tuple(seq) function
dic1 = {1: 'a', 2: 'b', 3: 'c'}
dk = tuple(dic1.keys())
dv = tuple(dic1.values())

print(f'converted dictionary keys to tuple is {dk}')
print(f'converted dictionary values to tuple is {dv}')
'''
Output:
converted dictionary keys to tuple is (1, 2, 3)
converted dictionary values to tuple is ('a', 'b', 'c')
'''

dic2 = {1: (2, 3, 4), 2: (3, 4, 5), 3: (4, 5, 6)}
print(dic2)
dk = dic2.keys()
dv = dic2.values()
dic2[1] = (1, 2, 3)
print(dk)
print(dv)
