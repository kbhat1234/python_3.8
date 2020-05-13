import json as j


# functions definition defined here
def dic_display():
    print(student['fname'])
    print(student['salary'])
    print(student['gender']['man'])
    print(student['contact no'])
    print(student['landline'])
    print(type(student))
    print(type(d1))
    print(f'student dic is {student}')


def tup_display():
    print(student1[0])
    print(student1[:2])
    print(student1[-1])
    print(f'student1 tup is {student1}')
    print(type(student1))
    print(type(d2))


def li_display():
    print(f'student2 list is {student2}')
    print(type(student2))
    print(type(d3))
    print(student2[0:2])
    print(student2[-3])


# student dictionary
student = {
    'fname': 'Karthik',
    'lname': 'Bhat',
    'mname': 'K',
    'age': 40,
    'salary': 2500000.77,
    'gender': {'man': 'male', 'woman': 'female'},
    'contact no': True,
    'mobile': 9886867677,
    'landline': None
}

# convert python dictionary object to JSON string
d1 = j.dumps(student)
print(f'convert python object (dictionary) to JSON string is \n{d1}')
dic_display()
'''
Output:
convert python object (dictionary) to JSON string is 
{"fname": "Karthik", "lname": "Bhat", "mname": "K", "age": 40, "salary": 2500000.77, "gender": {"man": "male", "woman": "female"}, "contact no": true, "mobile": 9886867677, "landline": null}
Karthik
2500000.77
male
True
None
<class 'dict'>
<class 'str'>
student dic is {'fname': 'Karthik', 'lname': 'Bhat', 'mname': 'K', 'age': 40, 'salary': 2500000.77, 'gender': {'man': 'male', 'woman': 'female'}, 'contact no': True, 'mobile': 9886867677, 'landline': None}
'''

# student1 tuple
student1 = ('karthik', 23233, 40, 3423434.232)

# convert python tuple object to JSON string
d2 = j.dumps(student1)
print(f'convert python object (tuple) to JSON string is \n{d2}')
tup_display()
'''
Output:
convert python object (tuple) to JSON string is 
["karthik", 23233, 40, 3423434.232]
karthik
('karthik', 23233)
3423434.232
student1 tup is ('karthik', 23233, 40, 3423434.232)
<class 'tuple'>
<class 'str'>
'''

# student2 list
student2 = ['ishani', 'kaustubh', 'rini', 'karthik']

# convert python list object to JSON string
d3 = j.dumps(student2)
print(f'convert python object (list) to JSON string is \n{d3}')
li_display()
'''
Output:
convert python object (list) to JSON string is 
["ishani", "kaustubh", "rini", "karthik"]
student2 list is ['ishani', 'kaustubh', 'rini', 'karthik']
<class 'list'>
<class 'str'>
['ishani', 'kaustubh']
kaustubh
'''