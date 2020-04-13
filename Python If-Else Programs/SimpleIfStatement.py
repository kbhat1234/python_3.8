# Simple if statement
a = int(input('enter integer to perform if operation '))

# executes if number entered is greater than 10
if a > 10:
    a *= 4
    print(f'{a}')

"""
Output:
enter integer to perform if operation 13
52
end of program
"""

# executes if number entered is lesser than or equal to 10
if a <= 10:
    a += 2
    print(f'{a}')

"""
Output:
enter integer to perform if operation 10
12
end of program
"""
print('end of program')
