import json as j

# tuple tup
tup = (10, 20, 30, 40, 50, 60)
print(f'"type(tup)" is {type(tup)}')
print(f'tup elements is {tup}')
'''
Output:
"type(tup)" is <class 'tuple'>
tup elements is (10, 20, 30, 40, 50, 60)
'''

# convert python object (tuple) to JSON string object
d1 = j.dumps(tup)
print(f'"type(d1)" is {type(d1)}')
print(f'converting python object (tuple) to JSON string object is {d1}')
'''
Output:
"type(d1)" is <class 'str'>
converting python object (tuple) to JSON string object is [10, 20, 30, 40, 50, 60]
'''

# convert JSON string object to python object
d2 = j.loads(d1)
print(f'converting JSON string object to python object is {d2}')
print(f'"type(d2)" is {type(d2)}')
'''
Output:
converting JSON string object to python object is [10, 20, 30, 40, 50, 60]
"type(d2)" is <class 'list'>
'''

# dictionary dict1
dict1 ={
    'name': 'karthik',
    'age': 40,
    'gender': {'man': 'male', 'woman': 'female'},
    'address': {'street': 'anurag old state bank lane', 'area': 'volakadu', 'city': 'udupi', 'state': 'karnataka'},
    'office address': False,
    'home address': True,
    'landline no': None
}

print(f'dict1 elements is {dict1}')
print(f'"type(dict1)" is {type(dict1)}')
'''
Output:
dict1 elements is {'name': 'karthik', 'age': 40, 'gender': {'man': 'male', 'woman': 'female'}, 'address': {'street': 'anurag old state bank lane', 'area': 'volakadu', 'city': 'udupi', 'state': 'karnataka'}, 'office address': False, 'home address': True, 'landline no': None}
"type(dict1)" is <class 'dict'>
'''

# convert python object (dictionary) to JSON string object
d3 = j.dumps(dict1)
print(f'"type(d3)" is {type(d3)}')
print(f'converting python object to JSON string object is {d3}')
'''
Output:
"type(d3)" is <class 'str'>
converting python object to JSON string object is {"name": "karthik", "age": 40, "gender": {"man": "male", "woman": "female"}, "address": {"street": "anurag old state bank lane", "area": "volakadu", "city": "udupi", "state": "karnataka"}, "office address": false, "home address": true, "landline no": null}
'''

# convert JSON string object to python object
d4 = j.loads(d3)
print(f'"type(d4)" is {type(d4)}')
print(f'converting JSON string object to python object is {d4}')
'''
Output:
"type(d4)" is <class 'dict'>
converting JSON string object to python object is {'name': 'karthik', 'age': 40, 'gender': {'man': 'male', 'woman': 'female'}, 'address': {'street': 'anurag old state bank lane', 'area': 'volakadu', 'city': 'udupi', 'state': 'karnataka'}, 'office address': False, 'home address': True, 'landline no': None}
'''

# list li
li = [10, 20, ['karthik', 'rini', 'kaustubh'], 20.433, True, False, None]
print(f'"type(li)" is {type(li)}')
print(f'li elements is {li}')
print(li[1])
print(li[2][1])
print(li[2])
'''
Output:
"type(li)" is <class 'list'>
li elements is [10, 20, ['karthik', 'rini', 'kaustubh'], 20.433, True, False, None]
20
rini
['karthik', 'rini', 'kaustubh']
'''

# convert python object list to JSON string object
d5 = j.dumps(li)
print(f'"type(d5)" is {type(d5)}')
print(f'converting python object to JSON string object is {d5}')
'''
Output:
"type(d5)" is <class 'str'>
converting python object to JSON string object is [10, 20, ["karthik", "rini", "kaustubh"], 20.433, true, false, null]
'''

# convert JSON string object to python object
d6 = j.loads(d5)
print(f'"type(d6)" is {type(d6)}')
print(f'coverting JSON string object to python object is {d6}')
'''
Output:
"type(d6)" is <class 'list'>
coverting JSON string object to python object is [10, 20, ['karthik', 'rini', 'kaustubh'], 20.433, True, False, None]
'''

# string str1
str1 = "welcome to jungle"
print(f'str1 is {str1}')
print(f'"type(str1)" is {type(str1)}')
'''
Output:
str1 is welcome to jungle
"type(str1)" is <class 'str'>
'''

# convert python object String to JSON string object
d7 = j.dumps(str1)
print(f'"type(d7)" is {type(d7)}')
print(f'converting python object to JSON string object is {d7}')
'''
Output:
"type(d7)" is <class 'str'>
converting python object to JSON string object is "welcome to jungle"
'''

# converting JSON string object to python object
d8 = j.loads(d7)
print(f'"type(d8)" is {type(d8)}')
print(f'converting JSON object to python object is {d8}')
'''
Output:
"type(d8)" is <class 'str'>
converting JSON object to python object is welcome to jungle
'''