# superset(days1>days2), subset(days1<days2), equivalent(days1==days2) using comparision operators
days1 = {'monday', 'tuesday', 'wednesday', 'thursday'}
days2 = {'monday', 'tuesday'}
days3 = {'monday', 'tuesday', 'friday', 'saturday', 'sunday'}

print(f'days1 is {days1}')
print(f'days2 is {days2}')
print(f'days3 is {days3}')
'''
Output:
days1 is {'wednesday', 'thursday', 'monday', 'tuesday'}
days2 is {'monday', 'tuesday'}
days3 is {'friday', 'monday', 'saturday', 'sunday', 'tuesday'}
'''

s1 = days1 > days2  # days1 is superset of days2
print(f'days1 is superset of days2 is {s1}')
'''
Output:
days1 is superset of days2 is True
'''
s2 = days2 > days1  # days2 is subset of days1
print(f'days2 is subset of days1 is {s2}')
'''
Output:
days2 is superset of days1 is False
'''
s3 = days1 < days2  # days1 is subset of days2
print(f'days1 is subset of days2 is {s3}')
'''
Output:
days1 is subset of days2 is False
'''
s4 = days2 < days1  # days2 is subset of days1
print(f'days2 is subset of days1 is {s4}')
'''
Output:
days2 is subset of days1 is True
'''
s5 = days1 > days3  # days1 is the superset of days3
print(f'days1 is the superset of days3 is {s5}')
'''
Output:
days1 is the superset of days3 is False
'''
s6 = days1 < days3  # days1 is the subset of days3
print(f'days1 is the subset of days3 is {s6}')
'''
Output:
days1 is the subset of days3 is False
'''
s7 = days3 > days1  # days3 is the superset of days1
print(f'days3 is the superset of days1 is {s7}')
'''
Output:
days3 is the superset of days1 is False
'''
s8 = days3 < days1  # days3 is the subset of days1
print(f'days3 is the subset of days1 is {s8}')
'''
Output:
days3 is the subset of days1 is False
'''

# set equivalence using == operator
print(f'"(days1 == days2)" is {days1 == days2}')
'''
Output:
"(days1 == days2)" is False
'''
print(f'"(days1 == days3)" is {days1 == days3}')
'''
Output:
"(days1 == days3)" is False
'''
print(f'"(days2 == days3)" is {days2 == days3}')
'''
Output:
"(days2 == days3)" is False
'''