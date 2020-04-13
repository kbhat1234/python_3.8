# creating a dictionary with integer keys
dic1 = {1: 'Python', 2: 'Java', 3: 'C#', 4: 'Java script', 5: 'C'}

print(dic1)
"""
Output:
{1: 'Python', 2: 'Java', 3: 'C#', 4: 'Java script', 5: 'C'}
"""

print(f'{dic1[1]} \n{dic1[2]} \n{dic1[3]} \n{dic1[4]} \n{dic1[5]}')
"""
Output:
Python 
Java 
C# 
Java script 
C
"""

print(str(dic1))
"""
Output:
{1: 'Python', 2: 'Java', 3: 'C#', 4: 'Java script', 5: 'C'}
"""

print(dic1.keys())
print(dic1.values())
"""
Output:
dict_keys([1, 2, 3, 4, 5])
dict_values(['Python', 'Java', 'C#', 'Java script', 'C'])
"""

# creating a dictionary with mixed keys
dic2 = {1: 2345, 'color': 'red', 'gender': ['male', 'female']}

print(dic2)
"""
Output:
{1: 2345, 'color': 'red', 'gender': ['male', 'female']}
"""

print(dic2.keys())
print(dic2.values())
"""
Output:
dict_keys([1, 'color', 'gender'])
dict_values([2345, 'red', ['male', 'female']])
"""

print(f"{dic2[1]} \n{dic2['color']} \n{dic2['gender'][0]} \n{dic2['gender'][1]}")
"""
Output:
2345 
red 
male 
female
"""
print(str(dic2))

# creating an empty dictionary
dic3 = {}

print(f'{dic3}')
"""
Output:
{}
"""

# creating a dictionary using dict() method
dic4 = dict({1: 'red', 2: 'orange', 3: 'yellow'})

print(f'{dic4}')
"""
Output:
{1: 'red', 2: 'orange', 3: 'yellow'}
"""

# creating a dictionary with each item as a pair using dict() method
dic5 = dict([(10, 'dog'), (20, 'cat'), (30, 'bird')])

print(dic5)
"""
Output:
{10: 'dog', 20: 'cat', 30: 'bird'}
"""