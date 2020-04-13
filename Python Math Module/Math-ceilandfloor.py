from math import floor, ceil, pow, sqrt, log, log10, e
'''
floor(x) and ceil(x) math function
floor(x) gives the rounded value, 4.76 rounded to 4.0
ceil(x) gives the rounded value, 4.36 rounded to 5.0
'''

print(f'floor({4.78}) is {floor(4.78)}')
'''
Output:
floor(4.78) is 4
'''

print(f'ceil({4.34}) is {ceil(4.34)}')
'''
Output:
ceil(4.34) is 5
'''

# mixed
print(f'floor(pow({2}, {3}))) is {floor(pow(2, 3))}')
'''
Output:
floor(pow(2, 3))) is 8
'''

print(f'ceil(sqrt({10})) is {ceil(sqrt(10))}')
'''
Output:
ceil(sqrt(10)) is 4
'''

print(f'ceil(log({4}, e)) is {ceil(log(4, e))}')
'''
Output:
ceil(log(4, e)) is 2
'''

print(f'floor(log10({4})) is {floor(log10(4))}')
'''
Output:
floor(log10(4)) is 0
'''

