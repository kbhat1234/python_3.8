# identity operators
x1 = [5, 'karthik', 3434.44]

if type(x1[0]) is int:
    print('value is of integer')
else:
    print('value is other datatypes')

"""
Output:
value is of integer
"""

if type(x1[1]) is str:
    print('value is of string')
else:
    print('value is other datatypes')

"""
Output:
value is of string
"""

if type(x1[2]) is float:
    print('value is of float')
else:
    print('value is other datatypes')

"""
Output:
value is of float
"""

x2 = [223.34, 23, 'rini']
if type(x2[0]) is not int:
    print('value is not integer')
else:
    print('value is an integer')

"""
Output:
value is not integer
"""

if type(x2[1]) is not str:
    print('value is not string')
else:
    print('value is an string')

"""
Output:
value is not string
"""

if type(x2[2]) is not float:
    print('value is not float')
else:
    print('value is an float')

"""
Output:
value is not float
"""

x = 'welcome'
if type(x) is str:
    print(f'value of x is string')
else:
    print(f'value of x is not string')

"""
Output:
value of x is string
"""

if type(x) is not int:
    print(f'value of x is not integer')
else:
    print(f'value of x is a string')

"""
Output:
value of x is not integer
"""

tuple = ('rini', 20.773, 89, "ishani")

if type(tuple[1]) is float:
    print(f'{tuple[1]} is of float data type')
else:
    print(f'{tuple[1]} is not of float date type')

"""
Output:
20.773 is of float data type
"""

if type(tuple[2]) is not str:
    print(f'{tuple[2]} is not of string data type')
else:
    print(f'{tuple[2]} is of string data type')

"""
Output:
89 is not of string data type
"""

dic = {'name': 'karthik', 'roll no': 3343, 'class': 5}

if type(dic['name']) is str:
    print(f"{dic['name']} is of string type")
else:
    print(f"{dic['name']} is not of string type")

"""
Output:
karthik is of string type
"""

if type(dic['roll no']) is int:
    print(f"{dic['roll no']} is of integer type")
else:
    print(f"{dic['roll no']} is not of integer type")

"""
Output:
3343 is of integer type
"""