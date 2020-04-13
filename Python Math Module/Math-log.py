# math module - log(x, base) - base -> e, 2, 10

import math
import math as m
from math import log, e, sqrt, factorial

# log() with base 'e' defined in parameter
loge = log(2, e)
print(f'log to base e is {loge}')
'''
Output:
log to base e is 0.6931471805599453
'''

# log() no base
loge = log(2)
print(f'log to base e is {loge}')
'''
Output:
log to base e is 0.6931471805599453
'''
mixede = m.log(m.pow(2, 3), e)
print(f'{mixede}')
'''
Output:
2.0794415416798357
'''

# log() with base 2 defined in parameter
log2 = log(2, 2)
print(f'{log2}')
'''
Output:
1.0
'''

mixed2 = log(sqrt(9), 2)
print(f'{mixed2}')
'''
Output:
1.5849625007211563
'''

# log() with base 10 defined in parameter
log10 = log(2, 10)
print(f'{log10}')
'''
Output:
0.30102999566398114
'''

mixed10 = log(factorial(3), 10)
print(f'{mixed10}')
'''
Output:
0.7781512503836435
'''