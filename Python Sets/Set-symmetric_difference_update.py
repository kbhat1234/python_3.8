set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

print("--------------------------------------set1.symmetric_difference_update(set2)-----------------------------")
set1.symmetric_difference_update(set2)
print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')
'''
Output:
set1 is {1, 4}
set2 is {2, 3, 4}
set3 is {3, 4, 5}
'''
print("-------------------------------set2.symmetric_difference_update(set1)----------------------------")
set2.symmetric_difference_update(set1)
print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')
'''
Output:
set 1 is {1, 4}
set 2 is {1, 2, 3}
set 3 is {3, 4, 5}
'''

print("------------------------set1.symmetric_difference_update(set3)---------------------------------")
set1.symmetric_difference_update(set3)
print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')
'''
Output:
set1 is {1, 3, 5}
set 2 is {1, 2, 3}
set 3 is {3, 4, 5}
'''

print("--------------------------------------set3.symmetric_difference_update(set1)--------------------------")
set3.symmetric_difference_update(set1)
print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')
'''
Output:
set1 is {1, 3, 5}
set 2 is {1, 2, 3}
set 3 is {1, 4}
'''

print("-----------------------------------------set2.symmetric_difference_update(set3)-------------------------")
set2.symmetric_difference_update(set3)
print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')
'''
Output:
set1 is {1, 3, 5}
set 2 is {2, 3, 4}
set 3 is {1, 4}
'''

print("------------------------------set3.symmetric_difference_update(set2)----------------------------------")
set3.symmetric_difference_update(set2)
print(f'set1 is {set1}')
print(f'set2 is {set2}')
print(f'set3 is {set3}')
'''
Output:
set1 is {1, 3, 5}
set 2 is {2, 3, 4}
set 3 is {1, 2, 3}
'''