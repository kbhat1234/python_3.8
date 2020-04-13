from math import factorial, sqrt

'''
factorial(x) math method
factorial(4) gives 4x3x2x1 = 24
'''

number = int(input('enter any integer number here '))
f = factorial(number)
print(f'factorial({number}) is {factorial(number)}')
'''
Output:
factorial(5) is 120
'''

# mixed
f1 = factorial(sqrt(9))
print(f1)

print(factorial(pow(2, 3)))
