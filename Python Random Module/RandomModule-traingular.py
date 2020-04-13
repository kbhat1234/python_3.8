import random

print(random.triangular())  # default low=0, high=1 and mode=0.5
print(random.triangular(20, 30))  # low=20, high=30, mode=None
print(random.triangular(20, 30, 25))  # low=20, high=30, mode=25
