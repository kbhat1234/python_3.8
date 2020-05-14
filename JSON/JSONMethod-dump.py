import json as j


def dic_display():
    print(type(student))
    print(student)
    print(student['firstname'])
    print(student['rollno'])
    print(student['subject'][-1])
    print(student['subject'])
    print(student['gender'])
    print(student['gender']['man'])
    print(student['gender']['woman'])


def tup_display():
    print(f'student1 tuple is {student1}')
    print(type(student1))
    print(student1[2:])
    print(student1[-3])


def li_display():
    print(f'student2 list is {student2}')
    print(type(student2))
    print(student2[2])


# student dictionary
student = {
    'firstname': 'Karthik',
    'lastname': 'Bhat',
    'rollno': 534535,
    'grade': 'A',
    'subject': ['english', 'maths', 'computers'],
    'gender': {'man': 'male', 'woman': 'female'}
}

# open or create a file with write mode to student.json
with open('json files/student.json', 'w') as file_write:
    # using dump() function, convert python data object (dictionary) to JSON data object and write to file
    j.dump(student, file_write)
    file_write.close()
dic_display()
'''
Output:
<class 'dict'>
{'firstname': 'Karthik', 'lastname': 'Bhat', 'rollno': 534535, 'grade': 'A', 'subject': ['english', 'maths', 'computers'], 'gender': {'man': 'male', 'woman': 'female'}}
Karthik
534535
computers
['english', 'maths', 'computers']
{'man': 'male', 'woman': 'female'}
male
female
'''

# student1 tuple
student1 = ('karthik', 20, 20033.88, 'male')

# open or create file with open mode to write to student1.json
with open('json files/student1.json', 'w') as file_write:
    j.dump(student1, file_write)
    file_write.close()
tup_display()
'''
Output:
student1 tuple is ('karthik', 20, 20033.88, 'male')
<class 'tuple'>
(20033.88, 'male')
20
'''

# student2 list
student2 = ['karthik', 20, 20033.88, 'male']

# open or create file with write mode to student2.json
with open('json files/student2.json', 'w') as file_write:
    j.dump(student2, file_write)
    file_write.close()
li_display()
'''
Output:
student2 list is ['karthik', 20, 20033.88, 'male']
<class 'list'>
20033.88
'''
