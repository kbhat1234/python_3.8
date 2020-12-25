def sum(a, b):
    c = a + b
    return c


def diff(a, b):
    if a > b:
        c = a - b
        return c
    else:
        c = b - a
        return c


def mul(a, b):
    c = a * b
    return c


def div(a, b):
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


