s = 1  # global definition of variable s


def func1():
    name = 'karthik'
    emp_id = 32342344
    print(f'name is {name}, empid is {emp_id}')


def func2():
    name = 'Ishani'
    emp_id = 65645643
    print(f'name is {name}, empid is {emp_id}')


def func3():
    s = 0  # local definition of variable s
    print(f's value inside the function is {s}')


def func4():
    func1()
    func2()
    func3()


# func1()
'''
Output:
name is karthik, empid is 32342344
'''

# func2()
'''
Output:
name is Ishani, empid is 65645643
'''

# func3()
'''
Output:
s value inside the function is 0
'''

func4()

print(f's value outside function is {s}')
'''
Output:
s value outside function is 1
'''

# print(f'name is {name}')
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Functions/Function-ScopeOfVariables.py", line 53, in <module>
    print(f'name is {name}')
NameError: name 'name' is not defined
'''