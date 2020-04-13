list1 = ['karthik', 'Rini', 'ISHANI', 'Kaustubh']  # list with string type of data
list2 = [25, 20, 14, 56, 88]  # list with integer type of data
list3 = [23.66, 76.66, 56.0, 66.67]  # list with float type of data
list4 = ['anurag', 1022, 'male', 43, 244343.003]  # list with various type of data
list5 = []  # empty list with no data

# display list items and length of each of the list
print(f'list1 is {list1}\tLength of list1 is {len(list1)}')
'''
Output:
list1 is ['karthik', 'Rini', 'ISHANI', 'Kaustubh']	Length of list1 is 4
'''
print(f'list2 is {list2}\tLength of list2 is {len(list2)}')
'''
Output:
list2 is [25, 20, 14, 56, 88]	Length of list2 is 5
'''
print(f'list3 is {list3}\tLength of list3 is {len(list3)}')
'''
Output:
list3 is [23.66, 76.66, 56.0, 66]	Length of list3 is 4
'''
print(f'list4 is {list4}\tLength of list4 is {len(list4)}')
'''
Output:
list4 is ['anurag', 1022, 'male', 43, 244343.003]	Length of list4 is 5
'''
print(f'list5 is {list5}\tLength of list5 is {len(list5)}')
'''
Output:
list5 is []	Length of list5 is 0
'''

# Accessing using [] and :
print(f'list1[{0}] is {list1[0]}')
'''
Output:
list1[0] is karthik
'''
print(f'list2[{2}] is {list2[2]}')
'''
Output:
list2[2] is 14
'''
print(f'list3[{-2}] is {list3[-2]}')
'''
Output:
list3[-2] is 56.0
'''
print(f'lsit4[{-3}] is {list4[-3]}')
'''
Output:
lsit4[-3] is male
'''

# list indexing and splitting
print(f'list1[{0}:{2}] is {list1[0:2]}')
'''
Output:
list1[0:2] is ['karthik', 'Rini']
'''
print(f'list1[{0}:] is {list1[0:]}')
'''
Output:
list1[0:] is ['karthik', 'Rini', 'ISHANI', 'Kaustubh']
'''
print(f'list1[{2}:{4}] is {list1[1:4]}')
'''
Output:
list1[2:4] is ['Rini', 'ISHANI', 'Kaustubh']
'''
print(f'list1[:{2}] is {list1[:2]}')
'''
Output:
list1[:2] is ['karthik', 'Rini']
'''
print(f'list1[:] is {list1[:]}')
'''
Output:
list1[:] is ['karthik', 'Rini', 'ISHANI', 'Kaustubh']
'''
print(f'list1[{-4}:{-2}] is {list1[-4:-2]}')
'''
Output:
list1[-4:-2] is ['karthik', 'Rini']
'''

# list concatenation (+)
c1 = list1 + list2
c2 = list3 + list4
print(f'concatenation of list1 and list2 is {c1}')
'''
Output:
concatenation of list1 and list2 is ['karthik', 'Rini', 'ISHANI', 'Kaustubh', 25, 20, 14, 56, 88]
'''
print(f'concatenation of list3 and list4 is {c2}')
'''
concatenation of list3 and list4 is [23.66, 76.66, 56.0, 66.67, 'anurag', 1022, 'male', 43, 244343.003]
'''

# list repetition (*)
r1 = c1 * 2
r2 = c2 * 2
print(f'c1 * {2} is {r1}')
'''
Output:
c1 * 2 is ['karthik', 'Rini', 'ISHANI', 'Kaustubh', 25, 20, 14, 56, 88, 'karthik', 'Rini', 'ISHANI', 'Kaustubh', 25, 20, 14, 56, 88]
'''
print(f'c2 * {2} is {r2}')
'''
Output:
c2 * 2 is [23.66, 76.66, 56.0, 66.67, 'anurag', 1022, 'male', 43, 244343.003, 23.66, 76.66, 56.0, 66.67, 'anurag', 1022, 'male', 43, 244343.003]
'''

