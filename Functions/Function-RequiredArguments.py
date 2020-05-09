# the argument name is the required argument to the function function
def func1(name):
    print(f'hello {name}')


def func2(name):
    message = 'hello ' + name
    return message


def simpleInterest(a, b, c):
    print(f'principle is {a}')
    print(f'term is {b}')
    print(f'rate of interest is {c}')
    return (a*b*c)/100


def SimpleInterest(x, y, z):
    print(f'principle is {x}')
    print(f'term is {y}')
    print(f'rate of interest is {z}')
    si = (x*y*z)/100
    print(f'simple interest is {si}')


def compute(a, b):
    return a * b


n = input('enter name ')
func1(n)  # func1(n) calling with parameter n
'''
Output:
enter name karthik
hello karthik
'''

print(func2(n))  # func2(n) calling with parameter n with return for printing
'''
Output:
hello karthik
'''

# simple interest calculator
p = float(input('enter principle '))
t = float(input('enter term '))
r = float(input('enter rate of interest '))
print(f'simpleInterest({p}, {t}, {r}) is {simpleInterest(p, t, r)}')
'''
Output:
enter principle 100000
enter term 1
enter rate of interest 4.4
principle is 100000.0
term is 1.0
rate of interest is 4.4
simpleInterest(100000.0, 1.0, 4.4) is 4400.000000000001
'''

SimpleInterest(p, t, r)  # calling function SimpleInterest() with arguments p, t, r
'''
Output:
principle is 100000.0
term is 1.0
rate of interest is 4.4
simple interest is 4400.000000000001
'''

print(f'compute is {compute(10, 20)}')
'''
Output:
compute is 200
'''

# print(compute(10))
'''
Output:
Traceback (most recent call last):
  File "C:/Users/karth/PycharmProjects/PythonPackage/Programs/Functions/Function-RequiredArguments.py", line 75, in <module>
    print(compute(10))
TypeError: compute() missing 1 required positional argument: 'b'
'''


