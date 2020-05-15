import collections as c

# namedtuple syntax
student = c.namedtuple('student', ['name', 'age', 'marks'])
s1 = student('karthik', 40, 180)

print(f'student tuple is {student}')
'''
Output:
student tuple is <class '__main__.student'>
'''

print(f'"type(student)" is {type(student)}')
'''
Output:
"type(student)" is <class 'type'>
'''

print(f'namedtuple s1 is {s1}')
'''
Output:
namedtuple s1 is student(name='karthik', age=40, marks=180)
'''

# accessing the tuple elements using field type - name, age, marks
print(f'"s1.name" is {s1.name}')
print(f'"s1.age" is {s1.age}')
print(f'"s1.marks" is {s1.marks}')
'''
Output:
"s1.name" is karthik
"s1.age" is 40
"s1.marks" is 180
'''

# accessing the namedtuple values using index - 0, 1, 2, etc...
print(f'"s1[0]" is {s1[0]}')
print(f'"s1[1]" is {s1[1]}')
print(f'"s1[2]" is {s1[2]}')
'''
Output:
"s1[0]" is karthik
"s1[1]" is 40
"s1[2]" is 180
'''