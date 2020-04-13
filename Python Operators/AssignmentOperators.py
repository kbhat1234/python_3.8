a = int(input('enter 1st number here '))
b = int(input('enter 2nd number here '))

a = a + 10
print(f'value of a is {a}')

# a += b
a += b  # a = a + b
print(f'value of a is (a += b) {a}')

# a -= b
a -= b  # a = a - b
print(f'value of a is (a -= b) {a}')

# a *= b
a *= b  # a = a * b
print(f'value of a is (a *= b) {a}')

# a /= b (ceil division)
a /= b  # a = a / b
print(f'value of a is (a /= b) {a}')

# a //= b (floor division)
a //= b  # a = a // b
print(f'value of a is (a //= b) {a}')

# a %= b (modulus - remainder)
a %= b  # a = a % b
print(f'value of a is (a %= b) {a}')

# a **= b
a **= b  # a = a ** b
print(f'value of a is (a **= b) {a}')

"""
Output:
enter 1st number here 5
enter 2nd number here 3
value of a is 15
value of a is (a += b) 18
value of a is (a -= b) 15
value of a is (a *= b) 45
value of a is (a /= b) 15.0
value of a is (a //= b) 5.0
value of a is (a %= b) 2.0
value of a is (a **= b) 8.0
"""