# creating the set using curly braces
days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
print(f'days is {days}')
print(f'type(days) is {type(days)}')
'''
Output:
days is {'sunday', 'saturday', 'friday', 'monday', 'wednesday', 'thursday', 'tuesday'}
type(days) is <class 'set'>
'''
print('.....looping the elements of days.....')
for i in days:
    print(i, end=', ')
print('\nend of loop')
'''
Output:
.....looping the elements of days.....
sunday, saturday, friday, monday, wednesday, thursday, tuesday, 
end of loop
'''

# creating the set using the set() method
months = set(['january', 'febrauary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'])
print(f'months is {months}')
print(f'type(months) is {type(months)}')
'''
Output:
months is {'june', 'september', 'october', 'january', 'may', 'march', 'febrauary', 'april', 'july', 'december', 'august', 'november'}
type(months) is <class 'set'>
'''
print('....looping elements of months....')
for i in months:
    print(i, end=', ')
print('\nend of loop')
'''
Output:
....looping elements of months....
june, september, october, january, may, march, febrauary, april, july, december, august, november, 
end of loop
'''

set2 = set([])
print(set2)
set2.add('karthik')
set2.update(['rini', 'ishani', 'kaustubh'])  # list
print(set2)
set2.clear()
print(set2)
set2.update({'karthik', 'rini', 'ishani'})  # set
print(set2)
set2.update({1: 'rini', 2: 'kaustubh'})  # dictionary
print(set2)
set2.update('mouse')  # string
print(set2)