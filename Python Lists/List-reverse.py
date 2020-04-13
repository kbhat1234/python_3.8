# reverse() will reverse the elements of the given list
list = ['a', 'p', 'p', 'l', 'e']
print(f'original list is {list}')
list.reverse()  # reverses the elements of list
print(f'reversed list is {list}')

# reversing the already empty list
l = []
print(f'original list is {l}')
l.reverse()  # reversing the empty list
print(f'reversed empty list is {l}')

# reversing 1 list and comparing the lists equal or not
l1 = ['a', 'p', 'p', 'l', 'e']
l2 = ['e', 'l', 'p', 'p', 'a']

print(f'original list l1 is {l1}')
print(f'original list l2 is {l2}')
# reverse either l1 and l2
l1.reverse()
print(f'reversed list l1 is {l1}')

if l1 == l2:
    print(f'lists l1 and l2 are equal')
else:
    print(f'lists l1 and l2 are not equal')

'''
Output:
original list is ['a', 'p', 'p', 'l', 'e']
reversed list is ['e', 'l', 'p', 'p', 'a']
original list is []
reversed empty list is []
original list l1 is ['a', 'p', 'p', 'l', 'e']
original list l2 is ['e', 'l', 'p', 'p', 'a']
reversed list l1 is ['e', 'l', 'p', 'p', 'a']
lists l1 and l2 are equal
'''


