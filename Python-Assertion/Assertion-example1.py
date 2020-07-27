def avg(m):
    assert len(m) != 0, 'list is empty'
    return sum(m)/len(m)


marks = [10, 20]
print(f'average marks is {avg(marks)}')

x = 7
y = 1

print(f'x/y is ')
assert y != 0, 'Divide by 0 error'
print(x/y)

p = 'hello'

assert p == 'hello', 'passed'
print(p)

assert p == 'welcome', 'failed'
print(p)