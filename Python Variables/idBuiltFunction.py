a = 10
b = a
print(f'{a} -> {id(a)} {b} -> {id(b)}')

c = 20

print(f'{c} -> {id(c)}')

a = b = c = 100
print(f'{a} {b} {c}')

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

x = y = z = 10, 1, 2
print(f'{x} {type(x)}')
print(y)
print(z)
