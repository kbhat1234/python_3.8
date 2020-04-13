"""
==, !=, >, <, >=, <= comparision operators
"""
temp = 35

if temp >= 35:
    print('hot day')
elif temp <= 25:
    print('warm pleasant day')
else:
    print('Weather is good')

print('end of weather report')

name = input('enter name here ')
n = len(name)
if n < 3:
    print('name must be atleast 3 characters long')
elif n > 50:
    print('name can be a maximum of 50 characters long')
else:
    print(f'name looks good, name is {name}')

print('Have a nice day')


a = 5
b = 5
c = 3
# != comparison operator
if a != b:
    print('a is not equal to b')
else:
    print('a is equal to b')
print('end of program')

# == comparison operator
if a == b:
    print('a is equal to b')
else:
    print('a is not equal to b')
print('end of program')

# > comparison operator
if a > b and a > c:
    print('a is greater')
elif b > a and b > c:
    print('b is greater')
elif c > a and c > b:
    print('c is greater')
else:
    print('Hello World')
print('end of program')

# < comparison operator
if a < b:
    print('a is less than b')
elif b < a:
    print('b is less than a')
else:
    print('a and b are equal')
print('end of program')

temperature = 15
# >=, <= comparison operator
if temperature >= 35:
    print('Very hot day ahead')
elif temperature >= 25 and temperature < 35:
    print('sunny day ahead')
elif temperature >= 16 and temperature < 25:
    print('chilly day ahead')
else:
    print('very cold weather ahead')
print('end of program')