# random.setstate() method is used to restore the state of the random number generator back to the specified state
import random

# print the random number
print(random.random())

# capture the state of random number generator
state = random.getstate()
print(state)

# print another random number
print(random.random())

# restore the state
print(random.setstate(state))

# next random number should be same as when you capture the state
print(random.random())