import json as j


def dic_display():
    print(f'dic1 elements is {dic1}')
    print(f'"type(d1)" is {type(dic1)}')


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
    'gender': {'man': 'male', 'woman': 'female'},
    'mobile no': None,
    'is_profile': True
}
dic_display()
'''
Output:
dic1 elements is {'fname': 'karthik', 'lname': 'bhat', 'age': 40, 'gender': {'man': 'male', 'woman': 'female'}, 'mobile no': None, 'is_profile': True}
"type(d1)" is <class 'dict'>
'''

# convert (serialize) python object dictionary to JSON string object
with open('json files/dic1.json', 'w') as w:
    j.dump(dic1, w)
    w.close()
'''
Output:
dic1.json is created and dictionary data is written to file.
'''

# convert (deserialize) JSON string object to python object
with open('json files/dic1.json', 'r') as r:
    l1 = j.load(r)
    print(f'convert JSON file contents to python dictionary object {l1}')
    print(f'"type(l1)" is {type(l1)}')
    r.close()
'''
Output:
convert JSON file contents to python dictionary object {'fname': 'karthik', 'lname': 'bhat', 'age': 40, 'gender': {'man': 'male', 'woman': 'female'}, 'mobile no': None, 'is_profile': True}
"type(l1)" is <class 'dict'>
'''

# tuple tup
tup = (20, 10, 'karthik', 343.333, True, False, None)
tup_display()
'''
Output:
tup elements is (20, 10, 'karthik', 343.333, True, False, None)
"type(tup)" is <class 'tuple'>
'''

# convert (serialize) python object tuple to JSON string object
with open('json files/tup.json', 'w') as w:
    j.dump(tup, w)
    w.close()
'''
Output:
tup.json file is created and tup data is written to the file.
'''

# convert (deserialize) JSON string object to python object
with open('json files/tup.json', 'r') as r:
    l2 = j.load(r)
    print(f'convert JSON file contents to python tuple object {l2}')
    print(f'"type(l2)" is {type(l2)}')
    r.close()
'''
Output:
convert JSON file contents to python tuple object [20, 10, 'karthik', 343.333, True, False, None]
"type(l2)" is <class 'list'>
'''

# list li
li = ['karthik', 'rini', 'ishani', 'kaustubh', True, False, None]
li_display()
'''
Output:
li elements is ['karthik', 'rini', 'ishani', 'kaustubh', True, False, None]
"type(li)" is <class 'list'>
'''

# convert (serialize) python object list to JSON string object
with open('json files/li.json', 'w') as w:
    j.dump(li, w)
    w.close()
'''
Output:
li.json file is been created and li data is written to file.
'''

# convert (deserialize) JSON string object to python object
with open('json files/li.json', 'r') as r:
    l3 = j.load(r)
    print(l3)
    print(type(l3))
    r.close()
'''
Output:
['karthik', 'rini', 'ishani', 'kaustubh', True, False, None]
<class 'list'>
'''