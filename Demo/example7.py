glo = 1000


def sum(a, b):
    print(glo)
    c = a + b
    return c


def diff(a, b):
    print(glo)
    if a > b:
        c = a - b
        return c
    else:
        c = b - a
        return c


def mul(a, b):
    print(glo)
    c = a * b
    return c


def div(a, b):
    print(glo)
    if a > b:
        c = a / b
        return c
    else:
        c = b / a
        return c


s = sum(10, 2)
print(f'Sum is {s}')

d = diff(10, 3)
print(f'Difference is {d}')

m = mul(5, 2)
print(f'Multiply is {m}')

d1 = div(2, 10)
print(f'Division is {d1}')

#  print(f'{a} {b} {c}')
print(glo)

print(id(glo))
#  del glo

