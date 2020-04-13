dic = {1: 'software engineer', 2: 'Doctor', 3: 'Accountant', 4: 'Sportsman', 5: 'hardware engineer', 6: {'A': 'support', 'B':'front end', 'C': 'back end'}}
print(dic)

"""
Output:
{1: 'software engineer', 2: 'Doctor', 3: 'Accountant', 4: 'Sportsman', 5: 'hardware engineer', 6: {'A': 'support', 'B': 'front end', 'C': 'back end'}}
"""

print(dic.keys())
print(dic.values())
print(len(dic))
"""
Output:
dict_keys([1, 2, 3, 4, 5, 6])
dict_values(['software engineer', 'Doctor', 'Accountant', 'Sportsman', 'hardware engineer', {'A': 'support', 'B': 'front end', 'C': 'back end'}])
6
"""

# deleting a key value
del dic[1]
print(dic)
"""
Output:
{2: 'Doctor', 3: 'Accountant', 4: 'Sportsman', 5: 'hardware engineer', 6: {'A': 'support', 'B': 'front end', 'C': 'back end'}}
"""

print(dic.keys())
print(dic.values())
print(len(dic))
"""
Output:
dict_keys([2, 3, 4, 5, 6])
dict_values(['Doctor', 'Accountant', 'Sportsman', 'hardware engineer', {'A': 'support', 'B': 'front end', 'C': 'back end'}])
5
"""

# deleting a key from nested dictionary
del dic[6]['B']
print(dic)
"""
Output:
{2: 'Doctor', 3: 'Accountant', 4: 'Sportsman', 5: 'hardware engineer', 6: {'A': 'support', 'C': 'back end'}}
"""

print(dic.keys())
print(dic.values())
print(len(dic))
"""
Output:
dict_keys([2, 3, 4, 5, 6])
dict_values(['Doctor', 'Accountant', 'Sportsman', 'hardware engineer', {'A': 'support', 'C': 'back end'}])
5
"""

# deleting entire dictionary
# del Dict will delete the entire dictionary and hence printing it after deletion will raise an Error.
#del dic
#print(dic)
"""
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/RemovingElementsDictionary.py", line 57, in <module>
    print(dic)
NameError: name 'dic' is not defined
"""