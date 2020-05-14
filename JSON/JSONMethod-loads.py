import json as j


def dic1_display():
    print(f'dic1 elements is {dic1}')
    print(f'"type(dic1)" is {type(dic1)}')


def tup_display():
    print(f'tup elements is {tup}')
    print(f'"type(tup)" is {type(tup)}')


def li_display():
    print(f'li elements is {li}')
    print(f'"type(li)" is {type(li)}')


# dictionary dic1
dic1 = {
    'fname': 'karthik',
    'lname': 'bhat',
    'age': 40,
    'gender': {'man': 'male', 'woman': 'female'}
}
dic1_display()
'''
Output:
dic1 elements is {'fname': 'karthik', 'lname': 'bhat', 'age': 40, 'gender': {'man': 'male', 'woman': 'female'}}
"type(dic1)" is <class 'dict'>
'''

d1 = j.dumps(dic1)
print(f'convert python object dic1 to JSON string object is \n{d1}')
print(f'"type(d1)" is {type(d1)}')
'''
Output:
convert python object dic1 to JSON string object is 
{"fname": "karthik", "lname": "bhat", "age": 40, "gender": {"man": "male", "woman": "female"}}
"type(d1)" is <class 'str'>
'''

d2 = j.loads(d1)
print(f'comvert JSON string object to python object is \n{d2}')
print(f'"type(d2)" is {type(d2)}')
'''
Output:
comvert JSON string object to python object is 
{'fname': 'karthik', 'lname': 'bhat', 'age': 40, 'gender': {'man': 'male', 'woman': 'female'}}
"type(d2)" is <class 'dict'>
'''

# tuple tup
tup = (10, 20, 20.3, 'karthik', 'rini', True, False, None)
tup_display()
'''
Output:
tup elements is (10, 20, 20.3, 'karthik', 'rini', True, False, None)
"type(tup)" is <class 'tuple'>
'''

d3 = j.dumps(tup)
print(f'convert python object tuple to JSON string object \n{d3}')
print(f'"type(d3)" is {type(d3)}')
'''
Output:
convert python object tuple to JSON string object 
[10, 20, 20.3, "karthik", "rini", true, false, null]
"type(d3)" is <class 'str'>
'''

d4 = j.loads(d3)
print(f'converts JSON object to python object \n{d4}')
print(f'"type(d4)" is {type(d4)}')
'''
Output:
converts JSON object to python object 
[10, 20, 20.3, 'karthik', 'rini', True, False, None]
"type(d4)" is <class 'list'>
'''

# list li
li = ['karthik', 'rini', True, False, None, 'a', 2020, 2723.6663]
li_display()
'''
Output:
li elements is ['karthik', 'rini', True, False, None, 'a', 2020, 2723.6663]
"type(li)" is <class 'list'>
'''

d5 = j.dumps(li)
print(f'convert python object list to JSON string object \n{d5}')
print(f'"type(d5)" is {type(d5)}')
'''
Output:
convert python object list to JSON string object 
["karthik", "rini", true, false, null, "a", 2020, 2723.6663]
"type(d5)" is <class 'str'>
'''

d6 = j.loads(d5)
print(f'convert JSON string object to python object \n{d6}')
print(f'"type(d6)" is {type(d6)}')
'''
Output:
convert JSON string object to python object 
['karthik', 'rini', True, False, None, 'a', 2020, 2723.6663]
"type(d6)" is <class 'list'>
'''