def func1(name, age=22):
    print(f'My name is {name}, and My age is {age}')


def func2(name, age=30):
    print(f'My name is {name}, and My age is {age}')


# func1() call is having name='karthik' as keyword argument and do not have age parameter passed
# but age is defined in the func1() definition
func1(name='karthik')
'''
Output:
My name is karthik, and My age is 22
'''

# func2() call is having 2 arguments passed as name='karthik' and age=33, but on func2() definition age=30
# this will override the value of defintion and assign age value to 33.
func2(name='karthik', age=33)
'''
Output:
My name is karthik, and My age is 33
'''