def Sum(x, y):
    return x + y


def Diff(x, y):
    return x - y


def Mul(x, y):
    return x * y


def Div(x, y):
    return x / y


def Mod(x, y):
    return x % y


def display():
    print(f'a is {a}')
    print(f'b is {b}')


def func1(name):
    print(f'name is {name}')
    hello_world()


def hello_world():
    print('Hello world program')


def simple_interest(pr, tr, rt):
    return (pr*tr*rt) / 100


a = int(input('enter a '))
b = int(input('enter b '))
display()
Sum(15, 10)
'''
Output:
enter a 20
enter b 15
a is 20
b is 15
Sum is 35
'''

print(f'Sum is {Sum(a, b)}')
'''
Sum is 35
'''
print(f'Diff is {Diff(a, b)}')
'''
Diff is 5
'''
print(f'Mul is {Mul(a, b)}')
'''
Mul is 300
'''
print(f'Div is {Div(a, b)}')
'''
Div is 1.3333333333333333
'''
print(f'Mod is {Mod(a, b)}')
'''
Mod is 5
'''

# passing n as input to calling function func1(n) as string.
n = input('enter name ')
func1(n)
'''
enter name rini
name is rini
Hello world program
'''
func1('karthik')
'''
name is karthik
Hello world program
'''

# p = 100000
# t = 2
# r = 8.35
print(f'simple interest calculation is {simple_interest(p, t, r)}')
'''
simple interest calculation is 16700.0
'''