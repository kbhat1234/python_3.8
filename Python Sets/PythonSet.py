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

# adding tuple to set
# set of vowels
vowels = {'a', 'i', 'u'}
# tuple of ('e', 'o')
tup = ('e', 'o')
print(f'vowels set is {vowels}')
print(f'tuple is {tup}')
vowels.add(tup)
print(f'adding tuple to set is {vowels}')

# adding again same tuple
vowels.add(tup)  # it will not add again the tup to set
print(f'adding again tuple to set is {vowels}')

