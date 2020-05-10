def SimpleInterestCalculator(p, t, r):
    print('----------simple interest calculator---------')
    return (p*t*r)/100


def func1(name, message):
    print(f'{name} {message}')


def func2(name1, message, name2):
    print(f'{name1} {message} {name2}')


# The function SimpleInterestCalculator(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case
print(f'simple interest is {SimpleInterestCalculator(p=100000, t=1, r=6.3)}')
'''
Output:
----------simple interest calculator---------
simple interest is 6300.0
'''

# The function SimpleInterestCalculator(t, r, p) is called with the keyword arguments the order of arguments doesn't matter in this case
print(f'simple interest is {SimpleInterestCalculator(t=1, r=7.3, p=100000)}')
'''
Output:
----------simple interest calculator---------
simple interest is 7300.0
'''

# The function SimpleInterestCalculator(r, p, t) is called with the keyword arguments the order of arguments doesn't matter in this case
print(f'simple interest is {SimpleInterestCalculator(r=9, p=100000, t=2)}')
'''
Output:
----------simple interest calculator---------
simple interest is 18000.0
'''

# function func1 is called with the name and message as the keyword arguments
func1(name='karthik', message='hello')
'''
Output:
karthik hello
'''

# function func1 is called with the name and message as the keyword arguments
func1(message='hello', name='karthik')
'''
Output:
karthik hello
'''

# doesn't find the exact match of the name of the arguments (keywords)
# print(SimpleInterestCalculator(pr=100000, tr=1, rt=6.3))
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Functions/Function-KeywordArguments.py", line 15, in <module>
    print(SimpleInterestCalculator(pr=100000, tr=1, rt=6.3))
TypeError: SimpleInterestCalculator() got an unexpected keyword argument 'pr'
'''

func2('karthik', message='welcome to', name2='bhat')
'''
Output:
karthik welcome to bhat
'''

# func2('karthik', message='welcome to', 'bhat')
'''
Output:
"C:\Program Files\Python38\python.exe" C:/Users/karth/PycharmProjects/PythonPackage/Programs/Functions/Function-KeywordArguments.py
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Functions/Function-KeywordArguments.py", line 63
    func2('karthik', message='welcome to', 'bhat')
                                           ^
SyntaxError: positional argument follows keyword argument
'''

func2('karthik', 'welcome to', name2='bhat')
'''
Output:
karthik welcome to bhat
'''

func2('karthik', 'welcome to', 'bhat')
'''
Output:
karthik welcome to bhat
'''