# symmetric difference - it will create the set with elements which are not common in both the sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')

sd1 = set1.symmetric_difference(set2)
print(f'"set1.symmetric_difference(set2)" is {sd1}')
'''
Output:
"set1.symmetric_difference(set2)" is {1, 4}
'''

sd2 = set2.symmetric_difference(set1)
print(f'"set2.symmetric_difference(set1)" is {sd2}')
'''
"set2.symmetric_difference(set1)" is {1, 4}
'''

sd3 = set1.symmetric_difference(set3)
print(f'"set1.symmetric_difference(set3)" is {sd3}')
'''
"set1.symmetric_difference(set3)" is {1, 2, 4, 5}
'''

sd4 = set2.symmetric_difference(set3)
print(f'"set2.symmetric_difference(set3)" is {sd4}')
'''
"set2.symmetric_difference(set3)" is {2, 5}
'''

list1 = [10, 30, 14, 83]
list2 = [11, 30, 32, 14, 44]

# converting list to set using set() method
s1 = set(list1)
s2 = set(list2)

sd01 = s1.symmetric_difference(s2)
print(f'"s1.symmetric_difference(s2)" is {sd01}')
'''
"s1.symmetric_difference(s2)" is {10, 83, 11, 32, 44}
'''

sd02 = s2.symmetric_difference(s1)
print(f'"s2.symmetric_difference(s1)" is {sd02}')
'''
"s2.symmetric_difference(s1)" is {10, 83, 11, 32, 44}
'''