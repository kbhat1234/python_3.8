price = 10
print(price)
price = 20
rating = 4.9
name = 'karthik'
is_selected = True

"""
not valid identifiers
@sbc = 12
a!sadhh = 121
class = 12
def = 20
in = 20
"""

print(f'Price:{price} \tRatings:{rating} \tName:{name} \tSelected:{is_selected}')
print(f'Price:{price} \nRatings:{rating} \nName:{name} \nSelected:{is_selected}')
age = 20
is_new = True

print(f'Name:{name} Age:{age} IsNew:{is_new}')

c = 1 + 2j
print(f'value of c is {c}')

print(f'{type(price)}')
print(f'{type(rating)}')
print(f'{type(name)}')
print(f'{type(is_selected)}')
print(type(c))

# assigning single value to multiple variables
a = b = c = 20
print(f'value of a {a} \nvalue of b {b} \nvalue of c {c}')

# assigning multiple values to multiple variables
a, b, c = 5, 10, 20
print(f'value of a {a} \nvalue of b {b} \nvalue of c {c}')
