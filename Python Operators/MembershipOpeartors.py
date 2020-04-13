# membership operators

s1 = '"Welcome to Python programming"'

if 'Python' in s1:
    print(f'Python is present in {s1}')
else:
    print(f'Psython is not present in {s1}')

"""
Output:
Python is present in "Welcome to Python programming"
"""

if 'python' not in s1:
    print(f'python is not present in {s1}')
else:
    print(f'python is present in {s1}')

"""
Output:
python is not present in "Welcome to Python programming"
"""

list = [20, 30, 15, 27]
if 30 in list:
    print(f'{list[1]} is present in list -> {list}')
else:
    print(f'{list[1]} is not present in list -> {list}')

"""
Output:
30 is present in list -> [20, 30, 15, 27]
"""

if 31 not in list:
    print(f'31 is not present in list -> {list}')
else:
    print(f'31 is present in list -> {list}')

"""
Output:
31 is not present in list -> [20, 30, 15, 27]
"""

tuple = (10, 29, 40, 35)
if 40 in tuple:
    print(f'40 is present in tuple -> {tuple}')
else:
    print(f'40 is not present in tuple -> {tuple}')

"""
Output:
40 is present in tuple -> (10, 29, 40, 35)
"""

if 32 not in tuple:
    print(f'32 is not present in tuple ->{tuple}')
else:
    print(f'32 is present in tuple -> {tuple}')

"""
Output:
32 is not present in tuple ->(10, 29, 40, 35)
"""

dic = {1: 'red', 2: 'orange', 3: 'yellow', 4: 'blue'}

if 'red' in dic.values():
    print(f'red value is present in {dic}')
else:
    print(f'red value is not present in {dic}')

"""
Output:
red value is present in {1: 'red', 2: 'orange', 3: 'yellow', 4: 'blue'}
"""

if 2 in dic.keys():
    print(f'2 key is present in {dic}')
else:
    print(f'2 key is not present in {dic}')

"""
Output:
2 key is present in {1: 'red', 2: 'orange', 3: 'yellow', 4: 'blue'}
"""

if 'purple' not in dic.values():
    print(f'purple value is not present in {dic}')
else:
    print(f'purple value is present in {dic}')

"""
Output:
purple value is not present in {1: 'red', 2: 'orange', 3: 'yellow', 4: 'blue'}
"""

if 5 not in dic.keys():
    print(f'5 key is not present in {dic}')
else:
    print(f'5 key is present in {dic}')

"""
Output:
5 key is not present in {1: 'red', 2: 'orange', 3: 'yellow', 4: 'blue'}
"""

