# set the seed value to 10 - random.seed(a, version), a is the integer number to generate random number. version is default value is 2.
# from random import random, seed

import random

# seeding with integer value
random.seed(10)  # seed value is integer
print(f'random value is {random.random()}')
'''
Output:
random value is 0.5714025946899135
'''

# seeding with same integer value and calling random() again will give the same result twice
random.seed(10)  # seed value is integer
print(f'random value is {random.random()}')
'''
Output:
random value is 0.5714025946899135
'''

# seeding with floating value
random.seed(12.88267)
print(f'random value is {random.random()}')
'''
Output:
random value is 0.41996597940235236
'''
