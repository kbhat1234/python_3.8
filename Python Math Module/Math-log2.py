# log2(x) math method
from math import log2, sqrt, factorial
log_2 = log2(5)
print(f'{log_2}')
'''
Output:
2.321928094887362
'''

# mixed
mixed2 = log2(sqrt(9))
print(mixed2)
'''
Output:
1.584962500721156
'''

mixed2 = log2(factorial(pow(2, 2)))
print(f'{mixed2}')
'''
Output:
4.584962500721156
'''