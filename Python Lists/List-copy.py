# copy() method used to copy elements of one list to another
originallist = [20, 30, 10, 40]
copylist = []  # empty list
# 1. copy using list copy() method
copylist = originallist.copy()
print(f'original list is {originallist}')
'''
Output:
original list is [20, 30, 10, 40]
'''

print(f'copylist list is {copylist}')
'''
Output:
copylist list is [20, 30, 10, 40]
'''

# 2. copy using slice operation [:]
orlist = [30, 37, 22, 45]
colist = []  # empty list
colist = orlist[:]  # copy all elements from list orlist to colist
print(f'original list is {orlist}')
'''
Output:
original list is [30, 37, 22, 45]
'''

print(f'copylist is {colist}')
'''
Output:
copylist is [30, 37, 22, 45]
'''

# 3. copy list using assignment operator (=)
orglist = [20, 88, 34, 66]
coplist = []
coplist = orglist
print(f'original list is {orglist}')
'''
Output:
original list is [20, 88, 34, 66]
'''

print(f'copylist list is {coplist}')
'''
Output:
copylist list is [20, 88, 34, 66]
'''