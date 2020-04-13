t1 = (10, 20, 30, 40, 50)
t2 = (1, 2, 3, 4, 5)

print(f'tuple t1 is {t1}')
print(f'tuple t2 is {t2}')
'''
Output:
tuple t1 is (10, 20, 30, 40, 50)
tuple t2 is (1, 2, 3, 4, 5)
'''

# tuple concatenation using + operator
t3 = t1 + t2  # concat t1 + t2 = (10, 20, 30, 40, 50, 1, 2, 3, 4, 5)
t4 = t2 + t1  # concat t2 + t1 = (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)
t5 = t3  # t5 will hold tuple t3 = (10, 20, 30, 40, 50, 1, 2, 3, 4, 5)
t6 = t4  # t6 will hold tuple t4 = (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)
t7 = t5 + t6  # concat t5 + t6 = (10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50)
print(f't1 concatenation with t2 is {t3}')
print(f't2 concatenation with t1 is {t4}')
print(f't5 = t3 is {t5}')
print(f't6 = t4 is {t6}')
print(f't5 concatenation with t6 is {t7}')
'''
Output:
t1 concatenation with t2 is (10, 20, 30, 40, 50, 1, 2, 3, 4, 5)
t2 concatenation with t1 is (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)
t5 = t3 is (10, 20, 30, 40, 50, 1, 2, 3, 4, 5)
t6 = t4 is (1, 2, 3, 4, 5, 10, 20, 30, 40, 50)
t5 concatenation with t6 is (10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50)
'''

# tuple repetiton using * operator
tup1 = ('apple', 'orange', 'banana', 'pineapple')
print(f'tuple tup1 is {tup1}')
'''
Output:
tuple tup1 is ('apple', 'orange', 'banana', 'pineapple')
'''

tup2 = tup1 * 2
print(f'tup1*2 is {tup2}')
'''
Output:
tup1*2 is ('apple', 'orange', 'banana', 'pineapple', 'apple', 'orange', 'banana', 'pineapple')
'''

tup3 = (1, 2, 3, 4, 5) * 3
print(f'tup3 is {tup3}')
'''
Output:
tup3 is (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
'''

# tuple operation using membership in operator
if 4 in tup3:
    print('element present in tuple')
else:
    print('element not present in tuple')
'''
Output:
element present in tuple
'''

# tuple operation using membership not in operator
if 9 not in tup3:
    print('element not present in tuple')
else:
    print('element present in tuple')
'''
Output:
element not present in tuple
'''

# tuple iteration using for loop
count = 0
for i in tup3:
    print(f'tup3[{count}] = {i}')
    count += 1
'''
Output:
tup3[0] = 1
tup3[1] = 2
tup3[2] = 3
tup3[3] = 4
tup3[4] = 5
tup3[5] = 1
tup3[6] = 2
tup3[7] = 3
tup3[8] = 4
tup3[9] = 5
tup3[10] = 1
tup3[11] = 2
tup3[12] = 3
tup3[13] = 4
tup3[14] = 5
'''

# tuple length using len() function
print(f'length of tup3 is {len(tup3)}')
'''
Output:
length of tup3 is 15
'''