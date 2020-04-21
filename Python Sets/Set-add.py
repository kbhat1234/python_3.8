# adding set elements using add() method
set1 = set()  # empty set
print(f'original set elements is {set1}')
print(f'type(set1) is {type(set1)}')
'''
Output:
original set elements is set()
type(set1) is <class 'set'>
'''
# adding only numbers to set
set1.add(10)
set1.add(5)
set1.add(9)
set1.add(1)
set1.add(2)
print(f'set1 elements after add is {set1}')
'''
Output:
set1 elements after add is {1, 2, 5, 9, 10}
'''
# looping the set1 elements
for i in set1:
    print(i, end=' ')
print('\nend of loop')
'''
Output:
1 2 5 9 10
end of loop
'''

# adding only string to set
set2 = set()
print(f'original set elements is {set2}')
print(f'type(set2) is {type(set2)}')
'''
Output:
original set elements is set()
type(set2) is <class 'set'>
'''
set2.add('monday')
set2.add('tuesday')
set2.add('wednesday')
set2.add('thursday')
set2.add('friday')
set2.add('saturday')
set2.add('sunday')
print(f'after adding set2 elements is {set2}')
'''
Output:
after adding set2 elements is {'sunday', 'friday', 'wednesday', 'thursday', 'saturday', 'tuesday', 'monday'}
'''

# adding elements to set with mixed
set3 = {'apple', 23, 70.4, 'orange', 'karthik', 'a'}
print(f'original set3 elements is {set3}')
print(f'type(set3) is {type(set3)}')
'''
Output:
original set3 elements is {70.4, 'a', 'orange', 'apple', 23, 'karthik'}
type(set3) is <class 'set'>
'''
set3.add('apple')  # adding item which is already in the original set, not this item to set
set3.add(80)  # 80 will be added to set
set3.add('pineapple')  # pineapple will be added to set
print(f'set3 elements after add is {set3}')
'''
Output:
set3 elements after add is {'pineapple', 70.4, 'a', 80, 'orange', 'apple', 23, 'karthik'}
'''
cfdsfgdg