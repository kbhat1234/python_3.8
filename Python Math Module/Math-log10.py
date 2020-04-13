# standard logarithm log10(x) math method
import math
import math as m
from math import log10, factorial, sqrt

log_10 = log10(4)
print(f'{log_10}')
'''
Output:
0.6020599913279624
'''

# mixed
mixed10 = log10(factorial(3))
print(f'{mixed10}')
'''
Output:
0.7781512503836436
'''

mixed10 = log10(factorial(sqrt(16)))
print(f'{mixed10}')
'''
Output:
1.380211241711606
'''