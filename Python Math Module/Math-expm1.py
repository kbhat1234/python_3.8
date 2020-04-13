# expm1(x) math function
from math import expm1, exp, sqrt, factorial

em1 = expm1(4)
print(f'{em1}')
'''
Output:
53.598150033144236
'''

# mixed
em2 = expm1(exp(4))
print(f'{em2}')
'''
Output:
5.148435562634557e+23
'''

em3 = expm1(sqrt(16))
print(f'{em3}')
'''
Output:
53.598150033144236
'''

em4 = expm1(sqrt(pow(2, 3)))
print(f'{em4}')
'''
Output:
15.918828678557901
'''

